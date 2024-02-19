def func(strs):
    if strs == "":
        return 0
    elif type(strs) != str:
        return 0
    elif strs == " ":
        return 0
    index1 = 0
    if strs[index1] == "-":
        return -int(strs[1:])
    index = 0
    while index == "0" and index < len(strs):
        index += 1
    return int(strs[index:])
    tmp = []
    for i in strs:
       if i < 96 and i > 48:
           tmp.append(i)
    return int("".join(tmp))

print(type(func("1234")))
print(func("0234"))
