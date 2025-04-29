# Functions & Methods:

nums = [65, 71, 23, 88]
# print(len(nums))
# print(sum(nums))
# print(min(nums), max(nums))

# .append adds element to the end
# nums.append(100)
# print(nums)

# .insert takes (index, number being added) 
# nums.insert(2, 30)
# print(nums)

# .clear() deletes all the elements in the list
# nums.clear()
# print(nums)

# .copy() creates a new copy and puts that copy in new_nums
# new_nums = nums.copy()
# print(new_nums, nums)

fruit = {'apple': 3, 'banana': 2, 'orange': 5}
# returns none is the key doesn't exist
# print(fruit.get('pear'))
# returns an error if key does not exist
# print(fruit['pear'])

items = fruit.items()
print(items)
