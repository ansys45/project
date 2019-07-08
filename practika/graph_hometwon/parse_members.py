import requests
import vk
import json

token= "6992e28f6992e28f6992e28fce69f99e94669926992e28f348f1922f8afaa0f540cc120"
people  = []
cities = []
petersburg = ["санкт-петербург", "питер", "spb", "спб", "peter", "saint-petersburg", "st-petersburg", "петербург"]
moscow = ["москва", "moscow"]
with open("cities.txt", "r") as c:
    for line in c.readlines():
        line = line.strip()
        cities.append(line.lower())
with open("users.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        line = line.split()
        i = 0
        for user in line:
            user = user[:-1]
            payload = {'access_token' : token, 'v' : '5.52', 'user_ids' : str(user), 'fields': 'home_town'}
            r = requests.get('https://api.vk.com/method/users.get', params=payload)
            info = r.json()["response"][0]
            if "home_town" in info:
                town = info["home_town"].lower()
                if town == " " or town == "":
                    continue
                if town in petersburg:
                    town = "санкт-петербург"
                if town in moscow:
                    town = "москва"
                if town not in cities:
                    continue
            else:
                continue
            name = info["first_name"]
            surname = info["last_name"]
            person = []
            person.append(user)
            person.append(town)
            people.append(person)
            i += 1
            if i == 1000:
                break
fout = open("t.txt", "w")
print(people, file = fout)
fout.close()

# this code opens file with all users from vk group "tproger"
# get information about each user
# if user has specified his/her hometown, than it chekcs that it is existing hometown of Russia
# if yes, it writes this user in file which will be used to draw a graph
