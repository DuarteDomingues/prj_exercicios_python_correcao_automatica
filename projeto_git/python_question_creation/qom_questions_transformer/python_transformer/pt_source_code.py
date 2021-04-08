# history
#
# 2020/05/27 Added get_parts_list. (jbs)
#





# the sandbox function
from python_transformer.sandbox import sandbox





class PTSourceCode:

    def __init__(self, lines_parts = []):
        
        self.lines_parts     = lines_parts
        self.sandbox_globals = None





    #def to_string(self, indent_level = 0):
    def to_string(self):

        result = ''
        for parts_list in self.lines_parts:
            for part in parts_list:
                result = result + part.to_string()

        return result





    def execute(self, filename = None):

        exec_string = self.to_string()

        (sandbox_output, sandbox_error, sandbox_exception, sandbox_globals) \
            = sandbox(exec_string, filename)

        self.sandbox_globals = sandbox_globals

        return (sandbox_output, sandbox_error, sandbox_exception)


        


    def get_global(self, variable):

        return self.sandbox_globals[variable]





    def get_indent(self, indent_level):

        return " " * (4 * indent_level)





    def append(self, other_pt_source_code):

        for line in other_pt_source_code.lines_parts:
            self.lines_parts.append(line)

            



    def get_parts_list(self):

        parts_list = []
        for line_parts_list in self.lines_parts:
            for part in line_parts_list:
                parts_list.append(part)

        return parts_list
