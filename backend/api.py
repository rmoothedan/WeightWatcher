from fastapi import FastAPI
import update
import schedule

app = FastAPI()

@app.get("/schedule/")
def return_best_time(timeString):
    return schedule.get_best_time(timeString)


@app.get("/update/api_to_json")
def print_api():
    return update.api_to_json()


@app.get("/update/update_structure")
def print_api():
    return update.update_structure()


@app.get("/update/get_weeks")
def print_api():
    return update.get_weeks()

