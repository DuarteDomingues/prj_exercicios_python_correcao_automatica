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
	
		self.__seed     = None

		self.__numbers1 = None
		self.__numbers2 = None
		self.__numbers3 = None
		self.__numbers4 = None
		self.__numbers5 = None
		self.__numbers6 = None

		self.__numbers12 = None
		self.__numbers22 = None
		self.__numbers32 = None
		self.__numbers42 = None
		self.__numbers52 = None
		self.__numbers62 = None


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

		#seed = random.randint(10000,99999)
		#self.__seed = seed
		


		# generation of the train numbers
		numbers1 = [random.randint(10,30) for i in range(3)]
		numbers2 = [random.randint(100,300) for i in range(3)]

		numbers3 = [random.randint(1000,2000) for i in range(2)]
		numbers4 = [random.randint(4000,8000) for i in range(2)]

		numbers5 = [random.randint(2,50) for i in range(2)]
		numbers6 = [random.randint(150,350) for i in range(2)]


		self.__numbers1 = numbers1
		self.__numbers2 = numbers2
		self.__numbers3 = numbers3
		self.__numbers4 = numbers4
		self.__numbers5 = numbers5
		self.__numbers6 = numbers6


		# generation of the test numbers
		numbers12 = [random.randint(10,30) for i in range(2)]
		numbers22 = [random.randint(100,300) for i in range(2)]

		numbers32 = [random.randint(1000,2000) for i in range(3)]
		numbers42 = [random.randint(4000,8000) for i in range(3)]

		numbers52 = [random.randint(2,50) for i in range(4)]
		numbers62 = [random.randint(150,350) for i in range(4)]


		self.__numbers12 = numbers12
		self.__numbers22 = numbers22
		self.__numbers32 = numbers32
		self.__numbers42 = numbers42
		self.__numbers52 = numbers52
		self.__numbers62 = numbers62


		list_strings = ["100", "numero", "minima", "maxima", "10", "20", "30", "101", "200", "300", "1000", "2000", "5000", "8000", "25", "12", "150", "350",\
						"13",  "14", "102", "103", "80", "90", "110", "500", "600", "700", "120", "130", "140", "160", "800", "900", "1001", "1002"]

		self.add_changable_strings(list_strings)

		change_token_all_occurrences(list_strings[0], str(seed))#seed
		change_all_occurrences(list_strings[1], "número")
		change_all_occurrences(list_strings[2], "mínima")
		change_all_occurrences(list_strings[3], "máxima")

		# treino
		change_token_all_occurrences(list_strings[4], str(numbers1[0]))
		change_token_all_occurrences(list_strings[5], str(numbers1[1]))
		change_token_all_occurrences(list_strings[6], str(numbers1[2]))

		change_token_all_occurrences(list_strings[7], str(numbers2[0]))
		change_token_all_occurrences(list_strings[8], str(numbers2[1]))
		change_token_all_occurrences(list_strings[9], str(numbers2[2]))

		change_token_all_occurrences(list_strings[10], str(numbers3[0]))
		change_token_all_occurrences(list_strings[11], str(numbers3[1]))

		change_token_all_occurrences(list_strings[12], str(numbers4[0]))
		change_token_all_occurrences(list_strings[13], str(numbers4[1]))

		change_token_all_occurrences(list_strings[14], str(numbers5[0]))
		change_token_all_occurrences(list_strings[15], str(numbers5[1]))

		change_token_all_occurrences(list_strings[16], str(numbers6[0]))
		change_token_all_occurrences(list_strings[17], str(numbers6[1]))



		# teste
		change_token_all_occurrences(list_strings[18], str(numbers12[0]))
		change_token_all_occurrences(list_strings[19], str(numbers12[1]))


		change_token_all_occurrences(list_strings[20], str(numbers22[0]))
		change_token_all_occurrences(list_strings[21], str(numbers22[1]))


		change_token_all_occurrences(list_strings[22], str(numbers32[0]))
		change_token_all_occurrences(list_strings[23], str(numbers32[1]))
		change_token_all_occurrences(list_strings[24], str(numbers32[2]))

		change_token_all_occurrences(list_strings[25], str(numbers42[0]))
		change_token_all_occurrences(list_strings[26], str(numbers42[1]))
		change_token_all_occurrences(list_strings[27], str(numbers42[2]))


		change_token_all_occurrences(list_strings[28], str(numbers52[0]))
		change_token_all_occurrences(list_strings[29], str(numbers52[1]))
		change_token_all_occurrences(list_strings[30], str(numbers52[2]))
		change_token_all_occurrences(list_strings[31], str(numbers52[3]))


		change_token_all_occurrences(list_strings[32], str(numbers62[0]))
		change_token_all_occurrences(list_strings[33], str(numbers62[1]))
		change_token_all_occurrences(list_strings[34], str(numbers62[2]))
		change_token_all_occurrences(list_strings[35], str(numbers62[3]))


		clear()

		return list_python_programs,seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):
		

		latex_parts = self.get_text_files(general_latex_files)


		random.seed(self.__seed)

		# generate the answers for the train
		numbers_generated_1 = [random.randint(self.__numbers1[i], self.__numbers2[i]) for i in range(len(self.__numbers1))]
		numbers_generated_2 = [(i*-1)*random.randint(self.__numbers3[i-1], self.__numbers4[i-1]) for i in range(1, len(self.__numbers3)+1)]
		numbers_generated_3 = [random.randint(self.__numbers5[i], self.__numbers6[i]) for i in range(len(self.__numbers5))]

		list_all_numbers = [numbers_generated_1, numbers_generated_2, numbers_generated_3]

		maximum_value = 0
		for index in range(len(list_all_numbers)):
			maximum_value = max(list_all_numbers[index]) if max(list_all_numbers[index]) > maximum_value else maximum_value

		minimum_value = 0
		for index in range(len(list_all_numbers)):
			minimum_value = min(list_all_numbers[index]) if min(list_all_numbers[index]) < minimum_value else minimum_value

		sum_total = 0

		for index in range(len(list_all_numbers)):
			sum_total += sum(list_all_numbers[index])

		num_lists = len(list_all_numbers)

		num_indexes = 0

		for index in range(len(list_all_numbers)):
			for index2 in range(len(list_all_numbers[index])):
				num_indexes+=1



		# generate the answers for the test
		numbers_generated_12 = [random.randint(self.__numbers12[i],self.__numbers22[i]) for i in range(len(self.__numbers12))]
		numbers_generated_22 = [(i*-1)*random.randint(self.__numbers32[i-1], self.__numbers42[i-1]) for i in range(1, len(self.__numbers32)+1)]
		numbers_generated_32 = [random.randint(self.__numbers52[i], self.__numbers62[i]) for i in range(len(self.__numbers52))]

		list_all_numbers2 = [numbers_generated_12, numbers_generated_22, numbers_generated_32]


		maximum_value2 = 0
		for index in range(len(list_all_numbers2)):
			maximum_value2 = max(list_all_numbers2[index]) if max(list_all_numbers2[index]) > maximum_value2 else maximum_value2

		minimum_value2 = 0
		for index in range(len(list_all_numbers2)):
			minimum_value2 = min(list_all_numbers2[index]) if min(list_all_numbers2[index]) < minimum_value2 else minimum_value2

		sum_total2 = 0
		for index in range(len(list_all_numbers2)):
			sum_total2 += sum(list_all_numbers2[index])

		num_lists2 = len(list_all_numbers2)

		num_indexes2 = 0
		for index in range(len(list_all_numbers2)):
			for index2 in range(len(list_all_numbers2[index])):
				num_indexes2+=1


		random.seed(datetime.now())



		
		list_strings = [r'\verb+6+', r'\verb+-30+', r'\verb+150+', r'\verb+3+', r'\verb+7+', r'\verb+126+', r'\verb+-20+', r'\verb+100+',
						r'\verb+101t+', r'\verb+102t+', r'\verb+103t+', r'\verb+104t+', r'\verb+105t+', r'\verb+106t+', r'\verb+107t+', r'\verb+108t+',
						r'\verb+101f+', r'\verb+102f+', r'\verb+103f+', r'\verb+104f+', r'\verb+105f+', r'\verb+106f+', r'\verb+107f+', r'\verb+108f+',
						 "1101", "101", "2501","200", "3350", "300", "1000", "5000", "2000", "8000", "25", "151", "12", "350",
						 "13", "102", "14", "103", "80", "500", "90", "600", "110", "700", "120", "800", "130", "900", "140", "1001", "160", "1002",
						 "numero", "minima", "maxima"]

		self.add_changable_strings(list_strings)

		# change the train values
		change_all_occurrences(r'\verb+6+', r'\verb+' +str(sum(numbers_generated_1)) + '+')
		change_all_occurrences(r'\verb+-30+', r'\verb+' +str(sum(numbers_generated_2)) + '+')
		change_all_occurrences(r'\verb+150+', r'\verb+' +str(sum(numbers_generated_3)) + '+')

		change_all_occurrences(r'\verb+3+', r'\verb+' +str(num_lists) + '+')
		change_all_occurrences(r'\verb+7+', r'\verb+' +str(num_indexes) + '+')
		change_all_occurrences(r'\verb+126+', r'\verb+' +str(sum_total) + '+')
		change_all_occurrences(r'\verb+-20+', r'\verb+' +str(minimum_value) + '+')
		change_all_occurrences(r'\verb+100+', r'\verb+' +str(maximum_value) + '+')


		# change the test values to the true ones
		change_all_occurrences(r'\verb+101t+', r'\verb+' +str(sum(numbers_generated_12)) + '+')
		change_all_occurrences(r'\verb+102t+', r'\verb+' +str(sum(numbers_generated_22)) + '+')
		change_all_occurrences(r'\verb+103t+', r'\verb+' +str(sum(numbers_generated_32)) + '+')
		change_all_occurrences(r'\verb+104t+', r'\verb+' +str(num_lists2) + '+')
		change_all_occurrences(r'\verb+105t+', r'\verb+' +str(num_indexes2) + '+')
		change_all_occurrences(r'\verb+106t+', r'\verb+' +str(sum_total2) + '+')
		change_all_occurrences(r'\verb+107t+', r'\verb+' +str(minimum_value2) + '+')
		change_all_occurrences(r'\verb+108t+', r'\verb+' +str(maximum_value2) + '+')

		# change the test values to the false ones
		change_all_occurrences(r'\verb+101f+', r'\verb+' +str(sum(numbers_generated_12)+random.choice([-1,1])) + '+')
		change_all_occurrences(r'\verb+102f+', r'\verb+' +str(sum(numbers_generated_22)+random.choice([-1,1])) + '+')
		change_all_occurrences(r'\verb+103f+', r'\verb+' +str(sum(numbers_generated_32)+random.choice([-1,1])) + '+')
		change_all_occurrences(r'\verb+104f+', r'\verb+' +str(num_lists2) + '+')
		change_all_occurrences(r'\verb+105f+', r'\verb+' +str(num_indexes2) + '+')
		change_all_occurrences(r'\verb+106f+', r'\verb+' +str(sum_total2+random.choice([-1,1])) + '+')
		change_all_occurrences(r'\verb+107f+', r'\verb+' +str(minimum_value2+random.choice([-1,1])) + '+')
		change_all_occurrences(r'\verb+108f+', r'\verb+' +str(maximum_value2+random.choice([-1,1])) + '+')


		#make versions with the numbers to the train
		change_all_occurrences("1101", str(self.__numbers1[0]))
		change_all_occurrences("101", str(self.__numbers2[0]))

		change_all_occurrences("2501", str(self.__numbers1[1]))
		change_all_occurrences("200", str(self.__numbers2[1]))

		change_all_occurrences("3350", str(self.__numbers1[2]))
		change_all_occurrences("300", str(self.__numbers2[2]))

		change_all_occurrences("1000", str(self.__numbers3[0]))
		change_all_occurrences("5000", str(self.__numbers4[0]))

		change_all_occurrences("2000", str(self.__numbers3[1]))
		change_all_occurrences("8000", str(self.__numbers4[1]))

		change_all_occurrences("25", str(self.__numbers5[0]))
		change_all_occurrences("151", str(self.__numbers6[0]))

		change_all_occurrences("12", str(self.__numbers5[1]))
		change_all_occurrences("350", str(self.__numbers6[1]))



		# make version with numbers to test
		change_all_occurrences("13", str(self.__numbers12[0]))
		change_all_occurrences("102", str(self.__numbers22[0]))
		change_all_occurrences("14", str(self.__numbers12[1]))
		change_all_occurrences("103", str(self.__numbers22[1]))

		change_all_occurrences("80", str(self.__numbers32[0]))
		change_all_occurrences("500", str(self.__numbers42[0]))
		change_all_occurrences("90", str(self.__numbers32[1]))
		change_all_occurrences("600", str(self.__numbers42[1]))
		change_all_occurrences("110", str(self.__numbers32[2]))
		change_all_occurrences("700", str(self.__numbers42[2]))

		change_all_occurrences("120", str(self.__numbers52[0]))
		change_all_occurrences("800", str(self.__numbers62[0]))
		change_all_occurrences("130", str(self.__numbers52[1]))
		change_all_occurrences("900", str(self.__numbers62[1]))
		change_all_occurrences("140", str(self.__numbers52[2]))
		change_all_occurrences("1001", str(self.__numbers62[2]))
		change_all_occurrences("160", str(self.__numbers52[3]))
		change_all_occurrences("1002", str(self.__numbers62[3]))

		change_all_occurrences("numero", "número")
		change_all_occurrences("minima", "mínima")
		change_all_occurrences("maxima", "máxima")

		clear()

		return latex_parts

	