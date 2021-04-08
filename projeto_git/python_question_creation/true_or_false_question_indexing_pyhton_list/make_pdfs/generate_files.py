from answers_program import questions
from files_generator import FilesGenerator


file_names = ['answer_1_true',
			  'answer_1_false',
			  'answer_2_true',
			  'answer_2_false']


#file_gen = FilesGenerator(file_names, text_files = True)
file_gen = FilesGenerator(file_names, list_questions = questions)
#file_gen = FilesGenerator(file_names, list_questions = questions, maintain_files= True)
#file_gen = FilesGenerator(file_names, text_files = True, maintain_files= True)
#file_gen = FilesGenerator(file_names)

file_gen.execute()