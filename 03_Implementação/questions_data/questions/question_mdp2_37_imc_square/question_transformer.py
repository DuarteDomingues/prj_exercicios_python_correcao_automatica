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
		self.__output_true = None
		self.__output_false = None
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

		seed = random.randint(2000, 4000)
		range_len = random.randint(800, 1900)

		index = random.randint(1,range_len-2)

		random.seed(seed)

		lista_imc = []
		for i in range (range_len):
			lista_imc.append(imc(round(random.uniform(1,2),2),round(random.uniform(40,80),2)))
		
		output_true = lista_imc[index]
		self.__output_true = output_true

		output_false = 0
		random_numb = random.randint(0,1)
		if (random_numb ==0):
			output_false =lista_imc[index-1]
		else:
			output_false =lista_imc[index+1]

		self.__output_false = output_false

		six_value = random.randint(2,10)
		five_value = random.randint(2,10)

		list_strings = ["400","1000","420","6","5"]


		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0],str(seed))
		change_all_occurrences(list_strings[1], str(range_len))
		change_all_occurrences(list_strings[2], str(index))
		change_all_occurrences(list_strings[3],str(six_value) )
		change_all_occurrences(list_strings[4], str(five_value))

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

		list_strings = [r"\verb+outputTrue+",  r"\verb+outputFalse+"]

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], str(self.__output_true))
		change_all_occurrences(list_strings[1], str(self.__output_false))

		clear()

		return latex_parts
	



def imc(altura, massa):
    return (round(massa/(altura**2),2))

	