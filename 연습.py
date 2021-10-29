# str = "abcdefg"
#
# for i in range(0, len(str), 2):
#     print(str[i], end=" ")
#
# for x in str:
#     print(x, end=" ")
#
# arr = [3, 8, 4, 1]
# ret: 0
# x: 3


# def solution(arr):
#    left = 0
#    right = len(arr)-1
#    while left<len(arr)//2:      #for i in range(len(arr)//2)와 같음
#        arr[left], arr[right] = arr[right], arr[left]
#        left += 1
#        right -= 1
#    return arr
#
# arr = [3, 8, 4, 1, 7]
# print(solution(arr))
#
# def solution(scores):
#    count = 0
#    for s in scores:
#        if 650 <= s or s < 800:
#            count += 1
#    return count
# scores = [300, 500, 670, 700, 820, 560]
# print(solution(scores))

arr = [10,20,30,40]

for i, v in enumerate(arr):
    # return (i,v)

