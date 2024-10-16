class Solution:
     def reverseString(self, s: str) -> str:
        return s[::-1]

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        ob = Solution()
        print(ob.reverseString(s))
        t = t - 1
