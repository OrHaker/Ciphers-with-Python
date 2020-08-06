import string
import math
import os.path
import random

# Practice python logic by writing ciphers
EXCEPTION_MESSAGE = "An exception occurred  "


def brute_force_attack(string):
    """Enter string to use Brute-Force Attack """
    try:
        for key in range(1, 26):
            string_to_return = ""
        for l in string:
            if not(l >= 'A'and l <= 'Z' or l >= 'a'and l <= 'z'):
                string_to_return += l
            elif key + ord(l.upper()) > ord('Z'):
                string_to_return += chr(ord('A') + ord('Z') - ord(l.upper()))
            else:
                string_to_return += chr(ord(l.upper())+key)
        print(string_to_return)
        return string_to_return
    except Exception as ex:
        print(EXCEPTION_MESSAGE, ex)


def route_encrypt(text, key):
    """encrypt text using route cipher spiral way"""
    # create matrix to hold the data
    try:
        cols_size = key  # calc how many cols
        rows_size = math.ceil(len(text)/key)  # calc how many rows
        # matrix of X
        matrix = [['X' for i in range(cols_size)]for j in range(rows_size)]
        pos = 0
        # text = text.replace(' ', '')  # to remove spaces
        # put the string in the matrix
        for i in range(rows_size):
            for j in range(cols_size):
                if not pos >= len(text):
                    matrix[i][j] = text[pos]
                    pos += 1
        text_to_return = ""

        # scan the matrix in the spiral route
        # going the maxiest way of rounds (given by the cols or rows)
        for i in range(max(cols_size, rows_size)):
            # Going down on right side
            for j in range(i, rows_size-i-1):
                text_to_return += matrix[j][cols_size-i-1]
                # Going left on the bottom side
            for j in range(cols_size-i-1, i, -1):
                text_to_return += matrix[rows_size-i-1][j]
                # Going up on the left side
            for j in range(rows_size-i-1, i, -1):
                text_to_return += matrix[j][i]
                # Going right on the top side
            for j in range(i, cols_size-i-1):
                text_to_return += matrix[i][j]
        print(text_to_return)
        return text_to_return
    except (ValueError, IndexError, Exception) as ex:
        print(EXCEPTION_MESSAGE, ex)


def route_decrypt(text, key):
    """decrypt text using route cipher spiral way"""
    try:
        # create matrix to hold the data
        cols_size = key  # calc how many cols
        rows_size = int(len(text)/key)  # calc how many rows
        # matrix of X
        matrix = [['X' for i in range(cols_size)]for j in range(rows_size)]
        pos = 0
        # scan the matrix in the spiral route
        # going the maxiest way of rounds (given by the cols or rows)
        for i in range(max(cols_size, rows_size)):
            # Going down on right side
            for j in range(i, rows_size-i-1):
                matrix[j][cols_size-i-1] = text[pos]
                pos += 1
                # Going left on the bottom side
            for j in range(cols_size-i-1, i, -1):
                matrix[rows_size-i-1][j] = text[pos]
                pos += 1
                # Going up on the left side
            for j in range(rows_size-i-1, i, -1):
                matrix[j][i] = text[pos]
                pos += 1
                # Going right on the top side
            for j in range(i, cols_size-i-1):
                matrix[i][j] = text[pos]
                pos += 1

        # concate the string from the matrix
        str_to_return = ""
        for i in range(rows_size):
            for j in range(cols_size):
                str_to_return += matrix[i][j]
        return str_to_return.strip('X')
    except (ValueError, IndexError, Exception) as ex:
        print(EXCEPTION_MESSAGE, ex)

# one time pad  cipher

# keys and text taken from text file


def one_time_pad_decrypt():
    try:
        txt_file, key_file = None, None
        txt_file = open("G:\\text.txt", "r", encoding='utf-8')
        text = list(txt_file.read())
        key_file = open("G:\\key.txt", "r")
        keys = key_file.read().split(',')
        return "".join([chr(ord(text[i]) ^ int(keys[i])) for i in range(len(text))])
    except Exception as ex:
        print(exception_message, ex)
    finally:
        if txt_file != None:
            txt_file.close()
        if key_file != None:
            key_file.close()


# gets arguments from other functions
def one_time_pad_decrypt2(text, keys):
    return "".join([chr(ord(text[i]) ^ int(keys[i])) for i in range(len(text))])


# encrypt a string
def one_time_pad_encrypt(str):
    # returns a list with encrypted string and keys list
    keys = [random.randint(0, 255) for i in range(len(str))]
    return ["".join([chr(ord(str[i]) ^ int(keys[i])) for i in range(len(str))]), keys]


