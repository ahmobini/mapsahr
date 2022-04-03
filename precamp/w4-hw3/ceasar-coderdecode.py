'''
1-write a function to receive two entries (key and a message) and returns an encoded string.
2-write a function to receive two entries (key and encoded message) and returns decodes message.

more info about encode and decode operation:
https://en.wikipedia.org/wiki/Caesar_cipher
'''

key = int(input('enter a key number for encoding: '))
plaintext = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'


def coded(plaintext, key):
    result = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)

        else:
            result += chr((ord(char) + key - 97) % 26 + 97)

    return result

print(coded(plaintext, key))

#
# key = int(input('enter a key number for encoding: '))
# encryptedtext = 'WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ'
#
#
# def decoded(encryptedtext, key):
#     result = ""
#
#     for i in range(len(encryptedtext)):
#         char = encryptedtext[i]
#
#         if (char.isupper()):
#             result += chr((ord(char) - key - 65) % 26 + 65)
#
#         else:
#             result += chr((ord(char) - key - 97) % 26 + 97)
#
#
#     return result
#
# print(decoded(encryptedtext, key))