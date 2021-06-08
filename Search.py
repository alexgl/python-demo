"""

"""

__author__ = 'Alex Golovin'

# python modules
import re
from itertools import tee

# project classes
import TextProcessor


class SearchFile:

    _underscore = False
    _color = False
    _machine = False


    def __init__(self, path_to_file, param):
        self._underscore = False
        self._color = False
        self._machine = False

        self._list_of_matches = []

        self._file_path = path_to_file
        self._file = TextProcessor.File(path_to_file)

        if param is not None:
            if param == '-u' or param == '--underscore':
                self._underscore = True

            if param == '-c' or param == '--color':
                self._color = True

            if param == '-m' or param == '--machine':
                self._machine = True

    def get_lines_of_file(self, path_to_file):
        text_processor = TextProcessor.File(path_to_file)
        text_processor.print_out_lines_of_file()
        return text_processor.get_lines_of_file()

    def search_lines_for_regex(self, regex):
        list_of_lines_of_file = self.get_lines_of_file(self._file_path)

        line_counter = 0
        print('->Matches<-')
        for line in list_of_lines_of_file:
            line_counter += 1
            result = re.finditer(regex, line)

            result, result_copy = tee(result)

            result_length = len(list(result_copy))

            if result_length != 0:
                self._list_of_matches.append(self._file_path
                                       + ':'
                                       + str(line_counter)
                                       + self.format_result(result)
                                       )

        self.print_results(self._list_of_matches)

    """
    Formats based on arguments passed in
    """
    def format_result(self, result):
        return_string = ''

        if self._underscore:
            return_string = ' '
            for group in result:
                return_string = '\n' + group.string

                pre_caret_string = ' ' * group.regs[0][0]
                caret_string = '^' * (group.regs[0][1] - group.regs[0][0])

                return_string += pre_caret_string + caret_string

            return return_string

        if self._color:
            return_string = ' '
            for group in result:
                pre_color_string = group.string[0:group.regs[0][0]]
                color_string = '\x1b[6;30;42m' + group.string[group.regs[0][0]:group.regs[0][1]] + '\x1b[0m'
                post_color_string = group.string[group.regs[0][1]:len(group.string)]

                return_string += (pre_color_string + color_string + post_color_string)

            return return_string
        if self._machine:
            for group in result:
                return_string += ':' + str(group.regs[0][0]) + ':' + group.string

            return return_string

    def print_results(self, results):
        for result_string in results:
            print(result_string)
