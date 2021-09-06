import random
import sys
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
	def __init__(self, python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path,repeat_seed=None):

		super().__init__(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, repeat_seed)

		self.__first   = None
		self.__second  = None
		self.__third   = None
		self.__forth   = None
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


		first = random.randint(0,99)
		self.__first = first

		second = random.randint(0,450)
		self.__second = second

		third = [random.randint(1, 25) for i in range(3)]
		self.__third = third

		forth = random.randint(0, 40)
		self.__forth = forth

		list_strings = ["2", "1", "1 2 3", "3"]

		self.add_changable_strings(list_strings)


		change_token_all_occurrences("2", str(first))
		change_token_all_occurrences("1", str(second))
		change_all_occurrences("1 2 3", f'{third[0]} {third[1]} {third[2]}')
		change_token_all_occurrences("3", str(forth))
		clear()

		return list_python_programs,seed

	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)


		list_strings = [r'\verb+2+',  r'\verb+22+', r"\verb+1+", r"\verb+1 2 3+", r"\verb+3+", r"\verb+2 1 1 2 3 3+"]

		self.add_changable_strings(list_strings)

	
		change_all_occurrences(r'\verb+2+', r'\verb+' + str(self.__first) + '+')
		change_all_occurrences(r'\verb+22+', r'\verb+' + str(self.__second) + '+')



		change_all_occurrences(r"\verb+1+", r"\verb+" + str(self.__second) + "+")
		change_all_occurrences(r"\verb+1 2 3+", r"\verb+" + ' '.join([str(elem) for elem in self.__third]) + "+")
		change_all_occurrences(r"\verb+3+", r"\verb+" + str(self.__forth) + "+")



		change_all_occurrences(r"\verb+2 1 1 2 3 3+", r"\verb+" + str(self.__first)+" "+ str(self.__second)+" "+\
													' '.join([str(elem) for elem in self.__third])+" "+\
													str(self.__forth)+"+")
		clear()

		return latex_parts

	