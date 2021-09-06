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

		letter = random.choices(string.ascii_lowercase)

		numbers_list = random.sample(range(10,1000), 3)

		list_strings = ["1", "2", "3", "x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8", "x9", "x10"]

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], str(numbers_list[0]))
		change_all_occurrences(list_strings[1], str(numbers_list[1]))
		change_all_occurrences(list_strings[2], str(numbers_list[2]))
		for i in range(1,11):
			change_token_all_occurrences(list_strings[2+i], letter[0]+str(i))

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)


		true_output = "<class 'NoneType'>"+r"\newline"+"\n"+\
						"<class 'str'>"+r"\newline"+"\n"+\
						"<class 'list'>"+r"\newline"+"\n"+\
						"<class 'bool'>"+r"\newline"+"\n"+\
						"<class 'bool'>"+r"\newline"+"\n"+\
						"<class 'list'>"+r"\newline"+"\n"+\
						"<class 'float'>"+r"\newline"+"\n"+\
						"<class 'int'>"+r"\newline"+"\n"+\
						"<class 'tuple'>"+r"\newline"+"\n"+\
						"<class 'str'>"


		false_output = true_output
		false_output = true_output.replace("NoneType", "None")
		false_output = false_output.replace("str", "string")

		false_output2 = true_output.replace("float", "int")

		false_output = false_output if random.randint(0, 9) > 4 else false_output2

		list_strings = [r'\verb+output1+', r"\verb+output2+"]


		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], true_output)
		change_all_occurrences(list_strings[1], false_output)

		clear()

		return latex_parts

	