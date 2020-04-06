# -*- coding: utf-8 -*-
import random

IMGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
    |   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''','''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''','''
   ''']     

WORDS=[
    'lavadora',
    'secadora',
    'sofa',
    'diputado',
    'perro',
    'computador',
    'teclado',
    'carro'
]
def display_board(hidden_word, tries):
    print(IMGES[tries])
    print('')
    print(hidden_word)    

def random_word():
    idx = random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def is_contain(current_letter, word):

    for i in word:
        if i == current_letter:
            return True

    return False    


def run():
    word=random_word()
    hidden_word=['-']*len(word)
    tries=0

    while tries<8:
        display_board(hidden_word,tries)

        if hidden_word.count('-')==0:
            print('F E L I C I D A D E S  H A S  G A N A D O')
            print('La palabra es: {}'.format(word))
            break

        current_letter=str(input('Escoje una letra: '))

        if is_contain(current_letter, word):
            for i in range(0,len(word)):
                if word[i] == current_letter:
                    hidden_word[i]=word[i]                                                        
        else:
            tries+=1
            print('intenta con otra palabra')

                    
        if tries==8:
            print('E S T Á S  M U E R T O  X-X')
    

if __name__=='__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()