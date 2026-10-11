# LeetCode
# 118. Pascal's Triangle

"""
Instruction

Given an integer numRows, return the first numRows of Pascal's triangle.
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        temp = [1]

        for i in range(1, numRows):
            for j in range(1, len(triangle[i - 1])):
                temp.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            temp.append(1)
            triangle.append(temp)
            temp = [1]

        return triangle

"""
Notes

Two iterations needed: row and elements in each row
iteration 1: in range(1, numRows) since the first row is always [1]
iteration 2: in range(1, len(triangle[i - 1])) the first element is always 1, so skip the first element.
Add j - 1 and j of previous row and store it in temp
Add last 1 to temp
Add temp to triangle as a list

return triangle
"""