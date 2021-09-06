
import logging

from text_transformer.tt_text_transformer import TTTextTransformer
from text_transformer.tt_text_part import TTTextPart



text_transformer = TTTextTransformer()



def clear():
    """Use this operation start using new texts and new changeable strings.

    """

    text_transformer.clear()





def load_text(text_string):

    # text_part = TTTextPart(text_string, text_transformer)

    # text_transformer.load_part(text_part)

    text_part = text_transformer.load_text(text_string)

    return text_part





def load_indivisible_text(text_string):

    # text_part = TTTextPart(text_string, text_transformer)

    # text_transformer.load_part(text_part)

    text_part = text_transformer.load_indivisible_text(text_string)

    return text_part





def add_changeable(a_string):
    """This method adds a string that can be changeable in the future
    using operations change_all_occurrences or change_one_occurrence.
    This step of adding the changeable strings before actually
    changing them is need to prevent small strings to be changed that
    apear in bigger ones destroying the bigger ones. The changes are made
    from bigger strings to be changed to smaller strings to be
    changed. Thats why the processor must know a priori all strings
    that can be changed.

    If you try to added changeable strings after changing a string,
    and exception is raised.

    """

    text_transformer.add_changeable(a_string)





def change_all_occurrences(original_string, new_string):
    """If original_string was not added as changeable an exception is
    raised.

    """


    logging.debug("tt_text_transformer_interface.change_all_occurrences"
                  + " original_string = \"" + original_string + "\" new_string"
                  + " = \"" + new_string + "\"")

    text_transformer.change_all_occurrences(original_string, new_string)





def change_all_indivisible_occurrences(original_string, new_string):
    """If original_string was not added as changeable an exception is
    raised.

    """


    logging.debug("tt_text_transformer_interface.change_all_indivisibleoccurrences"
                  + " original_string = \"" + original_string + "\" new_string"
                  + " = \"" + new_string + "\"")

    text_transformer.change_all_indivisible_occurrences(original_string,
                                                        new_string)





def change_all_occurrences_in_parts(original_string, new_string, parts_list):
    """If original_string was not added as changeable an exception is
    raised.

    """


    logging.debug("tt_text_transformer_interface.change_all_occurrences"
                  + " original_string = \"" + original_string + "\" new_string"
                  + " = \"" + new_string + "\"")

    text_transformer.change_all_occurrences_in_parts(original_string,
                                                     new_string,
                                                     parts_list)





def change_one_occurrence(original_string, new_string, occurrence):
    """If original_string was not added as changeable an exception is
    raised.

    """

    text_transformer.change_one_occurrence(original_string,
                                           new_string,
                                           occurrence)





    
def change_one_indivisible_occurrence_in_parts(original_string,
                                               new_string,
                                               occurrence_number,
                                               parts_list):
    """If original_string was not added as changeable an exception is
    raised.

    """

    logging.debug(
        f'tt_text_transformer_interface.change_one_indivisible_occurrence_in_parts original_string = \"{original_string}\" new_string = \"{new_string}\" occurrence_number = {str(occurrence_number)}')

    text_transformer.change_one_indivisible_occurrence_in_parts(
        original_string, new_string, occurrence_number, parts_list)





