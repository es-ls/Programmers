def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced_array = sorted(array[i-1:j])
        answer.append(sliced_array[k-1])
    return answer