import pickle

with open("email-classifier.pickle", "rb") as file:
    model = pickle.load(file)

from fastapi import FastAPI
from pydantic import BaseModel # data kasto hunu parxa vanne pydantic le vanxa

class Data(BaseModel):
    email: str


app = FastAPI()

@app.get("/")
def homepage():
    return {"msg": "Success"}



@app.post("/submit")
def submit(item: Data):
    email = item.email
    y_pred = model.predict([email])[0]
    return {"label": y_pred}