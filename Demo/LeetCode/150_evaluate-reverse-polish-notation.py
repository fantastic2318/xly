def evalRPN(tokens: list[str]) -> int:
    stack = []
    for item in tokens:
        if item == "+" or item == "-" or item == "*" or item == "/":
            nums2 = int(stack.pop())
            nums1 = int(stack.pop())
            if item == "+":
                res = nums1 + nums2
                stack.append(res)
            elif item == "-":
                res = nums1 - nums2
                stack.append(res)
            elif item == "*":
                res = nums1 * nums2
                stack.append(res)
            else:
                res = int(nums1 / nums2)
                stack.append(res)
        else:
            stack.append(item)
    return stack.pop()


print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))