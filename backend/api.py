from fastapi import FastAPI
import update
import schedule

app = FastAPI()

@app.get("/schedule/")
def return_best_times(timeString):
    return schedule.get_best_times(timeString)


@app.get("/update/api_to_json")
def print_api():
    return update.api_to_json()


@app.get("/update/update_structure")
def print_api():
    return update.update_structure()


@app.get("/update/get_weeks")
def print_api():
    return update.get_weeks()

@app.get("/schedule.py/parse_user_data")
def print_api():
    return schedule.parse_user_data("Sunday", "Level 1",  "12:30PM-04:30PM,07:30PM-10:30PM")

@app.get("/schedule.py/get_week_intervals")
def print_api():
    return schedule.get_week_intervals()