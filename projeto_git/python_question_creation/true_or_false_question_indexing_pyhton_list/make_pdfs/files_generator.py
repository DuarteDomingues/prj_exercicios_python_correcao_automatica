import os
from make_pdfs.helper import Helper
from pathlib import Path

class FilesGenerator():

	# file_names      -> list of the names for files
	# text_files      -> if the questions is on text files
	# list_questions  -> list with questions on string format
	# maintain_files  -> if want to keep log and aux files
	def __init__(self, file_names, directory, num_versions = 1, maintain_files = False):

		
		self.__file_names     = file_names
		self.__maintain_files = maintain_files
		self.__num_versions   = num_versions
		self.__directory      = directory


		# only used when the questions is on a text file 
		latex_extension = ".tex"
		aux_extension   = ".aux"
		log_extension   = ".log"
		pdf_extension   = ".pdf"


		# name of the files tex
		self.__latex_file_names       = Helper().add_extension_list(file_names, latex_extension)
		# name of the files aux created
		self.__latex_file_aux_remove  = Helper().add_extension_list(file_names, aux_extension)
		# name of the log files created
		self.__text_file_log_remove   = Helper().add_extension_list(file_names, log_extension)
		# name of the pdf files
		self.__pdf_file_names         = Helper().add_extension_list(file_names, pdf_extension)


	


	# converts the text file to pdf and after to png
	def execute(self):
		for index in range(1, self.__num_versions+1):

			# converts the .tex to pdf and dont remove the aux and log files
			self.__convert_latex_to_pdf(self.__latex_file_names, index)

			# converts the pdf files to png
			self.__convert_pdf_to_png(self.__pdf_file_names, self.__latex_file_aux_remove,
									 self.__text_file_log_remove, index, maintain_files = self.__maintain_files)


	# @args  
	#latex_file_names -> list of strings with name of .tex files
	#latex_file_aux_remove -> list of strings with name of .aux files
	#text_file_log_remove -> list of strings with name of .log files
	#maintain_files -> to maintain files like 
	def __convert_latex_to_pdf(self, latex_file_names, index):

		current_directory = Path.cwd()

		# creates the pdf file with the .tex file
		for name in latex_file_names:

			if self.__directory != None:
				os.chdir(self.__directory+str(index))


			#command to generate 
			command = 'pdflatex '+name


			#execute the command to create files
			os.system(command)

			if self.__directory != None:
				os.chdir(current_directory)

			

	# converts the pdf files to png
	# @args  
	#list_names -> list of strings with name of files
	def __convert_pdf_to_png(self, latex_file_names, latex_file_aux_remove, text_file_log_remove, index, maintain_files=False):

		current_directory = Path.cwd()

		for i in range(len(latex_file_names)):

			if self.__directory != None:
				os.chdir(self.__directory+str(index))
		
			output_file = str(Path(latex_file_names[i]).with_suffix('.png'))

			ghostscript_command = 'gs -r150 -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sDEVICE=png16m -o '+output_file+' '+ latex_file_names[i]

			os.system(ghostscript_command)
		
			#remove temporary files
			if not maintain_files:
				os.remove(latex_file_aux_remove[i])
				os.remove(text_file_log_remove[i])

			if self.__directory != None:
				os.chdir(current_directory)
