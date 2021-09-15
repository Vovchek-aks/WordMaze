WORDS = set(open('words.txt', encoding='UTF-8').read().split())

maze = []

s = input()
while s:
    maze += [s]
    s = input()

# print(*maze, sep='\n')

maze_words = []


def maze_to_words(x: int, y: int, word: str):
    global maze_words

    if x == 0 and y == 0:
        word += maze[y][x]
        maze_words += [word]
        return

    if x < 0 or y < 0:
        return

    word += maze[y][x]

    maze_to_words(x - 1, y, word)
    maze_to_words(x, y - 1, word)


n_maze = len(maze) - 1

maze_to_words(n_maze, n_maze, '')

maze_words = set(maze_words)

f = True
for i in maze_words:
    if i in WORDS:
        print(i)
        f = False
        break
if f:
    print('Не найдено')

















