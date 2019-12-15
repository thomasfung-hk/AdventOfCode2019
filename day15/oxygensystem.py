from intcodecomputer import parseIntcode, IntcodeComputer
import collections
import copy

class RepairDroid:
    def __init__(self, puzzle_input):
        self.computer = IntcodeComputer(puzzle_input)
        self.position = (0, 0)
        self.walls = set()
        self.map = {(0, 0): set()}
        self.oxygensystem = None
        self.makeMap()

    @classmethod
    def returnDirection(cls, dir):
        opposites = {1: 2, 2: 1, 3: 4, 4: 3}
        return opposites[dir]

    @classmethod
    def nextPoint(cls, pos, dir):
        if dir not in {1, 2, 3, 4}:
            raise ValueError(f"Invalid direction: {dir}")
        if dir == 1:
            return (pos[0], pos[1] + 1)
        elif dir == 2:
            return (pos[0], pos[1] - 1)
        elif dir == 3:
            return (pos[0] - 1, pos[1])
        else:
            return (pos[0] + 1, pos[1])

    def move(self, origin, des):
        if des == (origin[0], origin[1] + 1):
            input = 1
        elif des == (origin[0], origin[1] - 1):
            input = 2
        elif des == (origin[0] - 1, origin[1]):
            input = 3
        elif des == (origin[0] + 1, origin[1]):
            input = 4
        else:
            return ValueError(f"Non-adjacent points: Origin={origin}, Des={des}.")
        self.computer.insertInput(input)
        self.computer.runCode()
        self.position = des
        return

    def makeMap(self):
        visited = {(0, 0)}
        frontier_for_point = self.makeFrontier(visited)
        for next_point in frontier_for_point:
            self.DFS(next_point, (0, 0), visited)
        return

    def makeFrontier(self, visited):
        frontier_for_point = []
        for dir in range(1, 5):
            point_to_explore = RepairDroid.nextPoint((self.position), dir)
            if point_to_explore not in visited:
                self.computer.insertInput(dir)
                status = self.computer.runCode()
                if status == 0:
                    self.walls.add(point_to_explore)
                elif status in {1, 2}:
                    self.map[self.position].add(point_to_explore)
                    if point_to_explore not in self.map:
                        self.map[point_to_explore] = {self.position}
                    else:
                        self.map[point_to_explore].add(self.position)
                    if status == 2 and not self.oxygensystem:
                        self.oxygensystem = point_to_explore
                    frontier_for_point.append(point_to_explore)
                    self.computer.insertInput(RepairDroid.returnDirection(dir))
                    self.computer.runCode()
        return frontier_for_point


    def DFS(self, point, origin, visited):
        self.move(origin, point)
        visited.add(point)
        frontier_for_point = self.makeFrontier(visited)
        for next_point in frontier_for_point:
            self.DFS(next_point, point, visited)
        self.move(point, origin)
        return

    def BFS_shortestpath(self, origin, destination):
        explored = []
        queue = collections.deque([[origin]])
        if origin == destination:
            return [origin]

        while queue:
            path = queue.popleft()
            current_point = path[-1]
            if current_point not in explored:
                neighbors = self.map[current_point]
                for neighbor in neighbors:
                    if neighbor != current_point:
                        new_path = copy.deepcopy(path)
                        new_path.append(neighbor)
                        queue.append(new_path)
                        if neighbor == destination:
                            return new_path
                explored.append(current_point)

    def BFS_oxygenspread(self, origin):
        frontier = set(self.map.keys())
        frontier.remove(origin)
        current_level = [origin]
        minutes = 0
        while frontier:
            next_level = set()
            for point in current_level:
                for next_point in self.map[point]:
                    if next_point in frontier:
                        frontier.remove(next_point)
                        next_level.add(next_point)
            current_level = next_level
            minutes += 1
        return minutes

def partOne(puzzle_input):
    droid = RepairDroid(puzzle_input)
    path = droid.BFS_shortestpath((0,0), droid.oxygensystem)
    print(f"The shortest path is {len(path) - 1} steps.")

def partTwo(puzzle_input):
    droid = RepairDroid(puzzle_input)
    minutes_needed = droid.BFS_oxygenspread(droid.oxygensystem)
    print(f"It takes {minutes_needed} minutes for oxygen to fill the whole area.")

def main():
    puzzle_input = parseIntcode('input.txt')
    partOne(puzzle_input)
    partTwo(puzzle_input)

if __name__ == '__main__':
    main()
