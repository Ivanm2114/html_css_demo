"""Берем данные о пользователе из cabinet miem"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

student_id = os.getenv("USER_CABINET_ID")
player_id = os.getenv("PLAYER_ID")
key = os.getenv("STEAM_API_KEY")

RESPONSE = requests.get(f"https://cabinet.miem.hse.ru/public"
                        f"-api/student_"
                        f"statistics/{student_id}", timeout=1).text
RESPONSE = bytes(response, "utf-8").decode("unicode_escape")

print(RESPONSE)

# GENRAL STATS
steam_stats = requests.get(
    f"http://api.steampowered.com/"
    f"ISteamUser/GetPlayerSummaries/"
    f"v0002/?key={key}&steamids={player_id}", timeout=1).text
print(steam_stats)

# CS:GO
cs_stats = requests.get(
    f"http://api.steampowered.com/"
    f"ISteamUserStats/GetUserStatsForGame/"
    f"v0002/?appid=730&key={key}&steamid={player_id}", timeout=1).text
print(cs_stats)

# PAYDAY 2
payday_stats = requests.get(
    f"http://api.steampowered.com/"
    f"ISteamUserStats/GetUserStatsForGame/"
    f"v0002/?appid=218620&key={key}&steamid={player_id}", timeout=1).text
print(payday_stats)

arr = [RESPONSE, steam_stats, cs_stats, payday_stats]
with open("answer.txt", mode='w', encoding='utf-8') as file:
    # CABINET MIEM INFO
    for el in arr:
        file.write(el + '\n')
