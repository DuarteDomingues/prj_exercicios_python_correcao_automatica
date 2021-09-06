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
		self.__output__f2c_true = None
		self.__output__f2c_false = None
		self.__output__c2f_true = None
		self.__output__c2f_false = None
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

		ranges = random.sample(range(1000, 2000), 4)
		index_f2c = random.randint(1,ranges[0]-2)
		index_c2f = random.randint(1,ranges[1]-2)

		random.seed(self.__seed)


		lista_f2c = []
		for i in range (ranges[0]):
			lista_f2c.append(f2c(round(random.uniform(30,100),2)))
		
		lista_c2f = []
		for j in range (ranges[1]):
			lista_c2f.append(c2f(round(random.uniform(1,38),2)))
		self.__output__c2f_true = lista_c2f[index_c2f]
		self.__output__c2f_false = lista_c2f[index_c2f-1]

        	
		
		output_true = lista_f2c[index_f2c]
		self.__output__f2c_true = output_true

		output_false = 0
		random_numb = random.randint(0,1)
		if (random_numb ==0):
			output_false =lista_f2c[index_f2c-1]
		elif (random_numb ==1):
			output_false =lista_f2c[index_f2c+1]

		lista_f2c = None


		self.__output__f2c_false = output_false

		

		list_strings = ["3353","1040","1029","677","520"]


		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], str(seed))
		change_all_occurrences(list_strings[1], str(ranges[0]))
		change_all_occurrences(list_strings[2], str(ranges[1]))
		change_all_occurrences(list_strings[3], str(index_c2f) )
		change_all_occurrences(list_strings[4], str(index_f2c))

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		list_strings = [r"\verb+outputTrue_1+",  r"\verb+outputFalse_1+", r"\verb+outputTrue_2+", r"\verb+outputFalse_2+"]

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], str(self.__output__c2f_true))
		change_all_occurrences(list_strings[1], str(self.__output__c2f_false))
		change_all_occurrences(list_strings[2], str(self.__output__f2c_true))
		change_all_occurrences(list_strings[3], str(self.__output__f2c_false))


		clear()

		return latex_parts
	



def c2f(celsius):

    return round(1.8*celsius +32,2)

def f2c(fahreinheit):

    return round((fahreinheit-32)/1.8,2)

	