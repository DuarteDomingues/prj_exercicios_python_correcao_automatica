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
	def __init__(self, python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path,repeat_seed=None):

		super().__init__(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path,repeat_seed)
		self.__str_python = ""
		self.__repeated_seed = repeat_seed



	# makes the changes on the python files and adds to the lists created on the constructor
	# adds to the lists to be also known on the latex files the new numbers
	def create_python_program(self, python_files_list, version):

		list_python_programs = self.get_programs_python(python_files_list)
		
		strgs = ["walrus","python", "monkey", "turtle", "parrot", "alpaca","rabbit", "pigeon", "dinner","circle","beauty", "animal","before","bridge","future","lisbon","chelas"]

		seed = random.choice(range(10000, 99999))
		self.__seed = seed

		# if is to repeat a created exercise
		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed
		
		random.seed(self.__seed)





		rd_strg = ''.join(random.choice(string.ascii_lowercase) for i in range(6))

		if random.randint(0,10) > 4:
			self.__str_python = random.choice(strgs)

		else:
			self.__str_python = rd_strg
		

		list_strings = ["P","Py","Pyt","Pyth","Pytho","Python"]

		self.add_changable_strings(list_strings)

		change_all_occurrences("P", self.__str_python[0])
		change_all_occurrences("Py", self.__str_python[0:2])
		change_all_occurrences("Pyt", self.__str_python[0:3])
		change_all_occurrences("Pyth", self.__str_python[0:4])
		change_all_occurrences("Pytho", self.__str_python[0:5])
		change_all_occurrences("Python", self.__str_python[0:6])




		clear()

		return list_python_programs,seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		list_strings = [r'\verb+Python+', r'\verb+1 inicial+',r'\verb+1 final+',r'\verb+indice 0+',r'\verb+indice i+']

		self.add_changable_strings(list_strings)

		wrong_program_type =  (random.randint(0,3))

		if (wrong_program_type==0):

			change_all_occurrences(r'\verb+1 inicial+',str(0) )
			change_all_occurrences(r'\verb+indice 0+',str(0) )
			change_all_occurrences(r'\verb+indice i+', "i")
		elif (wrong_program_type==1):
			
			change_all_occurrences(r'\verb+1 inicial+', str(1)  )
			change_all_occurrences(r'\verb+indice 0+', str(1) )
			change_all_occurrences(r'\verb+indice i+', "i" )
		
		elif (wrong_program_type==2):
			
			change_all_occurrences(r'\verb+1 inicial+', str(0) )
			change_all_occurrences(r'\verb+indice 0+', str(0) )
			change_all_occurrences(r'\verb+indice i+', "i+1" )
		
		elif (wrong_program_type==3):
			
			change_all_occurrences(r'\verb+1 inicial+',  str(0) )
			change_all_occurrences(r'\verb+indice 0+',  str(1))
			change_all_occurrences(r'\verb+indice i+', "i" )
		


		change_all_occurrences(r'\verb+Python+', self.__str_python )
		change_all_occurrences(r'\verb+1 final+', str(1) )


		clear()

		return latex_parts

	