# number-txt-file-parser
A Python script that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt.

# Installation
To run the program, you'll need to have [Python 3](https://www.python.org/downloads/) installed on your computer.
**Note: I used [VS Code](https://code.visualstudio.com/download) to create and run the program.**

# Dependencies
The script requires the following Python packages:

* I. PySimpleGUI
* II. pyperclip

````Use pip install PySimple````

# How the code works
1. Clone the repository or download the odd_number_sorter.py file.
2. Open a terminal and navigate to the directory containing the script:
```cd /path/to/directory```
3. Run the script using python:
````python odd_number_sorter.py````
4. When prompted, use the "Browse" button to select the file to process.
5. To sort the odd and even integers in the file, click the "Process File" button.
6. While the script is processing the file, a loading bar will show.
7. When the processing is finished, the even and odd numbers will be shown in separate text boxes. By pressing the "Save File" option, you can save them as independent text files.
9. Click the "Copy Even" or "Copy Odd" buttons to transfer the contents of the even or odd text boxes to the clipboard.
10. Click the "Exit" button or close the window to exit the script.