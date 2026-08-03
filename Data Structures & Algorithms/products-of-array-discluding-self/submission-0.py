import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref_prods, suff_prods, res = [0] * n , [0] * n, [0] * n

        pref_prods[0] = suff_prods[n - 1] = 1
        for i in range(len(nums)):
            pref_prods[i] = math.prod(nums[ : i ])
            suff_prods[i] = math.prod(nums[ i + 1 : ])
        
        res = []

        for i in range(len(pref_prods)):
            res.append(pref_prods[i] * suff_prods[i])
        return res