from fastapi import FastAPI , Path , HTTPException
import json
def load_data():
    with open("patients.json" , 'r') as f:
        data = json.load(f)
        return data


app = FastAPI()
@app.get("/")
def about():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return{"message" : "This is my first API"}

@app.get("/patients")
def patients():
    patient_info = load_data()
    return patient_info

@app.get("/patients/{patient_id}")
def patients(patient_id : str = Path(..., description="Patient ID" , example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
