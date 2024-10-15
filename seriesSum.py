class Solution:
    # For higher of n this approach shall use more memory
    # def seriesSum(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     return n + self.seriesSum(n - 1)

    # Expected Time Limit exceed
    # def seriesSum(self, n: int) -> int:
    #     sum=0
    #     for i in range(1,n+1):
    #         sum+=i
    #     return sum

    # Test case failed 111861738879538208
    # def seriesSum(self, n: int) -> int:
    #     return int(n*(n+1)/2)

    def seriesSum(self, n: int) -> int:
        """
        Calculates the sum of the first 'n' natural numbers using the formula: n * (n + 1) // 2.

        This method efficiently computes the sum by avoiding the need for loops or recursion.
        It uses integer division (//) to prevent precision issues that might occur with floating-point division,
        especially for very large values of 'n'. While Python handles arbitrary precision integers well,
        this ensures accuracy across all environments that may rely on fixed precision.

        :param n: The number up to which the sum is calculated. Should be a non-negative integer.
        :return: The sum of the first 'n' natural numbers as an integer.
        """
        return int(n * (n + 1) // 2)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        obj = Solution()
        res = obj.seriesSum(n)

        print(res)

# Input Format:
# The first input is an integer t, indicating the number of test cases.
# The second input is an integer n.
