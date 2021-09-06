from file_generator.helper import Helper
import os

class MergeFiles():

	# @args
	# file_names        -> list of the names for LaTeX files
	# directory         -> directory of the files, just need to add the number of the version on the end to access it
	# num_versions      -> number versions existing
	# remove_tex        -> flag if wants to keep the LaTeX used to build the PDF file with all the questions, False keep the file
	# add_new_line      -> flag to add the command \newline on the LaTeX, used when the output is just text, if it's code set False
	def __init__(self, file_names, directory, num_versions, remove_tex=True, add_new_line=True):

		latex_extension      = ".tex"

		# sets the attribute to variables
		self.__latex_files   = Helper().add_extension_list(file_names, latex_extension)
		self.__directory     = directory
		self.__num_versions  = num_versions
		self.__remove_tex    = remove_tex
		self.__add_new_line  = add_new_line

		# auxiliar variables to help build the file
		self.__current_dir   = os.getcwd()
		self.__file_name     = "result.tex"

		# LaTeX strings used to join all the files in one file 
		self.__original_type_latex    = r'\documentclass[12pt,varwidth=16cm,border=17pt]{standalone}'
		self.__new_type_latex         = r'\documentclass[a4paper]{article}'
		self.__begin_latex            = r"\begin{document}"
		self.__end_latex              = r"\end{document}"
		self.__purple_color_latex     = r"\definecolor{backbox}{RGB}{173,113,253}"
		self.__red_color_latex        = r"\definecolor{falsecolor}{RGB}{188, 84, 75}"
		self.__green_color_latex      = r"\definecolor{truecolor}{RGB}{93, 187, 99}"
		self.__new_line               = r"\newline"


	#returns the indexes from the beginning until the end of a small string inside a bigger one 
	# @args
	# big_str   -> big string which contains all the content
	# small_str -> small string that wants to find where it is on the bigger string and return the begin and end indexes
	def get_indexes_of_small_string(self, big_str, small_str):

		# when don't find the small string on the bigger one
		if big_str.find(small_str) == -1:
			return False

		index_str = 0
		start_index = 0
		end_index = 0
		for index in range(len(big_str)):
			#when found the whole string
			if index_str == len(small_str)-1:
				end_index = index
				break

			# found the index of current string
			if big_str[index] == small_str[index_str]:
				# set the beginning of thr string
				if index_str == 0:
					start_index = index
				index_str += 1

			# when the string is not equal
			else:
				index_str = 0

		return [start_index,end_index]

	# execute the join of all the files created and create a PDF file with all the content
	def execute(self):

		for index in range(1, self.__num_versions+1):

			# gets the string of latex question
			#path_to_question = self.__version_path+"/version_"+str(index)+"/"
			path_to_question = self.__directory+str(index)+"/"

			# gets the whole file of latex
			content_question = Helper().get_file_content(path_to_question+self.__latex_files[0])

			# trade the header to a better view of the file
			content_question = content_question.replace(self.__original_type_latex, self.__new_type_latex)

			# gets the first index of the end of end of document
			index_question = self.get_indexes_of_small_string(content_question, self.__end_latex)[0]

			# gets the whole document until the part that will suffer changes
			new_str = content_question[0:index_question].strip()+self.__purple_color_latex+self.__red_color_latex+self.__green_color_latex

			count = 1
			# loops over the answers
			for question_index in range(1, len(self.__latex_files )):

				# gets the whole file of answer
				content_answer = Helper().get_file_content(path_to_question+self.__latex_files[question_index])

				# gets the last index of the start document
				index_begin_answer =self.get_indexes_of_small_string(content_answer, self.__begin_latex)[1]

				# gets the first index of the end of end of answer
				index_end_answer = self.get_indexes_of_small_string(content_answer, self.__end_latex)[0]

				# gets the text of the question without newline
				text_question = "\n"+r"\noindent"+"\n"+content_answer[index_begin_answer+1:index_end_answer-1].strip()

				# adds a separator marker to facilitate the interpretation
				if question_index % 2 != 0:

					# adds the question to the file
					text_added = "\n"+r"\par\noindent\rule{\textwidth}{0.4pt}"+"\n"+r"\vspace{2mm}"+"\n"+r"\newline"+"\n"+r"\fcolorbox{backbox}{backbox}{\begin{minipage}{15em}"\
									+"\n"+r"\large"+"\n"+"Pergunta "+str(count)+"\n"+r"\end{minipage}}"+"\n"+r"\vspace{6mm}"+"\n"

					# adds the box saying it's true
					text_added += "\n"+r"\noindent"+"\n"+r"\fcolorbox{truecolor}{truecolor}{\begin{minipage}{8em}"+"\n"\
									+r"\large"+"\n"+"Verdadeiro"+"\n"+r"\end{minipage}}"+"\n"+r"\vspace{6mm}"+"\n"+self.__new_line

					if self.__add_new_line:
						text_question = text_added+text_question+self.__new_line+"\n"+self.__new_line+"\n"

					else:
						text_question = text_added+text_question

					count+=1

				else:
					# adds the box saying it's false
					text_added = "\n"+r"\noindent"+"\n"+r"\fcolorbox{falsecolor}{falsecolor}{\begin{minipage}{8em}"+"\n"+r"\large"+"\n"+r"Falso"+"\n"+r"\end{minipage}}"\
								+"\n"+r"\vspace{6mm}"+"\n"+self.__new_line

					if self.__add_new_line:
						text_question = text_added+text_question+"\n"+self.__new_line+"\n"
						
					else:
						text_question = text_added+text_question+"\n"


				# adds to the whole file
				new_str += text_question

			new_str += self.__end_latex

			Helper().write_to_file(path_to_question+self.__file_name, new_str)

			# change the dir to the question with a certain version
			os.chdir(path_to_question)

			command = 'pdflatex '+self.__file_name

			# converts the latex file to pdf
			os.system(command)

			os.remove("result.aux")
			os.remove("result.log")
			if self.__remove_tex:
				os.remove(self.__file_name)

			# return to the current dir
			os.chdir(self.__current_dir)
