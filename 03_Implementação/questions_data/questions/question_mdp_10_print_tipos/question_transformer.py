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
		self.__list_numbers_to_change = []
		self.__output_line_1 = ""
		self.__output_line_2 = ""
		self.__output_line_3 = ""
		self.__repeated_seed = repeat_seed



	# makes the changes on the python files and adds to the lists created on the constructor
	# adds to the lists to be also known on the latex files the new numbers
	def create_python_program(self, python_files_list, version):

		list_python_programs = self.get_programs_python(python_files_list)

		list_strings = ["None","3.0","1","2","3","2.0","'3.0'"]

		seed = random.choice(range(10000, 99999))
		self.__seed = seed

		# if is to repeat a created exercise
		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed
		
		random.seed(self.__seed)

		self.__list_numbers_to_change = random.sample(range(5, 25), 3)

		num_1 = self.__list_numbers_to_change[0]
		num_2 = self.__list_numbers_to_change[1]
		num_3 = self.__list_numbers_to_change[2]


		switch_variables = random.randint(0,5)
		

		self.add_changable_strings(list_strings)
		
		if switch_variables == 0:
			
			change_all_occurrences("2.0",str(num_2)+".0")
			change_all_occurrences("'3.0'","'"+str(num_3)+".0'")

			self.__output_line_1 = 'NoneType'
			self.__output_line_2 = 'str'
			self.__output_line_3 = 'float'



		if switch_variables == 1:

			change_all_occurrences("2.0","'"+str(num_3)+".0'")
			change_all_occurrences("'3.0'",str(num_2)+".0")

			self.__output_line_1 =  'NoneType'
			self.__output_line_2 = 'float'
			self.__output_line_3 =  'str'
			
		
		elif switch_variables == 2:

			change_all_occurrences("None",str(num_2)+".0")
			change_all_occurrences("'3.0'","None")
			change_all_occurrences("2.0","'"+str(num_3)+".0'")

			self.__output_line_1 ='float'
			self.__output_line_2 = 'NoneType'
			self.__output_line_3 = 'str'
		
		elif switch_variables == 3:
		
			change_all_occurrences("None",str(num_2)+".0")
			change_all_occurrences("2.0","None")
			change_all_occurrences("'3.0'","'"+str(num_3)+".0'")

			self.__output_line_1 ='float'
			self.__output_line_2 = 	'str'
			self.__output_line_3 = 'NoneType'
		
		elif switch_variables == 4:
		
			change_all_occurrences("None","'"+str(num_3)+".0'")
			change_all_occurrences("2.0",str(num_2)+".0")
			change_all_occurrences("'3.0'","None")

			self.__output_line_1 ='str'
			self.__output_line_2 = 	'NoneType'
			self.__output_line_3 = 'float'
			
		
		elif switch_variables == 5:
		
			change_all_occurrences("None","'"+str(num_3)+".0'")
			change_all_occurrences("2.0","None")
			change_all_occurrences("'3.0'",str(num_2)+".0")

			self.__output_line_1 = 'str'
			self.__output_line_2 = 	'float'
			self.__output_line_3 = 'NoneType'
		
		

		change_all_occurrences("1", str(num_1))
		change_all_occurrences("2", str(num_2))
		change_all_occurrences("3", str(num_3))


		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)



		list_strings = ["'NoneType1'", "'str2'", "'float3'","'NoneType1 false'", "'str2 false'", "'float3 false'","'str false'", "'list false'" ]
		


		self.add_changable_strings(list_strings)

		switch_false_answers = random.randint(0,1)

		if switch_false_answers==0:
			
			change_all_occurrences( "'list false'", "'str'")
			change_all_occurrences( "'str false'", "'str'")
			change_all_occurrences("'NoneType1 false'", "'"+self.__output_line_1+"'")
			change_all_occurrences( "'str2 false'", "'"+self.__output_line_2+"'")
			change_all_occurrences( "'float3 false'", "'"+self.__output_line_3+"'")
		

		else:

			change_all_occurrences( "'list false'", "'list'")
			change_all_occurrences( "'str false'", "'bool'")

			if (self.__output_line_1 ==  'str'):

				change_all_occurrences("'NoneType1 false'", "'float'")
				change_all_occurrences( "'str2 false'", "'"+self.__output_line_2+"'")
				change_all_occurrences( "'float3 false'", "'"+self.__output_line_3+"'")

			elif (self.__output_line_2 ==  'str'):

				change_all_occurrences("'NoneType1 false'", "'"+self.__output_line_1+"'")
				change_all_occurrences( "'str2 false'",  "'float'")
				change_all_occurrences( "'float3 false'", "'"+self.__output_line_3+"'")
			
			elif (self.__output_line_3 ==  'str'):

				change_all_occurrences("'NoneType1 false'", "'"+self.__output_line_1+"'")
				change_all_occurrences( "'str2 false'", "'"+self.__output_line_2+"'")
				change_all_occurrences( "'float3 false'", "'float'")



		change_all_occurrences("'NoneType1'", "'"+self.__output_line_1+"'")
		change_all_occurrences( "'str2'", "'"+self.__output_line_2+"'")
		change_all_occurrences( "'float3'", "'"+self.__output_line_3+"'")


		clear()

		return latex_parts

	