# TODO здесь писать код

class Cell:
    def __init__(self, position, status=0):
        self.position = position
        self.status = status

    def __str__(self):
        return str(self.status)

    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    pass


class Board:
    def __init__(self):
        self.cells_list = [[Cell(str(j + 1) + str(i + 1)) for i in range(3)] for j in range(3)]

    def info(self):
        print('Position:')
        for i in self.cells_list:
            for j in i:
                print(j.position, end=' ')
            print()
        print('Status:')
        for i in self.cells_list:
            for j in i:
                print(str(j), end=' ')
            print()

    #  Класс поля, который создаёт у себя экземпляры клетки
    pass


class Player:
    def __init__(self, name):
        self.name = name

    #  У игрока может быть
    #   - имя
    #   - на какую клетку ходит
    pass


class Game:
    def __init__(self, board, players_list, status=True):
        self.status = status
        self.players_list = players_list
        self.board = board

    def chek_win(self, status):
        way = self.board.cells_list
        if way[0][0].status == way[0][1].status == way[0][2].status != 0 or \
                way[1][0].status == way[1][1].status == way[1][2].status != 0 or \
                way[2][0].status == way[2][1].status == way[2][2].status != 0 or \
                way[0][0].status == way[1][0].status == way[2][0].status != 0 or \
                way[0][1].status == way[1][1].status == way[2][0].status != 0 or \
                way[0][2].status == way[1][2].status == way[2][2].status != 0 or \
                way[0][0].status == way[1][1].status == way[2][2].status != 0 or \
                way[0][2].status == way[1][1].status == way[2][0].status != 0:
            status = False
        return status

    def go_to_motion(self, name_player):
        while True:
            print(f'Ходит игрок с именем: {name_player}')
            board_for_game.info()
            num_cell = input(f'Игрок {name_player}, введите номер клетки в формате XX(строка)(столбец): ')
            if self.board.cells_list[int(num_cell[0]) - 1][int(num_cell[1]) - 1].status == 0:
                self.board.cells_list[int(num_cell[0]) - 1][int(num_cell[1]) - 1].status = name_player
                break
            else:
                print(f'ячейка с индексом {num_cell} занята!')

    # Класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    # А также методы:
    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.
    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.
    pass


player_1 = Player('player_1')
player_2 = Player('player_2')
board_for_game = Board()
game = Game(board_for_game, [player_1, player_2])

while game.status:
    for player in game.players_list:
        game.go_to_motion(player.name)
        game_flag = game.chek_win(game.status)
        if not game_flag:
            print(f'Победил игрок с именем: {player.name}, игра окончена!')
            game.status = False
            break

# Нужно визуализировать доску, почистить код от коментов
