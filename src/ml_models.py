import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

class SkinToneClassifier:
    """
    ML Algo 1: Predicts the user's continuous ITA value from an image.
    Treated as a Regression task.
    """
    def __init__(self, model_path=None):
        self.model = self._build_cnn_model()
        if model_path:
            self.model.load_weights(model_path)
            
    def _build_cnn_model(self, input_shape=(224, 224, 3)):
        """Builds a simple CNN for ITA Regression."""
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(128, activation='relu'),
            Dense(1, activation='linear') # Output is a single continuous ITA value
        ])
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        return model

    def train(self, X_train, y_train, epochs=20):
        """Trains the CNN model."""
        self.model.fit(X_train, y_train, epochs=epochs, validation_split=0.2)

    def predict_ita(self, image_preprocessed):
        """Predicts the ITA value for a single preprocessed image."""
        # Ensure image is resized/normalized as expected by the model
        return self.model.predict(np.expand_dims(image_preprocessed, axis=0))[0][0]


class ShadeRecommender:
    """
    ML Algo 2: Recommends the closest foundation shade based on the predicted ITA.
    Treated as a Nearest Neighbor search.
    """
    def __init__(self, shades_csv_path='data/processed_shades.csv'):
        # Load the curated dataset of foundation shades
        self.shades_df = pd.read_csv(shades_csv_path)
        
        # Prepare the feature matrix (ITA is the primary feature)
        # Assuming processed_shades.csv has an 'ITA' column
        self.features = self.shades_df[['ITA']].values 
        
        # Initialize k-Nearest Neighbors model
        self.nn_model = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
        self.nn_model.fit(self.features)

    def recommend(self, ita_value, k=5):
        """
        Finds the k closest foundation shades to the input ITA value.
        
        Args:
            ita_value (float): The predicted ITA value from the classifier.
            k (int): Number of top recommendations to return.
            
        Returns:
            pd.DataFrame: Top k matching shades.
        """
        # Need to search for the closest point in the feature space
        query_point = np.array([[ita_value]])
        
        distances, indices = self.nn_model.kneighbors(query_point, n_neighbors=k)
        
        # Get the recommended shades from the original DataFrame
        recommendations = self.shades_df.iloc[indices[0]]
        
        # Optionally, add the distance for confidence/sorting
        recommendations['distance'] = distances[0]
        
        return recommendations.sort_values(by='distance')
