# coding=utf-8
import re
from module_regex.handbook import Handbook


class Regex(object):
    def __init__(self):
        self.__handbook = None

    def loadhandbook(self):
        if not self.__handbook:
            self.__handbook = Handbook()

    def show_compile(self):
        pass

    def show_match(self):
        pass
