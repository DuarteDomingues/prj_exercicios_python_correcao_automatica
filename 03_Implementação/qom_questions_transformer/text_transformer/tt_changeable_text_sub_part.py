




class TTChangeableTextSubPart:





    def __init__(self, text_string):

        self.original_string = text_string

        self.transformed_string = None





    def get_original_text(self):

        return self.original_string





    def to_string(self):

        if self.transformed_string != None:

            return self.transformed_string

        else:

            return self.original_string





    def transform(self, new_string):

        self.transformed_string = new_string




