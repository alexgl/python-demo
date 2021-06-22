from behave import *
import subprocess
from subprocess import PIPE
import pathlib
import io
from contextlib import redirect_stdout
import sys

@given('I run search script with "{text}"')
def step_i_run_search_script_with_args(context, text):
    text = 'main.py ' + text
    run_change_dir = str(pathlib.Path().absolute()).replace('/features', '', 1)
    #run_arg = 'python3 ' + str(pathlib.Path().absolute()) + text
    run_arg = 'python3 ' + text
    #run_arg = text
    print("PATH IS " + run_arg)
    print("~_~_~_Text is >" + run_arg + "<")
    print(subprocess.run('pwd', cwd=run_change_dir, stdout=PIPE).stdout)
    print(subprocess.run('ls', cwd=run_change_dir, stdout=PIPE).stdout)
    context.completed_process = subprocess.Popen(run_arg, cwd=run_change_dir, shell=True, stdout=PIPE, stderr=PIPE)

@then('I verify output has "{text}"')
def step_i_verify_output_has_text(context, text):
    found_text = False
    for line in context.completed_process.stdout:
        if text in str(line):
            found_text = True

    assert found_text

