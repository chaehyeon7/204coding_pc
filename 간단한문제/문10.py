movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

result = list()

for x in movie_rank:
    if x != '럭키':
        result.append(x)
    else:
        continue
print(result)


# movie_rank.remove('럭키')
# print(movie_rank)