# import os.path
import pathlib
import argparse

import Search

parser = argparse.ArgumentParser(description='Use Regex to find pattern in file')
parser.add_argument('-l', '--list', nargs='+', help='Pass list of files to search')
parser.add_argument('-r', '--regex', type=str, help='Pass regex to search for', required=True)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-u", "--underscore", action='store_true')
group.add_argument("-c", "--color", action='store_true')
group.add_argument("-m", "--machine", action='store_true')

args = parser.parse_args()

search_output_type = ''
if args.underscore:
    search_output_type = '-u'

if args.color:
    search_output_type = '-c'

if args.machine:
    search_output_type = '-m'

relative_path = str(pathlib.Path().absolute()) + '/Data/SampleInput.txt'

# search_file = Search.SearchFile.get_lines_of_file(relative_path)
search_file = Search.SearchFile(relative_path, search_output_type)
search_file.search_lines_for_regex(args.regex)
