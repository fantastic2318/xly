def replaceSpace(s: str):
    index1 = len(s) - 1
    count = 0
    for i in s:
        if i == " ":
            count += 1
    total = 2 * count
    s = list(s)
    plus = ["" for i in range(total)]
    s = s + plus
    index2 = len(s) - 1
    while index1 >= 0:
        if s[index1] != " ":
            s[index2] = s[index1]
            index1 -= 1
            index2 -= 1
        else:
            s[index2-2: index2+1] = ["%","2","0"]
            index2 -= 3
            index1 -= 1
    return "".join(s)


print(replaceSpace("We are happy."))