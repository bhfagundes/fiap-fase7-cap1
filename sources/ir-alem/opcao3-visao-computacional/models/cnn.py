import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50V2

def create_cnn_model(input_shape=(224, 224, 3), num_classes=5):
    """
    Cria um modelo CNN baseado em ResNet50V2 com transfer learning
    
    Args:
        input_shape: Formato das imagens de entrada
        num_classes: Número de classes para classificação
        
    Returns:
        Modelo CNN compilado
    """
    # Carrega o modelo base pré-treinado
    base_model = ResNet50V2(
        weights='imagenet',
        include_top=False,
        input_shape=input_shape
    )
    
    # Congela as camadas do modelo base
    base_model.trainable = False
    
    # Adiciona camadas de classificação
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    # Compila o modelo
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

def fine_tune_model(model, num_layers=10):
    """
    Realiza fine-tuning do modelo descongelando as últimas camadas
    
    Args:
        model: Modelo CNN pré-treinado
        num_layers: Número de camadas para descongelar
    """
    # Descongela as últimas camadas do modelo base
    for layer in model.layers[0].layers[-num_layers:]:
        layer.trainable = True
    
    # Recompila o modelo com learning rate menor
    model.compile(
        optimizer=tf.keras.optimizers.Adam(1e-5),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model 