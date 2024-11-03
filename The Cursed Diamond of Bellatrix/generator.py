import random
import subprocess
def shuffle_spells(spells: list):
    list_length = len(spells)
    for i in range(list_length):
        random_index = random.randint(0, list_length - 1)
        temp = spells[i]
        spells[i] = spells[random_index]
        spells[random_index] = temp

file_path = './list of spells.txt'

with open(file_path, 'r') as file:
    spells_content = file.read()

spells_list = list(map(str.strip, spells_content.split("\n")))
total_tc = 15
tc_count = 0
base_file_name = f"./Test Cases"
shuffle_spells(spells=spells_list)
for i in range(total_tc):
    tc_count = i+1
    input_file_name = f"{base_file_name}/input{tc_count}.txt"
    output_file_name = f"{base_file_name}/output{tc_count}.txt"
    input_file = open(input_file_name,"w")
    input_file.write(f"{len(spells_list[i])}\n")
    input_file.write(f"{spells_list[i]}\n")
    with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
        subprocess.run(["soln.exe"], stdin=input_file, stdout=output_file, check=True)



