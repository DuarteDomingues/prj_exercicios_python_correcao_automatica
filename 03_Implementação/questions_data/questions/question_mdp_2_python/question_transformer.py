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
	
		self.__str_python = ""
		self.__str_monty  = ""
		self.__str_1      = ""
		self.__str_2      = ""
		self.__str_3      = ""
		self.__str_4      = ""
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


		[self.__str_python,self.__str_monty] = random.sample(strgs,2)

		
		list_strings = ["py  th  on","Python","python","monty","PYTHON","p y t h o n"]

		self.add_changable_strings(list_strings)
		
		self.__str_1 = self.__str_python[0:2]+'  '+self.__str_python[2:4]+'  '+self.__str_python[4:6]
		self.__str_2 = self.__str_python.capitalize()
		self.__str_3 = self.__str_python.upper()
		self.__str_4 = ""

		for i in self.__str_python:
			if (i != len(self.__str_python)-1):
				self.__str_4 = self.__str_4+i+" "
			else:
				self.__str_4 = self.__str_4+i
    		

		change_all_occurrences("py  th  on", self.__str_1)
		change_all_occurrences("Python", self.__str_2)
		change_all_occurrences("python", self.__str_python)
		change_all_occurrences("monty", self.__str_monty)
		change_all_occurrences("PYTHON", self.__str_3)
		change_all_occurrences("p y t h o n", self.__str_4 )

		clear()

		return list_python_programs,seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

				
		list_strings = [r'\verb+python+',r'\verb+py  th  on+',r'\verb+monty+',r'\verb+Python+',r'\verb+PYTHON+', r'\verb+p y t h o n+']

		self.add_changable_strings(list_strings)

		change_all_occurrences(r'\verb+py  th  on+', r'\verb+' +self.__str_1 + '+')
		change_all_occurrences(r'\verb+Python+', r'\verb+' +self.__str_2 + '+')
		change_all_occurrences(r'\verb+python+', r'\verb+' +self.__str_python + '+')
		change_all_occurrences(r'\verb+monty+', r'\verb+' +self.__str_monty + '+')
		change_all_occurrences(r'\verb+PYTHON+', r'\verb+' +self.__str_3 + '+')
		change_all_occurrences(r'\verb+p y t h o n+', r'\verb+' +self.__str_4 + '+')

		clear()

		return latex_parts

	