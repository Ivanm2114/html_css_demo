import os
import requests


# CABINET MIEM INFO
def cabinet_student_text(student_id):
    RESPONSE = requests.get(f"https://cabinet.miem.hse.ru/public"
                            f"-api/student_"
                            f"statistics/{student_id}", timeout=1).text
    RESPONSE = bytes(RESPONSE, "utf-8").decode("unicode_escape")
    return RESPONSE


# GENRAL STATS
def steam_profile_stats(key, steam_id):
    steam_stats = requests.get(
        f"http://api.steampowered.com/"
        f"ISteamUser/GetPlayerSummaries/"
        f"v0002/?key={key}&steamids={steam_id}", timeout=1).text
    return steam_stats


def cs_steam_stats(key, steam_id):
    cs_stats = requests.get(
        f"http://api.steampowered.com/"
        f"ISteamUserStats/GetUserStatsForGame/"
        f"v0002/?appid=730&key={key}&steamid={steam_id}", timeout=1).text
    return cs_stats


def payday2_steam_stats(key, steam_id):
    payday_stats = requests.get(
        f"http://api.steampowered.com/"
        f"ISteamUserStats/GetUserStatsForGame/"
        f"v0002/?appid=218620&key={key}&steamid={steam_id}", timeout=1).text
    return payday_stats
