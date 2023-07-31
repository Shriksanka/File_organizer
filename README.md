## File Organizer Python Script

This Python script helps organize files in a directory by moving them into specific folders based on their file formats. The script uses predefined mappings of file formats to directory names and scans the current working directory to identify files and their corresponding formats. It then moves each file to the appropriate folder according to its format.

### How It Works:

1. The script defines a dictionary called `DIRECTORIES`, where each key represents a folder name, and the corresponding value is a list of file formats that belong in that folder.

2. Another dictionary, `FILE_FORMATS`, is defined to invert the mapping in `DIRECTORIES`. It maps each file format to its corresponding folder name.

3. The main function `organize_junk()` is defined, which performs the file organization process.

4. The function uses `os.scandir()` to iterate through the files and directories in the current working directory.

5. For each entry in the directory, it checks if it is a file and extracts its file format using the `Path` object's `suffix` attribute.

6. If the file format matches any format in `FILE_FORMATS`, the function moves the file to the corresponding folder using the `rename` method of the `Path` object.

7. If a folder does not exist, the function creates it using the `mkdir` method with the `exist_ok=True` parameter to avoid errors if the folder already exists.

8. After organizing the files, the function attempts to remove any empty directories left in the working directory.

9. The script is executed using `if __name__ == "__main__":`, which calls the `organize_junk()` function to initiate the file organization process.

### How to Use:

1. Copy the provided Python script to the desired directory you want to organize.

2. Open a terminal or command prompt in the same directory.

3. Run the script using the command: `python script_name.py`

4. The script will automatically organize the files in the directory into specific folders based on their file formats.

This Python script is a handy utility to help keep your files organized and grouped by file format, making it easier to manage and locate files with similar formats.
