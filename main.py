"""Берем данные о пользователе из cabinet miem,
 данные о steam аккаунте, статистику из CS:GO и PAYDAY 2"""
import os
import json

from jinja2 import Environment, FileSystemLoader

from dotenv import load_dotenv
from funcs import cs_steam_stats, cabinet_student, \
    steam_profile_stats, payday2_steam_stats, zulip_data, gitlab_data, \
    prepare_data

load_dotenv()

student_id = os.getenv("USER_CABINET_ID")
player_id = os.getenv("PLAYER_ID")
steam_key = os.getenv("STEAM_API_KEY")
gitlab_token = os.getenv("GITLAB_TOKEN")
zulip_id = os.getenv("ZULIP_ID")
zulip_key = os.getenv("ZULIP_API_KEY")
zulip_email = os.getenv("ZULIP_EMAIL")
zulip_url = os.getenv("ZULIP_URL")

# CABINET MIEM INFO
cabinet_json = cabinet_student(student_id)

zulip_json = zulip_data(zulip_id, zulip_key, zulip_email, zulip_url)

gitlab_json = gitlab_data(gitlab_token)

steam_json = steam_profile_stats(steam_key, player_id)
cs_json = cs_steam_stats(steam_key, player_id)
payday2_json = payday2_steam_stats(steam_key, player_id)
d = {"cabinet_miem": cabinet_json, "zulip_json": zulip_json,
     "gitlab_json": gitlab_json, "steam_json": steam_json,
     "cs_json": cs_json, "payday2_json": payday2_json}

with open("data/data.json", mode='w', encoding='utf-8') as file:
    json.dump(d, file, ensure_ascii=False, indent=4)
    print(d)

env = Environment(loader=FileSystemLoader("templates/"))
template = env.get_template('index.html')

data = prepare_data(d)

template_text = template.render(data=data)

with open("templates/ready.html", mode='w') as file:
    file.write(template_text)
    print(template_text)
