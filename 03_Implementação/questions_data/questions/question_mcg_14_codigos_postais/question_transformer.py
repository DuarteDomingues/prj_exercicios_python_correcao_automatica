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
from questions.question_mcg_14_codigos_postais.gestor_codigos_postais import GestorCodigoPostais, CodigoPostal
		


class QuestionTransformer(GenerateRandomVersion):

	# python_files_list -> name of the files (python) that wants to be changed
	# general_files_to_change_list -> name of the files (latex) that wants to be generated
	# num_versions -> number of verstions that wants to be created
	# output_index -> index of the output (1-question, 2-answer)
	def __init__(self, python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, repeat_seed=None):

		super().__init__(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, repeat_seed)
		self.__outputs = []
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

		list_strings = ["30","12000","1100","40","OEIRAS_LOCALIDADE","questions.question_mcg_14_objeto_parametros_insuficientes.gestor_codigos_postais"]

		self.add_changable_strings(list_strings)

	


		rand = random.randint(0,1)

		num_12000 = 12000
		num_1100  = 1100

		if rand == 0:
			num_12000 = num_12000 -random.randint(0,1000)
		else:
			num_12000 = num_12000 +random.randint(0,1000)
		

		num_1100 = num_1100 +random.randint(0,200)


		list_locals = ["LOURES","MAFRA","OEIRAS","CASCAIS","ESPINHO","MAIA","OVAR"]

		local = random.choice (list_locals)


		outputs,num_40 = program_code(num_12000,num_1100, local, seed)
		self.__outputs = outputs

		change_all_occurrences("30", str(seed))
		change_all_occurrences("12000",str( num_12000))
		change_all_occurrences("1100", str(num_1100))
		change_all_occurrences("40", str(num_40))
		change_all_occurrences("OEIRAS_LOCALIDADE", local)
		change_all_occurrences(list_strings[5], "pergunta")

		clear()

		return list_python_programs,seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)
		
		list_strings = [r'\verb+len_codigos_postais+',r'\verb+len_codigos_postais_falso+',r'\verb+output_codigo_postal_falso+',r'\verb+output_codigo_postal+', r'\verb+len_codigos_postais_distrito+',r'\verb+len_codigos_postais_distrito_falso+']


		self.add_changable_strings(list_strings)
		
		change_all_occurrences(list_strings[0], r'\verb+' +str(self.__outputs[0]) + '+')
		change_all_occurrences(list_strings[1], r'\verb+' +str(self.__outputs[0]+1) + '+')
		change_all_occurrences(list_strings[2], r'\verb+' +str(self.__outputs[2]) + '+')
		change_all_occurrences(list_strings[3], r'\verb+' +str(self.__outputs[1]) + '+')
		change_all_occurrences(list_strings[4], r'\verb+' +str(self.__outputs[3]) + '+')
		change_all_occurrences(list_strings[5], r'\verb+' +str(self.__outputs[3]-1) + '+')

		clear()

		return latex_parts
	

def program_code(max_len_num_4_digitos,max_len_num_3_digitos, local, numb_seed):

	random.seed(numb_seed)

	list_localidades = ["LOURES","MAFRA","OEIRAS","CASCAIS","lisboa","ESPINHO","MAIA","Amarante","valongo","OVAR","Pombal","Batalha"]
	outputs = []
	codigos_postais = []
	
	for i in range (1000):
		num_4_digits =  random.randint(1,max_len_num_4_digitos)
		num_3_digits =  random.randint(1,max_len_num_3_digitos)
		localidade   =  random.choice(list_localidades)
		code_i       =  CodigoPostal(num_4_digits,num_3_digits,localidade)
		codigos_postais.append(code_i)
	
	
	g = GestorCodigoPostais(codigos_postais)
	g.validar_codigos_postais()
	print(len(g.codigos_postais))
	outputs.append(len(g.codigos_postais))
	l_codigos = len(g.codigos_postais)
	rand = random.randint(0,l_codigos-1)
	output_2 = str(str(g.codigos_postais[rand].digitos4)+"-"+str(g.codigos_postais[rand].digitos3)+" "+str(g.codigos_postais[rand].localidade))
	output_2_falso = str(str(g.codigos_postais[rand-1].digitos4)+"-"+str(g.codigos_postais[rand-1].digitos3)+" "+str(g.codigos_postais[rand-1].localidade))
	outputs.append(output_2)
	cods = g.obter_codigos_postais_por_localidade(local)
	outputs.append(output_2_falso)
	outputs.append(len(cods))





	return outputs,rand

	



	

	


		

 


	
