import os, csv

files_directory = "csv_index_files"

def remove_quotation_marks(file_directory):
    with os.scandir(files_directory) as files:
        for file in files:

            with open(file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                # for line in csv_reader:
                #     line.replace('"', "'")
                
                with open("new_file.csv", "w") as new_file:  
                    csv_writer = csv.writer(new_file, delimiter=',')
                    for line in csv_reader:
                        csv_writer.writerow(line)
            

remove_quotation_marks(files_directory)