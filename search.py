class Solution:
    def search(self, arr, x):
        try:
            return arr.index(x)
        except:
            return -1


def main():
    T = int(input().strip())
    while T > 0:
        A = [int(x) for x in input().strip().split()]
        x = int(input().strip())
        ob = Solution()
        print(ob.search(A, x))
        T -= 1


if __name__ == "__main__":
    main()
