class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def set_password(self, new_password):
        self.password = new_password
        return self
    def check_password(self, password):
        if password == self.password:
            return True
        else:
            return False

account = UserAccount('L1pol', 'xxxxxx', 'yarik')
print('Ваш текущий пароль: ', account.password)
newp = input('Введите новый пароль: ')
print(account.set_password(newp))
if account.password == 'yarik':
    print('Пароль совпадает с текущим, придумайте новый')
else:
    print('Ваш новый пароль: ', account.password)