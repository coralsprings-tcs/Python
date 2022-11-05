possible_passwords = ['something','password123','a thing', 'a password']
password = 'password123'

def guess_password_with_input(guess:str, password:str) -> bool:
    if guess == password:
        return True
    return False

for guess in possible_passwords:
    if guess_password_with_input(guess, password):
        print(f'Access granted! (password is {guess})')
        break
    else:
        print(f'Access denied. (password tried was {guess})')
