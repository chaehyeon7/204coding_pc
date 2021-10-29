# 빈 리스트에서 기존의 값들보다 큰 값이 추가될 때마다 카운팅
# ex) 빈 리스트에서 [1, 3, 2, 6, 4, 9, 5]가 추가되는 상황


# 방법 1
arr = [1,3,2,6,4,9,5]
count = 0
max = -1

# arr에 있는 모든 요소 x를 순서대로 반복
for x in arr:
    # x 값이 max값 보다 크다면 :
    if x > max:
        # max값을 x로 갱신
        max = x
        # count값 1 증가
        count += 1


# 방법 2
arr = [1,3,2,6,4,9,5]
count = 1
max = arr[0]

# arr에 있는 [1]부터의 요소 x를 순서대로 반복
for x in arr[1:]:
    # x 값이 max값 보다 크다면 :
    if x > max:
        # max값을 x로 갱신
        max = x
        # count값 1 증가
        count += 1