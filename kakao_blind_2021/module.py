import requests
import json 
from pprint import pprint


# GET 
def rest_get(url):
    response = requests.get(url) 
    # print(str(response.status_code) + " | " + response.text) 
    return json.loads(response.text)

def rest_get_raw(url, header):
    response = requests.get(url, headers=header) 
    return json.loads(response.text)

# POST (JSON) 
def rest_post(url, token, data):
    header = {'X-Auth-Token': token, 'Content-Type': 'application/json; chearset=utf-8'}
    response = requests.post(url, data=json.dumps(data), headers=header) 
    # print(str(response.status_code) + " | " + response.text)
    return json.loads(response.text)

def rest_post_raw(url, header, data):
    response = requests.post(url, data=json.dumps(data), headers=header) 
    return json.loads(response.text)

def rest_put_raw(url, header, data):
    response = requests.put(url, data=json.dumps(data), headers=header)
#     print(str(response.status_code) + " | " + response.text)
    return json.loads(response.text)


BASE_URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
LEADER_BOARD_URL = 'https://si1kddo29f.execute-api.ap-northeast-2.amazonaws.com/prod/leaderboard'
X_AUTH_TOKEN = "a21ffa7f526d9fa87ec8107ddf9926bf"

#  start 
def startAPI(problem):
    url = f"{BASE_URL}/start"
    data = {"problem": problem}
    start = rest_post(url, X_AUTH_TOKEN, data)
    auth_key = start["auth_key"]
    return auth_key


# waiting line API return List
def waitingLineAPI(auth_key):
    url = f"{BASE_URL}/waiting_line"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    waitingLine = rest_get_raw(url, header)
    return waitingLine["waiting_line"]

# game result API return List
def gameResultAPI(auth_key):
    url = f"{BASE_URL}/game_result"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    gameResult = rest_get_raw(url, header)
    return gameResult["game_result"]

# user info API return List
def userInfoAPI(auth_key):
    url = f"{BASE_URL}/user_info"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    userInfo = rest_get_raw(url, header)
    userInfoDict = dict()
    for user in userInfo["user_info"]:
        userInfoDict[user['id']] = user
    return userInfoDict

# match API
def matchAPI(data, auth_key):
    url = f"{BASE_URL}/match"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    match = rest_put_raw(url, header, data)
    return match

# change grade API -> decide after game result 
def changeGradeAPI(data, auth_key):
    url = f"{BASE_URL}/change_grade"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    changeGrade = rest_put_raw(url, header, data)
    return changeGrade

# 등급의 범위는 0 이상 9,999 이하 정수
# data format
# data = {
#     "commands": [
#         { "id": 1, "grade": 1900 }
#          ...
#     ]
# }

# get score API
def scoreAPI(auth_key):
    url = f"{BASE_URL}/score"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    score = rest_get_raw(url, header)
    return score

def status_print(auth_key):
    from pprint import pprint
    waiting = waitingLineAPI(auth_key)
    result = gameResultAPI(auth_key)
    if len(waiting) != 0:
        print("@ WAITING LINE")
        pprint(waiting)
        print()
    if len(result) != 0:
        print("@ GAME RESULT")
        pprint(result)