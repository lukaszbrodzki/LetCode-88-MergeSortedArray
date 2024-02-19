class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        for i in range(m + n):
            if nums1[i] == 0:
                n -= 1
                nums1[i] = nums2[n]
            if n == 0:
                break

        nums1.sort()
        print("")


if __name__ == '__main__':
    s = Solution()

    nums1 = [-1,0,0,3,3,3,0,0,0]
    m = 6
    nums2 = [1,2,2]
    n = 3
    s.merge(nums1, m, nums2, n)
