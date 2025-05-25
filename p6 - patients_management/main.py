from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()


class Patient(BaseModel):

    id: Annotated[str,
                  Field(..., description="ID of the Patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the Patient")]
    city: Annotated[str,
                    Field(..., description="City where the patient is living")]
    age: Annotated[int, Field(..., gt=0, lt=120,
                              description="Age of the Patient")]
    gender: Annotated[Literal['male', 'female', 'others'],
                      Field(..., description="Gander of the patient")]
    height: Annotated[float,
                      Field(..., gt=0, description="Height of the patient in mtrs")]
    weight: Annotated[float,
                      Field(..., gt=0, description="Weight of the patient in kgs")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


# function for saving data
def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f)


# function for loading data
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
        return data


# home page
@app.get("/")
def home():
    return {"message": "Welcome to Patient Management System"}


# viewing all patients
@app.get("/patients/")
def view_all():
    data = load_data()
    return data


# single patients
@app.get("/patients/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient from DB", example="P001")):

    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found in DB")


# custom sorting on data
@app.get("/sort/")
def sort_patients(sort_by: str = Query(..., description="Sort on the basic of (height, weight, bmi)"), order_by: str = Query("asc", description="Order by (asc, desc)")):

    valid_feilds = ["height", "weight", "bmi"]

    if sort_by not in valid_feilds:
        raise HTTPException(
            status_code=400, detail=f'Invalid field select from {valid_feilds}')

    if order_by not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400, detail='Invalid field select from (asc/desc)')

    data = load_data()

    order_by = True if order_by == "desc" else False

    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by), reverse=order_by)

    return sorted_data


@app.post("/create")
def create_patient(patient: Patient):
    # load the existing data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists.")

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save data into json file
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "patient created successfully"})
