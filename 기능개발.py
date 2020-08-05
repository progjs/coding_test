import itertools

def solution(progresses, speeds):
    answer = []
    while progresses:
        answer.append(0)
        while(progresses[0] < 100):
            progresses = [p+s for p,s in zip(progresses,speeds)]
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            answer[-1] += 1
        # print(progresses, answer)
    return answer