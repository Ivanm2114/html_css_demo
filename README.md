# About program

This code takes personal data from cabinet.meim and steam stats like your profile stats and CS:GO and PAYDAY 2 stats,
creates JSON and put it to html template.

# How to start
1. Download all libraries using 
```
pip install -r requirements.txt
```
2. Create .env file and write there variable
```
   USER_CABINET_ID = your cabinet.miem id number
   PLAYER_ID = Steam_id, you can get it on "about account" page
   STEAM_API_KEY = your key, you can get on https://steamcommunity.com/dev/apikey
   GITLAB_TOKEN = your gitlab_token, you can get yours on https://git.miem.hse.ru/-/profile/personal_access_tokens
   ZULIP_ID = your zulip id, you can watch on profile of every user
   ZULIP_API_KEY = your key, can be found on https://chat.miem.hse.ru/#settings/account-and-privacy
   ZULIP_EMAIL = your email which you use to login into zulip
   ZULIP_URL = your zulip-server address
```
3. Run programm

4. Get your template is at `templates/ready.html`

## Credits
Programm is written by Ivan Mityushkin БИВ224
