class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # just a binary search through sorted rows but you flatten the matrix
        # and treat it like one long row (given some index to retrive the value
        # its matrix[mid//n][mid%n]) so for the row its n (length of rows) to
        # see how many rows are before and cols is the remainder of row length

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (r + l) // 2
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False