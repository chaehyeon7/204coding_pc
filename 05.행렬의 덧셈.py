import copy


def solution(arr1, arr2):
    행길이 = len(arr1)
    열길이 = len(arr1[0])

    answer = [0] * 열길이
    answer = [copy.deepcopy(answer) for _ in range(행길이)]

    for i in range(행길이):
        for j in range(열길이):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer