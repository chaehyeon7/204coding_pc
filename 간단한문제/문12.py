cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]

# 함수 없이
result = list()
for x in cook:
    if x not in result:
        result.append(x)
    else:
        continue

a = len(result)

print(a)

#쌤
a = len(set(cook))
print(a)

#
# print(len(cook))