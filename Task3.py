def readfile(name):
    '''
    Чтение файла со списком игр
    :param name: str, name file
    :return: list, games
    '''
    f = open(name, 'r', encoding='utf-8')
    f.readline()
    games = []
    for i in range(500):
        games.append(f.readline().strip().split('$'))
    return games

games = readfile('game.txt')

def findchar(char):
    '''
    Поиск персонажа в текстовом файле и вывод, в каких играх этот персонаж встречается
    :param char:
    :return:
    '''
    gamechar = []
    n = 0
    for i in range(500):
        if char == (games[i][1]) and n <= 5:
            n+=1
            gamechar.append(games[i][0])
    if n < 5 and n > 0:
        print(f'Персонаж {char} встречается в играх:')
        for x in gamechar:
            print(x)
    if n == 0 and char != 'game':
        print('Этого персонажа не существует')
    if n == 5:
        print(f'Персонаж {char} встречается в играх:')
        for x in gamechar:
            print(x)
        print('и др.')

char = input()
while char != 'game':
    findchar(char)
    char = input()