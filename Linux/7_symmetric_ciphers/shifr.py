from dataclasses import dataclass, field
from random import randint
from re import findall
import  re
import string
import collections
import  random

@dataclass
class CEASAR():
    key: int
    input_message: str
    encrypted_message: str = field(init=False)
    decrypted_message: tuple = field(init=False)

    def __post_init__(self):
        self.encrypted_message = self.encrypt(self.key, self.input_message)
        self.decrypted_message = self.check_result(self.input_message,self.nonkey_decrypt())

    def encrypt(self, key, string):
        res = ''
        for char in string:
            if char.isalpha() is True:
                res += chr((ord(char) + key) % 65536)
            else:
                res += char
        return res

    def decrypt(self, k, msg):
        return self.encrypt((-1) * k, msg)

    def nonkey_decrypt(self):
        c = collections.Counter(filter(lambda ch: not ch.isspace(), self.encrypted_message))
        most_common = c.most_common()  # ordered by most -> least common
        plaintext = {}
        for ch, _ in most_common:
            for i in string.ascii_lowercase+''.join([chr(i) for i in range(ord('а'),ord('а')+32)]):
                diff = ord(ch) - ord(i)
                plaintext[diff] = self.decrypt(diff, self.encrypted_message)
        return plaintext

    def check_result(self, dec_messgage, dec_nonkey_message):
        for key, msg in dec_nonkey_message.items():
            if dec_messgage == msg:
                return msg,key


@dataclass
class VERNAN():
    key: str
    input_message: str
    encrypted_func: object = field(init=False)
    decrypted_func: object = field(init=False)
    d : list = field(init=False)
    prepval: object = field(init=False)

    def __post_init__(self):
        self.prepval = lambda val: zip(range(0, len(val)), val)
        self.d = [chr(i) for i in range(127)]
        self.encrypted_func = lambda ch, key: (ch + key) % len(self.d)
        self.decrypted_func =lambda ch, key: (ch - key + len(self.d)) % len(self.d)


    def vigenere(self, value, key, func):
        kl = len(key)
        value = self.prepval(value)
        e = [func(ord(c), ord(key[i % kl])) for (i, c) in value]
        return ''.join([self.d[c] for c in e])




if __name__ == "__main__":
    print('----------ШИФР ЦЕЗАРЯ----------')
    _ceasar = CEASAR(6, 'Я люблю мёд а вы любите мёд Он отлично сочетается с зеленым чаем чясчя ываыф вафыук ')
    print('Зашифрованное сообщение - ',_ceasar.encrypted_message)
    print('Расшифрованное сообщение - ',_ceasar.decrypt(_ceasar.key, _ceasar.encrypted_message))
    print('Все расшифрованные сообщения - ', _ceasar.nonkey_decrypt())
    print(f"Найденный ключ - {_ceasar.decrypted_message[1]}, Расшифрованное сообщение - {_ceasar.decrypted_message[0]}")
    print('----------ШИФР Вернама----------')
    _vernan = VERNAN('key','Hello world')
    tmp = _vernan.vigenere(_vernan.input_message, _vernan.key, _vernan.encrypted_func)
    print('Зашифрованное сообщение - ',tmp)
    print('Расшифрованное сообщение - ',_vernan.vigenere(tmp, _vernan.key, _vernan.decrypted_func))
