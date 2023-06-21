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


with open("python_fuzzer//codelists//schematron.txt", "w", encoding="utf-8") as file:
    file.write("names_list: List[str] = [")
    name_write_to = ["\"" + name + "\",\n" for name in names_list]
    file.writelines(name_write_to)
    file.write("]\n")

    file.write("codelist_list: List[List[str]] = [")
    for codelist in codelist_list:
        file.write("[")
        code_write_to = ["\"" + code + ",\"" for code in codelist]
        file.writelines(code_write_to)
        file.write("],\n")
    file.write("]\n")
