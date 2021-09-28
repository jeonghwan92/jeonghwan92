# 사용 X : 인덱스를 결과값으로 하는데 투 포인터는 정렬을 해야 하므로 인덱스가 바뀌게 된다.
def twoSum(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return left, right
