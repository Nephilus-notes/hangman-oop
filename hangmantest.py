import unittest
from unittest import mock
from io import StringIO
from hangman_main import Sacrifice, Player
import pdb


class HangmanTest(unittest.TestCase):
    

    # def underscore_test():
    #     with mock.patch('sys.stdout', new=StringIO()) as fake_out:
    #         # func()
    #         self.assertEqual(fake_out.getvalue(), string)

        
    def test_wrong_chars(self):
        mock_args = ['charles', 'yes','d','w','t']
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = mock_args
            game = Sacrifice()
            try:
                result1 = game.name_get()
            
                self.assertIn('d', game.player.wrong_chars)
                self.assertIsInstance(game.player.wrong_chars, list)
                test_passed = True
                result2=game.main()
                self.assertIsInstance(game.player.wrong_chars, list)
                game.main()
                self.assertIsInstance(game.player.wrong_chars, list)
                game.main()
            except StopIteration:
                test_passed = True            
            self.assertTrue(test_passed)

    def test_word_list(self):
        player = Player('Johnny')

        game = Sacrifice()
        game.player = player
        self.assertIn('cherry', game.words[1])
        self.assertIn('typography', game.words[2])
        self.assertIn('asymptote', game.words[3])

    def test_word_list_get(self):
        player = Player('Johnny')

        game = Sacrifice()
        game.player = player
        game.choose_secret_word(4)
        self.assertIn('carburetor', game.secret)
        game.choose_secret_word(10)
        self.assertIn('verisimilitude', game.secret)
        game.choose_secret_word(8)
        self.assertIn('carriage', game.secret)
        game.choose_secret_word(5)
        self.assertIn('marzipan', game.secret)

    # def test_secret(self):
    # potentially completely defunced.  needs the game() in reset game to be off to function.
    #     player = Player('Johnny')
    #     game = Sacrifice()
    #     game.player = player
    #     game.reset_game()
    #     self.assertTrue(game.secret)


    def test_display_secret_marzipan(self):
        player = Player('Johnny')
        game = Sacrifice()
        game.player = player
        game.choose_secret_word(5)
        self.assertIn('marzipan', game.secret)
        # def underscore_test():
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            game.display_secret()
            self.assertEqual(fake_out.getvalue(), '_ _ _ _ _ _ _ _ \n')
        
    def test_display_partial_marzipan(self):
        player = Player('Johnny')
        game = Sacrifice()
        game.player = player
        game.choose_secret_word(5)
        self.assertIn('marzipan', game.secret)
        game.reveal_character('a')
        game.reveal_character('m')
        # def underscore_test():
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            game.display_secret()
            self.assertEqual(fake_out.getvalue(), 'ma_ _ _ _ a_ \n')
        
    def test_game_over(self):
        player = Player('Johnny')
        game = Sacrifice()
        game.player = player
        game.choose_secret_word(5)
        game.reveal_character('b')
        game.reveal_character('c')
        game.reveal_character('d')
        game.reveal_character('e')
        game.reveal_character('f')
        game.reveal_character('g')
        game.reveal_character('h')
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            mock_args = ['no']
            with mock.patch('builtins.input') as mocked_input:
                mocked_input.side_effect = mock_args
                game.check_wrong_chars()
                self.assertEqual(fake_out.getvalue(), "You have lost Johnny and the hanged man sees not another day.\nUntil next time.\n")
        
        # game.reveal_character('j', player)

    # def test_char_choice(self):
    #     mock_args = ['m', 'a','d','w']
    #     with mock.patch('builtins.input') as mocked_input:
    #         with mock.patch('sys.stdout', new=StringIO()) as fake_out:
    #             # in order for test to be vaild you have to disable the while loop in the main function
    #             test_passed = True
    #             mocked_input.side_effect = mock_args
    #             player = Player('Johnny')
    #             game = Sacrifice()
    #             game.player = player
    #             game.choose_secret_word(5)
    #             try:
    #                 result1 = game.main()
    #             except StopIteration:
    #                 test_passed = True

    #             self.assertIn('m', game.player.chars)
    #             result2 = game.main()
    #             self.assertIn('a', game.player.chars)
                
    #             game.display_secret()
                
                    # result3 = game.main()   


                # self.assertTrue(test_passed)

    def test_game_over(self):
        mock_args = ['q', 'w','d','e','s','f','x','y',]
        with mock.patch('builtins.input') as mocked_input:
            with mock.patch('sys.stdout', new=StringIO()) as fake_out:
                # in order for test to be vaild you have to disable the while loop in the main function
                test_passed = True
                mocked_input.side_effect = mock_args
                player = Player('Johnny')
                game = Sacrifice()
                game.player = player
                game.choose_secret_word(5)
                try:
                    result1 = game.main()
                except StopIteration:
                    test_passed = True

                self.assertNotIn('q', game.player.chars)
                try:
                    result2 = game.main()
                except StopIteration:
                    test_passed = True
                self.assertNotIn('d', game.player.chars)
                
                game.display_secret()
                
                    # result3 = game.main()   


                self.assertTrue(test_passed)


    def test_name_get(self):
        mock_args = ['charles', 'o','d','w']
        with mock.patch('builtins.input') as mocked_input:
            game = Sacrifice()

            result1 = game.name_get


unittest.main()