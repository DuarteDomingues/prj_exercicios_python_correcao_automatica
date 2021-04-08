import sys
import os


sys.path.append('../qom_questions_transformer')

# loads the source code from another file python
from python_transformer.pt_util.pt_util_file import load_source_code_from_file
from text_transformer.tt_text_transformer_interface import add_changeable
from python_transformer.pt_source_code import PTSourceCode

# helper functions
from make_pdfs.helper import Helper
		



class QuestionsTransformer():

	# python_files_list -> name of the files (python) that wants to be changed
	# general_files_to_change_list -> name of the files (latex) that wants to be generated
	# num_versions -> number of verstions that wants to be created
	# output_index -> index of the output (0-question, 1-answer)
	def __init__(self, python_files_list, general_files_to_change_list, num_versions, output_index):

		self.__python_files_list            = python_files_list
		self.__general_files_to_change_list = general_files_to_change_list
		self.__num_versions                 = num_versions
		self.__output_index                 = output_index
		self.__latex_extension              = ".tex"
		self.__version_path_prefix          = "question/version_"


	@property
	def directory(self):
		return self.__version_path_prefix

	def create_python_program(self, python_files_list, version):

		raise NotImplementedError("Please Implement this method")


	def create_latex_files(self, general_latex_files, version, output_execution=None):

		raise NotImplementedError("Please Implement this method")


	#read the python files and return as a object
	#@args list with the python name files
	#return list with python code as a object
	def get_programs_python(self, program_file_names):

		python_files = []

		for program in program_file_names:

			python_code = load_source_code_from_file(program)

			python_files.append(python_code)

		return python_files

	#adds strings from a list to add to the library with add_changeable
	#@args list with the strings we want to change
	def add_changable_strings(self, list_string):

		for strg in list_string:
			add_changeable(strg)
	
	
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
			program_py = self.create_python_program(self.__python_files_list, i)

			# writes the program python to the directory as a string
			Helper().write_to_file(version_directory+"\\program.py", program_py[self.__output_index].to_string())

			# gets the output of the program python
			list_output_programs = self.__execute_python_code(program_py)

			# writes the output of the program on the directory as text(txt)
			Helper().write_to_file(version_directory+"\\output.txt", list_output_programs[self.__output_index])

			# changes the latex file and creates a new one and returns a list with the latex files 
			latex_parts = self.create_latex_files(general_latex_files, i) # add a third argument if it's needed the output of the question to build the question

			# writes all the latex files on the directory
			self.__write_latex_to_file(self.__general_files_to_change_list, latex_parts, version_directory)
	
	


	# creates a new directories for a specific version number
	# version         -> number of the version
	# returns path in string       
	def __create_versions_directories(self, version):

		version_path = self.__version_path_prefix + str(version + 1)
		if not os.path.exists(version_path):
			os.makedirs(version_path)
			
		return version_path



	# return the list of output of the programs passed with argument
	#@args list with the python programs
	#return strings with the output of programs
	def __get_execution_code(self, list_python_programs):

		list_result = []
		list_error = []
		list_exception = []

		for program in list_python_programs:
			full_program = PTSourceCode(program.lines_parts) # create the object with the code

			#print("programa: ",full_program.to_string()) # DEBUG to know what program is added

			(out, err, excp) = full_program.execute() # executar o codigo

			list_result.append(out) 
			list_error.append(err)
			list_exception.append(excp)

		# if there is any error with the program python it stops the execution and raise a error
		for i in list_error:
			if len(i) > 0:
				raise Exception('Error', 'The program python has a error')
				sys.exit(1)

		for i in list_exception:
			if len(i) > 0:
				raise Exception('Exception', 'The program python has a exception')
				sys.exit(1)

		return list_result
	
	def __execute_python_code(self, list_python_programs):

		return self.__get_execution_code(list_python_programs)


	#writes latex content to string
	def __write_latex_to_file(self, general_files_to_change_list, latex_parts, version_directory):

		for y in range(len(latex_parts)):

			content  = latex_parts[y].to_string()

			Helper().write_to_file(version_directory+"\\"+general_files_to_change_list[y]+self.__latex_extension, content)