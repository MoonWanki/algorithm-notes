# BACKJOON #5373 <큐빙>
# https://www.acmicpc.net/problem/5373

def onFlat(sides, dr):
    temp = sides.pop(7 if dr=='+' else 0)
    sides.insert(0 if dr=='+' else 7, temp)
    temp = sides.pop(7 if dr=='+' else 0)
    sides.insert(0 if dr=='+' else 7, temp)
    return sides

def turn(sides, dr):
    temp = sides.pop(11 if dr=='+' else 0)
    sides.insert(0 if dr=='+' else 11, temp)
    temp = sides.pop(11 if dr=='+' else 0)
    sides.insert(0 if dr=='+' else 11, temp)
    temp = sides.pop(11 if dr=='+' else 0)
    sides.insert(0 if dr=='+' else 11, temp)
    return sides

for _ in range(int(input())):
    cube = {
        'U': [['w']*3 for _ in range(3)],
        'D': [['y']*3 for _ in range(3)],
        'F': [['r']*3 for _ in range(3)],
        'B': [['o']*3 for _ in range(3)],
        'L': [['g']*3 for _ in range(3)],
        'R': [['b']*3 for _ in range(3)],
    }
    n=int(input())
    for side, dr in input().split():

        sides = [cube[side][0][0], cube[side][0][1], cube[side][0][2], cube[side][1][2], cube[side][2][2], cube[side][2][1], cube[side][2][0], cube[side][1][0]]
        cube[side][0][0], cube[side][0][1], cube[side][0][2], cube[side][1][2], cube[side][2][2], cube[side][2][1], cube[side][2][0], cube[side][1][0] = onFlat(sides, dr)
        
        sides = []
        if side=='U':
            sides = [
                cube['B'][0][2], cube['B'][0][1], cube['B'][0][0],
                cube['R'][0][2], cube['R'][0][1], cube['R'][0][0],
                cube['F'][0][2], cube['F'][0][1], cube['F'][0][0],
                cube['L'][0][2], cube['L'][0][1], cube['L'][0][0],
            ]
            cube['B'][0][2], cube['B'][0][1], cube['B'][0][0],cube['R'][0][2], cube['R'][0][1], cube['R'][0][0],cube['F'][0][2], cube['F'][0][1], cube['F'][0][0],cube['L'][0][2], cube['L'][0][1], cube['L'][0][0] = turn(sides, dr)
        elif side=='D':
            sides = [
                cube['F'][2][0], cube['F'][2][1], cube['F'][2][2],
                cube['R'][2][0], cube['R'][2][1], cube['R'][2][2],
                cube['B'][2][0], cube['B'][2][1], cube['B'][2][2],
                cube['L'][2][0], cube['L'][2][1], cube['L'][2][2],
            ]
            cube['F'][2][0], cube['F'][2][1], cube['F'][2][2],cube['R'][2][0], cube['R'][2][1], cube['R'][2][2],cube['B'][2][0], cube['B'][2][1], cube['B'][2][2],cube['L'][2][0], cube['L'][2][1], cube['L'][2][2] = turn(sides, dr)
        elif side=='F':
            sides = [
                cube['U'][2][0], cube['U'][2][1], cube['U'][2][2],
                cube['R'][0][0], cube['R'][1][0], cube['R'][2][0],
                cube['D'][0][2], cube['D'][0][1], cube['D'][0][0],
                cube['L'][2][2], cube['L'][1][2], cube['L'][0][2],
            ]
            cube['U'][2][0], cube['U'][2][1], cube['U'][2][2],cube['R'][0][0], cube['R'][1][0], cube['R'][2][0],cube['D'][0][2], cube['D'][0][1], cube['D'][0][0],cube['L'][2][2], cube['L'][1][2], cube['L'][0][2] = turn(sides, dr)
        elif side=='B':
            sides = [
                cube['U'][0][2], cube['U'][0][1], cube['U'][0][0],
                cube['L'][0][0], cube['L'][1][0], cube['L'][2][0],
                cube['D'][2][0], cube['D'][2][1], cube['D'][2][2],
                cube['R'][2][2], cube['R'][1][2], cube['R'][0][2],
            ]
            cube['U'][0][2], cube['U'][0][1], cube['U'][0][0],cube['L'][0][0], cube['L'][1][0], cube['L'][2][0],cube['D'][2][0], cube['D'][2][1], cube['D'][2][2],cube['R'][2][2], cube['R'][1][2], cube['R'][0][2] = turn(sides, dr)
        elif side=='L':
            sides = [
                cube['U'][0][0], cube['U'][1][0], cube['U'][2][0],
                cube['F'][0][0], cube['F'][1][0], cube['F'][2][0],
                cube['D'][0][0], cube['D'][1][0], cube['D'][2][0],
                cube['B'][2][2], cube['B'][1][2], cube['B'][0][2],
            ]
            cube['U'][0][0], cube['U'][1][0], cube['U'][2][0],cube['F'][0][0], cube['F'][1][0], cube['F'][2][0],cube['D'][0][0], cube['D'][1][0], cube['D'][2][0],cube['B'][2][2], cube['B'][1][2], cube['B'][0][2] = turn(sides, dr)
        elif side=='R':
            sides = [
                cube['U'][2][2], cube['U'][1][2], cube['U'][0][2],
                cube['B'][0][0], cube['B'][1][0], cube['B'][2][0],
                cube['D'][2][2], cube['D'][1][2], cube['D'][0][2],
                cube['F'][2][2], cube['F'][1][2], cube['F'][0][2],
            ]
            cube['U'][2][2], cube['U'][1][2], cube['U'][0][2],cube['B'][0][0], cube['B'][1][0], cube['B'][2][0],cube['D'][2][2], cube['D'][1][2], cube['D'][0][2],cube['F'][2][2], cube['F'][1][2], cube['F'][0][2] = turn(sides, dr)
        
    [print(r[0],r[1],r[2],sep='') for r in cube['U']]
