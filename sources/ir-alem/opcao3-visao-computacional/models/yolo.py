import cv2
import numpy as np
import tensorflow as tf

class YOLODetector:
    def __init__(self, model_path, conf_threshold=0.5):
        """
        Inicializa o detector YOLO
        
        Args:
            model_path: Caminho para o modelo YOLO
            conf_threshold: Limiar de confiança para detecções
        """
        self.model = tf.saved_model.load(model_path)
        self.conf_threshold = conf_threshold
        
    def preprocess_image(self, image):
        """
        Pré-processa a imagem para o modelo YOLO
        
        Args:
            image: Imagem de entrada (BGR)
            
        Returns:
            Imagem pré-processada
        """
        # Redimensiona para 416x416
        image = cv2.resize(image, (416, 416))
        
        # Normaliza para [0,1]
        image = image.astype(np.float32) / 255.0
        
        # Adiciona dimensão do batch
        image = np.expand_dims(image, axis=0)
        
        return image
    
    def detect(self, image):
        """
        Realiza detecção de objetos na imagem
        
        Args:
            image: Imagem de entrada (BGR)
            
        Returns:
            Lista de detecções (x, y, w, h, conf, class)
        """
        # Pré-processa a imagem
        input_image = self.preprocess_image(image)
        
        # Realiza a inferência
        detections = self.model(input_image)
        
        # Processa as detecções
        boxes = []
        scores = []
        classes = []
        
        # Filtra detecções pelo limiar de confiança
        for detection in detections:
            if detection[4] > self.conf_threshold:
                boxes.append(detection[:4])
                scores.append(detection[4])
                classes.append(detection[5])
        
        return boxes, scores, classes
    
    def draw_detections(self, image, boxes, scores, classes):
        """
        Desenha as detecções na imagem
        
        Args:
            image: Imagem original
            boxes: Lista de bounding boxes
            scores: Lista de scores
            classes: Lista de classes
            
        Returns:
            Imagem com detecções desenhadas
        """
        for box, score, class_id in zip(boxes, scores, classes):
            # Converte coordenadas normalizadas para pixels
            x, y, w, h = box
            x1 = int((x - w/2) * image.shape[1])
            y1 = int((y - h/2) * image.shape[0])
            x2 = int((x + w/2) * image.shape[1])
            y2 = int((y + h/2) * image.shape[0])
            
            # Desenha o retângulo
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Adiciona texto com classe e score
            text = f"{class_id}: {score:.2f}"
            cv2.putText(image, text, (x1, y1-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return image 