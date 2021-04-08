
import unittest

import logging

import sys

sys.path.append('/home/jbs/develop/201902_questions_transformer')

# this import removes an import error. I don't know why (jbs
# 2018/12/12).
#import py_transformer.ast_processor





from text_transformer.tt_text_transformer_interface import load_text
from text_transformer.tt_text_transformer_interface import add_changeable
from text_transformer.tt_text_transformer_interface import change_all_occurrences
from text_transformer.tt_text_transformer_interface import clear

from python_transformer.pt_python_transformer_interface import load_source_code
#from py_transformer.pt_python_transformer_interface import change_identifier_all_occurrences
from python_transformer.pt_python_transformer_interface import change_token_all_occurrences



# from py_transformer.py_transformer import CommentsNotSupportedException
# from py_transformer.py_transformer import BackslashesNotSupportedException
# from py_transformer.py_transformer import NonTerminatingNewLinesNotSupportedException





log = logging.getLogger(__name__)
logging.basicConfig(filename="pt_tests.log", level=logging.DEBUG)





class PythonTransformerTests(unittest.TestCase):

    def format(self, expected, obtained):

        return ("----- expected -----\n" + expected
                + "----- obtained -----\n" + obtained
                + "----- end -----\n")

    def test01_change_identifiers(self):

        text1 = r'''This is a text about function f().\n'''

        source_code1 = '''def f():
    print("hello world!")'''

        source_code2 = '''def g():
    print("hello world!")'''

        text_part = load_text(text1)
        code_structure = load_source_code(source_code1)

        add_changeable('f')

        change_token_all_occurrences('f', 'g')

        text2 = text_part.to_string()
        source_code3 = code_structure.to_string()

        expected = text1 + source_code2

        obtained = text2 + source_code3

        assert obtained == expected, self.format(expected, obtained)

    def test02_change_all_occurrences(self):

        clear()

        text1 = r'''This is a text about function f().\n'''
        text2 = r'''This is a text about gunction g().\n'''
        source_code1 = '''def f():
    print("hello world!")'''
        source_code2 = '''def g():
    print("hello world!")'''

        text_part = load_text(text1)
        code_structure = load_source_code(source_code1)

        add_changeable('f')

        change_all_occurrences('f', 'g')
        change_token_all_occurrences('f', 'g')

        text3 = text_part.to_string()
        source_code3 = code_structure.to_string()

        expected = text2 + source_code2

        obtained = text3 + source_code3

        assert obtained == expected, self.format(expected, obtained)




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
    #tests.test01_statements_list()
    #tests.test02_assignment()
    #tests.test03_literal_set()
    #tests.test11_slice()
    #tests.test12_attribute()
