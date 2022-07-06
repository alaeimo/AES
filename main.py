from AES import AES
import unittest
import string
import random
class TEST_AES(unittest.TestCase):
    def __generate_key(self):
        return ''.join([random.choice(string.ascii_letters + string.digits + ' ') for i in range(16)])
    def __generate_round(self):
        return random.choice([10,12,14])
    def __generate_text(self):
        return ''.join([random.choice(string.ascii_letters + string.digits + ' ') for i in range(1024)])
    def aes_test(self):
        key = self.__generate_key()
        rounds = self.__generate_round()
        text = self.__generate_text()
        aes = AES(key,rounds)
        encrypted = aes.encrypt(text)
        decrypted = aes.decrypt(encrypted)
        self.assertEqual(text,decrypted)

    def test_function_calls(self):
        print('Test1: 100 random texts, keys and rounds:\n')
        for _ in range(100):
            self.aes_test()
    def test_my_text(self):
        print('\nTest2: read a text file and encrypt it:\n')
        aes = AES('tobeornot',10)
        with open('in.txt','r',encoding='utf-8') as f:
            text = f.read()
        print(f'Current_text: {text}')
        encrypted = aes.encrypt(text)
        print(f'Encrypted: {encrypted}')
        decrypted = aes.decrypt(encrypted)
        print(f'Decrypted: {decrypted}')
        with open('out.txt','w',encoding='utf-8',errors='surrogateescape') as f:
            f.write(encrypted)
        self.assertEqual(text,decrypted)

    

if __name__ == "__main__":
    unittest.main()




