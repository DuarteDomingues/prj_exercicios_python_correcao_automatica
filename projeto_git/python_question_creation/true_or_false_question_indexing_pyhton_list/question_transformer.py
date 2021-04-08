import random
import sys
sys.path.append('../qom_questions_transformer')

from python_transformer.pt_python_transformer_interface import change_token_all_occurrences
from python_transformer.pt_python_transformer_interface import change_all_occurrences
from text_transformer.tt_text_transformer_interface import clear
from text_transformer.tt_text_transformer_interface import load_text

from make_pdfs.helper import Helper
from questions_transformer import QuestionsTransformer
		


class QuestionTransformer(QuestionsTransformer):

	# python_files_list -> name of the files (python) that wants to be changed
	# general_files_to_change_list -> name of the files (latex) that wants to be generated
	# num_versions -> number of verstions that wants to be created
	# output_index -> index of the output (1-question, 2-answer)
	def __init__(self, python_files_list, general_files_to_change_list, num_versions, output_index):

		super().__init__(python_files_list, general_files_to_change_list, num_versions, output_index)

		self.__list_first   = []
		self.__list_second  = []
		self.__list_third   = []
		self.__list_forth   = []


	# makes the changes on the python files and adds to the lists created on the constructor
	# adds to the lists to be also known on the latex files the new numbers
	def create_python_program(self, python_files_list, version):

		list_python_programs = self.get_programs_python(python_files_list)

		first = random.randint(0,99)
		self.__list_first.append(first)

		second = random.randint(0,450)
		self.__list_second.append(second)

		third = [random.randint(1, 25) for i in range(3)]
		self.__list_third.append(third)

		forth = random.randint(0, 40)
		self.__list_forth.append(forth)

		list_strings = ["2", "1", "1 2 3", "3"]

		self.add_changable_strings(list_strings)


		change_token_all_occurrences("2", str(first))
		change_token_all_occurrences("1", str(second))
		change_all_occurrences("1 2 3", f'{third[0]} {third[1]} {third[2]}')
		change_token_all_occurrences("3", str(forth))
		clear()

		return list_python_programs

	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output_execution=None):

		latex_parts = []

		# for every file change the content
		for latex in general_latex_files:
			# get the content from file
			latex_content = Helper().get_file_content(latex)
			# adds to library the content 
			text_part = load_text(latex_content)
			latex_parts.append(text_part)


		list_strings = [r'\verb+2+', r'\verb+1+']

		self.add_changable_strings(list_strings)

	
		change_all_occurrences(r'\verb+2+', r'\verb+' + str(self.__list_first[version]) + '+')
		change_all_occurrences(r'\verb+1+', r'\verb+' + str(self.__list_second[version]) + '+')
		clear()

		return latex_parts


	