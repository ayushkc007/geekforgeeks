class Solution:
    def get_min_max(self, arr):
        n = len(arr)
        if len == 1:
            return [arr[0], arr[0]]

        min, max = (arr[0],arr[0])
        for i in range(n - 1):
            if min > arr[i + 1]:
                min = arr[i + 1]
            if max < arr[i + 1]:
                max = arr[i + 1]
        return [min, max]

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1