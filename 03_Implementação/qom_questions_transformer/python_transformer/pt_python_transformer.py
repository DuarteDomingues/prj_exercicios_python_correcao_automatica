
from ast      import parse
from tokenize import tokenize, STRING, COMMENT
from io       import BytesIO

#from py_transformer.ast_processor import process_ast

# todo - detect comments, non terminating new lines and backslashes
# and warn the user that these constructs are not supported. They must
# be added by hand to the meta python structure.

# new 20190226
from python_transformer.pt_source_code              import PTSourceCode
from text_transformer.tt_text_transformer_interface import load_text
from text_transformer.tt_text_transformer_interface import load_indivisible_text
from text_transformer.tt_text_transformer           import TTTextTransformer





class CommentsNotSupportedException(Exception):
    """Comments are not supoorted now (2017/07/03). This exception is
    raised whenever comments are present in the source code supplied
    to py_transformer. Comments must be added to the py_transformer
    structure using the comments node (not available yet). Not to the
    source.

    """

    pass





class BackslashesNotSupportedException(Exception):
    """Line continuation backslashes are not supoorted now
    (2017/07/04). This exception is raised whenever backslashes are
    present in the source code supplied to py_transformer. Backslashes
    must be added to the py_transformer structure using the Backslashe
    node (not available yet). Not to the source.

    """

    pass





class NonTerminatingNewLinesNotSupportedException(Exception):
    """Non terminating line continuations are not supoorted now
    (2017/07/04). This exception is raised whenever non terminating
    line continuations are present in the source code supplied to
    py_transformer. Non terminating line continuations must be added
    to the py_transformer structure using the
    NonTerminatingLineContinuation node (not available yet). Not to
    the source.

    """

    pass





def get_ignored_lines(source_code_string):



    tokens = tokenize(BytesIO(source_code_string.encode('utf-8')).readline)
    ignored_lines = []

    for token in tokens:

        #print(token)
        
        (tok_type, tok_string, tok_start, tok_end, tok_line) = token

        line_number         = tok_start[0]
        start_column_number = tok_start[1]

        if tok_type == NL and tok_line == "\n":
            ignored_lines.append((line_number, "\n"))

        elif tok_type == COMMENT and start_column_number == 0:
            ignored_lines.append((line_number, tok_line))

    #print(ignored_lines)

    return ignored_lines
            




def get_non_terminating_newlines(source_code_string):

    tokens = tokenize(BytesIO(source_code_string.encode('utf-8')).readline)
    non_terminating_newlines = []

    for token in tokens:

        #print(token)
        
        (tok_type, tok_string, tok_start, tok_end, tok_line) = token

        #line_number         = tok_start[0]
        #start_column_number = tok_start[1]

        if tok_type == NL:
            non_terminating_newlines.append(token)

    return non_terminating_newlines





def check_comments(source_code_string):

    tokens = tokenize(BytesIO(source_code_string.encode('utf-8')).readline)

    for token in tokens:

        (tok_type, tok_string, tok_start, tok_end, tok_line) = token

        if tok_type == COMMENT:
            raise CommentsNotSupportedException





def check_backslashes(source_code_string):
    """Todo: the backslashes should be detected only in the python
statements and expressions. Currenntly it is also detected in
strings."""

    if source_code_string.find("\\") != -1:
        raise BackslashesNotSupportedException





def check_non_terminating_new_lines(source_code_string):

    tokens = tokenize(BytesIO(source_code_string.encode('utf-8')).readline)

    for token in tokens:

        (tok_type, tok_string, tok_start, tok_end, tok_line) = token

        if tok_type == NL:
            raise NonTerminatingNewLinesNotSupportedException





# # this is the old version 2019/02/27
# def load_source_code(source_code_string):

#     # a list with (line_number, line_string) tuples
#     ignored_lines_list = get_ignored_lines(source_code_string)

#     check_comments(source_code_string)
#     check_backslashes(source_code_string)
#     check_non_terminating_new_lines(source_code_string)

#     ast = parse(source_code_string)
        
#     level = 0
#     py_transformer_structure = process_ast(ast, ignored_lines_list)

#     return py_transformer_structure





