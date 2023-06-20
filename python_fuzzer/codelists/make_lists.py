# To make list from af part of the schematron document automatic

file = open("python_fuzzer//codelists//schematron.xml", "r")

names_list = []
codelist_list = []

Lines = file.readlines()
 
found_only_start_line = False
for line in Lines:
    if found_only_start_line:
        select = line.split(",")
        codelist_list.append(select[1:-1])
        found_only_start_line = False
    else:
        if "name=" in line and "select=" in line:
            select = line.split(",")
            codelist_list.append(select[1:-1])
            name = line.split("\"")[1]
            names_list.append(name)
        else:
            name = line.split("\"")[1]
            names_list.append(name)
            found_only_start_line = True

print(names_list)
print("-----------------------------")
print(codelist_list)