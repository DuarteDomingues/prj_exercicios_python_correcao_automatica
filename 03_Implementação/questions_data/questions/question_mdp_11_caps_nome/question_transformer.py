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
		self.__line_false = 1
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

		switch_variables = random.randint(0,2)

		list_strings = ["True", "False", "None","TRUE","FALSE","NONE","'true'","'false'","'none'","'TRUE'","'FALSE'","'NONE'"]
		self.add_changable_strings(list_strings)

		if switch_variables == 1:
			change_all_occurrences("True","'true'")
			change_all_occurrences("False","'false'")
			change_all_occurrences("None","'none'")

			change_all_occurrences("'true'","True")
			change_all_occurrences("'false'","False")
			change_all_occurrences("'none'","None")
			self.__line_false = 2

			switch_to_lower = random.randint(0,1)

			if switch_to_lower ==0:

				change_all_occurrences("TRUE","true")
				change_all_occurrences("FALSE","false")
				change_all_occurrences("NONE","none")
		
		if switch_variables == 2:
			change_all_occurrences("True","'TRUE'")
			change_all_occurrences("False","'FALSE'")
			change_all_occurrences("None","'NONE'")

			change_all_occurrences("'TRUE'","True")
			change_all_occurrences("'FALSE'","False")
			change_all_occurrences("'NONE'","None")
			self.__line_false = 3
			switch_to_lower = random.randint(0,1)

			if switch_to_lower ==0:

				change_all_occurrences("TRUE","true")
				change_all_occurrences("FALSE","false")
				change_all_occurrences("NONE","none")


			

		clear()

		return list_python_programs,seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		list_strings = [r'\verb+4+']
		self.add_changable_strings(list_strings)

		switch_variables = random.randint(0,1)


		if switch_variables==0:

			self.__line_false = 4

		change_all_occurrences(r'\verb+4+', r'\verb+' +str(self.__line_false)+ '+')

		clear()

		return latex_parts

	