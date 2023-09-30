from pywebio.input import *
from pywebio.output import put_text, put_link, put_info, put_error
from pywebio.platform.tornado import start_server
import requests
import json


url = "http://localhost:28081/api/items"


def call_api(data):
    postdata = {
        "repo": data["repo"],
        "job": data["job"],
    }
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(url,
                             headers=headers,
                             data=json.dumps(postdata))

    return response.json()


def index():
    repos = ["master", "develop", "feature"]
    env = ["dev", "stg", "prd"]
    jobs = ["A", "B"]
    info = input_group("設定",[
        select("リポジトリ", options=repos, name="repo"),
        select("環境", options=env, name="env"),
        select("JOB", options=jobs, name="job"),
        input("制限(ex: DD)", name="limit"),
        input("Dryrun(ex: --check)", name="Dryrun")
    ])
    print(info['repo'], info['job'], info["limit"])
    result = call_api(info)
    if not result:
        put_error(f"Error")

    if int(result["Status"]) == 200:
        put_info("Success")
    else:
        put_error(f"Error")

    put_text(f"request \n {info}")
    put_text(f"response \n {result}")
    put_link("設定に戻る", app="index")


start_server([index], port=18080)