from question_transformer import QuestionTransformer
from make_pdfs.files_generator import FilesGenerator
from make_pdfs.helper import Helper

python_files_list = [
    'program.py'
]


general_files_to_change_list = ['true_or_false_answer_1_true',
								'true_or_false_answer_1_false',
								'true_or_false_answer_2_true',
								'true_or_false_answer_2_false']

num_versions = 3


# output_index -> index of the output (0-question, 1-answer)
output_index = 0


# write the file with txt file (must have the questions on txt)
Helper().generate_latex_with_tex_files(general_files_to_change_list)

make_version = QuestionTransformer(python_files_list, general_files_to_change_list, num_versions, output_index)
make_version.make_versions()


# gets the directory used to create python and latex file
directory = make_version.directory
print(directory)


file_gen = FilesGenerator(general_files_to_change_list, directory=directory, num_versions=num_versions)
#file_gen = FilesGenerator(general_files_to_change_list, directory=directory, num_versions=num_versions, maintain_files= True)

file_gen.execute()