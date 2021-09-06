from pathlib import Path

class Helper():

	# function to read as a string the content of a file
	#@args name of the file
	#return string of content on the file
	@staticmethod
	def get_file_content(filename):

		with open(filename, "r", encoding="UTF-8") as f:
			content = f.read()

		f.close()
		return content


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

		with open(filename, "w", encoding="UTF-8") as file:
			file.write(content)

		file.close()