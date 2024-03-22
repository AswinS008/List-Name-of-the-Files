import os

def list_files_in_folder_and_save(folder_path, output_file):
    try:
        # Get a list of all files in the specified folder
        files = os.listdir(folder_path)

        # Save file names to a text file
        with open(output_file, 'w') as file:
            for file_name in files:
                file.write(file_name + '\n')

        print(f"File names saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"The folder '{folder_path}' does not exist.")
    except PermissionError:
        print(f"Permission error while accessing the folder '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_folder_path' with the actual path of the folder you want to list
folder_path = 'D:\Dolby\IMAX'

# Replace 'output.txt' with the desired name for the output text file
output_file = 'output.txt'

list_files_in_folder_and_save(folder_path, output_file)
