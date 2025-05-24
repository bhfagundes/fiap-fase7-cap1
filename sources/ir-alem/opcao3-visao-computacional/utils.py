import cv2
import numpy as np
import os
from datetime import datetime

def load_image(image_path):
    """
    Carrega uma imagem do disco
    
    Args:
        image_path: Caminho para a imagem
        
    Returns:
        Imagem carregada (BGR)
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Imagem não encontrada: {image_path}")
    
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Erro ao carregar imagem: {image_path}")
    
    return image

def save_image(image, output_dir, prefix="result"):
    """
    Salva uma imagem no disco
    
    Args:
        image: Imagem a ser salva
        output_dir: Diretório de saída
        prefix: Prefixo do nome do arquivo
    """
    # Cria diretório se não existir
    os.makedirs(output_dir, exist_ok=True)
    
    # Gera nome do arquivo com timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.jpg"
    output_path = os.path.join(output_dir, filename)
    
    # Salva a imagem
    cv2.imwrite(output_path, image)
    return output_path

def preprocess_image(image, target_size=(224, 224)):
    """
    Pré-processa uma imagem para o modelo CNN
    
    Args:
        image: Imagem de entrada (BGR)
        target_size: Tamanho alvo para redimensionamento
        
    Returns:
        Imagem pré-processada
    """
    # Redimensiona
    image = cv2.resize(image, target_size)
    
    # Converte para RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Normaliza
    image = image.astype(np.float32) / 255.0
    
    return image

def create_data_generator(directory, target_size=(224, 224), batch_size=32):
    """
    Cria um gerador de dados para treinamento
    
    Args:
        directory: Diretório com as imagens
        target_size: Tamanho alvo para redimensionamento
        batch_size: Tamanho do batch
        
    Returns:
        Gerador de dados
    """
    datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    
    return datagen.flow_from_directory(
        directory,
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical'
    )

def calculate_metrics(y_true, y_pred):
    """
    Calcula métricas de avaliação
    
    Args:
        y_true: Labels verdadeiros
        y_pred: Predições do modelo
        
    Returns:
        Dicionário com métricas
    """
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    
    metrics = {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted'),
        'recall': recall_score(y_true, y_pred, average='weighted'),
        'f1': f1_score(y_true, y_pred, average='weighted')
    }
    
    return metrics 