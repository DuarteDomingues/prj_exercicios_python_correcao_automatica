str_python = "beauty"

for i in range (0, len(str_python)+1):

   num_spaces = len(str_python) -i
   print(" " * num_spaces + str_python[0:i])