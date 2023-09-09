import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(slack_name: str, track: str):
    if not slack_name or not track:
        return {'message': 'enter query slack name and track'}
    current_datetime = datetime.datetime.utcnow()
    tolerance = datetime.timedelta(seconds=2)
    valid_time_lower = current_datetime - tolerance
    valid_time_upper = current_datetime + tolerance
    # Get the current UTC time again for validation
    current_utc_time2 = datetime.datetime.utcnow()
    # Check if the current time is within the valid time range
    if valid_time_lower <= current_utc_time2 <= valid_time_upper:
        # Format the date
        f_datetime = current_utc_time2.strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        # Format the date
        f_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
      "slack_name": slack_name,
      "current_day": datetime.datetime.now().strftime("%A"),
      "utc_time": f_datetime,
      "track": track,
      "github_file_url": "https://github.com/Senseiuc/zuri/task_one_api.py",
      "github_repo_url": "https://github.com/Senseiuc/zuri",
      "status_code": 200
    }
