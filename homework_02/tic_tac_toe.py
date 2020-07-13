# -*- coding: utf-8 -*-
import math
''' Программы игры крестики-нолики'''


class AlreadyExistsError(Exception):
    ''' Ошибка при выборе занятой клетки'''


class TicTacToe:
    ''' Класс игры крестики-нолики'''
    def __init__(self):
        ''' Инициализация поля и очередности хода'''
        self._table = ["_" for i in range(6)]
        self._table.extend([" " for i in range(6, 9)])
        self._crosses_move = True
        self.gamer1 = ''
        self.gamer2 = ''

    def run_game(self):
        ''' Основной поток игры'''
        # начало игры: приветствие и ввод никнеймов
        print('Добро пожаловать в игру крестики-нолики!')
        print('Для начала представьтесь:')
        print('Игрок 1:')
        self.gamer1 = input()
        print("Игрок 2:")
        self.gamer2 = input()
        print('Поехали!')
        while True:
            # начало хода: отрисовка таблицы координат и текущего поля
            print('\n_1_|_2_|_3_\n_4_|_5_|_6_\n 7 | 8 | 9')
            move = 'крестики' if self._crosses_move else 'нолики'
            print('Ходят ' + move)
            print("Выберите клетку:")
            self.draw_table()
            val = input()
            # считываем клетку и обрабатываем ошибки
            try:
                coord = self.read_coord(val)
                self.set_coord(coord)
            except ValueError:
                print("Введите число!")
                continue
            except IndexError:
                print("Выберите клетку (цифру от 1 до 9)")
                continue
            except AlreadyExistsError:
                print("Клетка занята!")
                continue

            # условия окончания игры
            if self.is_winner():
                print('Поздравляю! Победили ' + move)
                self.draw_table()
                break
            if '_' not in self._table and ' ' not in self._table:
                print("Игра окончена! Ничья.")
                self.draw_table()
                break

    def draw_table(self):
        ''' Отрисовка текущего поля'''
        print('_{}_|_{}_|_{}_\n_{}_|_{}_|_{}_\n {} | {} | {}'
              .format(*self._table))

    def is_winner(self):
        ''' Проверка наличия победителя'''
        # return ((self._table[0] == self._table[1] and
        #          self._table[1] == self._table[2] and
        #          self._table[0] != '_') or
        #         (self._table[3] == self._table[4] and
        #          self._table[4] == self._table[5] and
        #          self._table[3] != '_') or
        #         (self._table[6] == self._table[7] and
        #          self._table[7] == self._table[8] and
        #          self._table[6] != ' ') or
        #         (self._table[0] == self._table[3] and
        #          self._table[3] == self._table[6]) or
        #         (self._table[1] == self._table[4] and
        #          self._table[4] == self._table[7]) or
        #         (self._table[2] == self._table[5] and
        #          self._table[5] == self._table[8]) or
        #         (self._table[0] == self._table[4] and
        #          self._table[4] == self._table[8]) or
        #         (self._table[2] == self._table[4] and
        #          self._table[4] == self._table[6]))

        N = int(math.sqrt(len(self._table)))

        # проверка колонок
        for col in range(N):
            k = col
            for i in range(N-1):
                if ((self._table[k] != self._table[k + N]) or
                   (self._table[k] in [' ', '_'])):
                    break
                k += N
                if i == N-2:
                    return True

        # проверка рядов
        for row in range(0, len(self._table), N):
            for i in range(N-1):
                if ((self._table[row+i] != self._table[row + i + 1]) or
                   (self._table[row+i] in [' ', '_'])):
                    break
                if i == N-2:
                    return True
        # проверка первой диагонали
        k = 0
        for i in range(N-1):
            if ((self._table[k] != self._table[k+N+1]) or
               (self._table[k] in [' ', '_'])):
                break
            if i == N-2:
                return True
            k += N+1

        # проверка второй диагонали
        k = N-1
        for i in range(N-1):
            if ((self._table[k] != self._table[k+N-1]) or
               (self._table[k] in [' ', '_'])):
                break
            if i == N-2:
                return True
            k += N - 1

        return False

    def set_coord(self, coord):
        ''' Записывает крестик или нолик (в зависимости от очередности хода)
            в ячейку'''
        if self._table[coord - 1] not in [' ', '_']:
            raise AlreadyExistsError
        self._table[coord - 1] = 'X' if self._crosses_move else 'O'
        self._crosses_move = not self._crosses_move

    def read_coord(self, val):
        ''' Считывание пользовательского значения'''
        coord = int(val)
        if coord not in range(1, 10):
            raise IndexError
        return coord


if __name__ == "__main__":
    game = TicTacToe()
    game.run_game()
