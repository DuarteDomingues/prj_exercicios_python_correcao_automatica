import sys
import os


sys.path.append('../qom_questions_transformer')

# loads the source code from another file python
from python_transformer.pt_util.pt_util_file import load_source_code_from_file
from text_transformer.tt_text_transformer_interface import add_changeable
from text_transformer.tt_text_transformer_interface import clear
from text_transformer.tt_text_transformer_interface import load_text
from python_transformer.pt_python_transformer_interface import change_all_occurrences
from python_transformer.pt_source_code import PTSourceCode

# helper functions
from file_generator.helper import Helper
		



class GenerateRandomVersion():

	# python_files_list            -> name of the files (python) that wants to be changed
	# general_files_to_change_list -> name of the files (latex) that wants to be changed
	# directory_latex              -> directory where the question base is stored
	# num_versions                 -> number of verstions that wants to be created
	# output_index                 -> index of the output (0-question, 1-answer)
	# version_path                 -> directory where the generated question will be
	# repeat_seed                  -> seed to generate again a version with the passed seed
	def __init__(self, python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, repeat_seed):

		self.__python_files_list            = python_files_list
		self.__general_files_to_change_list = general_files_to_change_list
		self.__directory_latex              = directory_latex
		self.__num_versions                 = num_versions
		self.__output_index                 = output_index
		self.__latex_extension              = ".tex"
		self.__version_path_prefix          = version_path+"/version_"
		self.__repeat_seed                  = repeat_seed


	@property
	def directory(self):
		return self.__version_path_prefix

	@property
	def directory_tex(self):
		return self.__directory_latex

	@property
	def repeat_seed(self):
		return self.__repeat_seed
	
	# abstract method
	def create_python_program(self, python_files_list, version):

		raise NotImplementedError("Please Implement this method")

	# abstract method
	def create_latex_files(self, general_latex_files, version, output_list):

		raise NotImplementedError("Please Implement this method")


	#read the python files and return as a object
	#@args 
	#program_file_names -> list with the python name files
	#return list with python code as a object
	def get_programs_python(self, program_file_names):

		python_files = []

		for program in program_file_names:

			python_code = load_source_code_from_file(self.__directory_latex+program)

			python_files.append(python_code)

		return python_files

	#adds strings from a list to add to the library with add_changeable
	#@args 
	#list_string -> list with the strings we want to change
	def add_changable_strings(self, list_string):

		for strg in list_string:
			add_changeable(strg)


	#returns a list with all latex files loaded from library to change the file
	def get_text_files(self, general_latex_files):

		latex_parts = []

		for latex in general_latex_files:
			
			# get the content from file
			latex_content = Helper().get_file_content(self.directory_tex+latex)

			# adds to library the content 
			text_part = load_text(latex_content)
			latex_parts.append(text_part)

		return latex_parts
	
	
	#generates different versions of program file and tex files for each version, 
	#creating a new directory
	def make_versions(self):

		general_latex_files = Helper().add_extension_list(self.__general_files_to_change_list,
														 self.__latex_extension)
		
		for i in range(self.__num_versions):
			
			#gets the current directory
			curr_directory = os.getcwd()

			# creates directory for version 1, 2 ...
			version_directory = self.__create_versions_directories(i)

			#loads the python program as a object
			program_py, seed = self.create_python_program(self.__python_files_list, i)

			# writes the seed to generate the exercise on the directory
			Helper().write_to_file(version_directory+"/seed.txt", str(seed))

			# writes the question on latex
			self.__generate_question_latex(version_directory, self.__python_files_list, program_py[0].to_string(), general_latex_files[0])

			# writes the program python to the directory as a string
			Helper().write_to_file(version_directory+"/program.py", program_py[0].to_string())

			if len(program_py) > 1:
				Helper().write_to_file(version_directory+"/full_program.py", program_py[1].to_string())

			# gets the output of the program python
			list_output_programs = self.__get_execution_code(program_py)

			# writes the output of the program on the directory as text(txt)
			Helper().write_to_file(version_directory+"/full_program_output.txt", ''.join([str(elem) for elem in list_output_programs]))

			# changes the latex file and creates a new one and returns a list with the latex files 
			latex_parts = self.create_latex_files(general_latex_files, i, list_output_programs) # add a third argument if it's needed the output of the question to build the question

			# writes all the latex files on the directory
			self.__write_latex_to_file(self.__general_files_to_change_list, latex_parts, version_directory)


	# creates the question with the changed program on python
	#@args
	#directory        -> dicrectory where the program should be
	#previous_program -> python program before changed
	#program_changed  -> python program after changed
	#latex_file       -> name of the file to change
	def __generate_question_latex(self, directory, previous_program, program_changed, latex_file):

		previous = self.get_programs_python(previous_program)

		program = load_text(Helper().get_file_content(self.__directory_latex+latex_file))

		add_changeable(previous[0].to_string())

		change_all_occurrences(previous[0].to_string(), program_changed)

		clear()

		Helper().write_to_file(directory+"/"+latex_file, program.to_string())
		

	# creates a new directories for a specific version number
	# version         -> number of the version
	# returns path in string   
	def __create_versions_directories(self, version):

		version_path = self.__version_path_prefix + str(version + 1)
		if not os.path.exists(version_path):
			os.makedirs(version_path)
			
		return version_path



	# return the list of output of the programs passed with argument
	#@args 
	#list_python_programs -> list with the python programs
	#return strings with the output of programs
	def __get_execution_code(self, list_python_programs):

		program = list_python_programs[self.__output_index]

		full_program = PTSourceCode(program.lines_parts) # create the object with the code

		#print("programa: ",full_program.to_string()) # DEBUG to know what program is added

		(out, err, excp) = full_program.execute() # execute the code

		# if there is any error with the program python it stops the execution and raise a error
		if len(err) > 0:
			out += err
		
		if len(excp) > 0:
			out += excp
		
		return out


	#writes latex content to string
	#@args
	#general_files_to_change_list -> list with python programs
	#latex_parts                  -> object with python code
	#version_directory            -> directory of the version that is being executed
	def __write_latex_to_file(self, general_files_to_change_list, latex_parts, version_directory):

		for y in range(1, len(latex_parts)):

			content  = latex_parts[y].to_string()

			Helper().write_to_file(version_directory+"/"+general_files_to_change_list[y]+self.__latex_extension, content)