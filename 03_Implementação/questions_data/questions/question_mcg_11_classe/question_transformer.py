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

		strgs = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby", "One Hundred Years of Solitude", "In Cold Blood",
				 "Wide Sargasso Sea", "Brave New World", "I Capture The Castle", "Jane Eyre", "Crime and Punishment", "The Secret History",
				 "The Call of the Wild", "The Chrysalids", "Persuasion", "Moby-Dick", "To the Lighthouse", "A Byte of Pyhton", "Learning Python"]

		

		[str_book1, str_book2] = random.sample(strgs,2)

		#st = random.choice(strgs)

		[x_var, y_var] = random.sample(string.ascii_lowercase, 2)


		list_strings = ["A Byte of Pyhton", "Learning Python", "x", "y"]

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], str_book1)
		change_all_occurrences(list_strings[1], str_book2)
		change_token_all_occurrences(list_strings[2], x_var)
		change_token_all_occurrences(list_strings[3], y_var)

		clear()

		return list_python_programs,seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		list_erros = ['AttributeError', 'IndentationError','TabError', 'ZeroDivisionError', 'NotImplementedError', 'FloatingPointError']

		chosen_error = random.choice(list_erros)

		list_strings = [r'\verb+TabError+']

		self.add_changable_strings(list_strings)

		change_all_occurrences(r'\verb+TabError+', r'\verb+' +chosen_error + '+')

		clear()

		return latex_parts

	