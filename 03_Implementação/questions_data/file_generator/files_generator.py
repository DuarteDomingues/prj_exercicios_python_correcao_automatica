import os
from file_generator.helper import Helper
from pathlib import Path

class FilesGenerator():

	# @args
	# file_names      -> list of the names for files
	# directory       -> directory where the questions generated is stored, just need to add the number of the version on the end to access it
	# num_versions    -> number of versions created
	# maintain_files  -> if want to keep log and aux files (set is value to True to maintain)
	def __init__(self, file_names, directory, num_versions, maintain_files = False):

		# store the variables on the attributes
		self.__file_names     = file_names
		self.__maintain_files = maintain_files
		self.__num_versions   = num_versions
		self.__directory      = directory


		# to create lists with this extensions
		latex_extension = ".tex"
		png_extension   = ".png"
		aux_extension   = ".aux"
		log_extension   = ".log"
		pdf_extension   = ".pdf"


		# name of the files tex
		self.__latex_file_names       = Helper().add_extension_list(file_names, latex_extension)

		# name of the png files
		self.__png_file_names         = Helper().add_extension_list(file_names, png_extension)

		# name of the files aux created
		self.__aux_file_names         = Helper().add_extension_list(file_names, aux_extension)

		# name of the log files created
		self.__log_file_names         = Helper().add_extension_list(file_names, log_extension)

		# name of the pdf files
		self.__pdf_file_names         = Helper().add_extension_list(file_names, pdf_extension)


	# converts the LaTeX file to PDF and after to PNG
	def execute(self):
		for index in range(1, self.__num_versions+1):

			# converts the .tex to pdf
			self.__convert_latex_to_pdf(self.__latex_file_names, index)

			# converts the PDF files to PNG and on the end remove the .aux and .log files
			self.__convert_pdf_to_png(self.__pdf_file_names, self.__png_file_names , self.__aux_file_names,
									 self.__log_file_names, index, self.__maintain_files)

	# converts the LaTeX files to PDF
	# @args  
	#latex_file_names -> list of strings with name of .tex files
	#index            -> number of the version 
	def __convert_latex_to_pdf(self, latex_file_names, index):

		# store the current directory,
		# this way can go to a version and return to this directory
		current_directory = Path.cwd()

		# creates the pdf file with the .tex file
		for name in latex_file_names:

			# sets the directory to the curresponding version
			os.chdir(self.__directory+str(index))

			#command to generate 
			command = 'pdflatex '+name

			#execute the command to create files
			os.system(command)

			# restore the previous directory
			os.chdir(current_directory)

			

	# converts the pdf files to png
	# @args  
	# latex_file_names      -> list of strings with name of LaTeX files
	# png_file_names        -> list of strings with name of PDF files
	# aux_file_names        -> list of strings with name of PNG files
	# log_file_names        -> list of strings with name of .log files
	# index                 -> number of the version
	# maintain_files        -> to maintain or not the .aux and .log files
	def __convert_pdf_to_png(self, latex_file_names, png_file_names, aux_file_names, log_file_names, index, maintain_files):

		current_directory = Path.cwd()

		for i in range(len(latex_file_names)):

			# sets the directory to the curresponding version
			os.chdir(self.__directory+str(index))

			# script of commands line to generate the PNG file 
			ghostscript_command = 'gs -r150 -dTextAlphaBits=4 -dGraphicsAlphaBits=4 -sDEVICE=png16m -o '+png_file_names[i]+' '+ latex_file_names[i]

			# execute command
			os.system(ghostscript_command)
		
			# remove .aux and .log files
			if not maintain_files:
				os.remove(aux_file_names[i])
				os.remove(log_file_names[i])

			# restore the previous directory
			os.chdir(current_directory)
