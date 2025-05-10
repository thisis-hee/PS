import sys
sys.setrecursionlimit(10**6)

def room_check(room_num, room_dict):
    if(room_num not in room_dict.keys()):
        room_dict[room_num]=room_num+1
        return room_num
    
    empty_room = room_check(room_dict[room_num], room_dict)
    
    room_dict[room_num] = empty_room + 1
    
    return empty_room

def solution(k, room_number):
    room_dict={}
    
    answer = []
    
    for room_num in room_number:
        answer.append(room_check(room_num, room_dict))
    
    return answer