"""Берем данные о пользователе из cabinet miem,
 данные о steam аккаунте, статистику из CS:GO и PAYDAY 2"""

from dotenv import load_dotenv
from funcs import *

load_dotenv()

student_id = os.getenv("USER_CABINET_ID")
player_id = os.getenv("PLAYER_ID")
steam_key = os.getenv("STEAM_API_KEY")

# CABINET MIEM INFO
RESPONSE = cabinet_student_text(student_id)
# GENRAL STATS
steam_stats = steam_profile_stats(steam_key,player_id)

# CS:GO
cs_stats = cs_steam_stats(steam_key,player_id)

# PAYDAY 2
payday_stats = payday2_steam_stats(steam_key,player_id)

arr = [RESPONSE, steam_stats, cs_stats, payday_stats]
with open("answer.txt", mode='w', encoding='utf-8') as file:
    for el in arr:
        file.write(el + '\n' + "-" * 100 + '\n')
        print(el + '\n' + "-" * 100 + '\n')
