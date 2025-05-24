import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt

class CropClassifier:
    def __init__(self, input_shape=(224, 224, 3), num_classes=5):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self._build_model()
        
    def _build_model(self):
        """Constrói modelo CNN com transfer learning"""
        # Base model (InceptionV3)
        base_model = InceptionV3(
            weights='imagenet',
            include_top=False,
            input_shape=self.input_shape
        )
        
        # Congela camadas do modelo base
        base_model.trainable = False
        
        # Adiciona camadas de classificação
        model = models.Sequential([
            base_model,
            layers.GlobalAveragePooling2D(),
            layers.Dense(512, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(self.num_classes, activation='softmax')
        ])
        
        return model
    
    def compile_model(self, learning_rate=0.001):
        """Compila o modelo"""
        self.model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
    
    def train(self, train_dir, validation_dir, batch_size=32, epochs=20):
        """Treina o modelo"""
        # Data augmentation
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest'
        )
        
        validation_datagen = ImageDataGenerator(rescale=1./255)
        
        # Geradores de dados
        train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=self.input_shape[:2],
            batch_size=batch_size,
            class_mode='categorical'
        )
        
        validation_generator = validation_datagen.flow_from_directory(
            validation_dir,
            target_size=self.input_shape[:2],
            batch_size=batch_size,
            class_mode='categorical'
        )
        
        # Callbacks
        callbacks = [
            tf.keras.callbacks.EarlyStopping(
                monitor='val_loss',
                patience=5,
                restore_best_weights=True
            ),
            tf.keras.callbacks.ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.2,
                patience=3
            )
        ]
        
        # Treina o modelo
        history = self.model.fit(
            train_generator,
            validation_data=validation_generator,
            epochs=epochs,
            callbacks=callbacks
        )
        
        return history
    
    def evaluate(self, test_dir, batch_size=32):
        """Avalia o modelo"""
        test_datagen = ImageDataGenerator(rescale=1./255)
        
        test_generator = test_datagen.flow_from_directory(
            test_dir,
            target_size=self.input_shape[:2],
            batch_size=batch_size,
            class_mode='categorical',
            shuffle=False
        )
        
        return self.model.evaluate(test_generator)
    
    def predict(self, image_path):
        """Faz predição em uma imagem"""
        img = tf.keras.preprocessing.image.load_img(
            image_path,
            target_size=self.input_shape[:2]
        )
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.
        
        predictions = self.model.predict(img_array)
        return predictions
    
    def plot_training_history(self, history):
        """Plota histórico de treinamento"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        
        # Acurácia
        ax1.plot(history.history['accuracy'])
        ax1.plot(history.history['val_accuracy'])
        ax1.set_title('Model Accuracy')
        ax1.set_ylabel('Accuracy')
        ax1.set_xlabel('Epoch')
        ax1.legend(['Train', 'Validation'], loc='upper left')
        
        # Loss
        ax2.plot(history.history['loss'])
        ax2.plot(history.history['val_loss'])
        ax2.set_title('Model Loss')
        ax2.set_ylabel('Loss')
        ax2.set_xlabel('Epoch')
        ax2.legend(['Train', 'Validation'], loc='upper left')
        
        plt.tight_layout()
        plt.savefig('training_history.png')
        plt.close()
    
    def save_model(self, filepath):
        """Salva o modelo"""
        self.model.save(filepath)
    
    @classmethod
    def load_model(cls, filepath):
        """Carrega modelo salvo"""
        model = tf.keras.models.load_model(filepath)
        classifier = cls()
        classifier.model = model
        return classifier

def main():
    # Exemplo de uso
    classifier = CropClassifier(num_classes=5)
    classifier.compile_model()
    
    # Treina o modelo
    history = classifier.train(
        train_dir='data/train',
        validation_dir='data/validation',
        epochs=20
    )
    
    # Plota histórico
    classifier.plot_training_history(history)
    
    # Avalia no conjunto de teste
    test_loss, test_acc = classifier.evaluate('data/test')
    print(f'Test accuracy: {test_acc:.4f}')
    
    # Salva o modelo
    classifier.save_model('models/crop_classifier.h5')

if __name__ == "__main__":
    main() 