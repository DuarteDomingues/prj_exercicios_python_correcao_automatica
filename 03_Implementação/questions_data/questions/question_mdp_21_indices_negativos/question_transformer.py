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
	def __init__(self, python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path,  repeat_seed=None):

		super().__init__(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, repeat_seed)
	
		self.__string = None
		self.__numbers = None
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


		first_output = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
		self.__string = first_output

		numbers_list = random.sample(range(1,1000), 11)
		self.__numbers = numbers_list


		list_strings = ["abcdefghijk","10", "20", "3", "4", "5", "6", "7", "8", "9", "100", "110"]

		self.add_changable_strings(list_strings)


		change_all_occurrences(list_strings[0], first_output)
		for i in range(1, 12):
			change_token_all_occurrences(list_strings[i], str(numbers_list[i-1]))


		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		true_output_list = output[0].split("\n")

		
		true_output = self.__string[-1]+r"\newline "+self.__string[-2]+r"\newline "+str(self.__numbers[-11])


		false_output = self.__string[-2]+r"\newline "+self.__string[-3]+r"\newline "+"IndexError: list index out of range"

		list_strings = [r'\verb+output1+', r"\verb+output2+"]


		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], true_output)
		change_all_occurrences(list_strings[1], false_output)

		clear()

		return latex_parts

	