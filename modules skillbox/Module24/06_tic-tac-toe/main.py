# TODO здесь писать код

class Cell:
    def __init__(self, position, status=0):
        self.position = position
        self.status = status

    #  Клетка, у которой есть значения
    #   - занята она или нет
    #   - номер клетки
    pass


class Board:
    def __init__(self):
        self.cells_list = [[Cell(str(i + 1) + str(j + 1)) for i in range(3)] for j in range(3)]

    def info(self):
        print('Position:')
        for i in self.cells_list:
            for j in i:
                print(j.position, end=' ')
            print()
        print('Status:')
        for i in self.cells_list:
            for j in i:
                print(j.status, end=' ')
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
    def __init__(self, board, players_list):
        self.players_list = players_list
        self.board = board

    # def chek_win(self):
    #     if

    def go_to_motion(self, name_player):
        num_cell = input('Введите номер клетки в формате XX(строка)(столбец): ')
        if int(self.board.status.cells.list[num_cell[0]][num_cell[1]]) == 0:
            self.board.status.cells.list[num_cell[0]][num_cell[1]] = name_player

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

while True:
    board_for_game.info()
    for players in game.players_list:
        game.go_to_motion(player_1)

# Нужно запустить и пофиксить ошибки, после этого продолжить написание кода
