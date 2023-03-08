"""Берем данные о пользователе из cabinet miem, данные о steam аккаунте, статистику из CS:GO и PAYDAY 2"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

student_id = os.getenv("USER_CABINET_ID")
player_id = os.getenv("PLAYER_ID")
key = os.getenv("STEAM_API_KEY")

# CABINET MIEM INFO
RESPONSE = requests.get(f"https://cabinet.miem.hse.ru/public"
                        f"-api/student_"
                        f"statistics/{student_id}", timeout=1).text
RESPONSE = bytes(RESPONSE, "utf-8").decode("unicode_escape")

# GENRAL STATS
steam_stats = requests.get(
    f"http://api.steampowered.com/"
    f"ISteamUser/GetPlayerSummaries/"
    f"v0002/?key={key}&steamids={player_id}", timeout=1).text

# CS:GO
cs_stats = requests.get(
    f"http://api.steampowered.com/"
    f"ISteamUserStats/GetUserStatsForGame/"
    f"v0002/?appid=730&key={key}&steamid={player_id}", timeout=1).text

# PAYDAY 2
payday_stats = requests.get(
    f"http://api.steampowered.com/"
    f"ISteamUserStats/GetUserStatsForGame/"
    f"v0002/?appid=218620&key={key}&steamid={player_id}", timeout=1).text

arr = [RESPONSE, steam_stats, cs_stats, payday_stats]
with open("answer.txt", mode='w', encoding='utf-8') as file:
    for el in arr:
        file.write(el + '\n' + "-" * 100 + '\n')
        print(el + '\n' + "-" * 100 + '\n')
