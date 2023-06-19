from os import listdir, remove
from os.path import isfile, join, curdir


onlyfiles = [f for f in listdir(curdir) if isfile(join(curdir, f))]
for file in onlyfiles:
    # if "FAIL" in file:
    #    remove(file)
    f = open(file, "r")
    fuck = False
    for line in f:
        if "FUCK"  in line:
            fuck = True
    if fuck:
        print(file)
