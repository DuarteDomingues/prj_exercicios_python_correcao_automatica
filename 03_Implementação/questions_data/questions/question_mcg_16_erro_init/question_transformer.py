import random
import sys
import string
import numpy as np
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

		[a_var, b_var,c_var,y_var] = random.sample(string.ascii_lowercase, 4)

		var_1 = random

		list_strings = ["a","b","c","Y","y","1","2","3"]

		list_numbers_to_change = random.sample(range(1, 100), 3)

		self.add_changable_strings(list_strings)

		change_token_all_occurrences("a", a_var)
		change_token_all_occurrences("b", b_var)
		change_token_all_occurrences("c", c_var)
		change_token_all_occurrences("y", y_var)
		change_token_all_occurrences("Y", y_var.upper())
		change_all_occurrences("1", str(list_numbers_to_change[0]))
		change_all_occurrences("2", str(list_numbers_to_change[1]))
		change_all_occurrences("3", str(list_numbers_to_change[2]))
		

		clear()
		
		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)
		

		list_strings = [r'\verb+14+', r'\verb+da+']

		list_linhas = ["11","14"]

		str_erro_final = random.choice(list_linhas)

		self.add_changable_strings(list_strings)

		change_all_occurrences(r'\verb+14+', r'\verb+' +str_erro_final + '+')
		change_all_occurrences(r'\verb+da+', r'\verb+dá+')

		clear()

		return latex_parts