class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            result = [[1]]
        elif numRows == 2:
            result = [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
            for n in range(3, numRows + 1):
                l = result[-1]
                new = []
                is_odd = n % 2 > 0
                k = int(((n + 1) / 2)) if is_odd else int(n / 2)
                for i in range(k):
                    new_number = l[0] if i == 0 else l[i] + l[i - 1]
                    new.append(new_number)
                if is_odd:
                    new = new + new[-2::-1]
                else:
                    new = new + new[::-1]
                result.append(new)
        return result


# More elegant solution
"""
1. Set the length for each row first
2. Set the first and last elements
"""


class Solution:
    def generate(self, num_rows):
        triangle = []
        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle


if __name__ == "__main__":
    solution = Solution()
    num_row = 5
    print(solution.generate(num_row))
