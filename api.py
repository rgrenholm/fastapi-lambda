from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mangum import Mangum

from plant_classifier import PlantModel


plant_model = PlantModel()


class Plant(BaseModel):
    decoded_image: str


app = FastAPI()


@app.post("/image")
def upload_image(plant: Plant) -> str:
    encoded_image = plant.decoded_image.encode("ISO-8859-1")
    return plant_model.predict(img=encoded_image)


handler = Mangum(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
