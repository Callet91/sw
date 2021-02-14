import os
import datetime
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers, losses

class ExampleModel: 
    """Example model using Keras sequential modeling"""
    def __init__(self, config): 
        self.MODEL = models.Sequential()
        self.CONFIG = config        # Change the config file your model
        self.LOSS_FN = losses.SparseCategoricalCrossentropy(from_logits=True)

    def generate_model(self): 
        """Generate example model
        
        original model: 
        https://www.tensorflow.org/tutorials/quickstart/beginner       
        
        """

        # Here you add layers to your model 
        self.MODEL.add(layers.Flatten(input_shape=(28, 28)))
        self.MODEL.add(layers.Dense(128, activation=self.CONFIG['activation']))
        self.MODEL.add(layers.Dropout(0.2))
        self.MODEL.add(layers.Dense(10))


    def compile(self): 
        """Compile model"""

        self.MODEL.compile(
            optimizer = self.CONFIG['optimizer'],
            loss = self.LOSS_FN,     
            metrics = [self.CONFIG['metrics']]
        )

    def train_model(self, data_train_x, data_train_y, data_val_x, data_val_y): 
        """Train model"""
        history = self.MODEL.fit(
            x = data_train_x,
            y = data_train_y, 
            epochs = self.CONFIG["epochs"],
            batch_size = self.CONFIG["batch"],
            validation_data = (data_val_x, data_val_y),
            shuffle = True
        )

        return history 

    def evaluate_model(self, data_test_x, data_test_y): 
        """Evaluate model"""

        self.MODEL.evaluate(
            data_test_x, 
            data_test_y, 
            batch_size=32)