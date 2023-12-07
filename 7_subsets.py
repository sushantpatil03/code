def find_subset(nums, target):
    nums.sort()
    possible_ans = []
    helper(nums, target, 0, 0, possible_ans)

def helper(nums, target, index, current_sum, possible_ans):
    if current_sum == target:
        print(possible_ans)
        return

    prev_element = -1

    for i in range(index, len(nums)):
        if prev_element != nums[i]:
            if nums[i] + current_sum > target:
                break
            possible_ans.append(nums[i])
            prev_element = nums[i]
            helper(nums, target, i + 1, current_sum + nums[i], possible_ans)
            possible_ans.pop()

if __name__ == "__main__":
    nums = [1, 2, 5, 6, 8]
    find_subset(nums, 9)
