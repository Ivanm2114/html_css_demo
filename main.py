"""Берем данные о пользователе из cabinet miem"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

student_id = os.getenv("USER_CABINET_ID")
with open("answer.txt", mode='w', encoding='utf-8') as file:
    # CABINET MIEM INFO
    answer = requests.get(f"https://cabinet.miem.hse.ru/public"
                          f"-api/student_"
                          f"statistics/{student_id}", timeout=1).text
    print(answer)
    file.write(answer)
