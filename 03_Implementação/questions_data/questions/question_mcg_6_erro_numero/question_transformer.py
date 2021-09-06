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
		self.__output       = None
		self.__output_false = None
		self.__repeated_seed = repeat_seed

	# makes the changes on the python files and adds to the lists created on the constructor
	# adds to the lists to be also known on the latex files the new numbers
	def create_python_program(self, python_files_list, version):

		list_python_programs = self.get_programs_python(python_files_list)

		
		seed = random.choice(range(10000, 99999))
		seed_generated = seed
		self.__seed = seed

		# if is to repeat a created exercise
		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed
		
		random.seed(self.__seed)

		x_var = random.choice(string.ascii_lowercase)

		numero_var = random.randint(50,150)

		numero_indice_lista = numero_var - random.randint(10,40)
		
		tamanho_listas = random.randint(4,8)

		numero_indices_lista = tamanho_listas - random.randint(1,3)


		list_strings = ["70","5","6","2","x","50"]
		
		self.add_changable_strings(list_strings)

		seed = random.randint(151,500)
		random.seed(seed)

		change_token_all_occurrences("x", x_var)
		change_all_occurrences("70", str(numero_var))
		change_all_occurrences("50", str(seed))
		change_all_occurrences("5", str(tamanho_listas))
		change_all_occurrences("6", (str(numero_indice_lista)))
		change_all_occurrences("2", (str(numero_indices_lista)))

		list_total= []
		for i in range (numero_var):
			lista_i = random.sample(range(1,40),tamanho_listas )
			list_ordered = sorted(lista_i,key=None, reverse=True)
			list_total.append(list_ordered)
		

		self.__output = list_total[numero_indice_lista][numero_indices_lista]
		self.__output_false = list_total[numero_indice_lista][numero_indices_lista-1]
			

		# if is to repeat a created exercise
		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed
			
		else:
			seed = seed_generated
         
		clear()

		return list_python_programs,seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)
		

		list_strings = [r'\verb+output+',r'\verb+outputFalso+' ]

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], r'\verb+' +str(self.__output) + '+')
		change_all_occurrences(list_strings[1], r'\verb+' +str(self.__output_false) + '+')


		clear()

		return latex_parts


	