import requests
import vk
import math
import time
import json

app_id = "7044123"
token = "6992e28f6992e28f6992e28fce69f99e94669926992e28f348f1922f8afaa0f540cc120"

# function which returns the number of members in a group
def number_of_members(group_id):
	payload = {'access_token' : token, 'v' : '5.61', 'group_id' : str(group_id),
			'fields' : 'members_count'}
	r = requests.get('https://api.vk.com/method/groups.getById', params=payload)
	number = r.json()['response'][0]['members_count']
	return number

# function which returns id of each memeber of a group
def get_members(group_id):
    res = []
    num = number_of_members(group_id)
    offset = 0
    for i in range(math.ceil(num / 1000)):
        payload = {'access_token' : token, 'v' : '5.61', 'group_id' : str(group_id), 'count' : '1000', 'offset' : str(offset)}
        r = requests.get('https://api.vk.com/method/groups.getMembers', params=payload)
        res += r.json()['response']['items']
        offset += 1000
    return res

# write ids of all users to txt file
users = get_members("30666517")
f = open("users.txt", "w")
print(users, file=f)
f.close()
