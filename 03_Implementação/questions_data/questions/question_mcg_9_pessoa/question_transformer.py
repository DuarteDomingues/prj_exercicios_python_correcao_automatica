import random
import sys
import string
from datetime import datetime
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
	
		self.__first_output_true = None
		self.__second_output_true = None
		self.__first_output_false = None
		self.__second_output_false = None
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

		# creates the lower and highest value to make differente versions
		height_lower_value = round(random.uniform(1., 1.5),2)
		height_higher_value = round(random.uniform(1.6, 2.2),2)

		weight_lower_value = random.randint(20,60)
		weight_higher_value = random.randint(70,140)

		names = ["Eduardo", "Margarida", "Marta", "Massibas", "Leonor", "Diogo", "Madorna", "Duarte", "Pedro", "Miguel", "Beatriz", "Rita", "Fonseca"]
		#shuffle the names to make differente versions
		names_shuffled = random.sample(names, len(names))
		random.seed(seed)
		

		name_choosed = random.choice(names_shuffled)
		height = round(random.uniform(height_lower_value, height_higher_value), 2)
		weight = random.randint(weight_lower_value, weight_higher_value)


		# make a false value for all the values 
		name_choosed_false = None
		height_false = None
		weight_false = None
		while name_choosed_false == None:
			other_name = random.choice(names_shuffled)
			other_height = round(random.uniform(height_lower_value, height_higher_value), 2)
			other_weight = random.randint(weight_lower_value, weight_higher_value)
			if name_choosed != other_name and height != other_height and weight != other_weight:
				name_choosed_false = other_name
				height_false = other_height
				weight_false = other_weight



		self.__first_output_true = "Nome: "+str(name_choosed)+", com altura: "+str(height)+" e peso: "+str(weight)
		self.__second_output_true = str([name_choosed, height, weight])

		self.__first_output_false = "Nome: "+str(name_choosed_false)+", com altura: "+str(height_false)+" e peso: "+str(weight_false)
		self.__second_output_false = str([name_choosed_false, height_false, weight_false])

		random.seed(datetime.now())
		

		list_strings = [str(100), str(1.5),str(2.2), str(30), str(120)]

		for name in names:
			list_strings.append(name)

		self.add_changable_strings(list_strings)

		change_token_all_occurrences(list_strings[0], str(seed))
		change_token_all_occurrences(list_strings[1], str(height_lower_value))
		change_token_all_occurrences(list_strings[2], str(height_higher_value))
		change_token_all_occurrences(list_strings[3], str(weight_lower_value))
		change_token_all_occurrences(list_strings[4], str(weight_higher_value))

		for index in range(len(names)):
			change_all_occurrences(names[index], names_shuffled[index])

		clear()

		return list_python_programs,seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)

		list_strings = [r'\verb+ou1t+', r'\verb+ou1f+', r'\verb+nao gera+', "Bolinhas"]

		random_animal = random.choice(["Bolinhas", "Luigi", "Arya", "Parker", "Frodo", "Gohan", "Lua", "Ziggy", "Pipoca", "Bolacha"])

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], self.__first_output_true+r'\newline'+"\n"+self.__second_output_true)
		change_all_occurrences(list_strings[1], self.__first_output_false+r'\newline'+"\n"+self.__second_output_false)
		change_all_occurrences(list_strings[2],r'\verb+não gera+')
		change_all_occurrences(list_strings[3], random_animal)

		clear()

		return latex_parts

	