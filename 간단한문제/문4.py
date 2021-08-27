"http://sharebook.kr"
# a = url.split(".")
# print(a[-1])

url = "http://share.book.kr"
result = list()
start = 0
for i in range(len(url)) :
    if url[i] == ".":
        result.append(url[start:i])
        start = i+1
result.append(url[start:])
print(result[-1])
