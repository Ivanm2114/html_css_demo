"""Берем данные о пользователе из cabinet miem,
 данные о steam аккаунте, статистику из CS:GO и PAYDAY 2"""
import os
import json

from jinja2 import Environment, FileSystemLoader

from dotenv import load_dotenv
from funcs import get_cs_steam_stats, get_cabinet_student, \
    get_steam_profile_stats, get_payday2_steam_stats, get_zulip_data, get_gitlab_data, \
    prepare_data

load_dotenv()

STUDENT_ID = os.getenv("USER_CABINET_ID")
PLAYER_ID = os.getenv("PLAYER_ID")
STEAM_KEY = os.getenv("STEAM_API_KEY")
GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")
ZULIP_ID = os.getenv("ZULIP_ID")
ZULIP_KEY = os.getenv("ZULIP_API_KEY")
ZULIP_EMAIL = os.getenv("ZULIP_EMAIL")
ZULIP_URL = os.getenv("ZULIP_URL")

# CABINET MIEM INFO
cabinet_json = get_cabinet_student(STUDENT_ID)

zulip_json = get_zulip_data(ZULIP_ID, ZULIP_KEY, ZULIP_EMAIL, ZULIP_URL)

gitlab_json = get_gitlab_data(GITLAB_TOKEN)

steam_json = get_steam_profile_stats(STEAM_KEY, PLAYER_ID)
cs_json = get_cs_steam_stats(STEAM_KEY, PLAYER_ID)
payday2_json = get_payday2_steam_stats(STEAM_KEY, PLAYER_ID)
json_data = {"cabinet_miem": cabinet_json, "zulip_json": zulip_json,
     "gitlab_json": gitlab_json, "steam_json": steam_json,
     "cs_json": cs_json, "payday2_json": payday2_json}

with open("data/data.json", mode='w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
    print(json_data)

env = Environment(loader=FileSystemLoader("templates/"))
template = env.get_template('index.html')

html_data = prepare_data(json_data)

template_text = template.render(data=html_data)

with open("templates/ready.html", mode='w', encoding='utf-8') as file:
    file.write(template_text)
    print(template_text)
