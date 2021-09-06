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
		self.__str = ""
		self.__numbers_list = []
		# the index in the seven line changes in different versions
		self.__output_seven_line = ""
		self.__output_seven_line_false = ""
		self.__list = None
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
		
		loop = random.randint(1000, 1500)
		
		random.seed(self.__seed)

		lista_strings = []
		for i in range(loop):
			lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(6)]))

		self.__list = lista_strings

		index = random.randint(1, 400)
		self.__index = index


		self.__numbers_list = random.sample(range(1,20), 6)

		list_strings = ['4', "5", "600", "7", "8", "9", "100", "1000", "54"]

		self.add_changable_strings(list_strings)



		change_all_occurrences('4', str(self.__numbers_list[0]))
		change_all_occurrences('5', str(self.__numbers_list[1]))
		change_all_occurrences('600', str(self.__numbers_list[2]))
		change_all_occurrences('7', str(self.__numbers_list[3]))
		change_all_occurrences('8', str(self.__numbers_list[4]))
		change_all_occurrences('9', str(self.__numbers_list[5]))
		change_all_occurrences(list_strings[6], str(seed))
		change_all_occurrences(list_strings[7], str(loop))
		change_token_all_occurrences(list_strings[8], str(index-1))
		

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		true_result_2 = "("+str(self.__numbers_list[0])+", ["+str(self.__numbers_list[1])+", "+str(self.__numbers_list[2])+"], ("+\
						str(self.__numbers_list[3])+", "+str(self.__numbers_list[4])+", "+str(self.__numbers_list[5])+"), '"+self.__list[500]+"')"+"\n"+\
						"["+str(self.__numbers_list[1])+", "+str(self.__numbers_list[2])+"]""\n"+\
						str(self.__numbers_list[2])+"\n"+\
						str(self.__numbers_list[5])+"\n"+\
						self.__list[500][3]

		false_result_2 = "("+str(self.__numbers_list[0])+", ["+str(self.__numbers_list[1])+", "+str(self.__numbers_list[2])+"], ("+\
						str(self.__numbers_list[3])+", "+str(self.__numbers_list[4])+", "+str(self.__numbers_list[5])+"), '"+self.__list[500]+"')"+"\n"+\
						str(self.__numbers_list[0])+"\n"+\
						str(self.__numbers_list[0])+"\n"+\
						str(self.__numbers_list[2])+"\n"+\
						str(self.__numbers_list[5])


		list_strings = [r'\verb+index+', r'\verb+value1t+', r'\verb+value1f+', r'\verb+out2t+', r'\verb+out2f+']


		self.add_changable_strings(list_strings)

		

		change_all_occurrences(list_strings[0], r'\verb+'+str(self.__index)+"+")
		change_all_occurrences(list_strings[1],str(self.__list[self.__index-1]))
		change_all_occurrences(list_strings[2],str(self.__list[self.__index]))

		change_all_occurrences(list_strings[3], true_result_2)
		change_all_occurrences(list_strings[4], false_result_2)

		clear()

		return latex_parts

	