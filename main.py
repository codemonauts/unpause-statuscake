#! /usr/bin/env python3
import requests
from datetime import datetime
from math import floor
from config import API_KEY, USERNAME, THRESHOLD


def get_all_testids():
    headers = {"API": API_KEY, "Username": USERNAME}
    r = requests.get("https://app.statuscake.com/API/Tests/", headers=headers)
    if r.status_code == 200:
        ids = []
        for test in r.json():
            if test["Paused"]:
                ids.append(test["TestID"])
        return ids
    else:
        None

def paused_since(id):
    headers = {"API": API_KEY, "Username": USERNAME}
    params = {"TestID": id}
    r = requests.get("https://app.statuscake.com/API/Tests/Details/", headers=headers, params=params)
    if r.status_code == 200:
        last_tested = datetime.strptime(r.json()["LastTested"], "%Y-%m-%d %H:%M:%S")
        diff = datetime.utcnow() - last_tested
        return floor(diff.seconds / 3600)


def unpause(id):
    headers = {"API": API_KEY, "Username": USERNAME}
    params = {"TestID": id, "Paused": 0}
    r = requests.put("https://app.statuscake.com/API/Tests/Update/", headers=headers, data=params)
    if r.status_code == 200:
        print("Sucessfully unpaused the test")


def main():
    ids = get_all_testids()
    print("Found {} paused tests".format(len(ids)))
    for id in ids:
        duration = paused_since(id)
        if duration > THRESHOLD:
            print("Test {} has beedn paused for {}h now. Unpausing it".format(id, duration))
            unpause(id)
        else:
            print("Test {} has only been paused for {} hours".format(id, duration))


if __name__ == "__main__":
    main()

