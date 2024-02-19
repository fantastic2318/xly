class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 矩阵转置 将原矩阵按照对角线翻转（互换）
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 按照行反转
        for i in range(len(matrix)):
            matrix[i].reverse()
            #reversed(matrix)

        return matrix

s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))


