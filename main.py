"""Берем данные о пользователе из cabinet miem,
 данные о steam аккаунте, статистику из CS:GO и PAYDAY 2"""
import os
import json

from dotenv import load_dotenv
from funcs import cs_steam_stats, cabinet_student_text, \
    steam_profile_stats, payday2_steam_stats

load_dotenv()

student_id = os.getenv("USER_CABINET_ID")
player_id = os.getenv("PLAYER_ID")
steam_key = os.getenv("STEAM_API_KEY")

# CABINET MIEM INFO
cabinet_info = cabinet_student_text(student_id)
# GENRAL STATS
steam_stats = steam_profile_stats(steam_key, player_id)

# CS:GO
cs_stats = cs_steam_stats(steam_key, player_id)

# PAYDAY 2
payday_stats = payday2_steam_stats(steam_key, player_id)

d = {"cabinet_miem": cabinet_info, "steam_genera": steam_stats, "cs_stats": cs_stats, "payday_stats": payday_stats}
with open("data/data.json", mode='w', encoding='utf-8') as file:
    json.dump(d, file, ensure_ascii=False, indent=4)
    print(d)
