# 8.zip을 사용하는 반복문 예시
arr1 = [1, 2, 3]
arr2 = [10, 20, 30, 40]

# for z in zip(arr1, arr2):
#     print(z)

small = min(len(arr1), len(arr2))
for i in range(small):
    print(arr1[i], arr2[i])