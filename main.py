from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for index in range(len(nums)):
        for counter in range(index + 1, len(nums)):
            if nums[index] + nums[counter] == target:
                print("Output:", [index, counter])
                return [index, counter]

    return []
def main():
    twoSum([0,1,2,3,4], 7)

if __name__ =="__main__":
    main() 
