def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # True에 해당하는 요소(item)는 더한다.
        if signs[i] is True: # 아래쪽에 s를 비교
            answer += absolutes[i]
        # False 에 해당하는 요소(item)는 뺸다
        else:
            answer -= absolutes[i]
    return answer


if __name__ == "__main__":
a = [4, 7, 12]
s = [True, False, True]
print(solution(a, s))
