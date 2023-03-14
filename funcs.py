import requests
import zulip


# CABINET MIEM INFO
def cabinet_student(student_id):
    RESPONSE = requests.get(f"https://cabinet.miem.hse.ru/public"
                            f"-api/student_"
                            f"statistics/{student_id}", timeout=1).json()
    return RESPONSE


# CABINET MIEM INFO
def gitlab_data(private_token):
    RESPONSE = requests.get("https://git.miem.hse.ru/api/v4/projects/9594/repository/branches", timeout=1,
                            params={"PRIVATE-TOKEN": private_token}).json()
    return RESPONSE


def zulip_data(user_id, key, email, url):
    client = zulip.Client(email=email, api_key=key, site=url)
    result = client.get_user_by_id(user_id)
    return result


# GENRAL STATS
def steam_profile_stats(key, steam_id):
    steam_stats = requests.get(
        f"http://api.steampowered.com/"
        f"ISteamUser/GetPlayerSummaries/"
        f"v0002/?key={key}&steamids={steam_id}", timeout=1).json()
    return steam_stats


def cs_steam_stats(key, steam_id):
    cs_stats = requests.get(
        f"http://api.steampowered.com/"
        f"ISteamUserStats/GetUserStatsForGame/"
        f"v0002/?appid=730&key={key}&steamid={steam_id}", timeout=1).json()
    return cs_stats


def payday2_steam_stats(key, steam_id):
    payday_stats = requests.get(
        f"http://api.steampowered.com/"
        f"ISteamUserStats/GetUserStatsForGame/"
        f"v0002/?appid=218620&key={key}&steamid={steam_id}", timeout=1).json()
    return payday_stats
