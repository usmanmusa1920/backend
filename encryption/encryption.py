import random


# Python programm, a like of ransome ware script.
class Decrypt:
    def __init__(self):
        self.send = None
        self.store = []

        # added with the converted unicode character
        self.guess = random.randint(1, 9)

    # sender encrypts the data
    def sender_encrypts(self):
        self.send = input("\n  Enter secret data: ")
        print()

        # convert each character of the secret data to (Unicode code point for a one-character string.)
        self.store = [ord(i) + self.guess for i in self.send]
        print(f"  Encrypted data: {''.join(chr(i) for i in self.store)}\n")

    # receiver decrypts the data
    def receiver_decrypt(self):
        decrypt_data = "".join(chr(i - self.guess) for i in self.store)
        # The `decrypted_data` method Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

        print("  Decrypted data:", decrypt_data, "\n")


security = Decrypt()
security.sender_encrypts()
security.receiver_decrypt()
