
from python_transformer.pt_python_transformer_interface import load_source_code





def get_file_content(filename):

    with open(filename, "r") as file:
        content = file.read()

    return content





def load_source_code_from_file(filename):

    return load_source_code(get_file_content(filename))




