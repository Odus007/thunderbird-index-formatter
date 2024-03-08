import os, csv

files_directory = "csv_index_files"

# Function to format the csv files to split choose and then split the name and email address + clean it up
def format_csv(file_directory):
    # Loop through the files in the csv_index_files directory
    with os.scandir(files_directory) as files:
        for file in files:
            if file.is_file():  # Ensure we're dealing with a file
                # Create a list to store modified lines
                modified_lines = []

                # Open the file and read the lines
                with open(file, 'r', newline = '') as csv_file:
                    csv_reader = csv.reader(csv_file)

                    # Loop through the lines in the file
                    for line in csv_reader:
                        if len(line) > 1:  # Ensure there's at least an email column
                            sender_info = line[1].strip() # Get the name and email address

                            # Split the name and email address
                            sender_info = sender_info.split("<")

                            # Clean up the email address & name. Also ensure the split was successful
                            if len(sender_info) > 1:
                                name = sender_info[0].strip()
                                email = sender_info[1].replace(">", "").strip()
                                combined_info = f"{name}, {email}"
                                modified_lines.append([combined_info])
                            
                            #print(modified_lines)

                # Write the modified lines (with only the cleaned email addresses) to a temporary file
                temp_file_path = f"{file.path}_tmp"
                with open(temp_file_path, 'w', newline='') as temp_file:
                    csv_writer = csv.writer(temp_file)
                    csv_writer.writerows(modified_lines)
                
                # Replace the original file with the temporary file
                os.replace(temp_file_path, file.path)
            
# Call the function to format the csv files
format_csv(files_directory)