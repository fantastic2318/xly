def reverseWords(s: str) -> str:
    s = list(s)
    last = 0
    for first in range(len(s)):
        if s[first] == " ":
            s[last:first] = reverse1(s[last:first])
            first += 1
            last = first
        if first == len(s)-1:
            s[last:first+1] = reverse1(s[last:first+1])
    return "".join(s)


def reverse1(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


print(reverseWords("God Ding"))

print(reverseWords("Let's take LeetCode contest"))

print(reverseWords("God"))