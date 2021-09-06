import random
import sys
import string
from datetime import datetime
from re import search
import os
sys.path.append('../qom_questions_transformer')

print(os.getcwd())

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

		self.__seed         = None
		self.__string       = None
		self.__x            = None
		self.__y            = None
		self.__str_1_true   = None
		self.__num_1_true   = None
		self.__str_1_false  = None
		self.__num_1_false  = None
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

		loop = random.choice(range(1000, 5000))
		
		x = random.sample(string.ascii_lowercase,2)

		self.__x = x[0]
		self.__y = x[1]

		random_indexes = random.sample(range(1, 50), 2)


		random_ranges = random.choice(range(0, 21))
		random_ranges2 = random.choice(range(22, 51))

		st_characters = string.ascii_lowercase+string.ascii_uppercase
		generate_str =  ''.join([st_characters[self.pseudo_random_integer(random_ranges, random_ranges2)] for i in range(loop)])
		self.__string = generate_str[0:6]

		list_random_numbers = [self.pseudo_random_integer(10000, 99999) for i in range(loop)]
		self.__int = list_random_numbers[0:6]

		# recreate the object to add the question
		random_strgs   = []
		random_numbers = []

		for i in range(loop):
			random_strgs.append(generate_str[self.pseudo_random_integer(0, 5)])

		for i in range(loop):
			random_numbers.append(list_random_numbers[self.pseudo_random_integer(0, 5)])

		
		str_1_true = random_strgs[random_indexes[0]]
		self.__str_1_true = str_1_true
		num_1_true = random_numbers[random_indexes[1]]
		self.__num_1_true = num_1_true

		
		# to add to the new string if it's equal the true and false one
		char_str = ""
		while(char_str == ""):
			str_choosed = random.choice(string.ascii_lowercase)
			if not search(str_choosed, str_1_true):
				char_str = str_choosed

		str_1_false = random_strgs[random_indexes[0]-1] if random_strgs[random_indexes[0]-1] != str_1_true else random_strgs[random_indexes[0]-1][1:]+char_str
		self.__str_1_false = str_1_false
		num_1_false = random_numbers[random_indexes[1]-1] if random_numbers[random_indexes[1]-1] != num_1_true else random_numbers[random_indexes[1]-1]+1
		self.__num_1_false = num_1_false


		list_strings = ["100", "x", "y", "1000", "35", "25", "14", "51"]#"10000", "99999"

		self.add_changable_strings(list_strings)

		change_token_all_occurrences(list_strings[0], str(seed))
		change_all_occurrences(list_strings[1], x[0])
		change_all_occurrences(list_strings[2], x[1])
		change_token_all_occurrences(list_strings[3], str(loop))
		change_token_all_occurrences(list_strings[4], str(random_indexes[0]))
		change_token_all_occurrences(list_strings[5], str(random_indexes[1]))
		change_token_all_occurrences(list_strings[6], str(random_ranges))
		change_token_all_occurrences(list_strings[7], str(random_ranges2))
		clear()

		return list_python_programs, seed

	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)


		list_strings = [r'\verb+out1t+', r'\verb+out2t+',r'\verb+out1f+', r'\verb+out2f+', r'\verb+xpto+',  r'\verb+123+', r'\verb+x+', r'\verb+y+']

		self.add_changable_strings(list_strings)


		change_all_occurrences(list_strings[0], str(self.__str_1_true))
		change_all_occurrences(list_strings[1], str(self.__num_1_true))

		change_all_occurrences(list_strings[2], str(self.__str_1_false))
		change_all_occurrences(list_strings[3], str(self.__num_1_false))

		change_all_occurrences(r'\verb+xpto+', r'\verb+' + self.__string + '+')
		change_all_occurrences(r'\verb+123+', r'\verb+'+str(self.__int)+'+')

		change_all_occurrences(r'\verb+xpto+', r'\verb+' + self.__string + '+')
		change_all_occurrences(r'\verb+123+', r'\verb+'+str(self.__int)+'+')

		change_all_occurrences(r'\verb+x+', r'\verb+' + self.__x + '+')
		change_all_occurrences(r'\verb+y+', r'\verb+' + self.__y + '+')
		
		clear()

		return latex_parts

	def pseudo_random_integer(self, min_int, max_int):
		self.__seed = (16807*self.__seed) % 2147483647
		return int(min_int + (max_int - min_int) * self.__seed / 2147483646)