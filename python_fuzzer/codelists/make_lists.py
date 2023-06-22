# To make list from af part of the schematron document automatic

file = open("python_fuzzer//codelists//invoice_schematron.xml", "r")

names_list = []
codelist_list = []

Lines = file.readlines()

is_attribute = False
found_only_start_line = False
for line in Lines:
    if found_only_start_line:
        select = line.split("\'")
        select = select[1]
        select = select.split(",")
        if len(select) != 1 and not is_attribute:
            select = select[1:-1]
        codelist_list.append(select)
        is_attribute = False
        found_only_start_line = False
    else:
        if "name=" in line and "select=" in line:
            name = line.split("\"")[1]
            select = line.split("\'")
            select = select[1]
            select = select.split(",")
            if len(select) != 1 and "_" not in name:
                select = select[1:-1]
            codelist_list.append(select)
            names_list.append(name)
        else:
            name = line.split("\"")[1]
            if "_" in name:
                is_attribute = True
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