from bs4 import BeautifulSoup
import requests

url = "https://internet3.trincoll.edu/ptools/courselisting.aspx"

with requests.session() as s:
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    courses = [v["value"] for v in soup.select("#ddlList [value]")]

    for c in courses:
        data = {}
        for inp in soup.select("input[value][name]"):
            data[inp["name"]] = inp["value"]

        data["ddlList"] = c
        data["ddlLevelList"] = "0"
        data["ddlTermList"] = "1241"  # <-- Fall 2023
        data["ddlSession"] = "0"
        data["__EVENTTARGET"] = "ddlList"
        data["__EVENTARGUMENT"] = ""
        data["__LASTFOCUS"] = ""

        soup = BeautifulSoup(s.post(url, data=data).content, "html.parser")

        print(c)
        print("-" * 80)
        for id_, time, title, c_id in zip(soup.select(".TITLE_id"), soup.select(".TITLE_times"), soup.select(".TITLE_title"), soup.find_all('td', nowrap="true")):
            print(f"{id_.text:<10} {title.text} {time.text} {c_id.text}")
        print()