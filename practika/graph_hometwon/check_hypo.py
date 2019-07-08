import requests
import vk
import vk_api


def part_of_male(array):
 l = len(array)
 c = 0
 for i in array:
  if vk_api.sex(i) == 0:
   l -= 1
  if vk_api.sex(i) == 2:
   c += 1
 return (c / l) * 100


def gender_hypo(communitites):
    first = part_of_male(communitites[0])
    second = part_of_male(communitites[1])
    if first > 70 and second < 30:
        return True
    if first < 30 and second > 70:
        return True
    else:
        return False


def friends_hypo(communities):
    res = [True, True]
    for i1 in communities[0]:
        friends = vk_api.get_friends(i1)
        for i2 in communities[0]:
            if i1 == i2:
                continue
            if i2 not in friends:
                res[0] = False
                break
        if res[0] == False:
            break

    for i1 in communities[1]:
        friends = vk_api.get_friends(i1)
        for i2 in communities[1]:
            if i1 == i2:
                continue
            if i2 not in friends:
                res[1] = False
                break
        if res[1] == False:
            break
    if res[0] == False or res[0] == False:
        return False

def groups_hypo(communities):

    groups1 = []
    for i in communities[0]:
        groups = set(vk_api.get_subscriptions(i))
        if len(groups) == 0:
            continue
        groups1.append(groups)
    if len(groups1) == 0:
        return False
    groups = groups1[0]
    for i in groups1:
        groups = groups.intersection(i)
        if len(groups) == 0:
            return False

    groups2 = []
    for i in communities[1]:
        groups = set(vk_api.get_subscriptions(i))
        if len(groups) == 0:
            continue
        groups2.append(groups)

    groups = groups2[0]
    for i in groups2:
        groups = groups.intersection(i)
        if len(groups) == 0:
            return False

    return True

communitites = []
with open("karger.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace(",", "")
        line = line.replace("'", "")
        line = line.split()
        communitites.append(line)

print(gender_hypo(communitites))
print(friends_hypo(communitites))
print(groups_hypo(communitites))

# check three hypotesis: people in communities are friends, majority of people are of the same gender, have common groups (except tproger)
