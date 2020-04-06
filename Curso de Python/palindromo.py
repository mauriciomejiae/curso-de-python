#-*- coding: utf-8 -*-

def palindrome(word):
    word_list= list(word)
    word_list.reverse()
    reversed_word= ''.join(word_list)

    if reversed_word == word:
        return True

    return False


if __name__ == '__main__':

    word= input('Ingresa una palabra: ')

    result= palindrome(word)

    if result is True:
        print('{} Es palíndromo'.format(word))

    else:
        print('{} No es palíndromo'.format(word))