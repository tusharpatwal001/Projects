from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()


# function for loading data
def load_data():
    with open("patients.json", "r") as f:
        return json.load(f)


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
