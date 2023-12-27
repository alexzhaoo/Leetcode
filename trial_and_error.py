# def powerset(set,index,subset):
#     if index==len(subset):
#         return 
    
#     print(subset)

#     for i in range(len(set)):
#         subset.append(set[i])
#         return powerset(set,index+1,subset)




# print(powerset([1,2],0,[]))

# Python3 program to generate power set

# str : Stores input string
# curr : Stores current subset
# index : Index in current subset, curr


def powerSet(str1, index, curr):
	n = len(str1)
	if (index == n):
		return
	print(curr)
	for i in range(index + 1, n):
		curr += str1[i]
		powerSet(str1, i, curr)
		curr = curr.replace(curr[len(curr) - 1], "")
        


if __name__=="__main__":
    str = "abc"
    powerSet(str, -1, "")
