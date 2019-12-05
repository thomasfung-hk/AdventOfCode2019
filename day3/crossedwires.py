def parseInput(input):
    wirelist = open(input).readlines()
    wire_1 = wirelist[0].strip().split(',')
    wire_2 = wirelist[1].strip().split(',')
    return (wire_1, wire_2)

def lineBoundHelper(dir, distance, pos_x, pos_y):
    if dir == 'U':
        x_lower, x_upper, y_lower, y_upper = pos_x, pos_x, pos_y, pos_y+distance
        pos_y += distance
    elif dir == 'D':
        x_lower, x_upper, y_lower, y_upper = pos_x, pos_x, pos_y-distance, pos_y
        pos_y -= distance
    elif dir == 'L':
        x_lower, x_upper, y_lower, y_upper = pos_x-distance, pos_x, pos_y, pos_y
        pos_x -= distance
    elif dir == 'R':
        x_lower, x_upper, y_lower, y_upper = pos_x, pos_x+distance, pos_y, pos_y
        pos_x += distance
    else:
        raise ValueError
    return x_lower, x_upper, y_lower, y_upper, pos_x, pos_y

def pathSetGen(path):
    path_set = {(0,0)}
    pos_x = 0
    pos_y = 0
    for move in path:
        dir = move[0]
        distance = int(move[1:].strip())
        x_lower, x_upper, y_lower, y_upper, pos_x, pos_y = lineBoundHelper(
        dir, distance, pos_x, pos_y)
        for x in range(x_lower, x_upper+1):
            for y in range(y_lower, y_upper+1):
                path_set.add((x,y))
    path_set.remove((0,0))
    return path_set

def closestIntersection(path_1, path_2):
    path_set = pathSetGen(path_1)
    man_dis = float('inf')
    pos_x = 0
    pos_y = 0
    for move in path_2:
        dir = move[0]
        distance = int(move[1:].strip())
        x_lower, x_upper, y_lower, y_upper, pos_x, pos_y = lineBoundHelper(
        dir, distance, pos_x, pos_y)
        for x in range(x_lower, x_upper+1):
            for y in range(y_lower, y_upper+1):
                if (x,y) in path_set and abs(x)+abs(y) < man_dis:
                    man_dis = abs(x)+abs(y)
    return man_dis

def pathListGen(path):
    path_list = [(0, 0)]
    pos_x = 0
    pos_y = 0
    for move in path:
        dir = move[0]
        distance = int(move[1:].strip())
        if dir == 'U':
            for y in range(pos_y+1, pos_y+distance+1):
                path_list.append((pos_x,y))
            pos_y += distance
        elif dir == 'D':
            for y in range(pos_y-1, pos_y-distance-1, -1):
                path_list.append((pos_x,y))
            pos_y -= distance
        elif dir == 'L':
            for x in range(pos_x-1, pos_x-distance-1, -1):
                path_list.append((x,pos_y))
            pos_x -= distance
        elif dir == 'R':
            for x in range(pos_x+1, pos_x+distance+1):
                path_list.append((x,pos_y))
            pos_x += distance
        else:
            raise ValueError
    return path_list

def smallestDelay(path_1, path_2):
    path_list_1 = pathListGen(path_1)
    path_list_2 = pathListGen(path_2)
    delay = float('inf')
    for i, coordinate in enumerate(path_list_2[1:], start=1):
        if i >= delay:
            return delay
        try:
            intersection = path_list_1.index(coordinate)
        except ValueError:
            continue
        if intersection + i < delay:
            delay = intersection + i
    return delay


def main():
    filename = "input.txt"
    wire_1, wire_2 = parseInput(filename)
    manhattan_distance = closestIntersection(wire_1, wire_2)
    print(f'The Manhattan distance is {manhattan_distance}')
    smallest_signal_delay = smallestDelay(wire_1, wire_2)
    print(f'The fewest combined steps is {smallest_signal_delay}')

if __name__ == '__main__':
    main()
