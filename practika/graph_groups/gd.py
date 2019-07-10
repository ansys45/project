import community
import requests
import vk
import math
import time
import networkx as nx
import matplotlib.pyplot as plt
import random
from karger import change_graph, remove_loops, choose_random_edge, contract_edge, Kar, merge
from vk_api import number_of_subscriptions, get_subscriptions, get_group_name, number_of_members, get_members, get_friends, get_user_name, sex, country 

 
app_id = "7038793"
my_id = "154930966"
token = ""
tproger = "30666517"


def NXGr(graph):
	res = nx.Graph()
	for node in list(graph.keys()):
		res.add_node(node)
	for node in list(graph.keys()):
		for node2 in graph[node]:
			res.add_edge(node, node2)
	return res

def dfs(graph, vertex, path=set()):
    path.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs(graph, neighbor, path)
    return path

def part_of_male(array):
	l = len(array)
	c = 0
	for i in array:
		if sex(i) == 0:
			l -= 1
		if sex(i) == 2:
			c += 1
	return (c / l) * 100

def H1(group1, group2):
	v1 = part_of_male(group1)
	v2 = part_of_male(group2)
	if abs((v1 + v2) - 100) < 30:
		return True
	return False


def common_country(array):
	c = {}
	l = len(array)
	for i in array:
		co = country(i)
		if not co in c:
			c[co] = 0
		c[co] += 1
	for i in c:
		if c[i] == l / 2:
			return i
	return 0

def H2(group1, group2):
	if common_country(group1) and common_country(group2):
		if common_country(group1) != common_country(group2):
			return True
	return False

def luiH1(group):
	val = part_of_male(group)
	if val > 60 or val < 26:
		return True
	return False


def luiH2(group):
	if common_country(group):
		return True
	return False


def main():
	# file = open("members.txt", "r")
	# f = file.read().split(',') #list of str

	# # creating a dictionary of users and their groups
	# members = {} 
	# member_ids = []
	# o = open("input.txt", "w")
	# c = 0
	# for i in range(500):
	# 	user = f[i][1:]
	# 	if (number_of_subscriptions(user)):
	# 		user_s = get_subscriptions(user)
	# 		members[user] = user_s
	# 		member_ids.append(user)

	# 		#saving to the file to use in future
	# 		o.write("#" + user + ":\n")
	# 		for g in user_s:
	# 			o.write(str(g) + ", ")
	# 		o.write("\n\n")

	# 		if c == 50:
	# 			break
	# 		c += 1


	# # creating the graph of users by the rule of connection:  
	# # users have more tnan 7 communities in common
	# # using NetWorkX library to visualize the graph
	# people = {}
	# G = nx.Graph()
	# for u in member_ids:
	# 	people[u] = []
	# for u1 in member_ids:
	# 	for u2 in member_ids:
	# 		G.add_node(u1)
	# 		G.add_node(u2)
	# 		if u1 != u2:
	# 			s1 = set(members[u1])
	# 			s2 = set(members[u2])
	# 			inter = s1.intersection(s2)
	# 			if len(inter) > 5:
	# 				G.add_edge(u1, u2)
	# 				people[u1].append(u2)
		
	# # keeping only the largest connected component
	# pathes = []
	# cc = []
	# for i in people:
	#     pathes.append(dfs(people, i, path = set()))
	# for i in pathes:
	#     if len(i) > len(cc):
	#         cc = i
	# connected_component = {}
	# for i in cc:
	#     connected_component[i] = people[i]


	# # creating two groups for KARGER
	# new_g = change_graph(connected_component)
	# while len(new_g) > 2:
	# 	contract_edge(choose_random_edge(new_g), new_g)
	

	# nxpeople = NXGr(people)



	# kar = open("karger.txt", "a")
	# keys = list(new_g.keys())
	# group1 = list(keys[0])
	# group2 = list(keys[1])
	# print(group1, file = kar)
	# print(group2, file = kar)
	
	# # HYPOTHESIS 1 sex division
	# if H1(group1, group2):
	# 	print("H1 is TRUE")
	# else:
	# 	print("H1 is FALSE")


	# # HYPOTHESIS 2 common country
	# if H2(group1, group2):
	# 	print("H2 is TRUE")
	# else:
	# 	print("H2 is FALSE")


	# # Louivain 
	# partition = community.best_partition(G)
	# new = nx.Graph()
	# new.add_edges_from([pair for pair in partition.items() if pair[1]==1])

	# we have got 4 groups of nodes. Lets chech our hypothresis on them:

	#groups
	group1 = ['510', '640', '914', '1829', '1843', '2192', '2298', '2601', '2752', '2933', '3427']
	group2 = ['510', '640', '914', '1127', '1566', '1630', '1749', '1754', '1829', '2192', '2298', '2601', '2752', '2933', '2982']
	group3 = ['510', '640', '914', '1127', '1754', '1829', '2192', '2298', '2601', '2752', '2756', '2933']
	group4 = ['510', '640', '914', '1211', '1607', '1754', '1829', '1843', '2192', '2298', '2601', '2752']

	groups = [group1, group2, group3, group4]
	for i in groups:
		if luiH1(i):
			print("H1 is TRUE")
		else:
			print("H1 is FALSE") 

	for i in groups:
		if luiH2(i):
			print("H2 is TRUE")
		else:
			print("H2 is FALSE") 

	# drawing graphs 
	# nx.draw(new, with_labels = True, node_size = 20)
	# nx.draw(nxcc, with_labels = True, node_size = 20)
	plt.show()
	


if __name__ == '__main__':
	main()



	
