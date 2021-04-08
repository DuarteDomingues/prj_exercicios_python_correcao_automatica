
import unittest

import logging

import sys

sys.path.append('/home/jbs/develop/201902_questions_transformer')

from text_transformer.tt_text_transformer_interface import load_text
from text_transformer.tt_text_transformer_interface import add_changeable
from text_transformer.tt_text_transformer_interface import change_all_occurrences
from text_transformer.tt_text_transformer_interface import change_all_occurrences_in_parts
from text_transformer.tt_text_transformer_interface import change_one_occurrence
from text_transformer.tt_text_transformer_interface import clear

from text_transformer.tt_text_transformer_interface import load_indivisible_text
from text_transformer.tt_text_transformer_interface import change_all_indivisible_occurrences




log = logging.getLogger(__name__)
logging.basicConfig(filename="tt_tests.log", level=logging.DEBUG)





class TextTransformerTests(unittest.TestCase):





    def test01(self):

        text = "this is a line of text!"

        part = load_text(text)

        text2 = part.to_string()

        assert text == text2, ("text = \n" + text + "\ntext22 = \n" + text2
                               + "\ntext2 should be an unchanged version of "
                               + "text.")




        
    def test02(self):

        text1 = "this is a line of text!"
        text2 = "this is a LINE of text!"

        part = load_text(text1)

        add_changeable("line")
        change_all_occurrences("line", "LINE")

        text3 = part.to_string()

        assert text2 == text3, ("text2 = \n" + text2 + "\ntext3 = \n" + text3
                                + "\ntext3 should equal text2.")




        
    def test03(self):

        text1 = "this is a line of text!\n and this is another line of text..."
        text2 = "this is a LINE of text!\n and this is another LINE of text..."

        clear()

        part = load_text(text1)

        add_changeable("line")
        change_all_occurrences("line", "LINE")

        text3 = part.to_string()

        assert text2 == text3, ("text2 = \n" + text2 + "\ntext3 = \n" + text3
                                + "\ntext3 should equal text2.")




        
    def test04(self):

        text1 = "this is a line of text!\n and this is another line of text..."
        text2 = "this is a LINE of text!\n and this is ANOTHER LINE of text..."

        clear()

        part = load_text(text1)

        add_changeable("line")
        add_changeable("another")

        change_all_occurrences("line",    "LINE")
        change_all_occurrences("another", "ANOTHER")

        text3 = part.to_string()

        assert text2 == text3, ("text2 = \n" + text2 + "\ntext3 = \n" + text3
                                + "\ntext3 should equal text2.")





    def test05(self):

        text1 = "f"
        text2 = "g"

        clear()

        part = load_text(text1)

        add_changeable("f")

        change_all_occurrences("f", "g")

        text3 = part.to_string()

        assert text2 == text3, ("text2 = \n" + text2 + "\ntext3 = \n" + text3
                                + "\ntext3 should equal text2.")




        
    def test06(self):

        text1 = "f f f\n"
        text2 = "f f f\n"
        text3 = "g g g\n"

        clear()

        part1 = load_text(text1)
        part2 = load_text(text2)

        add_changeable("f")

        change_all_occurrences_in_parts("f", "g", [part2])

        text4 = part1.to_string()
        text5 = part2.to_string()

        target = text1 + text3
        result = text4 + text5

        assert target == result, ("result = \n" + result + "\ntarget = \n" 
                                  + target
                                + "\nresult should equal target.")




        
    def test07(self):

        text1 = "def "
        text2 = "f"
        text3 = "g"

        clear()

        part1 = load_indivisible_text(text1)
        part2 = load_indivisible_text(text2)

        add_changeable("f")

        change_all_occurrences("f", "g")

        text4 = part1.to_string()
        text5 = part2.to_string()

        target = text1 + text3
        result = text4 + text5

        assert target == result, ("result = \n" + result + "\ntarget = \n" 
                                  + target
                                + "\nresult should equal target.")




        
    def test07(self):

        text1 = "texto sobre a função f."
        text2 = "f"
        text3 = "g"

        clear()

        part1 = load_text(text1)
        part2 = load_indivisible_text(text2)

        add_changeable("f")

        change_all_indivisible_occurrences("f", "g")

        text4 = part1.to_string()
        text5 = part2.to_string()

        target = text1 + text3
        result = text4 + text5

        assert target == result, ("result = \n" + result + "\ntarget = \n" 
                                  + target
                                + "\nresult should equal target.")




        
if __name__ == '__main__':

    # to run all tests
    logging.debug("")
    logging.debug("running unit tests...")
    logging.debug("")
    unittest.main(verbosity=2)

