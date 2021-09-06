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
		
		self.__codigoPostalDic ={}
		self.__dic_random_keys = []
		self.__x               = ""
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

		[x_var, y_var] = random.sample(string.ascii_lowercase, 2)

		self.__codigoPostalDic['Fiat'] = ['Fiat',500,2007]
		self.__codigoPostalDic['Mini'] = ['Mini',1000, 2000]
		self.__codigoPostalDic['Toyota'] = ['Toyota','Supra', 1980]
		self.__codigoPostalDic['Nissan'] = ['Nissan','GTR',2010]
		self.__codigoPostalDic['Chevrolet'] = ['Chevrolet','Camaro',2008]
		self.__codigoPostalDic['Audi'] = ['Audi','R8',2020]
		self.__codigoPostalDic['BMW'] = ['BMW','M4',2019]
		self.__codigoPostalDic['Ford'] = ['Ford','Punto',2013]
		self.__codigoPostalDic['Tesla'] = ['Tesla','X',2020]
		
		self.__dic_random_keys = random.sample(list(self.__codigoPostalDic),3)

		list_strings = ["x","y","Fiat","Mini","500","1000","2007","2000"]

		self.add_changable_strings(list_strings)

		marca_fiat = [self.__dic_random_keys][0][0]
		marca_mini = [self.__dic_random_keys][0][1]
		
		change_token_all_occurrences("x", x_var)
		change_token_all_occurrences("y", y_var)

		self.__x = x_var

		change_all_occurrences("Fiat", marca_fiat)
		change_all_occurrences("Mini",marca_mini)

		change_all_occurrences("500",str(self.__codigoPostalDic[marca_fiat][1]))
		change_all_occurrences("1000", str(self.__codigoPostalDic[marca_mini][1]))
		change_all_occurrences("2007", str(self.__codigoPostalDic[marca_mini][2]))
		change_all_occurrences("2000", str(self.__codigoPostalDic[marca_fiat][2]))

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = []


		for latex in general_latex_files:
			
			# get the content from file
			latex_content = Helper().get_file_content(self.directory_tex+latex)

			# adds to library the content 
			text_part = load_text(latex_content)
			latex_parts.append(text_part)
		

		marca_carro_1 = self.__dic_random_keys[0]
		marca_carro_2 = self.__dic_random_keys[1]

		modelo_carro_1 = self.__codigoPostalDic[marca_carro_1][1]
		modelo_carro_2 = self.__codigoPostalDic[marca_carro_2][1]


		list_strings = [r'\verb+outputTrue+', r'\verb+outputFalso+', r'\verb+x.__ano+']

		self.add_changable_strings(list_strings)
		

		str_output_false = "" f"{marca_carro_1} {modelo_carro_1} \n{marca_carro_2} {modelo_carro_2}  "

		str_output_true = ""+ str(marca_carro_1)+" "+str(modelo_carro_1)+"\n"+str(marca_carro_1)+" "+str(modelo_carro_1)+"\n"+str(marca_carro_2)+" "+str(modelo_carro_2)+"\n" + str(marca_carro_2)+" "+str(modelo_carro_2)


		change_all_occurrences(r'\verb+outputTrue+', str_output_true )
		change_all_occurrences(r'\verb+outputFalso+', str_output_false )
		change_all_occurrences(r'\verb+x.__ano+', self.__x+".__ano"  )

		clear()

		return latex_parts