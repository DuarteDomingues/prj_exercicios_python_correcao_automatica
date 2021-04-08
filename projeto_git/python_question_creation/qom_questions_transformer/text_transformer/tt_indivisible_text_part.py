
import logging

from text_transformer.tt_unchangeable_text_sub_part import TTUnchangeableTextSubPart
from text_transformer.tt_changeable_text_sub_part import TTChangeableTextSubPart





class TTIndivisibleTextPart:
    """A TTIndivisibleTextPart is a text part that can be changed only in
it's complete form. Can not be diviseble. It is usefull for situations
like computer programs transformations, where each program token must
be changed only in it's complete for. Example. Consider changing the
function name "f" to "g" in a Python program. The "f" in the "def"
keyword should not be changed to "g"..

    """





    def __init__(self, text_string):

        self.sub_part = TTUnchangeableTextSubPart(text_string)

        # keys are the substrings in the original string to be
        # transformed (changeable strings).  values are lists with
        # subsparts ocurrences objects
        self.sub_parts_dictionary = {}





    def to_string(self):

        return self.sub_part.to_string()




        
    # def get_string_sub_parts(self, original_text, changeable_string):

    #     splited_text = original_text.split(changeable_string)

    #     sub_parts_list = []

    #     for element in splited_text[0:-1]:

    #         sub_part = TTUnchangeableTextSubPart(element)
    #         sub_parts_list.append(sub_part)

    #         sub_part = TTChangeableTextSubPart(changeable_string)
    #         sub_parts_list.append(sub_part)
    #         #self.transformer.append_sub_part(changeable_string, sub_part)
    #         self.sub_parts_dictionary[changeable_string].append(sub_part)

    #     last_element = splited_text[-1]
    #     sub_part = TTUnchangeableTextSubPart(last_element)
    #     sub_parts_list.append(sub_part)

    #     return sub_parts_list
        




    def create_sub_parts(self, changeable_string):

        logging.debug("TTIndivisibleTextPart: create_sub_parts original_string = \""
                      + changeable_string + "\"")

        self.sub_parts_dictionary[changeable_string] = []

        if isinstance(self.sub_part, TTUnchangeableTextSubPart):

            if self.get_original_text() == changeable_string:

                new_sub_part = TTChangeableTextSubPart(changeable_string)
                self.sub_part = new_sub_part
                self.sub_parts_dictionary[changeable_string].append(new_sub_part)

        elif isinstance(self.sub_part, TTChangeableTextSubPart):

            # already a TTChangeableTextSubPart. Nothing to do.
            pass

        else:
            raise Exception("TTTextPart this should be impossible to reach.")





    # def get_sub_parts_list(self):

    #     return self.sub_parts_list





    def get_changeable_sub_parts(self, changeable_string):

        return self.sub_parts_dictionary[changeable_string]





    def transform(self, original_string, new_string):

        #print('|||||||| part transform')

        if (isinstance(self.sub_part, TTChangeableTextSubPart) and
            self.sub_part.get_original_text() == original_string):

            #print('|||||||| sub part transform')
            
            sub_part.transform(new_string)
        




    def get_original_text(self):

        return self.sub_part.get_original_text()
       
