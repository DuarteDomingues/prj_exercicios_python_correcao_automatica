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

		super().__init__(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path,repeat_seed)
		
		self.__chars_selected = None
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

		x = random.sample(string.ascii_lowercase, 4)
		self.__chars_selected = x

		list_strings = ["a", "b", "c", "d"]

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], x[0])
		change_all_occurrences(list_strings[1], x[1])
		change_all_occurrences(list_strings[2], x[2])
		change_all_occurrences(list_strings[3], x[3])

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		false_str = self.__chars_selected[3]+r'\newline'+"\n" 
		for i in range(len(self.__chars_selected)-1):
			false_str+= self.__chars_selected[i]+r'\newline'+"\n"



		list_strings = [r'\verb+out1t+', r'\verb+out1f+']

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], false_str)
		change_all_occurrences(list_strings[1], self.__chars_selected[3])

		clear()

		return latex_parts

	