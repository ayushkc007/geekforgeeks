class Solution:
    def peakElement(self, arr, n):
        # Code here
        if n == 1:
            return 0
        for i in range(n):
            if i == 0 and arr[i] >= arr[i + 1]:
                return i
            elif i == n - 1 and (arr[i] >= arr[i - 1]):
                return i
            elif arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return i
        return None


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] >= arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] >= arr[index - 1]:
                flag = True
            elif arr[index - 1] <= arr[index] and arr[index] >= arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)

# Input Format:
# The first input is an integer t, indicating the number of test cases.
# The second input is an integer n, specifying the length of the array.
# The third input contains n space-separated integers, representing the array arr[].
