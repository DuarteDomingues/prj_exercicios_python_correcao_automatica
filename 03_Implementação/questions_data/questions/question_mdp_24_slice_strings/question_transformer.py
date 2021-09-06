import random
import sys
import string
from datetime import datetime
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
		self.__output_true = [""] *7
		self.__output_false = [""] *7
		self.__list = None
		self.__index = None
		self.__repeated_seed = repeat_seed


	# makes the changes on the python files and adds to the lists created on the constructor
	# adds to the lists to be also known on the latex files the new numbers
	def create_python_program(self, python_files_list, version):

		list_python_programs = self.get_programs_python(python_files_list)

		seed = random.choice(range(10000, 99999))
		previous_seed = seed
		self.__seed = seed

		# if is to repeat a created exercise
		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed
		
		random.seed(self.__seed)

		seed = random.randint(1000, 4000)
		loop = random.randint(1000, 2000)
		

		random.seed(seed)

		lista_strings = []

		for i in range(1000):
			lista_strings.append(''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(3)]))

		self.__list = lista_strings

		index = random.randint(100, 400)
		self.__index = index

		rand_num = random.randint(2,8)

		str_program = 'hello python world!'
		
		rand_num_11 = rand_num+5
		rand_num_12 = rand_num+6
		rand_num_7  = rand_num+1
		rand_num_13 = rand_num+7

		list_strings = ['6','11', '12','7','13', '100', '1000', '65']

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], str(rand_num))
		change_all_occurrences(list_strings[1], str(rand_num_11))
		change_all_occurrences(list_strings[2], str(rand_num_12))
		change_all_occurrences(list_strings[3], str(rand_num_7))
		change_all_occurrences(list_strings[4], str(rand_num_13))
		change_all_occurrences(list_strings[5], str(seed))
		change_all_occurrences(list_strings[6], str(loop))
		change_token_all_occurrences(list_strings[7], str(self.__index-1))

		output_0 = "hello python world!"
		output_1 = str_program[rand_num:rand_num_11]
		output_2 = str_program[rand_num:rand_num_12]
		output_3 = str_program[rand_num:-rand_num_7]
		output_4 = str_program[-rand_num_13:-rand_num_7]
		output_5 = str_program[:-rand_num_7]
		output_6 = str_program[rand_num:]

		self.__output_true[0] = output_0
		self.__output_true[1] = output_1
		self.__output_true[2] = output_2
		self.__output_true[3] = output_3
		self.__output_true[4] = output_4
		self.__output_true[5] = output_5
		self.__output_true[6] = output_6

			
		output_1_false = str_program[rand_num+1:rand_num_11+1]
		output_2_false = str_program[rand_num+1:rand_num_12+1]
		output_3_false = str_program[rand_num+1:-rand_num_7+1]
		output_4_false = str_program[-rand_num_13+1:-rand_num_7+1]
		output_5_false = str_program[:-rand_num_7]
		output_6_false = str_program[rand_num:]

		self.__output_false[1] = output_1_false
		self.__output_false[2] = output_2_false
		self.__output_false[3] = output_3_false
		self.__output_false[4] = output_4_false
		self.__output_false[5] = output_5_false
		self.__output_false[6] = output_6_false


		clear()

		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed
		else:
			seed = previous_seed

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		list_strings = [r'\verb+hello python world!+', r'\verb+pytho+',r'\verb+python_1+',\
						r'\verb+python_2+',r'\verb+python_3+', r'\verb+hello python+',r'\verb+python world!+',r'\verb+pytho_f+',\
						r'\verb+python_1_f+',r'\verb+python_2_f+',r'\verb+python_3_f+', r'\verb+hello python_f+', r'\verb+python world!_f+',\
						r'\verb+index+', r'\verb+out1t+', r'\verb+out1f+']
		self.add_changable_strings(list_strings)



		change_all_occurrences(list_strings[0], self.__output_true[0])
		change_all_occurrences(list_strings[1], self.__output_true[1])
		change_all_occurrences(list_strings[2], self.__output_true[2])
		change_all_occurrences(list_strings[3], self.__output_true[3])
		change_all_occurrences(list_strings[4], self.__output_true[4])
		change_all_occurrences(list_strings[5], self.__output_true[5])
		change_all_occurrences(list_strings[6], self.__output_true[6])

		change_all_occurrences(list_strings[7], self.__output_false[1])
		change_all_occurrences(list_strings[8], self.__output_false[2])
		change_all_occurrences(list_strings[9], self.__output_false[3])
		change_all_occurrences(list_strings[10], self.__output_false[4])
		change_all_occurrences(list_strings[11], self.__output_false[5])
		change_all_occurrences(list_strings[12], self.__output_false[6])

		change_all_occurrences(list_strings[13], str(self.__index))
		change_all_occurrences(list_strings[14], self.__list[self.__index-1])
		change_all_occurrences(list_strings[15], str(self.__list[self.__index]))

		clear()

		return latex_parts

	