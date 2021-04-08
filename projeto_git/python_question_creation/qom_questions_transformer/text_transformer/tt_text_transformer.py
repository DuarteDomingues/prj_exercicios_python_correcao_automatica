
import logging

from text_transformer.tt_text_part             import TTTextPart
from text_transformer.tt_indivisible_text_part import TTIndivisibleTextPart





class TTTextTransformer:





    def __init__(self):

        self.clear()





    def clear(self):

        self.text_parts_list             = []
        self.indivisible_text_parts_list = []

        # keys are the substrings in the original string to be
        # transformed (changeable strings). values are lists with
        # subsparts ocurrences objects
        self.sub_parts_dictionary = {}

        self.changeable_strings_list = []
        self.changeable_strings_list_already_processed = False
        




    # def create_all_sub_parts(self, text_part):

    #     for original_string in self.sub_parts_dictionary.keys():

    #         text_part.create_sub_parts(original_string)
        



        
    def load_part(self, text_part):

        self.text_parts_list.append(text_part)





    def load_indivisible_part(self, text_part):

        self.indivisible_text_parts_list.append(text_part)





    def load_text(self, text_string):

        text_part = TTTextPart(text_string)

        self.load_part(text_part)

        return text_part





    def load_indivisible_text(self, text_string):

        text_part = TTIndivisibleTextPart(text_string)

        self.load_indivisible_part(text_part)

        return text_part





    def add_changeable(self, a_string):

        if self.changeable_strings_list_already_processed == True:

            raise Exception("TTTextTransformer add_changeable: you can't add "
                            + "changeable strings after having already changed"
                            + "strings. Use this operation before the "
                            + "operations  change_all_occurrences and "
                            + "change_one_occurrence. If you want to add "
                            + "new changeables from scratch user restart.")

        # to prevent repetitions and warn user that he alredy added the string
        if a_string in self.changeable_strings_list:

            raise Exception("TTTextTransformer add_changeable: the string \"" 
                            + a_string + "\" was alreday added.")

        self.changeable_strings_list.append(a_string)





    def process_changeable_strings_list(self):

        self.changeable_strings_list.sort(key = len, reverse = True)

        logging.debug("TTTextTransformer process_changeable_strings_list "
                      + "sorted changeable_strings_list = "
                      + str(self.changeable_strings_list))

        for changeable_string in self.changeable_strings_list:

            self.create_sub_parts(changeable_string)

        self.changeable_strings_list_already_processed = True





    def append_sub_part(self, changeable_string, sub_part):

        self.sub_parts_dictionary[changeable_string].append(sub_part)





    def create_sub_parts(self, changeable_string):

        logging.debug("TTTextTransformer create_new_sub_parts "
                      + "original_string = \"" + changeable_string + "\"")

        self.sub_parts_dictionary[changeable_string] = []

        for text_part in self.text_parts_list:

            text_part.create_sub_parts(changeable_string)

        for text_part in self.indivisible_text_parts_list:

            text_part.create_sub_parts(changeable_string)





    # def create_new_sub_parts_if_necessary(self, original_string):

    #     logging.debug("TTTextTransformer create_new_sub_parts_if_necessary "
    #                   + "original_string = \"" + original_string + "\"")

    #     if not (original_string in self.sub_parts_dictionary):

    #         self.create_new_sub_parts(original_string)





    def check_if_is_changeable(self, a_string):

        if not(a_string in self.changeable_strings_list):

            raise Exception("the string \"" + a_string
                            + "\" is not changeable. To be able to change it "
                            + "you must use add_changeable operation before "
                            + "changing it.")





    def change_all_occurrences(self, changeable_string, new_string,
                               parts_list = None):

        self.check_if_is_changeable(changeable_string)

        if self.changeable_strings_list_already_processed == False:

            self.process_changeable_strings_list()

        #self.create_new_sub_parts_if_necessary(original_string)

        if parts_list == None:
            parts_list = self.text_parts_list

        for part in parts_list:

            sub_parts_list = part.get_changeable_sub_parts(changeable_string)

            for sub_part in sub_parts_list:

                sub_part.transform(new_string)





    def change_all_occurrences_in_parts(self, original_string, new_string,
                                        parts_list):

        self.change_all_occurrences(original_string, new_string, parts_list)





    def change_all_indivisible_occurrences(self, changeable_string, new_string,
                                           parts_list = None):

        parts_list_to_use = []

        if parts_list != None:

            for part in parts_list:
                for indivisible_part in self.indivisible_text_parts_list:
                    if part is indivisible_part:
                        parts_list_to_use.append(part)

        else:
            
            parts_list_to_use = self.indivisible_text_parts_list
        
        self.change_all_occurrences_in_parts(changeable_string,
                                             new_string,
                                             parts_list_to_use)





    def change_one_occurrence(self, original_string, new_string, occurrence):

        self.check_if_is_changeable(original_string)

        if self.changeable_strings_list_already_processed == False:

            self.process_changeable_strings_list()

        #self.create_sub_parts_if_necessary(original_string)

        sub_parts_list = self.sub_parts_dictionary[original_string]

        sub_part_index = occurrence - 1

        sub_part = sub_parts_list[sub_part_index]

        sub_part.transform(new_string)



        

    def get_sub_parts_list(self, original_string, parts_list):

        sub_parts_list = []
        for part in parts_list:
            sub_parts_list.extend(
                part.get_changeable_sub_parts(original_string))

        return sub_parts_list



    
        
    def change_one_occurrence_in_parts(self,
                                       original_string,
                                       new_string,
                                       occurrence_number,
                                       parts_list):

        self.check_if_is_changeable(original_string)

        if self.changeable_strings_list_already_processed == False:

            self.process_changeable_strings_list()

        sub_parts_list = self.get_sub_parts_list(original_string, parts_list)

        sub_part_index = occurrence_number - 1

        sub_part = sub_parts_list[sub_part_index]

        sub_part.transform(new_string)



        

    def get_indivisible_parts(self, parts_list):

        indivisible_parts_list = []

        for part in parts_list:
            for indivisible_part in self.indivisible_text_parts_list:
                if part is indivisible_part:
                    indivisible_parts_list.append(part)

        return indivisible_parts_list




    
    def change_one_indivisible_occurrence_in_parts(self,
                                                   changeable_string,
                                                   new_string,
                                                   occurrence_number,
                                                   parts_list):

        indivisible_parts = self.get_indivisible_parts(parts_list)
        
        self.change_one_occurrence_in_parts(changeable_string,
                                            new_string,
                                            occurrence_number,
                                            indivisible_parts)





