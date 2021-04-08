from pathlib import Path

class Helper():

	# function to read as a string the content of a file
	#@args name of the file
	#return string of content on the file
	@staticmethod
	def get_file_content(filename):

		with open(filename, "r") as f:
			content = f.read()

		return content

	#converts the string to 8859-1 enconding
	#@args list with strings on utf-8 enconding
	#return	list with strings on iso-8859-1 enconding
	@staticmethod
	def convert_list_to_iso8859(list_utf8):

		for i in range(len(list_utf8)):
			list_utf8[i] = list_utf8[i].encode().decode("ISO-8859-1")

		return list_utf8


	# adds a certain extension to the name of files on the string
	# @args  
	#list_names -> list of strings with name of files
	#extension -> estension of the file that wants to add
	# return list with strings with extension
	@staticmethod
	def add_extension_list(list_names, extension):

		# if dont copy it return the reference to the object and not a new one
		new_list = list_names.copy()

		for i in range(len(list_names)):
			new_list[i] = str(Path(new_list[i]).with_suffix(extension))

		return new_list


	# writes the content on the file
	#@args 
	#filname -> string with the name of the file
	#content -> string with the content that wants to be written
	@staticmethod
	def write_to_file(filename, content):

		with open(filename, "w") as file:
			file.write(content)

	# content of a standard latex file (begin)
	@staticmethod
	def _initial_latex_content():
		return "\\documentclass[12pt,varwidth=16cm,border=1pt]{standalone}\n\n"\
				+ "\\usepackage[T1]{fontenc}\n"+"\\usepackage[utf8]{inputenc}\n"\
				+ "\\usepackage[portuguese]{babel}\n\n" + "\\begin{document}\n\n"

	# content of the end os standard latex file
	@staticmethod
	def _end_latex_content():
		return "\n\n\\end{document}"

	#generate tex files with the content inside the txt file
	#@args
	#file_names - name of the txt files
	@staticmethod
	def generate_latex_with_text(file_names):

		file_txt = Helper().add_extension_list(file_names, ".txt")
		file_latex = Helper().add_extension_list(file_names, ".tex")

		for i in range(len(file_names)):
			file = open(file_latex[i], "w")
			content = Helper().get_file_content(file_txt[i])
			file.write(Helper()._initial_latex_content()+content+Helper()._end_latex_content())
			file.close()

	#generate tex files with the list created on a python file
	#@args
	#file_names     -> name of the files that whats to be created(.tex)
	#list_questions -> list that contains strings to be written on the
	@staticmethod
	def generate_latex_with_list(file_names, list_questions):
		# converts the content of the string to iso-8859-1 because by default it's utf-8
		list_question = Helper().convert_list_to_iso8859(list_questions)
		file_latex = Helper().add_extension_list(file_names, ".tex")
		

		for i in range(len(list_question)):
			file = open(file_latex[i], "w")
			file.write(Helper()._initial_latex_content()+list_question[i]+Helper()._end_latex_content())
			file.close()

