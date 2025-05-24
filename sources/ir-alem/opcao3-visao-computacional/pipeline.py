import cv2
import numpy as np
from models.cnn import create_cnn_model, fine_tune_model
from models.yolo import YOLODetector
import tensorflow as tf

class VisionPipeline:
    def __init__(self, cnn_model_path, yolo_model_path):
        """
        Inicializa o pipeline de visão computacional
        
        Args:
            cnn_model_path: Caminho para o modelo CNN
            yolo_model_path: Caminho para o modelo YOLO
        """
        # Carrega o modelo CNN
        self.cnn_model = tf.keras.models.load_model(cnn_model_path)
        
        # Inicializa o detector YOLO
        self.yolo_detector = YOLODetector(yolo_model_path)
        
    def process_image(self, image):
        """
        Processa uma imagem usando CNN e YOLO
        
        Args:
            image: Imagem de entrada (BGR)
            
        Returns:
            Dicionário com resultados
        """
        # Realiza detecção com YOLO
        boxes, scores, classes = self.yolo_detector.detect(image)
        
        # Para cada detecção, classifica com CNN
        results = []
        for box, score, class_id in zip(boxes, scores, classes):
            # Extrai região da imagem
            x, y, w, h = box
            x1 = int((x - w/2) * image.shape[1])
            y1 = int((y - h/2) * image.shape[0])
            x2 = int((x + w/2) * image.shape[1])
            y2 = int((y + h/2) * image.shape[0])
            
            # Garante que as coordenadas estão dentro da imagem
            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(image.shape[1], x2)
            y2 = min(image.shape[0], y2)
            
            # Extrai e redimensiona a região
            region = image[y1:y2, x1:x2]
            region = cv2.resize(region, (224, 224))
            
            # Classifica com CNN
            region = region.astype(np.float32) / 255.0
            region = np.expand_dims(region, axis=0)
            cnn_pred = self.cnn_model.predict(region)[0]
            
            # Adiciona resultado
            results.append({
                'box': (x1, y1, x2, y2),
                'yolo_score': float(score),
                'yolo_class': int(class_id),
                'cnn_pred': cnn_pred.tolist()
            })
        
        return results
    
    def draw_results(self, image, results):
        """
        Desenha os resultados na imagem
        
        Args:
            image: Imagem original
            results: Lista de resultados do processamento
            
        Returns:
            Imagem com resultados desenhados
        """
        for result in results:
            # Extrai informações
            x1, y1, x2, y2 = result['box']
            yolo_score = result['yolo_score']
            yolo_class = result['yolo_class']
            cnn_pred = result['cnn_pred']
            
            # Desenha bounding box
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Adiciona texto com informações
            text = f"Class: {yolo_class} ({yolo_score:.2f})"
            cv2.putText(image, text, (x1, y1-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Adiciona predições da CNN
            for i, pred in enumerate(cnn_pred):
                text = f"CNN {i}: {pred:.2f}"
                cv2.putText(image, text, (x1, y1+20+i*20),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return image 