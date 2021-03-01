import requests
import json
newDict = dict()

change_from = input()
url = 'http://www.floatrates.com/daily/' + change_from + ".json"
response = requests.get(url)
json_data = json.loads(response.text)
if change_from != 'usd':
    newDict["usd"] = json_data['usd']
if change_from != 'eur':
    newDict["eur"] = json_data['eur']

while True:
    try:
        change_to = input()
        if change_to == "":
            break
        amount = int(input())
        key = str(change_from) + str(change_to)
        print("Checking the cache...")
        if key in newDict or change_to in newDict:
            print("Oh! It is in the cache!")
            if key in newDict:
                final_thing = newDict[key]['rate'] * int(amount)
            else:
                final_thing = newDict[change_to]['rate'] * int(amount)
            print(f'You received {round(final_thing, 2)} {change_to.upper()}.')
        else:
            print("Sorry, but it is not in the cache!")
            url = 'http://www.floatrates.com/daily/' + change_from + '.json'
            response = requests.get(url)
            json_data = json.loads(response.text)
            newDict[key] = json_data[change_to.lower()]
            final_thing = newDict[key]['rate'] * int(amount)
            print(f'You received {round(final_thing, 2)} {change_to.upper()}.')
    except EOFError:
        break
