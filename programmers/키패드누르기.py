def solution(numbers, hand):
    answer = ''
    cur = {'left':[0,0], 'right':[2,0]} # left:* right:#
    keyboard ={ 0:(1,0), 1:(0,3), 2:(1,3), 3:(2,3), 4:(0,2), 5:(1,2), 6:(2,2), 7:(0,1), 8:(1,1), 9:(2,1) }
    cal_dist = lambda x,y: abs(cur[x][0]-keyboard[y][0]) + abs(cur[x][1]-keyboard[y][1])
    
    for num in numbers:
        if num != 0 and num % 3 == 1:
            cur['left'] = keyboard[num]
            answer += 'L'
        elif num != 0 and num % 3 == 0:
            cur['right'] = keyboard[num]
            answer += 'R'
        else:
            dist_left = cal_dist('left', num)
            dist_right = cal_dist('right', num)
            if dist_left < dist_right:
                cur['left'] = keyboard[num]
                answer += 'L'
            elif dist_left > dist_right:
                cur['right'] = keyboard[num]
                answer += 'R'
            else:
                cur[hand] = keyboard[num]
                answer += hand[0].upper()
    return answer