import os
import subprocess

# Directory containing the files
input_directory = input("Enter the path to the input directory: ")
output_directory = input("Enter the path to the output directory: ")
series_name = input("Enter the series name: ")
author_name = input("Enter the author name: ")

# Iterate over all files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".cbz"):
        # Construct the full file path
        file_path = os.path.join(input_directory, filename)

        # Construct the command
        command = [
            "python3",
            "kcc-c2e.py",
            file_path,
            "-p",
            "KPW5",
            "-m",
            "-u",
            "-s",
            "-r",
            "2",
            "-o",
            output_directory,
            "-f",
            "MOBI",
            "--metadata",
            f"series={series_name};author={author_name}",
        ]

        # Call the command
        subprocess.run(command)
