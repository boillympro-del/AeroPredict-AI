from fastapi import FastAPI  # on importe l’outil.
from pydantic import BaseModel

import data


class MachineEntrante(BaseModel):
    identifiant: str
    temperature: int
    speed: int

app = FastAPI()  # on crée l’application


@app.get(
    "/machines"
)  # route qui renvoie toutes les machines en JSON
def listes_machines():

    machines= data.afficher_machines()

    result=[]

    for m in machines:

        result.append({"identifiant" : m[0], "temperature" : m[1], "vitesse" : m[2]})

    return result