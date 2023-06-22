# To make list from af part of the schematron document automatic

file = open("python_fuzzer//codelists//invoice_schematron.xml", "r")

names_list = []
codelist_list = []
attributes_list = []
attributes_names_list = []

Lines = file.readlines()
 
found_only_start_line = False
is_attrbute = False

for line in Lines:
    # If the codelist is on the next line
    if found_only_start_line:
        select = line.split(",")
        if is_attrbute:
            attributes_list.append(select[1:-1])
            is_attrbute = False
        else:
            codelist_list.append(select[1:-1])    

        found_only_start_line = False
    else:
        # If name and codelist is on the same line
        if "name=" in line and "select=" in line:
            
            name = line.split("\"")[1]
            select = line.split(",")
            # If it is for attributes
            if "_" in name:
                attributes_names_list.append(name)
                attributes_list.append(select[1:-1])
            else:
                names_list.append(name)
                codelist_list.append(select[1:-1])
            
        # If not on same line, save name and, make True
        else:

            name = line.split("\"")[1]
            # If it is for attributes
            if "_" in name:
                attributes_names_list.append(name)
                is_attrbute = True
            else:
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
        code_write_to = ["\"" + code + "\"," for code in codelist]
        file.writelines(code_write_to)
        file.write("],\n")
    file.write("]\n")

    file.write("attributes_names_list: List[str] = [")
    name_write_to = ["\"" + name + "\",\n" for name in attributes_names_list]
    file.writelines(name_write_to)
    file.write("]\n")

    file.write("attributes_list: List[List[str]] = [")
    for codelist in attributes_list:
        file.write("[")
        code_write_to = ["\"" + code + "\"," for code in codelist]
        file.writelines(code_write_to)
        file.write("],\n")
    file.write("]\n")
