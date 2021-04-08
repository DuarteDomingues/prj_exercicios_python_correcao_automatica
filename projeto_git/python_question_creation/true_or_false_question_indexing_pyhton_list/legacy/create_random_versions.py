import os
from random import choice
from random import randint
from random import seed

version_path_prefix = "question/version_"
write_seed_flag=True
seed_filename="seed.txt"


def write_to_file(filename, content):

    with open(filename, "w") as file:
        file.write(content)

def write_seed(a_seed, version_path, seed_filename):

    filename = os.path.join(version_path, seed_filename)
    content  = str(a_seed)

    write_to_file(filename, content)


def read_seed(version_path, seed_filename):

    filename = os.path.join(version_path, seed_filename)

    with open(filename, "r") as file:
        content = file.read()

    return int(content)



def create_versions(number_of_versions):

    
    for version in range(number_of_versions):

        #creates directories (version_version) for each version
        version_path = version_path_prefix + str(version +1)
        if not os.path.exists(version_path):
            os.makedirs(version_path)

        #generates a random seed, and writes the seed in the file
        if write_seed_flag == True:
            a_seed = randint(1000, 9999)
            write_seed(a_seed, version_path, seed_filename)
        else:
            a_seed = read_seed(version_path, seed_filename)
        
        seed(a_seed)





        
# To create directorys and write a seed file randomly on text file
#create_versions(2)
