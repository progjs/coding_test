# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    length, cur, out_list = len(board), 0, []
    
    for move in moves:
        for i in range(length):
            if board[i][move-1]:
                cur = board[i][move-1]
                board[i][move-1] = 0
                break
        else:
            continue
        if out_list and out_list[-1] == cur:
            out_list.pop()
            answer += 2
        else:
            out_list.append(cur)
    
    return answer


# 성능 조금 높임
def solution(board, moves):
    answer = 0
    length, cur, out_list = len(board), 0, [0]
    for move in moves:
        for i in range(length):
            if board[i][move-1]:
                cur = board[i][move-1]
                board[i][move-1] = 0
                break
        else:
            continue
        if out_list[-1] == cur: # out_list 초기화 [0]으로해서 empty체크 제거
            out_list.pop()
            answer += 2
        else:
            out_list.append(cur)
    
    return answer