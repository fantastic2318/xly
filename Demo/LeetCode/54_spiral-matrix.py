def spiralOrder(matrix: list[list[int]]) -> list[int]:
    ans = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        if len(ans) < len(matrix) * len(matrix[0]):
            for i in range(left, right + 1):  # 从左向右
                ans.append(matrix[top][i])
            top += 1
        if len(ans) < len(matrix) * len(matrix[0]):
            for j in range(top, bottom + 1):  # 从上向下
                ans.append(matrix[j][right])
            right -= 1
        if len(ans) < len(matrix) * len(matrix[0]):
            for i in range(right, left - 1, -1):  # 从右向左
                ans.append(matrix[bottom][i])
            bottom -= 1
        if len(ans) < len(matrix) * len(matrix[0]):
            for j in range(bottom, top - 1, -1):  # 从下向上
                ans.append(matrix[j][left])
            left += 1
    return ans
# print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
#print(spiralOrder([[6,9,7]]))

