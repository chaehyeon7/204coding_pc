def solution(a, b):
    sum = 0
    if a>b: # 테스트 3번 해결
        a, b = b, a
        
    for x in range(a, b+1):
        sum += x

    return sum