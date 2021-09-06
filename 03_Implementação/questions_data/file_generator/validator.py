from file_generator.helper import Helper
from pathlib import Path
import os

class Validator():

	# @args
	# python_file_names -> list of the names for python files
	# directory         -> directory where the files generated is stored, just need to add the number of the version on the end to access it
	# num_versions      -> number versions created
	def __init__(self, python_file_names, directory, num_versions):

		self.__python_file_names = python_file_names
		self.__directory         = directory
		self.__num_versions      = num_versions

	def execute(self):

		list_programs, list_full_program =  self.__get_program_python(self.__python_file_names, self.__directory, self.__num_versions)

		self.__check_program_python(list_programs,list_full_program)

	# gets the code of the program and full program
	# @args 
	# python_file_names -> list of the names for python files
	# directory         -> directory where the files generated
	# num_versions      -> number versions created
	# returns two list with the content of the program and full program, if there is no full program the full program list will have length 0
	def __get_program_python(self, python_file_names, directory, num_versions):

		current_directory = Path.cwd()
		list_programs = []
		list_full_program = []

		# gets all the content from the python files
		for version in range(1, num_versions+1):
			os.chdir(directory+str(version))

			for program in range(len(python_file_names)):
				if program == 0:
					list_programs.append(Helper().get_file_content(python_file_names[program]))

				else:
					list_full_program.append(Helper().get_file_content(python_file_names[program]))

			os.chdir(current_directory)


		return list_programs, list_full_program


	# prints if there is any program python or full program equal
	# @args 
	# list_programs     -> list with all the content of the programs python created
	# list_full_program -> list with all the content of the full the programs python created
	def __check_program_python(self, list_programs, list_full_program):
		# compares the strings to see if there is any equal and prints if there is any equal
		list_equals_str = []

		for program in range(len(list_programs)):
			for program2 in range(len(list_programs)):
				if list_programs[program] == list_programs[program2] and program != program2:
					list_equals_str.append(str(program+1)+";"+str(program2+1))


		for index in list_equals_str:
			print("Programas iguais no índice: "+index)

		if len(list_equals_str) == 0:
			print("Não existe programas iguais")

		# same as before but to the full program
		if len(list_full_program) > 0:
			list_equals_str = []
			for program in range(len(list_full_program)):
				for program2 in range(len(list_full_program)):
					if list_full_program[program] == list_full_program[program2] and program != program2:
						list_equals_str.append(str(program+1)+";"+str(program2+1))

			for index in list_equals_str:
				print("Programas completos iguais no índice: "+index)

			if len(list_equals_str) == 0:
				print("Não existe programas completos iguais")



