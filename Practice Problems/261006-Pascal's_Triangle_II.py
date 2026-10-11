# LeetCode
# 119. Pascal's Triangle II

"""
Instruction

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
"""

"""
Reference: Pascal's Triangle

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

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            row.append(1)
            
            for j in range(len(row) - 2, 0, -1):
                row[j] = row[j - 1] + row[j]

        return row

"""
Notes

When rowIndex = 3

row = [1]

when i = 1
row = [1, 1], len(row) = 2
    when j = 0 -> no iteration, r = [1, 1]

when i = 2
row = [1, 1, 1] len(row) = 3
    when j = 1 row = [1, 2, 1]

when i = 3 (last iteration)
row = [1, 2, 1, 1] len(row) = 4
    when j = 2 row = [1, 2, 3, 1]
    when j = 1 row = [1, 3, 3, 1]

return [1, 3, 3, 1]

Approach: In-place Dynamic Programming (Space-Optimized)
- Time Complexity: O(k^2) where k = rowIndex
- Space Complexity: O(k) by reusing a single list

Key Logic:
1. Start with base row [1].
2. For each row iteration, append '1' to expand the list.
3. Update elements in-place from right to left (excluding boundaries) 
   using the formula: row[j] = row[j - 1] + row[j].
4. Backward iteration prevents overwriting values needed for subsequent calculations.
"""
