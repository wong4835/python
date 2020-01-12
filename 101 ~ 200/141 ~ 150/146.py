filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in filenames :
    if file.split('.')[1] == "h" :
        print(file)
for file in filenames :
    if file.split('.')[1] == "c" :
        print(file)
