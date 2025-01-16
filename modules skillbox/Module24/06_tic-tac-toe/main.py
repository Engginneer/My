# TODO здесь писать код

class Cell:
    def __init__(self, position, status=0):
        self.position = position
        self.status = status

    def __str__(self):
        return str(self.status)




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
            print('----------------')
            print('|', end=' ')
            for j in i:
                if j.status == game.players_list[0].name:
                    print(' X |', end=' ')
                elif j.status == game.players_list[1].name:
                    print(' O |', end=' ')
                else:
                    print('   |', end=' ')
            print()
        print('----------------')
        print()



class Player:
    def __init__(self, name):
        self.name = name



class Game:
    def __init__(self, board, players_list, status=True):
        self.status = status
        self.count_of_moves = 0
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
            num_cell = input(f'Игрок {name_player}, введите номер клетки в формате XX(строка)(столбец): ')
            if self.board.cells_list[int(num_cell[0]) - 1][int(num_cell[1]) - 1].status == 0:
                self.board.cells_list[int(num_cell[0]) - 1][int(num_cell[1]) - 1].status = str(name_player)
                break
            else:
                print(f'ячейка с индексом {num_cell} занята!')



player_1 = Player('player_1')
player_2 = Player('player_2')
board_for_game = Board()
game = Game(board_for_game, [player_1, player_2])


while game.status:
    for player in game.players_list:
        game.count_of_moves += 1
        board_for_game.info()
        game.go_to_motion(player.name)
        #game_flag = game.chek_win(game.status)
        if not game.chek_win(game.status):
            board_for_game.info()
            print(f'Победил игрок с именем: {player.name}, игра окончена!')
            game.status = False
            break
        elif game.count_of_moves == 9:
            board_for_game.info()
            print('Игра окончена ничей!')
            game.status = False
            break

