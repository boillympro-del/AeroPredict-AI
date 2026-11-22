from fastapi import FastAPI, HTTPException  # on importe l’outil. 
from pydantic import BaseModel, Field

import data


class MachineEntrante(BaseModel):
    identifiant: str
    temperature: int = Field(ge=0, le=150)
    speed: int = Field(ge=0, le=3600)


class MachineModification(BaseModel):
    temperature: int = Field(ge=0, le=150)
    speed: int = Field(ge=0, le=3600)


app = FastAPI()  # on crée l’application


@app.get("/machines")  # route qui renvoie toutes les machines en JSON
def listes_machines():

    machines = data.afficher_machines()

    result = []

    for m in machines:
        result.append({"identifiant": m[0], "temperature": m[1], "vitesse": m[2]})

    return result


@app.post("/machines")  # Permet d'ajouter les machines hors du terminal
def ajouter_machine_api(machine: MachineEntrante):
    ok = data.ajouter_machine(machine)
    if ok == True:
        return {"message": "Machine added successfully"}
    else:
        return {"message": "This ID already exists"}


@app.delete("/machines/{identifiant}")
def supprimer_machine_api(identifiant: str):
    result=data.supprimer_machine(identifiant)
    if result==False:
        raise HTTPException(status_code=404, detail="Machine not Found !")
    else:
        return {"message": "Deleted Successfully"}


@app.put("/machines/{identifiant}")
def modifier_machine_api(identifiant: str, machine: MachineModification):
    result1=data.modifier_machine(identifiant, machine.temperature, machine.speed)
    if result1==False:
        raise HTTPException(status_code=404, detail="Machine not Found !")
    else:
        return {"message": "Machine modified successfully."}


    


@app.get("/stats/")
def afficher_stats():
    count = data.count_machines()[0][0]
    avg = data.avg_machines()[0]
    max = data.max_machines()[0]
    min = data.min_machines()[0]
    dictionnaire = {
        "Total Machines": count,
        "Average Temperature": avg[0],
        "Average Speed": avg[1],
        "Highest temperature": max[0],
        "Highest speed": max[1],
        "Lowest temperature": min[0],
        "Lowest speed": min[1],
    }
    return dictionnaire
