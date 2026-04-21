class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums[-1] % k

    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        my_set = set(friends)
        answer = []
        for number in order:
            if number in friends:
                answer.append(number)
        return answer

    def buildArray(nums):
        middle = []
        for element in nums:
            middle.append(nums[element])
        return middle

    def minimumOperations(self, nums):
        answer: int = 0
        for element in nums:
            if 0 != element % 3:
                answer += 1
        return answer

    def finalValueAfterOperations(self, operations):
        value = 0
        for operation in operations:
            value = (value + 1) if ("+" == operation[1]) else (value - 1)
        return value
