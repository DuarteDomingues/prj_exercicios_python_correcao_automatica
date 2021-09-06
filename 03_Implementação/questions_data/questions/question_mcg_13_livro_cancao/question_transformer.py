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
		


class QuestionTransformer(GenerateRandomVersion):

	# python_files_list -> name of the files (python) that wants to be changed
	# general_files_to_change_list -> name of the files (latex) that wants to be generated
	# num_versions -> number of verstions that wants to be created
	# output_index -> index of the output (1-question, 2-answer)
	def __init__(self, python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, repeat_seed=None):

		super().__init__(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, repeat_seed)
	
		self.__song = None
		self.__book = None
		self.__numpages = None
		self.__duration = None
		self.__repeated_seed = repeat_seed


	# makes the changes on the python files and adds to the lists created on the constructor
	# adds to the lists to be also known on the latex files the new numbers
	def create_python_program(self, python_files_list, version):

		list_python_programs = self.get_programs_python(python_files_list)

		books = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby", "One Hundred Years of Solitude", "In Cold Blood",
				 "Wide Sargasso Sea", "Brave New World", "I Capture The Castle", "Jane Eyre", "Crime and Punishment", "The Secret History",
				 "The Call of the Wild", "The Chrysalids", "Persuasion", "Moby-Dick", "To the Lighthouse", "A Byte of Pyhton", "Learning Python"]

		songs = ["Star Shopping", "Life is Beautiful", "16 Lines", "Falling down", "The brightside",
				 "Beamer boy", "Teen Romance", "U said", "Numb", "One Step Closer", "Castle of Glass",
				 "In the end", "Crawling", "Papercut", "What Ive done", "Somewhere I Belong", "Breaking the Habit", "Waiting for the end",
				 "Clocks", "Talk", "Forest Fires", "Dirt", "HDMI", "LooseScrew"]


		seed = random.choice(range(10000, 99999))
		self.__seed = seed

		# if is to repeat a created exercise
		if self.__repeated_seed != None:
			self.__seed = self.__repeated_seed
			seed = self.__repeated_seed
		
		random.seed(self.__seed)

		book = random.choice(books)
		song = random.choice(songs)

		numpages = random.randint(100,500)

		duration = round(random.uniform(2, 5),3)
		self.__book = book
		self.__song = song
		self.__numpages = numpages
		self.__duration = duration

		list_strings = ["A Byte of Pyhton", "Os putos", "150", "3", "x"]

		self.add_changable_strings(list_strings)

		change_all_occurrences(list_strings[0], book)
		change_all_occurrences(list_strings[1], song)
		change_token_all_occurrences(list_strings[2], str(numpages))
		change_token_all_occurrences(list_strings[3], str(duration))

		clear()

		return list_python_programs, seed

		
	# makes changes to latex files
	def create_latex_files(self, general_latex_files, version, output):

		latex_parts = self.get_text_files(general_latex_files)


		list_strings = [r'\verb+A Byte of Pyhton2+', r'\verb+A Byte of Pyhton+', r'\verb+150+', r'\verb+160+']

		self.add_changable_strings(list_strings)

		change_all_occurrences(r'\verb+A Byte of Pyhton2+', r'\verb+' +self.__song + '+')
		change_all_occurrences(r'\verb+150+', r'\verb+' +str(self.__numpages) + '+')
		change_all_occurrences(r'\verb+A Byte of Pyhton+', r'\verb+' +self.__book + '+')
		change_all_occurrences(r'\verb+160+', r'\verb+' +str(self.__duration) + '+')


		clear()

		return latex_parts

	