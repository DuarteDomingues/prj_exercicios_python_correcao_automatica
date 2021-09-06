from questions.question_mdp2_19_fun_soma.question_transformer import QuestionTransformer
from file_generator.files_generator import FilesGenerator
from file_generator.helper import Helper
from file_generator.merge_files import MergeFiles
from file_generator.validator import Validator

directory_latex = "questions/question_mdp2_19_fun_soma/"

python_files_list = [
    'program.py'
]


# the question must be always the index 0
general_files_to_change_list = ['true_or_false_question',
								'true_or_false_answer_1_true',
								'true_or_false_answer_1_false']

num_versions = 3


# output_index -> index of the output (0-question, 1-answer)
output_index = 0

# folder where the question is going to be
version_path = "question_mdp2_19_fun_soma"



make_version = QuestionTransformer(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path)
#make_version = QuestionTransformer(python_files_list, general_files_to_change_list, directory_latex, num_versions, output_index, version_path, 29201)
make_version.make_versions()


# gets the directory used to create python and latex file
directory = make_version.directory
print(directory)



file_gen = FilesGenerator(general_files_to_change_list, directory, num_versions)
#file_gen = FilesGenerator(general_files_to_change_list, directory, num_versions, maintain_files= True)
file_gen.execute()


merge_latex_file = MergeFiles(general_files_to_change_list, directory, num_versions)
# gets all the latex files and merge them and create a pdf file with them
merge_latex_file.execute()


validator = Validator(python_files_list, directory, num_versions)
validator.execute()