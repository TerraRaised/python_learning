# #todo: Написать авторизацию пользователя в систему.
# При реализации авторизации спроектировать абстрактный класс и реализовать методы в наследуемом классе
# login, check_password, check_login

# При запуске программы пользователю необходимо ввести
# логин и пароль, поэтапно.
# login: _________
# password: ________
#
# При неправильном вводе логина должно генерироваться пользовательское исключение LoginNotFound
# Введеный пароль должен проверятся на длину. Длина должна быть более 8 символов иначе генерируем пользовательское
# исключение LengthError
# При вводе некорректного пароля генерируем соответсвуещее исключение
# При успешном заходе генерируем исключение "Доступ разрешен!"

from abc import ABC

truelog = "admin"
truepswd = "rfhfcbr123"


class LengthError(Exception):
    pass


class LoginNotFound(Exception):
    pass


class WrongPassword(Exception):
    pass


class Authorization(ABC):
    def check_password(self):
        if len(self.pswd) < 8:
            raise LengthError
        if self.pswd != truepswd:
            raise WrongPassword

    def check_login(self):
        if self.log != truelog:
            raise LoginNotFound

    def login(self, log, pswd):
        print("login: _________")
        log = input()
        self.log = log
        try:
            self.check_password()
        print("password: ________")
        pswd = input()
        self.pswd = pswd
        pass