def atbash_cipher(s):
    """uses atbash cipher to encrypt word"""
    try:
        new_s = ""
        for l in s:
            if string.ascii_lowercase.find(l, 0) != -1:
                pos = string.ascii_lowercase.find(l, 0)
                reverse = string.ascii_lowercase[::-1]
                new_s += reverse[pos]
            elif string.ascii_uppercase.find(l, 0) != -1:
                pos = string.ascii_uppercase.find(l, 0)
                reverse = string.ascii_uppercase[::-1]
                new_s += reverse[pos]
            else:
                new_s += l
        return new_s
    except (ValueError, IndexError) as ex:
        print(EXCEPTION_MESSAGE, ex)


def rot13_cipher(s):
    """uses rot13 cipher to encrypt word"""
    try:
        new_s = ""
        for l in s:
            # if the letter is lowercase and in the first half
            if string.ascii_lowercase[:13].find(l, 0) != -1:
                pos = string.ascii_lowercase[:13].find(l, 0)
                opposite = string.ascii_lowercase[13:]
                new_s += opposite[pos]
            # if the letter is lowercase and in the second half
            elif string.ascii_lowercase[13:].find(l, 0) != -1:
                pos = string.ascii_lowercase[13:].find(l, 0)
                opposite = string.ascii_lowercase[:13]
                new_s += opposite[pos]
            # if the letter is uppercase and in the first half
            elif string.ascii_uppercase[:13].find(l, 0) != -1:
                pos = string.ascii_uppercase[:13].find(l, 0)
                opposite = string.ascii_uppercase[13:]
                new_s += opposite[pos]
            # if the letter is uppercase and in the second half
            elif string.ascii_uppercase[13:].find(l, 0) != -1:
                pos = string.ascii_uppercase[13:].find(l, 0)
                opposite = string.ascii_uppercase[:13]
                new_s += opposite[pos]
            else:
                new_s += l
        return new_s
    except (ValueError, IndexError) as ex:
        print(EXCEPTION_MESSAGE, ex)


def rail_fence_encrypt(string, key):
    """ encrypt function that gets string and key and uses rail fence cipher"""
    try:
        cols_size = len(string)
        arr_of_words = [[0 for i in range(cols_size)] for j in range(key)]
        pos = 0
        direction = 1
        for j in range(0, cols_size):
            #  direction variable sets the moving direction
            arr_of_words[pos][j] = string[j]
            pos += direction
            if pos == 0 or pos == key-1:
                direction *= (-1)

        str_to_return = ""  # concat the new string
        for i in range(key):
            for j in range(cols_size):
                if arr_of_words[i][j] != 0:
                    str_to_return += arr_of_words[i][j]
        return str_to_return
    except (ValueError, IndexError) as ex:
        print(EXCEPTION_MESSAGE, ex)


def rail_fence_decrypt(string, key):
    try:
        cols_size = len(string)
        arr_of_words = [[0 for i in range(cols_size)] for j in range(key)]
        pos = 0
        direction = 1
        # find cipher route
        for j in range(0, cols_size):
            arr_of_words[pos][j] = -1
            pos += direction
            if pos == 0 or pos == key-1:
                direction *= (-1)
        pos = 0
        for i in range(key):
            for j in range(cols_size):
                if arr_of_words[i][j] == -1:
                    arr_of_words[i][j] = string[pos]
                    pos += 1
        str_to_return = ""  # concat decrypted string
        pos = 0
        direction = 1
        for j in range(0, cols_size):
            str_to_return += arr_of_words[pos][j]
            if pos == 0 or pos == key-1:
                direction *= (-1)
        return str_to_return
    except (ValueError, IndexError, Exception) as ex:
        print(exception_message, ex)


def caesar_cipher_encrept(string, key):
    """Enter string to  Encrept in caesar cipher ; Please enter size of key you want to use"""
    try:
        string_to_return = ""
        for l in string:
            if not(l >= 'A'and l <= 'Z' or l >= 'a'and l <= 'z'):
                string_to_return += l
            elif key + ord(l.upper()) > ord('Z'):
                string_to_return += chr(ord('A') + ord('Z') - ord(l.upper()))
            else:
                string_to_return += chr(ord(l.upper())+key)
        return string_to_return
    except (ValueError, IndexError, Exception) as ex:
        print(EXCEPTION_MESSAGE, ex)


def caesar_cipher_decrept(string, key):
    """Enter string to Decrept  in caesar cipher enter size of key you want to use """
    try:
        string_to_return = ""
        for l in string:
            if not(l >= 'A'and l <= 'Z' or l >= 'a'and l <= 'z'):
                string_to_return += l
            elif ord(l.upper()) - key < ord('A'):
                string_to_return += chr(ord('Z') - ord('A') + ord(l.upper()))
            else:
                string_to_return += chr(ord(l.upper())-key)
        return string_to_return
    except (ValueError, IndexError, Exception) as ex:
        print(EXCEPTION_MESSAGE, ex)
