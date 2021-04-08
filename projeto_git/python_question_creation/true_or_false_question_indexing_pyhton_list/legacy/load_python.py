import random
import sys

# import the library to get useful functions to manipulate python files
sys.path.append('../qom_questions_transformer')

# loads the source code from another file python
from python_transformer.pt_util.pt_util_file import load_source_code_from_file
from text_transformer.tt_text_transformer_interface import add_changeable
from python_transformer.pt_python_transformer_interface import change_token_all_occurrences
from python_transformer.pt_python_transformer_interface import change_all_occurrences
from text_transformer.tt_text_transformer_interface import clear
from text_transformer.tt_text_transformer_interface import load_text
from python_transformer.pt_source_code import PTSourceCode
from make_pdfs.helper import Helper
		

#read the python files and return as a object
def get_programs_python(program_file_names):

	python_files = []

	for program in program_file_names:

		python_code = load_source_code_from_file(program)

		python_files.append(python_code)

	return python_files



# return the list of output of the programs passed with argument
#@args list with the python programs
#return strings with the output of programs
def get_execution_code(list_python_programs):

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

## TODO
# PASSADOS NO CONSTRUTOR general_files_to_change_list, num_versions, output_index, 

# python_files_list -> name of the files (python) that wants to be changed
# general_files_to_change_list -> name of the files (latex) that wants to be generated
# num_versions -> number of verstions that wants to be created
# output_index -> index of the output (1-question, 2-answer)
def make_versions(python_files_list, general_files_to_change_list, num_versions, output_index):

	latex_extension = ".tex"


	general_latex_files = Helper().add_extension_list(general_files_to_change_list,
														 latex_extension)

	for i in range(num_versions):

		program_py = create_python_program(python_files_list, i)


		## TODO
		Helper().write_to_file("program"+str(i)+".py", program_py[output_index].to_string())



		list_output_programs = execute_python_code(program_py)

		## TODO
		Helper().write_to_file("output"+str(i)+".txt", list_output_programs[output_index])


		latex_parts = create_latex_files(general_latex_files, i)


		write_latex_to_file(general_files_to_change_list, latex_parts, latex_extension, i)

def add_changable_strings(list_string):

	for strg in list_string:
		add_changeable(strg)


# TODO
list_first  = []
list_second = []
list_third  = []
list_forth  = []


def create_python_program(python_files_list, version):

	list_python_programs = get_programs_python(python_files_list)


	first = random.randint(0,99)
	list_first.append(first)

	second = random.randint(0,450)
	list_second.append(second)

	third = [random.randint(1, 25) for i in range(3)]
	list_third.append(third)

	forth = random.randint(0, 40)
	list_forth.append(forth)

	list_strings = ["2", "1", "1 2 3", "3"]

	add_changable_strings(list_strings)

	# change the prints from the file
	'''add_changeable("1") 
	add_changeable("2") 
	add_changeable("1 2 3") 
	add_changeable("3")'''

	

	change_token_all_occurrences("2", str(first))
	change_token_all_occurrences("1", str(second))
	change_all_occurrences("1 2 3", f'{third[0]} {third[1]} {third[2]}')
	change_token_all_occurrences("3", str(forth))
	clear()

	return list_python_programs


def execute_python_code(list_python_programs):

	return get_execution_code(list_python_programs)


def create_latex_files(general_latex_files, version):

	latex_parts = []


	# for every file change the content
	for latex in general_latex_files:
		# get the content from file
		latex_content = Helper().get_file_content(latex)
		# adds to library the content 
		text_part = load_text(latex_content)
		latex_parts.append(text_part)


	list_strings = [r'\verb+2+', r'\verb+1+']

	add_changable_strings(list_strings)

	
	change_all_occurrences(r'\verb+2+', r'\verb+' + str(list_first[version]) + '+')
	change_all_occurrences(r'\verb+1+', r'\verb+' + str(list_second[version]) + '+')
	clear()

	return latex_parts

def write_latex_to_file(general_files_to_change_list, latex_parts, latex_extension, version):

	for y in range(len(latex_parts)):

		content  = latex_parts[y].to_string()

		#TODO
		Helper().write_to_file(general_files_to_change_list[y]+str(version)+latex_extension, content)