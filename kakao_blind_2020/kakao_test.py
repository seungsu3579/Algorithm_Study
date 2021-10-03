import requests
import json 

# GET 
def rest_get(url):
    response = requests.get(url) 
    return json.loads(response.text)

def rest_get_raw(url, header):
    response = requests.get(url, headers=header) 
    return json.loads(response.text)

# POST (JSON) 
def rest_post(url, token, data):
    header = {'X-Auth-Token': token, 'Content-Type': 'application/json; chearset=utf-8'}
    response = requests.post(url, data=json.dumps(data), headers=header) 
    return json.loads(response.text)

def rest_post_raw(url, header, data):
    response = requests.post(url, data=json.dumps(data), headers=header) 
    return json.loads(response.text)

# PUT (JSON)
def rest_put_raw(url, header, data):
    response = requests.put(url, data=json.dumps(data), headers=header)
    return json.loads(response.text)

######################################################
BASE_URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
X_AUTH_TOKEN = "ed99770e51cc89c9937ec8ce68eaeb2a"

# get location info
def get_location(auth_key):
    url = f"{BASE_URL}/locations"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    location = rest_get_raw(url, header)
    return location

# get truck info
def get_truck(auth_key):
    url = f"{BASE_URL}/trucks"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    truck = rest_get_raw(url, header)
    return truck

def put_simulate(auth_key, data):
    url = f"{BASE_URL}/simulate"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    simulate = rest_put_raw(url, header, data)
    return simulate

def get_score(auth_key):
    url = f"{BASE_URL}/score"
    header = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    score = rest_get_raw(url, header)
    return score

def find_max_loc(truck, MAX_LOC, location, MEAN):
    value = 100000
    answer = (-1, -1)
    for loc, k in MAX_LOC:
        if location['locations'][loc]['located_bikes_count'] > MEAN:
            v = loc - truck['location_id']
            x = v // 5
            y = v % 5
            for i in range(src + 1, src+y+1, 1 if src+y > src else -1):
                if i % 5 == 0:
                    x += 1
                    y += -5

            if abs(x) + abs(y) < value:
                value = abs(x) + abs(y)
                answer = (truck, loc)
    print(answer)
    return answer


def find_truck(trucks, loc):
    value = 100000
    answer = -1
    
    for tr in trucks:
        v = loc - tr['location_id']
        x = v // 5
        y = v % 5
        for i in range(src + 1, src+y+1, 1 if src+y > src else -1):
            if i % 5 == 0:
                x += 1
                y += -5
        
        if abs(x) + abs(y) == value:
            answer = answer if answer['loaded_bikes_count'] > tr['loaded_bikes_count'] else tr
        elif abs(x) + abs(y) < value:
            value = abs(x) + abs(y)
            answer = tr
            
    return answer, value


def truck_move_plan(src, dst):
    v = dst - src
    x = v // 5
    y = v % 5
    for i in range(src + 1, src+y+1, 1 if src+y > src else -1):
        if i % 5 == 0:
            x += 1
            y += -5
    
    plan = []
    for i in range(abs(x)):
        if x > 0:
            plan.append(2)
        else:
            plan.append(4)
    for i in range(abs(y)):
        if y > 0:
            plan.append(1)
        else:
            plan.append(3)
    
    return plan
    

if __name__ == "__main__":
    # start api
    url = f"{BASE_URL}/start"
    data = {"problem": 1}
    start = rest_post(url, X_AUTH_TOKEN, data)
    auth_key = start["auth_key"]

    while True:

        command = [{"truck_id": i, "command": []} for i in range(5)]

        # get info
        location = get_location(auth_key)
        truck = get_truck(auth_key)

        # check status
        MAX_LOC = []
        MIN_LOC = []
        MEAN = round(sum(list(map(lambda x: x['located_bikes_count'],location['locations'])))/len(location['locations']))
        for loc in location['locations']:
            if loc["located_bikes_count"] > MEAN:
                MAX_LOC.append((loc["id"], loc["located_bikes_count"]))
            elif loc["located_bikes_count"] < MEAN:
                MIN_LOC.append((loc["id"], loc["located_bikes_count"]))

        MAX_LOC.sort(key=lambda x : -x[1])
        MIN_LOC.sort(key=lambda x : x[1])
        
        # make command
        if len(MAX_LOC) != 0 and len(MIN_LOC) != 0:

            # 이미 bike 싣고 있음
            loaded_trucks = list(filter(lambda tr : tr['loaded_bikes_count'] >= 2, truck["trucks"]))

            # bike가 없는 경우
            unloaded_trucks = list(filter(lambda tr : tr['loaded_bikes_count'] < 2, truck["trucks"]))
            tmp_dict = {}
            for tr in unloaded_trucks:
                tr, loc = find_max_loc(tr, MAX_LOC, location, MEAN)
                if tr == -1:
                    break

                load_num = location['locations'][loc]['located_bikes_count'] - MEAN
                command[tr['id']]["command"] += truck_move_plan(truck['trucks'][tr['id']]['location_id'], loc) \
                            + [5 for i in range(load_num)]
                truck['trucks'][tr['id']] = {'id': tr['id'], 'loaded_bikes_count': load_num, 'location_id': loc}
                location['locations'][loc]['located_bikes_count'] -= load_num
                loaded_trucks.append(truck['trucks'][tr['id']])


            # 배송    
            for dst in MIN_LOC[:5]:
                
                if len(loaded_trucks) == 0:
                    break
                    
                # 운행
                dst = dst[0]
                tr, v = find_truck(loaded_trucks, dst)
                src = tr['location_id']
                plan = truck_move_plan(src, dst)

                loaded_trucks.remove(tr)
                load_num = tr['loaded_bikes_count']
                command[tr['id']]["command"] += plan + [6 for i in range(load_num)]
                location['locations'][dst]['located_bikes_count'] += load_num
                truck['trucks'][tr['id']] = {'id': tr['id'], 'loaded_bikes_count': 0, 'location_id': dst}
                # 하차

            for cmd in command:
                cmd['command'] += [0 for i in range(10 - len(cmd['command']))]
                
        result = put_simulate(auth_key, {"commands": command})

        flag = result["status"]

        if flag == "finished":
            score = get_score(auth_key)
            print(score)
            break