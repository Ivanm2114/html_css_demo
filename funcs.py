import requests
import zulip


# CABINET MIEM INFO
def get_cabinet_student(student_id):
    response = requests.get(f"https://cabinet.miem.hse.ru/public"
                            f"-api/student_"
                            f"statistics/{student_id}", timeout=1).json()
    return response


# CABINET MIEM INFO
def get_gitlab_data(private_token):
    response = requests.get("https://git.miem.hse.ru/api/v4/projects/9594"
                            "/repository/branches", timeout=1,
                            params={"PRIVATE-TOKEN": private_token}).json()
    return response


def get_zulip_data(user_id, key, email, url):
    client = zulip.Client(email=email, api_key=key, site=url)
    result = client.get_user_by_id(user_id)
    return result


# GENRAL STATS
def get_steam_profile_stats(key, steam_id):
    steam_stats = requests.get(
        f"http://api.steampowered.com/"
        f"ISteamUser/GetPlayerSummaries/"
        f"v0002/?key={key}&steamids={steam_id}", timeout=1).json()
    return steam_stats


def get_cs_steam_stats(key, steam_id):
    cs_stats = requests.get(
        f"http://api.steampowered.com/"
        f"ISteamUserStats/GetUserStatsForGame/"
        f"v0002/?appid=730&key={key}&steamid={steam_id}", timeout=1).json()
    return cs_stats


def get_payday2_steam_stats(key, steam_id):
    payday_stats = requests.get(
        f"http://api.steampowered.com/"
        f"ISteamUserStats/GetUserStatsForGame/"
        f"v0002/?appid=218620&key={key}&steamid={steam_id}", timeout=1).json()
    return payday_stats


def find_last_commited_branch(gitlab_json):
    last_commited_branch_json = gitlab_json[0]
    for i in range(1, len(gitlab_json)):
        if gitlab_json[i]["commit"]["created_at"] > \
                last_commited_branch_json["commit"]["created_at"]:
            last_commited_branch_json = gitlab_json[i]
    return last_commited_branch_json


def get_value_from_steam_game_stats(game_json, field):
    for el in game_json["playerstats"]["stats"]:
        if el["name"] == field:
            return el["value"]
    return -1


def prepare_data(input_data):
    data = {}
    photo_s = "https://chat.miem.hse.ru" + \
              input_data["zulip_json"]["user"]["avatar_url"]
    photo_list = list(photo_s)
    photo_list.insert(photo_s.find("?") - 4, "-medium")
    photo_s = ''.join(photo_list)
    data["email"] = input_data["zulip_json"]["user"]["email"]
    data["photo"] = photo_s
    data["branch_amount"] = len(input_data["gitlab_json"])
    last_commited_branch_json =\
        find_last_commited_branch(input_data["gitlab_json"])
    data["last_commited_branch"] = last_commited_branch_json["name"]
    data["last_commit_title"] = last_commited_branch_json["commit"]["title"]
    data["amount_of_games_won"] = \
        get_value_from_steam_game_stats(input_data["cs_json"],
                                        "total_matches_won")
    data["succed_heists"] = \
        get_value_from_steam_game_stats(input_data["payday2_json"],
                                        "heist_success")
    return data
