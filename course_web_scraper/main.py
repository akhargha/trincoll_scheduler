import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://internet3.trincoll.edu/ptools/courselisting.aspx"


def wait_a_bit(wait_for: int = 5) -> None:
    time.sleep(wait_for)


with requests.session() as session:
    course_selection = (
        BeautifulSoup(session.get(url).text, "html.parser")
        .select("#ddlList [value]")
    )
    all_courses = [[c.get("value"), c.getText()] for c in course_selection]

    for course in all_courses:
        course_id, course_name = course
        print(f"Getting {course_name}...")

        v_state = (
            BeautifulSoup(session.get(url).text, "html.parser")
            .find("input", {"name": "__VIEWSTATE"})["value"]
        )
        event_validation = (
            BeautifulSoup(session.get(url).text, "html.parser")
            .find("input", {"name": "__EVENTVALIDATION"})["value"]
        )

        payload = {
            "__EVENTVALIDATION": event_validation,
            "__VIEWSTATE": v_state,
            "__VIEWSTATEGENERATOR": "3786FA90",
            "rblLstType": 1,
            "ddlList": course_id,
            "ddlLevelList": 0,
            "ddlTermList": 1241,
            "ddlSession": 0,
            "btnSubmit": "Submit",
        }

        response = session.post(url, data=payload)
        courses = (
            BeautifulSoup(response.text, "html.parser")
            .select_one('table[class="TITLE_tbl"]')
        )

        table_rows = zip(
            courses.select(".TITLE_id"),
            courses.select(".TITLE_times"),
            courses.select(".TITLE_title"),
            courses.find_all('td', nowrap="true"),
        )

        my_table = [
            [
                id_.getText(),
                time.getText(),
                title.getText(),
                c_id.getText(),
            ] for id_, time, title, c_id in table_rows
        ]

        df = pd.DataFrame(my_table, columns=["ID", "Time", "Title", "Course ID"])
        df.to_csv(f"{course_id}_{course_name}.csv", index=False)
        print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))

        wait_a_bit(wait_for=3)