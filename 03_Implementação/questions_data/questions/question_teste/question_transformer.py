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

		self.__seed           = None
		self.__variable       = None
		self.__variable_loop  = None
		self.__loop           = None
		self.__begin          = None
		self.__end            = None
		self.__indexes        = None
		self.__a              = []
		self.__repeated_seed = repeat_seed


	# makes the changes on the python files and adds to the lists created on the constructor
	# adds to the lists to be also known on the latex files the new numbers
	def create_python_program(self, python_files_list, version):

		list_python_programs = self.get_programs_python(python_files_list)

		seed = random.randint(100000, 999999)
		self.__seed = seed

		# if is to repeat a created exercise
		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed

		random.seed(self.__seed)

		variable  = random.sample(string.ascii_lowercase, 2)
		self.__variable = variable[0]
		self.__variable_loop = variable[1]

		variable = random.sample(string.ascii_lowercase, 2)
		self.__variable = variable

		loop = random.randint(10000, 99999)
		self.__loop = loop

		begin = random.randint(500, 1000)
		self.__begin = begin

		end = random.randint(1500, 9000)
		self.__end = end


		self.__a = []

		x = seed
		for i in range(loop):
			x = (16807*x) % 2147483647
			self.__a.append(int(begin + (end - begin) * x / 2147483646))


		differente = self.__end - self.__begin+1

		[index_1, index_2, index_3, index_4, index_5] = random.sample(range(0, differente), 5)
		self.__indexes = [index_1, index_2, index_3, index_4, index_5]


		list_strings = ["123456", "a", "n", "1000", "100","200", "11", "22", "33", "44", "55"]


		self.add_changable_strings(list_strings)


		change_all_occurrences("123456", str(seed))
		change_token_all_occurrences("a", variable[0])
		change_token_all_occurrences("n", variable[1])
		change_all_occurrences("1000", str(loop))
		change_all_occurrences("100", str(begin))
		change_all_occurrences("200", str(end))
		change_token_all_occurrences(list_strings[6], str(index_1))
		change_token_all_occurrences(list_strings[7], str(index_2))
		change_token_all_occurrences(list_strings[8], str(index_3))
		change_token_all_occurrences(list_strings[9], str(index_4))
		change_token_all_occurrences(list_strings[10], str(index_5))

		clear()

		return list_python_programs, seed

	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)


		list_strings = [r'\verb+a+', r'\verb+1+',  r'\verb+11+', r'\verb+111+', r'\verb+2+',  r'\verb+22+', r'\verb+222+',r'\verb+3+',  r'\verb+33+', r'\verb+333+',
						r'\verb+4+',  r'\verb+44+', r'\verb+444+',r'\verb+5+',  r'\verb+55+', r'\verb+555+']

		self.add_changable_strings(list_strings)


		differente = self.__end - self.__begin+1


		index_1 = self.__indexes[0]
		index_2 = self.__indexes[1]
		index_3 = self.__indexes[2]
		index_4 = self.__indexes[3]
		index_5 = self.__indexes[4]


		dif_1 = random.choice([-1, 1])
		dif_2 = random.choice([-1, 1])
		dif_3 = random.choice([-1, 1])
		dif_4 = random.choice([-1, 1])
		dif_5 = random.choice([-1, 1])

	
		change_all_occurrences(r'\verb+a+', r'\verb+' + str(self.__variable[0]) + '+')

		change_all_occurrences(r'\verb+1+', r'\verb+' + str(index_1) + '+')
		change_all_occurrences(r'\verb+11+', r'\verb+' + str(self.__a[index_1]) + '+')
		change_all_occurrences(r'\verb+111+', r'\verb+' + str(self.__a[index_1]+dif_1) + '+')

		change_all_occurrences(r'\verb+2+', r'\verb+' + str(index_2) + '+')
		change_all_occurrences(r'\verb+22+', r'\verb+' + str(self.__a[index_2]) + '+')
		change_all_occurrences(r'\verb+222+', r'\verb+' + str(self.__a[index_2]+dif_2) + '+')

		change_all_occurrences(r'\verb+3+', r'\verb+' + str(index_3) + '+')
		change_all_occurrences(r'\verb+33+', r'\verb+' + str(self.__a[index_3]) + '+')
		change_all_occurrences(r'\verb+333+', r'\verb+' + str(self.__a[index_3]+dif_3) + '+')

		change_all_occurrences(r'\verb+4+', r'\verb+' + str(index_4) + '+')
		change_all_occurrences(r'\verb+44+', r'\verb+' + str(self.__a[index_4]) + '+')
		change_all_occurrences(r'\verb+444+', r'\verb+' + str(self.__a[index_4]+dif_4) + '+')

		change_all_occurrences(r'\verb+5+', r'\verb+' + str(index_5) + '+')
		change_all_occurrences(r'\verb+55+', r'\verb+' + str(self.__a[index_5]) + '+')
		change_all_occurrences(r'\verb+555+', r'\verb+' + str(self.__a[index_5]+dif_5) + '+')

		self.__a = []

		clear()

		return latex_parts

	