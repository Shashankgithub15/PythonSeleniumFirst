#filename should also start with test keyword
#pytest method name always start with test
#anycode should be wrapped in methods
#method name should have sense
#-k stands for method names execution, -s logs in output, -v stand for more info
#we can run specific file as folder name . file name
#we can mark (tag) tests @pytest.mark.smoke or whatever name we want other than smoke and then run with -m

import pytest

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])


# @pytest.mark.smoke
# def test_firstProgram():
#     print("hello")
#
# def test_secondProgram():
#     print("Good Morning")