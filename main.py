class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Solution using dictionary
        frequency = {}
        for number in nums:
            if number not in frequency:
                frequency[number] = 1
            else:
                return True
        return False

        ## Note that using the dictionary is superfluous since you don't need the frequency. Using a set is actually better designed for this.

        # Solution using set
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
