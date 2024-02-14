def readfile(name):
    '''
    Чтение файла со списком игр, в которых возикли ошибки
    :param name: str, name file
    :return: list, games
    '''
    f = open(name, 'r', encoding='utf-8')
    f.readline()
    games = []
    for i in range(500):
        games.append(f.readline().strip().split('$'))
    return games

def finderror():
    '''
    Поиск ошибки с числом 55 в ней и ее замена
    :return: list, game without error key=55
    '''
    for i in range(500):
        if '55' in games[i][2]:
            print(f'У персонажа {games[i][1]} \n в игре {games[i][0]} \n нашлась ошибка с кодом {games[i][2]} \n Дата фиксации {games[i][3]}')
            games[i][2] = 'Done'
            games[i][3] = '0000-00-00'
    return games

def writefile(name):
    '''
    Записываем измененный файл
    :param name: str, geme_new.csv
    '''
    f = open(name, 'w', encoding='utf-8')
    f.write('$'.join(games[0]) + '\n')
    for i in range(500):
        f.write('$'.join(games[i])+'\n')
    f.close

games = readfile('game.txt')
finderror()
writefile('games_new.csv')