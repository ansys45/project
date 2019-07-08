import requests
import vk
import math
import time
import networkx as nx
import matplotlib.pyplot as plt
import random

app_id = "7038793"
my_id = "154930966"
token = "b4c86af9069493b2b731efdb9c109f16df5c83da7e2c0f1a592dae0301df84e1456a5e94c8351a4cd3511"
tproger = "30666517"


def number_of_subscriptions(user_id):
	try:
		payload = {'access_token' : token, 'v' : '5.65', 'user_id' : str(user_id)}
		r = requests.get('https://api.vk.com/method/groups.get', params=payload).json()
		return r['response']['count']
	except KeyError:
		return 0	

#returns an array of ids (int) of groups on which the user is subscribed
def get_subscriptions(user_id):
	subscriptions = []
	try:
		num = number_of_subscriptions(user_id)
		offset = 0
		for i in range(math.ceil(num / 1000)):
			if i % 3 == 0:
				time.sleep(1)
			payload = {'access_token' : token, 'v' : '5.61', 'user_id' : str(user_id), 
				'count' : '1000', 'offset' : str(offset)}
			r = requests.get('https://api.vk.com/method/groups.get', params=payload)
			subscriptions += r.json()['response']['items']
			offset += 1000

		return subscriptions

	except KeyError:
		return subscriptions


#returns the name (str) of the group by its id
def get_group_name(group_id):
	payload = {'access_token' : token, 'v' : '5.61', 'group_id' : str(group_id)}
	r = requests.get('https://api.vk.com/method/groups.getById', params=payload)
	name = r.json()['response'][0]['name']
	return name


#returns the numbers (int) of members of the community by its id
def number_of_members(group_id):
	payload = {'access_token' : token, 'v' : '5.61', 'group_id' : str(group_id), 
			'fields' : 'members_count'}
	r = requests.get('https://api.vk.com/method/groups.getById', params=payload)
	number = r.json()['response'][0]['members_count']
	return number


#returns an array of ids (int) of the group on members
def get_members(group_id):
	res = []
	num = number_of_members(group_id)
	offset = 0
	for i in range(math.ceil(num / 1000)):
		if i % 3 == 0:
			time.sleep(1)

		payload = {'access_token' : token, 'v' : '5.61', 'group_id' : str(group_id), 
			'count' : '1000', 'offset' : str(offset)}
		r = requests.get('https://api.vk.com/method/groups.getMembers', params=payload)
		res += r.json()['response']['items']
		offset += 1000
	return res

#returns an array of ids (int) of the user's friends
def get_friends(user_id):
	friends = []
	try:
		payload = {'access_token' : token, 'v' : '5.1', 'user_id' : str(user_id)}
		r = requests.get('https://api.vk.com/method/friends.get', params=payload)
		friends = r.json()['response']['items']
		return friends
	except KeyError:
		return friends

#returns the real name of the user (str)
def get_user_name(user_id):
	try:
		payload = {'access_token' : token, 'v' : '5.52', 'user_id' : user_id}
		r = requests.get('https://api.vk.com/method/users.get', params=payload)
		name = r.json()['response'][0]['first_name'] + " " + r.json()['response'][0]['last_name']
		return name
	except KeyError:
		pass

def sex(user_id):
	try:
		payload = {'access_token' : token, 'v' : '5.101', 'user_id' : str(user_id), 'fields' : 'sex'}
		r = requests.get('https://api.vk.com/method/users.get', params=payload)
		sex = r.json()['response'][0]['sex']
		return sex
	except KeyError:
		pass

def country(user_id):
	try:
		payload = {'access_token' : token, 'v' : '5.52', 'user_id' : str(user_id), 'fields' : 'country'}
		r = requests.get('https://api.vk.com/method/users.get', params=payload)
		country = r.json()['response'][0]['country']['id']
		return country
	except KeyError:
		pass