# -*- coding: utf-8 -*-
''' Модуль тестирования основной программы-игры
    крестики-нолики(tic_tac_toe.py)'''
import unittest
from tic_tac_toe import TicTacToe, AlreadyExistsError


class TestTicTacToe(unittest.TestCase):
    ''' Класс тестирования функций программы'''
    def test_read_coord(self):
        ''' Тесты функции read_coord()'''
        game = TicTacToe()
        with self.assertRaises(ValueError):
            game.read_coord('string')
        with self.assertRaises(IndexError):
            game.read_coord('0')
        self.assertEqual(game.read_coord('1'), 1)

    def test_set_coord(self):
        ''' Тесты функции set_coord()'''
        game = TicTacToe()
        for i in range(9):
            game.set_coord(i)
        with self.assertRaises(AlreadyExistsError):
            game.set_coord(3)

        game = TicTacToe()
        for i in range(1, 10):
            game.set_coord(i)
        self.assertListEqual(game._table,
                             ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'])

    def test_is_winner(self):
        ''' Тесты двух случаев игры с победителем и без'''
        game = TicTacToe()
        game.set_coord(1)
        game.set_coord(2)
        game.set_coord(5)
        game.set_coord(3)
        game.set_coord(9)
        self.assertTrue(game.is_winner())

        game = TicTacToe()
        game.set_coord(1)
        game.set_coord(2)
        self.assertFalse(game.is_winner())


if __name__ == '__main__':
    unittest.main()
