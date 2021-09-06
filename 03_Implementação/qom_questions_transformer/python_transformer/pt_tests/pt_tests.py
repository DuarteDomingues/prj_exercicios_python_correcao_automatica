
import unittest

import logging

import sys

sys.path.append('/home/jbs/develop/201902_questions_transformer')

from python_transformer.pt_python_transformer_interface import load_source_code
from python_transformer.pt_python_transformer import CommentsNotSupportedException
from python_transformer.pt_python_transformer import BackslashesNotSupportedException
from python_transformer.pt_python_transformer import NonTerminatingNewLinesNotSupportedException

log = logging.getLogger(__name__)
logging.basicConfig(filename="pt_tests.log", level=logging.DEBUG)

class PythonTransformerTests(unittest.TestCase):

    def format(self, source_code, reversed_code):

        return ("----- source code -----\n" + source_code
                + "----- reversed code -----\n" + reversed_code
                + "----- end -----\n")

    def revert_code(self, source_code):

        logging.debug("")
        logging.debug("revert code: start")
        logging.debug("--- begin source code   ---")
        logging.debug("\n" + source_code)
        logging.debug("--- end source code     ---")

        code_structure = load_source_code(source_code)
        reversed_code  = code_structure.to_string()

        logging.debug("revert code: end")
        logging.debug("--- begin reversed code ---")
        logging.debug("\n" + reversed_code)
        logging.debug("--- end reversed code   ---")

        assert reversed_code == source_code, self.format(source_code, reversed_code)

    def test01_statements_list(self):

        source_code = "x"
        self.revert_code(source_code)

    def test02_assignment(self):

        source_code    = "x = y"
        self.revert_code(source_code)

    def test03_literal_set(self):

        source_code    = "A = {1, 2, 3}"
        self.revert_code(source_code)

    def test04_literal_empty_set(self):

        source_code    = "A = {}"
        self.revert_code(source_code)

    def test05_literal_dictionary(self):

        source_code    = "B = {1:2, 2:3}"
        self.revert_code(source_code)

    def test06_literal_empty_dictionary(self):

        source_code    = "B = {}"
        self.revert_code(source_code)

    def test07_set_intersection(self):

        source_code    = "A & B"
        self.revert_code(source_code)

    def test08_function_call(self):

        source_code    = "print(x)"
        self.revert_code(source_code)

    def test09_function_definition(self):

        source_code    = """def f(x):
    x = 0"""
        self.revert_code(source_code)

    def test10_function_definition(self):

        source_code    = """def f(x, y):
    x = 0
    z = y
    w = 1"""
        self.revert_code(source_code)

    def test10_for(self):

        source_code    = """for n in range(3):
    print(n)"""

        self.revert_code(source_code)

    def test11_slice(self):

        source_code    = """x[n]
x[0:]
x[:10]
x[5:9]
x[:]
x[10:20:5]
x[::5]"""

        self.revert_code(source_code)

    def test12_attribute(self):

        source_code    = """x.y = 1"""

        self.revert_code(source_code)

    def test13_list(self):

        source_code    = """x = []
y = [1]
z = [1, 2]
w = [x, y, z]"""

        self.revert_code(source_code)

    def test14_return(self):

        source_code    = """return 1
return
def f():
    return 2"""

        self.revert_code(source_code)

    def test15_class(self):

        source_code    = """class x:
    def __init__(self):
        self.y = 0
    def get_y(self):
        return self.y"""

        self.revert_code(source_code)

    def not_supported_yet_test15_backslash_line_continuation(self):

        source_code    = r"""x \
= y"""

        try:
            self.revert_code(source_code)
        except BackslashesNotSupportedException:
            logging.debug(" as expetected, a source code with backslashes raised the BackslashesNotSupportedException exception.")

    def test15_line_continuation(self):

        source_code    = r"""x = [1,
    2]"""

        try:
            self.revert_code(source_code)
        except NonTerminatingNewLinesNotSupportedException:
            logging.debug(" as expetected, a source code with non terminating new lines raised the NonTerminatingNewLinesNotSupportedException exception.")

    def test15_empty_line_continuation(self):

        source_code    = r"""x = 1

y = 2"""

        try:
            self.revert_code(source_code)
        except NonTerminatingNewLinesNotSupportedException:
            logging.debug(" as expetected, a source code with non terminating new lines raised the NonTerminatingNewLinesNotSupportedException exception.")

    def test16_comments(self):

        source_code    = """x = 1
y = 2 # a comment"""

        # try: 
        #     self.revert_code(source_code)
        # except CommentsNotSupportedException:
        #     logging.debug(" as expetected, a source code with comments raised the CommentsNotSupportedException exception.")

        self.revert_code(source_code)

    def test17_from_import(self):

        source_code = """from random import choice
from random import choice, randint
from random import choice as cho
from random import choice as cho, randint
from random import choice as cho, randint as ran"""
        self.revert_code(source_code)

    def test18_equality_sign(self):

        source_code = "x == y"
        self.revert_code(source_code)

    def test19_if(self):

        source_code = """if x == y:
    print(x)
    print(y)
if x == y:
    print(x)
else:
    print(y)"""
        self.revert_code(source_code)

    def test20_str(self):

        source_code = """\"a string\"
x = \"another string\""""
        self.revert_code(source_code)
        
    def test21_less_than_sign(self):

        source_code = "x < y"
        self.revert_code(source_code)

    def test22_sub_sign(self):

        source_code = "x - y"
        self.revert_code(source_code)


    def test23_add_sign(self):

        source_code = "x + y"
        self.revert_code(source_code)

    def test24_not_eq_sign(self):

        source_code = "x != y"
        self.revert_code(source_code)

    def test25_raise(self):

        source_code = "raise Exception(\"raising an exception...\")"
        self.revert_code(source_code)

    def test26_while(self):

        source_code = """x = 0
while x < 10:
    x = x + 1"""
        self.revert_code(source_code)

    def test27_and(self):

        source_code = """x and y
x and y and z
x == y and x == z""" # no parenthesis are supported for now
        self.revert_code(source_code)

    def test28_greater_or_equal_sign(self):

        source_code = "x >= y"
        self.revert_code(source_code)

    def test29_negative_number(self):

        source_code = "x = -1"
        self.revert_code(source_code)

    def test30_import(self):

        source_code = "import string"
        self.revert_code(source_code)

    def test31_global(self):

        source_code = """global x
global y, z"""
        self.revert_code(source_code)

    def test32_none(self):

        source_code = """None"""
        self.revert_code(source_code)





if __name__ == '__main__':

    logging.debug("-----------------------------------------------------------")
    logging.debug("-----------------------------------------------------------")
    logging.debug("----------------- running unit tests... -------------------")
    logging.debug("-----------------------------------------------------------")
    logging.debug("-----------------------------------------------------------")

    # to run all tests
    unittest.main(verbosity=2)
    #unittest.main()

    # to run a single test
    tests = PythonTransformerTests()
    # tests.test01_statements_list()
    # tests.test02_assignment()
    #tests.test03_literal_set()
    #tests.test10_function_definition()
    #tests.test11_slice()
    #tests.test12_attribute()
    #tests.test15_backslash_line_continuation()
    #tests.test16_comments()
