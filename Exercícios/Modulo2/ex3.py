list1 = [1,2,3]
list2 = [4,5,6]

def sunlist(list1,list2):
    res = []
    for i in range(len(list1)):
        res.append(list1[i] + list2[i])
    return res

print(sunlist(list1,list2))
