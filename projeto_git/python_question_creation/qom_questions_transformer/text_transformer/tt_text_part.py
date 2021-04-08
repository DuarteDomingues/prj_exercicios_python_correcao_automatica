#
# history
#
# 2020/05/27 added de possibility of asking for a changeable string
# that is not in the sub_parts_dictionary to support
# change_one_occurrence_in_parts. (jbs)
#





import logging

from text_transformer.tt_unchangeable_text_sub_part import TTUnchangeableTextSubPart
from text_transformer.tt_changeable_text_sub_part import TTChangeableTextSubPart





class TTTextPart:
    """A TTTextPart is a sequence of TTUnchangeableTextSubPart's and
    TTChangeableTextSubPart's.

    """





    #def __init__(self, text_string, text_transformer):
    def __init__(self, text_string):

        self.sub_parts_list = [TTUnchangeableTextSubPart(text_string)]

        #self.transformer = text_transformer

        # keys are the substrings in the original string to be
        # transformed (changeable strings).  values are lists with
        # subsparts ocurrences objects
        self.sub_parts_dictionary = {}





    def to_string(self):

        result = ""

        for sub_part in self.sub_parts_list:

            result = result + sub_part.to_string()

        return result




        
    def get_string_sub_parts(self, original_text, changeable_string):

        splited_text = original_text.split(changeable_string)

        sub_parts_list = []

        for element in splited_text[0:-1]:

            sub_part = TTUnchangeableTextSubPart(element)
            sub_parts_list.append(sub_part)

            sub_part = TTChangeableTextSubPart(changeable_string)
            sub_parts_list.append(sub_part)
            #self.transformer.append_sub_part(changeable_string, sub_part)
            self.sub_parts_dictionary[changeable_string].append(sub_part)

        last_element = splited_text[-1]
        sub_part = TTUnchangeableTextSubPart(last_element)
        sub_parts_list.append(sub_part)

        return sub_parts_list
        




    def create_sub_parts(self, changeable_string):

        logging.debug("TTTextPart: create_sub_parts original_string = \""
                      + changeable_string + "\"")

        new_sub_parts_list = []
        self.sub_parts_dictionary[changeable_string] = []

        for sub_part in self.sub_parts_list:

            if isinstance(sub_part, TTUnchangeableTextSubPart):
                original_text = sub_part.to_string()
                sub_parts_list = self.get_string_sub_parts(original_text,
                                                           changeable_string)
                new_sub_parts_list.extend(sub_parts_list)
            
            elif isinstance(sub_part, TTChangeableTextSubPart):

                new_sub_parts_list.append(sub_part)

            else:
                raise Exception("TTTextPart this should be impossible to reach.")

        self.sub_parts_list = new_sub_parts_list





    # def get_sub_parts_list(self):

    #     return self.sub_parts_list





    def get_changeable_sub_parts(self, changeable_string):

        # added de possibility of asking for a changeable string that
        # is not in the sub_parts_dictionary to support
        # change_one_occurrence_in_parts
        if changeable_string in self.sub_parts_dictionary:
        
            return self.sub_parts_dictionary[changeable_string]

        else:

            return []





    def transform(self, original_string, new_string):

        #print('|||||||| part transform')

        for sub_part in self.sub_parts_list:

            if (isinstance(sub_part, TTChangeableTextSubPart) and
                sub_part.get_original_text() == original_string):

                #print('|||||||| sub part transform')

                sub_part.transform(new_string)
        




    def get_original_text(self):

        result = ""

        for sub_part in self.sub_parts_list:

            result = result + sub_part.get_original_text()

        return result
       
