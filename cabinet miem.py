import requests
import os
from dotenv import load_dotenv

load_dotenv()

student_id = os.getenv("USER_CABINET_ID")


#CABINET MIEM INFO
answer = requests.get(f"https://cabinet.miem.hse.ru/public"
                      f"-api/student_statistics/{student_id}").json()
print(answer)
