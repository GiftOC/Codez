password= input(str('Enter your passcode: '))


alphabet = 'abcdefghijklmnopqrstuvwxyz'
passcode = password
encoder = 2

def encoding():

      encrypted_pass = ''
      for char in passcode.lower():
            if char == ' ':
                  encrypted_pass += char
            elif char in alphabet:
                  alphabet.find(char)
                  index = alphabet.find(char)
                  index += encoder % len(alphabet)
                  encrypted_pass += alphabet[index]
      print('plain passcode: ', passcode)
      print('encrypted passcode: ', encrypted_pass)
encoding()