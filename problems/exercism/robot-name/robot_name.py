from random import Random
import string


class Robot:
    __PREFIX_LEN = 2
    __SUFFIX_LEN = 3

    def __init__(self) -> None:
        self.random = Random()
        self.name = self.__assign_name()

    def reset(self):
        self.name = self.__assign_name()

    def __assign_name(self) -> str:
        name = []
        for _ in range(self.__PREFIX_LEN):
            name.append(self.random.choice(string.ascii_uppercase))
        for _ in range(self.__SUFFIX_LEN):
            name.append(self.random.choice(string.digits))
        return ''.join(name)
