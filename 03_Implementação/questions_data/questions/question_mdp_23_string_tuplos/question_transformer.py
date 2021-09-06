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
	
		self.__string = None
		self.__numbers = None
		self.__output_true = [None] * 4
		self.__string_list = None
		self.__index = None
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


		first_output = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
		self.__string = first_output


		numbers_list = random.sample(range(1,1000), 6)
		self.__numbers = numbers_list

		list_strings = ["abcdef", "10", "20", "30", "4", "5", "6" ,"100","1000", "65"]

		seed = random.randint(2000,5000)
		list_range = random.randint(1000,2000)

		idx = random.randint(1, list_range-1)
		self.__index = idx

		random.seed(seed)

		strings_ex_list = []

		for i in range(list_range):
			strings_ex_list.append(''.join([random.choice(string.ascii_lowercase) for i in range(7)]))	

		self.__string_list = strings_ex_list
		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], first_output)

		self.__output_true[0] = first_output[-1]
		self.__output_true[1] = numbers_list[5]
		self.__output_true[2] = numbers_list[1]
		self.__output_true[3] = numbers_list[2]


		for i in range(1, 7):
			change_token_all_occurrences(list_strings[i], str(numbers_list[i-1]))

		change_all_occurrences(list_strings[7], str(seed))
		change_all_occurrences(list_strings[8], str(list_range))
		change_token_all_occurrences(list_strings[9], str(self.__index))

		clear()

		# if is to repeat a created exercise
		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)


		ex_2_true = self.__string_list[self.__index]
		ex_2_false= self.__string_list[self.__index-1]


		true_output = str(self.__output_true[0])+r"\newline "+str(self.__output_true[1])+r"\newline "+str(self.__output_true[2])+r"\newline "+str(self.__output_true[3])


		false_output = str(self.__numbers[4])+r"\newline "+str(self.__numbers[1])+r"\newline "+str(self.__numbers[0])+r"\newline "+str(self.__numbers[1])

		list_strings = [r'\verb+output1+', r"\verb+output2+" , r'\verb+index+', r'\verb+valorFalse+',r'\verb+valorTrue+']


		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], true_output)
		change_all_occurrences(list_strings[1], false_output)
		change_all_occurrences(list_strings[2], str(self.__index))
		change_all_occurrences(list_strings[3], str(ex_2_false))
		change_all_occurrences(list_strings[4], str(ex_2_true))

		clear()

		return latex_parts

	