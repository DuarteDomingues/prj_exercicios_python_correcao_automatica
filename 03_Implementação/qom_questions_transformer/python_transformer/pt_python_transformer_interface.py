
import logging

#from text_transformer.tt_text_transformer import TTTextTransformer
#from text_transformer.tt_text_part import TTTextPart

from text_transformer.tt_text_transformer_interface import change_all_occurrences_in_parts
import text_transformer.tt_text_transformer_interface

#from py_transformer.pt_nodes.pt_identifier import PTIdentifier
#from py_transformer.pt_nodes.pt_str        import PTStr

#from py_transformer import py_transformer
# new filename 2019/02/26
#from pt_python_transformer import pt_python_transformer
from python_transformer.pt_python_transformer import PTPythonTransformer

from text_transformer.tt_text_transformer_interface import change_all_indivisible_occurrences





python_transformer = PTPythonTransformer()

def load_source_code(source_code_string):

    return python_transformer.load_source_code(source_code_string)





def change_token_all_occurrences(original_text, new_text):

    change_all_indivisible_occurrences(original_text, new_text)





def change_all_occurrences(original_text, new_text):

    text_transformer.tt_text_transformer_interface.change_all_occurrences(original_text, new_text)
    text_transformer.tt_text_transformer_interface.change_all_indivisible_occurrences(original_text, new_text)


    


def change_token_one_occurrence_in_parts(original_text,
                                         new_text,
                                         occurrence_number,
                                         parts_list):

    text_transformer.tt_text_transformer_interface.change_one_indivisible_occurrence_in_parts(original_text, new_text, occurrence_number, parts_list)



