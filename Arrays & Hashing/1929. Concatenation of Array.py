#this thing is very easy if you know how to use the append function in python
#just append the elements of the array to the new array and return the new array
#or you can use the + operator to concatenate the arrays
#or you can use the extend function to extend the array
#all of these methods are very easy to use and are very efficient

#Below I'm using list comprehension to solve the problem
#I'm iterating the list twice and adding the elements to the new list

#Time complexity: O(n)
#Space complexity: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [x for _ in range(2) for x in nums]
    

#Alternatives

# Method 1: Using + operator
def getConcatenation(self, nums: List[int]) -> List[int]:
    return nums + nums  # O(n) space

# Method 2: Using extend()
def getConcatenation(self, nums: List[int]) -> List[int]:
    ans = nums.copy()  # O(n) space
    ans.extend(nums)
    return ans

# Method 3: Using multiplication
def getConcatenation(self, nums: List[int]) -> List[int]:
    return nums * 2  # O(n) space