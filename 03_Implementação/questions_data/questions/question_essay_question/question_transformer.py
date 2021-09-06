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
		self.__previous_seed = repeat_seed
		self.__seed = None
		self.__variables = None
		self.__index = None
		self.__result = None



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

		variables = random.sample(string.ascii_lowercase, 5)
		self.__variables = variables

		loop = random.randint(1000, 2000)

		number_rand1 = random.randint(100, 200)
		number_rand2 = random.randint(250, 450)

		random_index = random.randint(0, loop-1)
		self.__index = random_index

		list_result = [self.random_int(number_rand1, number_rand2) for i in range(loop)]
		

		result = list_result[random_index]
		self.__result = result

		print("res: ", result)

		list_strings = ["X", "x", "y", "z", "w", "n", "123456", "1000", "100", "200", "300"]

		self.add_changable_strings(list_strings)


		change_all_occurrences(list_strings[0], variables[0].upper())
		change_all_occurrences(list_strings[1], variables[0])
		change_all_occurrences(list_strings[2], variables[1])
		change_all_occurrences(list_strings[3], variables[2])
		change_all_occurrences(list_strings[4], variables[3])
		change_all_occurrences(list_strings[5], variables[4])

		change_token_all_occurrences(list_strings[6], str(seed))
		change_token_all_occurrences(list_strings[7], str(loop))
		change_token_all_occurrences(list_strings[8], str(number_rand1))
		change_token_all_occurrences(list_strings[9], str(number_rand2))
		change_token_all_occurrences(list_strings[10], str(random_index))

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		list_strings = [r'\verb+y+', r'\verb+index+',r'\verb+w+', r'\verb+valuet+', r'\verb+valuef+']

		self.add_changable_strings(list_strings)


		change_all_occurrences(list_strings[0], self.__variables[1])
		change_all_occurrences(list_strings[1], str(self.__index))
		change_all_occurrences(list_strings[2], self.__variables[3])
		change_all_occurrences(list_strings[3], str(self.__result))
		change_all_occurrences(list_strings[4], str(self.__result+random.choice([-1, 1])))

		clear()

		return latex_parts

	
	def random_int(self, min, max):
		self.__seed = (16807*self.__seed) % 2147483647
		return int(min + (max - min)*(self.__seed / 2147483646))

	