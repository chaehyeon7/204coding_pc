# 7.리스트에서 특정 원소만 추출하기   ex) 2만 추출
arr = [1, 2, 2, 2, 3, 1, 1, 3, 2]

# 방법1
# arr에 반복횟수를 구한다.
반복횟수 = arr.count(2)

# 반복횟수 만큼
for i in range(반복횟수):
    # 2를 지운다.
    arr.remove(2)

# 방법2

# result = list()
#
# for x in arr:
#     if x != 2:
#         # result에 x를 추가
#         result.append(x)
#
# print(result)