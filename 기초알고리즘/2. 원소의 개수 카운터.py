# 2.원소의 갯수를 카운터하기
# ex) [1, 2, 2, 2, 3, 1, 1, 3, 2] 에서  2의 갯수를 카운팅

리스트 = [1,2,2,2,3,1,1,3,2]

# 카운팅을 위한 변수 0으로 초기화한다.
count = 0
# 리스트의 모든 원소를 하나씩 다 돈다.
for x in 리스트:
    # 각각의 원소가 2이면
    if x == 2:
        # 카운팅을 한다.
        count += 1
print(count)
