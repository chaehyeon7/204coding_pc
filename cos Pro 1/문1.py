def solution(K, words):
    for w in words:
        if current + len(w) > k:
            answer += 1
            current = len(w) + 1
        else:
            current = current + len(w) + 1
    answer = 0
    return answer

K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

print("solution 함수의 반환 값은", ret, "입니다.")



