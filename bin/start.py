from os import getcwd, path
from sys import path as sys_path
sys_path.insert(0, path.dirname(getcwd()))

from multiprocessing import Process

from conf.config import *
from core.GUImain import App


if __name__=='__main__':
    appGUI = App()