class PTPythonTransformer:
    '''Strings and commands are added to the general text transformer
througth load_text. Token's text are added to the local text
transformer token_text_transformer because tokens are changed only on
a word basis. Only the hole word in changed. Parts of words are not
changed. As an example if you have a function "f" and want to changed
it to "g" you don't want the "f" on the "def" keyword to be
changed.

    '''




    def __init__(self):

        self.string_parts_list     = []
        self.comment_parts_list   = []
        # keys are parts text strings. values are parts list.
        self.other_parts_by_text = {}





    def store_string_text_part(self, text_part):

        self.string_parts_list.append(text_part)





    def store_comment_text_part(self, text_part):

        self.comment_parts_list.append(text_part)





    def store_text_part(self, text_part):

        text = text_part.get_original_text()

        if text in self.other_parts_by_text:
            
            text_parts_list = self.other_parts_by_text[text]

        else:

            text_parts_list = []
            self.other_parts_by_text[text] = text_parts_list

        text_parts_list.append(text_part)





    def store_space_text_part(self, text_part):

        self.store_text_part(text_part)





    def store_token_text_part(self, tok_type, text_part):

        if tok_type == STRING:

            self.store_string_text_part(text_part)

        elif tok_type == COMMENT:

            self.store_comment_text_part(text_part)

        else:

            self.store_text_part(text_part)





    def get_space_part(self, previous_token, token, tok_line):
        '''Returns a text part with the space between two tokens in the same
line. The text used is copyed from the token line.

        '''

        previous_token_end        = previous_token.end
        previous_token_end_column = previous_token_end[1]
        token_start               = token.start
        token_start_column        = token_start[1]

        text = tok_line[previous_token_end_column:token_start_column]
        text_part = load_indivisible_text(text)
        
        return text_part





    def get_start_space_part(self, token, tok_line):
        '''Returns a text part with the space from the begining of line to the
token start. The text used is copyed from the token line.

        '''

        token_start               = token.start
        token_start_column        = token_start[1]

        text = tok_line[:token_start_column]
        text_part = load_indivisible_text(text)
        
        return text_part





    def load_text(self, tok_type, tok_string):

        if tok_type == STRING:

            text_part = load_text(tok_string)

        elif tok_type == COMMENT:

            text_part = load_text(tok_string)

        else:

            text_part = load_indivisible_text(tok_string)

        return text_part





    def process_source_code(self, source_code_string):

        # result is a list of logical lines.
        # a logical line is a list of parts
        result = []

        tokens = tokenize(BytesIO(source_code_string.encode('utf-8')).readline)

        # the first token has the file encoding. it is not appended to
        # the lines lists
        first_token = next(tokens)

        # a list that stores the identation strings used at each line.
        # this is needed because only the first IDENT token of each
        # indented block is generated by tokenizer
        indentation_list = []

        line_list = []
        result.append(line_list)
        previous_token = first_token
        for token in tokens:

            # https://docs.python.org/3/library/tokenize.html
            # token is a named tuple with attributes 'type', 'string',
            # 'start', 'end', 'line' and 'exact_type'.
            # 'start' and 'end' are (row, columns) tuples 

            #print(token)
            (tok_type, tok_string, tok_start, tok_end, tok_line) = token
            tok_exact_type = token.exact_type
            #print(tok_exact_type)

            # add space between tokens
            if (tok_line == previous_token.line):
                space_part = self.get_space_part(previous_token,
                                                 token,
                                                 tok_line)
                line_list.append(space_part)
            # switch line
            else:
                line_list = []
                result.append(line_list)
                space_part = self.get_start_space_part(token,
                                                       tok_line)
                line_list.append(space_part)

            self.store_space_text_part(space_part)
            
            text_part = self.load_text(tok_type, tok_string)
            line_list.append(text_part)
            self.store_token_text_part(tok_type, text_part)

            previous_token = token

        return result





    # new 20190226
    def load_source_code(self, source_code_string):

        lines_parts = self.process_source_code(source_code_string)

        source_code = PTSourceCode(lines_parts)

        return source_code





# def load_text(text_string):

#     py_transformer_text = None

#     return py_transformer_text





# class PyTransformer:
#     """This is a refactoring of the meta python project based on the fact
#     that meta python was not used in practice. There was a pre
#     processor to convert python to meta pyhton and there were ways to
#     change sources and text (based on variables that referenced all
#     source parts). Allthogh it could be possible to edit the meta
#     python code, in practice this was not done. It was not practical.

#     In this new aproach there is no meta python. Sources are parsed
#     using the python parser and a corresponding structure of objects is
#     constructed. This objects can be changed afecting both sources and
#     texts. This objets produce python code.

#     In a retrospective, the meta python aproach was usefull in a time
#     when a few python elements were supported. The meta python was
#     written from scrath. The python parser was not used. With the
#     introduction of the python parser trhougth the pre processor, the
#     meta python was never used (edited) again.

#     This refactoring avoids all the complexity of having an
#     intermediate (functional) language in the process, the meta python
#     language. In the future, the meta python language can be supported
#     by adding conviniente __repr__ methods to all nodes.
#     """

    # def __init__(self):

    #     self.source_list = []
    #     self.text_list   = []
    #     self.root        = Block()

    # def append_source(source_string):
    #     """Returns the root object created. Very usefull to generate code from
    #     just an item of the sources list.
    #     """

    #     self.source_list.append(source_string)

    #     ast = parse(source_string)
        
    #     level = 0
    #     root_node = process_ast(ast, level)

    #     return root_node

    # def append_text(text_string):
    #     """Returns the root object created. Very usefull to get just an item
    #     of the texts list.
    #     """

    #     self.text_list.append(source_string)

    # def set_content(id_string, content_string, id_index = None):

    #     pass

