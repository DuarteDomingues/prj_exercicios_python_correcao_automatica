import random
import sys
import string
sys.path.append('../qom_questions_transformer')

from python_transformer.pt_python_transformer_interface import change_token_all_occurrences
from python_transformer.pt_python_transformer_interface import change_all_occurrences
from text_transformer.tt_text_transformer_interface import clear
from text_transformer.tt_text_transformer_interface import load_text

from file_generator.helper import Helper
from generate_random_version.generate_random_version import GenerateRandomVersion
		


class QuestionTransformer(GenerateRandomVersion):

	# python_files_list -> name of the files (python) that wants to be changed
	# general_files_to_change_list -> name of the files (latex) that wants to be generated
	# num_versions -> number of verstions that wants to be created
	# output_index -> index of the output (1-question, 2-answer)
	def __init__(self, python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, repeat_seed=None):

		super().__init__(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, repeat_seed)
		self.__repeated_seed = repeat_seed



	# makes the changes on the python files and adds to the lists created on the constructor
	# adds to the lists to be also known on the latex files the new numbers
	def create_python_program(self, python_files_list, version):

		list_python_programs = self.get_programs_python(python_files_list)

		seed = random.choice(range(10000, 99999))
		self.__seed = seed

		# if is to repeat a created exercise
		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed
		
		random.seed(self.__seed)


		str_length  = random.randint(8,12)
		program_str = ''.join(random.choice(string.ascii_lowercase) for i in range(str_length))

		list_strings = ['abcdefghijk','10', '11','12']

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], program_str)
		change_all_occurrences(list_strings[1],str(str_length-1))
		change_all_occurrences(list_strings[2],str(str_length))
		change_all_occurrences(list_strings[3],str(str_length+1))

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		list_strings = [r'\verb+error+']

		self.add_changable_strings(list_strings)

		list_erros = ['ValueError', 'SyntaxError','TabError','SystemError','NameError']
		chosen_error = random.choice(list_erros)
		
		change_all_occurrences(list_strings[0],r"\verb+"+ chosen_error+"+")


		clear()

		return latex_parts

	