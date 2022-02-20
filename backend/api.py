from fastapi import FastAPI
import update

app = FastAPI()


@app.get("/update.py/api_to_json")
def print_api():
    return update.api_to_json()

@app.get("/update.py/update_structure")
def print_api():
    return update.update_structure()

@app.get("/update.py/get_weeks")
def print_api():
    return update.get_weeks()

