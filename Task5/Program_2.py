from functools import reduce

test_list = [[3,6,1],["g", 3, "o"],[9, "k", 4]]



print("The original list : " + str(test_list))
res = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], test_list, [])

print("The string instances : " + str(res))

res1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], test_list, [])

print("The integer instances : " + str(res1))