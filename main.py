"""Берем данные о пользователе из cabinet miem"""
import os
import requests
from dotenv import load_dotenv
import codecs

load_dotenv()

student_id = os.getenv("USER_CABINET_ID")
player_id = os.getenv("PLAYER_ID")
key = os.getenv("STEAM_API_KEY")

response = requests.get(f"https://cabinet.miem.hse.ru/public"
                        f"-api/student_"
                        f"statistics/{student_id}", timeout=1).text

print(response)

# GENRAL STATS
steam_stats = requests.get(
    f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={player_id}").text
print(steam_stats)

# CS:GO
cs_stats = requests.get(
    f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={key}&steamid={player_id}").text
print(cs_stats)

# PAYDAY 2
payday_stats = requests.get(
    f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=218620&key={key}&steamid={player_id}").text
print(payday_stats)

arr = [response, steam_stats, cs_stats, payday_stats]
with open("answer.txt", mode='w', encoding='utf-8') as file:
    # CABINET MIEM INFO
    for el in arr:
        file.write(el + '\n')
