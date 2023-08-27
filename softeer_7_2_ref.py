from copy import deepcopy

n, m = map(int, input().split())

move_map = []

for _ in range(n):
    row = list(map(int, input().split()))
    move_map.append(row)

move_list = []

for _ in range(m):
    a, b = map(int, input().split())
    move_list.append((a-1, b-1))


# 풀이
result = 0
# 들러야하는 포인트들의 리스트 , 이전에 지나온 맵, 현재 위치, 도착 위치
def move_cnt(points_to_visit, past_map, cur_point, goal_point):
    global result, n
    # 현재 위치 방문처리
    x, y = cur_point
    past_map = deepcopy(past_map)
    points_to_visit = deepcopy(points_to_visit)
    past_map[x][y] = 1
    # 만약 현재 위치가 다음 목적지와 동일할 경우 그 다음 목적지로 향하게끔
    if cur_point == goal_point:
        del points_to_visit[0]
        # 방금 갔던 곳이 마지막 목적지였다면 1 을 반환
        if len(points_to_visit) == 0:
            result += 1
            return
        # 아직 목적지가 남아있다면
        else:
            return move_cnt(points_to_visit[:], past_map[:], cur_point, points_to_visit[0])
    # 아직 현재 위치가 다음 목적지가 아닐 경우
    else:
        if x > 0 and past_map[x-1][y] == 0:
            move_cnt(points_to_visit[:], past_map[:], (x-1, y), goal_point)
        if y > 0 and past_map[x][y-1] == 0:
            move_cnt(points_to_visit[:], past_map[:], (x, y-1), goal_point)
        if x < n-1 and past_map[x+1][y] == 0:
            move_cnt(points_to_visit[:], past_map[:], (x+1, y), goal_point)
        if y < n-1 and past_map[x][y+1] == 0:
            move_cnt(points_to_visit[:], past_map[:], (x, y+1), goal_point)


move_cnt(move_list, move_map, move_list[0], move_list[0])

print(result)