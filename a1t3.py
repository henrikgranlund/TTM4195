import requests

block = 750744
blockURL = "https://chain.api.btc.com/v3/block/"

response = requests.get(blockURL+str(block))
prev_difficulty = response.json()['data']['difficulty_double']

for i in range(749960, 0, -1):
    response = requests.get(blockURL+str(i))
    difficulty = response.json()['data']['difficulty_double']
    print("Block: " +  str(i) + " Difficulty: " + str(difficulty))
    if difficulty != prev_difficulty:
        print("!!!!")
        break


