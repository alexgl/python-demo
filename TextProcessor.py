"""
TextProcessor class handles text
"""
__author__ = 'Alex Golovin'

import string
from typing import List, Any


class File:
    def __init__(self, path):
        self._path = path
        self._open_as_read_only(path)

    _path = ''
    _lines_of_file = []

    """
    Loads _lines_of_file with lines from read file
    """

    def _open_as_read_only(self, path):
        print("Path is " + str(path))
        file = open(path, 'r')
        self._lines_of_file = file.readlines()

    """
    returns the private variable __lines_of_file containing all the lines of the file
    as a list of strings 
    """

    def get_lines_of_file(self):
        return self._lines_of_file

    def print_out_lines_of_file(self):
        print('\n\nFILE path is ' + self._path)
        print('-BEGIN')
        for file_line in self._lines_of_file:
            file_line = file_line.rstrip("\n")
            print(file_line)
        print('-END\n\n')
