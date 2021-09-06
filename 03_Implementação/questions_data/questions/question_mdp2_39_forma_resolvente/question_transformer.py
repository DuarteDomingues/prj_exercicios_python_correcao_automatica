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

		super().__init__(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path,repeat_seed)
	
		self.__num1 = None
		self.__num2 = None
		self.__num3 = None
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

		num1 = random.randint(1, 9)
		num2 = random.randint(10, 99)
		num3 = random.randint(50, 150)

		self.__num1 = num1
		self.__num2 = num2
		self.__num3 = num3

		list_strings = ["20", "100", "200", "equacao", "raizes"]

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], str(self.__num1))
		change_all_occurrences(list_strings[1], str(self.__num2))
		change_all_occurrences(list_strings[2], str(self.__num3))
		change_all_occurrences(list_strings[3], "equação")
		change_all_occurrences(list_strings[4], "raízes")

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		result_true = self.formula_resolvente(-self.__num1, self.__num2, -self.__num3)

		list_strings = [r'\verb+value1+', r'\verb+value2+', r'\verb+value3+', r'\verb+value1t+', r'\verb+value2t+', r'\verb+value1f+', r'\verb+value2f+']

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], str(self.__num1))
		change_all_occurrences(list_strings[1], str(self.__num2))
		change_all_occurrences(list_strings[2], str(self.__num3))

		change_all_occurrences(list_strings[3], str(result_true[0]))
		change_all_occurrences(list_strings[4], str(result_true[1]))

		change_all_occurrences(list_strings[5], str(result_true[0]+random.choice([-0.1, 0.1])))
		change_all_occurrences(list_strings[6], str(result_true[1]+random.choice([-0.1, 0.1])))

		clear()

		return latex_parts

	def formula_resolvente(self, a, b, c):

		bx = ((b**2)-(4*a*c))**(1/2)
		bx1 = (-b+bx)/(2*a)
		bx2 = (-b-bx)/(2*a)
		return bx1, bx2

	