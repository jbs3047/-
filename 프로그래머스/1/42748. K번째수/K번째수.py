def solution(array, commands):
    answer = []
    for i in commands:
        a,b,c=i
        lst=sorted(array[a-1:b])
        answer.append(lst[c-1])
    return answer