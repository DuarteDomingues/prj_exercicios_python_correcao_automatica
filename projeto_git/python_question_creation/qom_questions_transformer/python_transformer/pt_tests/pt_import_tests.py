
import sys

sys.path.append('/home/jbs/develop.old/articles/201509_python_exercises_generator')





# from py_transformer.pt_nodes.pt_base_node import PTBaseNode

# this import removes an import error. I don't know why (jbs
# 2018/12/12).
import py_transformer.ast_processor

#from text_transformer.tt_text_transformer_interface import load_text

#from py_transformer.pt_nodes.pt_identifier import PTIdentifier

from py_transformer.pt_python_transformer_interface import change_identifier_all_occurrences
