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
	
		self.__first_output = None
		self.__index_string = None
		self.__numbers_indexes = None
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

		first_output = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
		self.__first_output = first_output

		numbers_list = random.sample(range(1,1000), 9)
		self.__numbers_list = numbers_list

		numbers_indexes = random.sample(range(1,10), 1)
		self.__numbers_indexes = numbers_indexes


		list_strings = ['123456789', "10", "1", "2", "3", "4", "5", "6", "7", "80", "90"]

		self.add_changable_strings(list_strings)

		change_all_occurrences('123456789', first_output)

		
		change_token_all_occurrences("1", str(numbers_indexes[0]))

		change_token_all_occurrences("10", str(numbers_list[0]))
		change_token_all_occurrences("2", str(numbers_list[1]))
		change_token_all_occurrences("3", str(numbers_list[2]))
		change_token_all_occurrences("4", str(numbers_list[3]))
		change_token_all_occurrences("5", str(numbers_list[4]))
		change_token_all_occurrences("6", str(numbers_list[5]))
		change_token_all_occurrences("7", str(numbers_list[6]))
		change_token_all_occurrences("80", str(numbers_list[7]))
		change_token_all_occurrences("90", str(numbers_list[8]))

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		list_strings = [r'\verb+output_true+', r"\verb+output_false+", "lel"]


		self.add_changable_strings(list_strings)

		index = self.__numbers_indexes[0]-1 if self.__numbers_indexes[0] != 0 else self.__numbers_indexes[0]+1


		change_all_occurrences(list_strings[0], str(self.__first_output[self.__numbers_indexes[0]]))
		change_all_occurrences(list_strings[1], str(self.__first_output[index]))
		change_all_occurrences(list_strings[2], "dá")


		clear()

		return latex_parts

	