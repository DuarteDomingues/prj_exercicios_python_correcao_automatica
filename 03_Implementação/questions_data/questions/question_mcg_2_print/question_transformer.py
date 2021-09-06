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

		self.__x_var = ""
		self.__y_var = ""
		self.__z_var = ""
		self.__p     = None
		self.__list_numbers_to_change = []
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


		[self.__x_var, self.__y_var, self.__z_var, self.__p] = random.sample(string.ascii_lowercase, 4)

		self.__list_numbers_to_change = random.sample(range(1, 50), 3)


		list_strings = ["x","y","z","X","1","2","3", "classe X", "atributo x", "metodo y", "tipo X", "INICIO", "criacao", "definicao", "inicializao", "lol", "execucao", "p"]

		self.add_changable_strings(list_strings)

		change_token_all_occurrences("x", self.__x_var)
		change_token_all_occurrences("X", self.__x_var.upper())
		change_token_all_occurrences("y", self.__y_var)
		change_token_all_occurrences("z", self.__z_var)
		change_all_occurrences("classe X", "classe "+ self.__x_var.upper())

		change_all_occurrences("1", str(self.__list_numbers_to_change[0]))
		change_all_occurrences("2", str(self.__list_numbers_to_change[1]))
		change_all_occurrences("3", str(self.__list_numbers_to_change[2]))

		change_all_occurrences("atributo x", "atributo "+self.__x_var)
		change_all_occurrences("metodo y", "metodo "+self.__y_var )
		change_all_occurrences("tipo X","tipo "+ self.__x_var)

		change_all_occurrences("INICIO","INÍCIO")
		change_all_occurrences("criacao","criação")
		change_all_occurrences("definicao","definição")
		change_all_occurrences("inicializao","inicialização")
		change_all_occurrences("lol","método")
		change_all_occurrences("execucao","execução")

		change_all_occurrences("p", self.__p)

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)
		

		list_strings = [r'\verb+x+',r'\verb+X+',r'\verb+1+', r'\verb+2+',r'\verb+y+', r'\verb+p+']

		self.add_changable_strings(list_strings)


		change_all_occurrences(r'\verb+x+', self.__x_var )
		change_all_occurrences(r'\verb+y+', self.__y_var )
		change_all_occurrences(r'\verb+X+', self.__x_var.upper())
		change_all_occurrences(r'\verb+p+', self.__p)
		change_all_occurrences(r'\verb+1+', str(self.__list_numbers_to_change[0]))
		change_all_occurrences(r'\verb+2+', str(self.__list_numbers_to_change[1]))

		clear()

		return latex_parts

	