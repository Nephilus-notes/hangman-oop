import random as r
import time
import pdb

class Player():
    def __init__(self, name):
        self.name = name
        self.chars = []
        self.wrong_chars= []
        
    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        return self.name.title()

    
    # @property
    # def wrong_chars(self):
    #     return f"These are the letters you've guessed: {self._wrong_chars}"

    # @wrong_chars.setter
    # def wrong_chars(self, new_wrong_chars=[]):
    #     self._wrong_chars = new_wrong_chars

class Sacrifice():
    def __init__(self):
        self.words = {
1:'cherry', 
2:'typography', 
3:'asymptote',
4: 'carburetor',
5: 'marzipan',
6: 'decadent',
7: 'swiss',
8: 'carriage',
9: 'palatial',
10: 'verisimilitude', 
11: 'blossom',
}
        self.input_options = {'name':[],
'yes':['yes','y','ye','yeah','yup','sure','mhm'],
'no': ['no','nope','naw','nuh uh', 'na', 'negatory', 'negative', 'n']
}
        self.ascii = {
            1:'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
            2:'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
            3:  '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
            4:'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
            5:'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
            6:'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
            7:'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
8:'''
  +---+
  |   |
  O __|
 /|__ |
 /    |
      |
=========''',
9:'''
  +---+
  |   |
__O   |
__|\  |
   \  |
      |
========='''

        }
        self.player = None #player
        self.secret = None
        # self.name_get()
        
    def name_get(self):
        name = input("Hey there! What's your name? ") 
        print(f"Hey {name.title()}! It's nice to meet ya.") 
        self.input_options['name'].append(name)  
        name = Player(name)
        self.player = name
        time.sleep(2.5)
        game_on = input("Do you want to play some Hangman? ")
        while True:
            if game_on in self.input_options['yes']:
                self.reset_game()
                break
            elif game_on in self.input_options['no']:
                print("That's okay! I never forget a face. See you around!")
                break
            else:
                game_on = input("Pardon? ")

    def main(self):
        
        game_running = True
        while game_running == True:
            self.guessed_chars()
            self.display_secret()
            char = self.guess_char()
            self.reveal_character(char)
            game_running = self.check_wrong_chars()
            

    def choose_secret_word(self, int):
        self.secret = self.words[int]

    def display_secret(self):
        secret = []
        for e in self.secret:

            if e in self.player.chars:
                # print(e)end=''
                secret.append(e)
            else:
                secret.append('_ ')
                # print( end='')

        secret = ''.join(secret)
        print(secret)
        if secret == self.secret:
            self.game_won()

        # print('_ ' * len(self.secret))

        # make sure to pass self.name to the player
    def reveal_character(self, char):
        if char in self.secret:
            self.player.chars.append(char)
            print("Nice. You got one!")

        else:
            self.player.wrong_chars.append(char)
            print(f"Sorry {char} is not in the secret word.")

    def guess_char(self):
        # is there something wrong with this while loop? it comes back when the game should end
        guessing = True
        while guessing == True:
            char = input("Guess a letter or the word: ").lower().strip()
            if char.isalpha() == True:
                if len(char) == 1 and char not in self.player.chars:
                    self.player.chars.append(char)
                    guessing = False
                    return char

                elif len(char) == 1 and char not in self.player.wrong_chars:
                    self.player.wrong_chars.append(char)
                    guessing = False
                    return char

                elif len(char) == len(self.secret):
                    if char == self.secret:
                        self.game_won()
                        guessing = False
                        break
                else:
                    input("That is not a valid letter.")


    def guessed_chars(self):
        while self.player.wrong_chars:
            print(self.ascii[len(self.player.wrong_chars)])
            print(self.player.wrong_chars)
            break

    def check_wrong_chars(self):
        if len(self.player.wrong_chars) >= 7:
            self.game_over()
            return False
        return True
    
    def reset_game(self):
        self.choose_secret_word(r.randint(1,10))
        self.player.chars = []
        self.player.wrong_chars = []
        self.main()

    
        
    def game_over(self):
        print(f"You have lost {self.player.name} and the hanged man sees not another day.")
        while True:
            print(self.ascii[8])
            time.sleep(.4)
            print(self.ascii[9])
            time.sleep(.4)
            print(self.ascii[8])
            time.sleep(.4)
            print(self.ascii[9])
            time.sleep(.4)
            break

        self.next_game()

    def game_won(self):
        print(f"Congratulations, you won! {self.secret.title()} is the secret word.")
        self.next_game()

    def next_game(self):
        while True:
            game_on = input("Would you like to play again? ").lower().strip()
            if game_on in self.input_options['yes']:
                self.reset_game()
                break
            elif game_on in self.input_options['no']:
                print('Until next time.')
                game_running = False
                guessing = False
                break


game = Sacrifice()
# # pdb.set_trace()
game.name_get()