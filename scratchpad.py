
import os
import sys
import csv

try:

    csv_file = sys.argv[1]
    dir_path = sys.argv[2]
    sav_dir = sys.argv[3]


    with open(csv_file, newline="") as f:
        csv_path = []
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            csv_path.append(row['Path'])
    d = dir_path
    for path, currentDirectory,files in os.walk(d):
        for f in files:
            full_path = os.path.join(path,f)
            if full_path.lower() in csv_path:
                with open(os.path.join(dir_path,"in_csv.txt"), "a") as in_csv:
                    in_csv.write('{} in CSV_File\n'.format(full_path))
            else:
                with open(os.path.join(dir_path,"not_in_csv.txt"), "a") as not_in_csv:
                    not_in_csv.write('{} is not in CSV_File\n'.format(full_path))
except:
    print('incorrect syntax, correct syntax = \n python scratchpad.py <directory of CSV> <directory of the files>')

