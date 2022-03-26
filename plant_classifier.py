import io

import numpy as np
import pandas as pd
from PIL import Image
import tensorflow.compat.v2 as tf
import tensorflow_hub as hub


def read_image_bytes(img: bytes) -> Image.Image:
    image = Image.open(io.BytesIO(img))
    return image


class PlantModel:
    def __init__(self):
        self.model = hub.KerasLayer(
            "https://tfhub.dev/google/aiy/vision/classifier/plants_V1/1"
        )
        self.IMAGE_SIZE = (224, 224)
        self.normalization_layer = tf.keras.layers.Rescaling(1.0 / 255)
        self.classes_map = pd.read_csv(
            "https://www.gstatic.com/aihub/tfhub/labelmaps/aiy_plants_V1_labelmap.csv",
            index_col="id",
        )

    def predict(self, img: bytes) -> str:

        img = read_image_bytes(img)
        img = np.asarray(img.resize(self.IMAGE_SIZE))[..., :3]
        img = np.expand_dims(img, 0)
        img = self.normalization_layer(img)
        probabilities = self.model(img)

        return self.classes_map.loc[np.argmax(probabilities), "name"]
