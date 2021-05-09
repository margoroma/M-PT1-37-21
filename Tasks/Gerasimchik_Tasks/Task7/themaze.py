import random


class Room:
    def __init__(self, room_id, doors):
        self.room_id = room_id
        self.doors = doors


class Maze:
    def __init__(self):
        self.maze = {}

    def maze_gen(self, room):
        self.maze[room.room_id] = room


class Doors:
    def doors_gen(self, doors_number, free_rooms):
        pass


class Npc:
    def __init__(self, npc_type, current_maze, npc_position=None):
        self.npc_type = npc_type
        self.current_maze = current_maze
        self.npc_position = npc_position

    def move(self):
        self.npc_position = random.choice(self.current_maze.maze[self.npc_position].doors)
        print(f'{self.npc_type} переместился в комнату {self.npc_position}')
        return self.npc_position


rooms_num = 20
maze = Maze()
maze.maze_gen(Room(0, [1, 2]))
maze.maze_gen(Room(1, [0, 3]))
maze.maze_gen(Room(2, [0, 10, 11, 12]))
maze.maze_gen(Room(3, [1, 4, 5, 6]))
maze.maze_gen(Room(4, [3, 7, 8]))
maze.maze_gen(Room(5, [3, 9]))
maze.maze_gen(Room(6, [3]))
maze.maze_gen(Room(7, [4]))
maze.maze_gen(Room(8, [4]))
maze.maze_gen(Room(9, [5]))
maze.maze_gen(Room(10, [2]))
maze.maze_gen(Room(11, [2, 13, 14]))
maze.maze_gen(Room(12, [2, 6, 7]))
maze.maze_gen(Room(13, [11, 15, 16]))
maze.maze_gen(Room(14, [11, 17]))
maze.maze_gen(Room(15, [13]))
maze.maze_gen(Room(16, [13]))
maze.maze_gen(Room(17, [14]))
maze.maze_gen(Room(18, [12]))
maze.maze_gen(Room(19, [12]))

hero = Npc('Супермен', maze, 0)
print(f'{hero.npc_type} заспавнился в комнате {hero.npc_position}')
monster = Npc('Годзила', maze, random.choice(list(maze.maze.keys())))
print(f'{monster.npc_type} заспавнился в комнате {monster.npc_position}')
cross = False
while not cross:
    hero.move()
    if hero.npc_position != monster.npc_position:
        monster.move()
        if hero.npc_position == monster.npc_position:
            cross = True
    else:
        cross = True

print(f'{hero.npc_type} и {monster.npc_type} встретились в комнате {hero.npc_position}')
