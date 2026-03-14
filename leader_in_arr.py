# def majorityElement(nums):
#
#     candidate1 = None
#     candidate2 = None
#     count1 = 0
#     count2 = 0
#
#     for num in nums:
#
#         if candidate1 == num:
#             count1 += 1
#
#         elif candidate2 == num:
#             count2 += 1
#
#         elif count1 == 0:
#             candidate1 = num
#             count1 = 1
#
#         elif count2 == 0:
#             candidate2 = num
#             count2 = 1
#
#         else:
#             count1 -= 1
#             count2 -= 1
#
#
#     result = []
#     n = len(nums)
#
#     if nums.count(candidate1) > n//3:
#         result.append(candidate1)
#
#     if nums.count(candidate2) > n//3:
#         result.append(candidate2)
#
#     return result
#
#
# nums = [1,2,3,1,1,2,2]
#
# print(majorityElement(nums))

#
# nums = [1,2,3,1,1,2,2]
#
#
# res = []
# count_dict = {}
#
#
# for i in range(len(nums)):
#
#     if nums[i] in count_dict:
#         count_dict[nums[i]] += 1
#     else:
#         count_dict[nums[i]] = 1
#
# print(count_dict)
#
# for j in count_dict:
#     if count_dict[j] > len(nums) // 3:
#         res.append(j)
#
# print(res)
#
#


#
# def majorityElement(nums):
#
#     candidate1 = None
#     candidate2 = None
#     count1 = 0
#     count2 = 0
#
#     for num in nums:
#
#         if candidate1 == num:
#             count1 += 1
#
#         elif candidate2 == num:
#             count2 += 1
#
#         elif count1 == 0:
#             candidate1 = num
#             count1 = 1
#
#         elif count2 == 0:
#             candidate2 = num
#             count2 = 1
#
#         else:
#             count1 -= 1
#             count2 -= 1
#
#
#     result = []
#     n = len(nums)
#
#     if nums.count(candidate1) > n//3:
#         result.append(candidate1)
#
#     if nums.count(candidate2) > n//3:
#         result.append(candidate2)
#
#     return result
#
#
# nums = [1,2,3,1,1,2,2]
#
# print(majorityElement(nums))





