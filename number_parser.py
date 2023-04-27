# import module
import PySimpleGUI as sg
import os
import pyperclip

# Define the PySimpleGUI layout for initiating a file
layout = [
    [sg.Text("Hi! I'm here to process your selected file and sort numbers within it.")],
    [sg.Text("Select a file to process:")],
    [sg.Input(), sg.FileBrowse()],
    [sg.Text("", size=(50, 1), key="file_path")],
    [sg.Button("Process File"), sg.Button("Exit")]
] 

# Create the PySimpleGUI window
window = sg.Window("Odd-Number Sorter", layout)

# Create a loop to process events and update the GUI
while True:
    event, values = window.read()

    # If the user clicks the "Exit" button or closes the window, exit the loop   
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    
    # If the user clicks the "Process File" button, execute the file processing
    if event == "Process File":
        # Open the selected file in read mode
        with open(values[0], "r") as num_file:
            content = num_file.read()

        # Split the contents into a list of integers
        numbers = [int(i) for i in content.split()]

        # Initialize two empty lists to store odd and even integers
        odd_int = []
        even_int = []

        # Sort each integer into the appropriate list based on parity
        for num in numbers:
            if num % 2 == 0:
                even_int.append(str(num))
            else:
                odd_int.append(str(num))

        # Create a string to display the even integers
        even_text = "EVEN INTEGERS\n\n" + "\n".join(even_int)

        # Create a string to display the odd integers
        odd_text = "ODD INTEGERS\n\n" + "\n".join(odd_int)

        # Update the file path text element with the selected file path
        window["file_path"].update(values[0])

        # Create a PySimpleGUI pop-up window to display the output
        output_layout = [
            [sg.Multiline(even_text, size=(30, 20)), sg.Multiline(odd_text, size=(30, 20))],
            [sg.Button("Save File"), sg.Button("OK")],
        ]
        output_window = sg.Window("Output", output_layout)

        # Wait for the user to close the output window
        while True:
            event, values = output_window.read()

            #If the user clicks the "Button", exit the loop
            if event == sg.WINDOW_CLOSED or event == "OK":
                break

            # If the user clicks the "Save File" button, write the output to a file
            if event == "Save File":   

                # Get the current working directory
                cwd = os.getcwd()

                # Specify the full file paths for the even and odd files
                even_file = os.path.join(cwd, "even.txt")
                odd_file = os.path.join(cwd, "odd.txt")

                # Update the file path text element with the selected file path
                window["file_path"].update(values[0])

                # Open and Write the even integers to the file
                with open("even.txt", "w") as num_file:
                    num_file.write("EVEN INTEGERS\n")
                    for num in even_int:
                        num_file.write(str(num) + "\n")

                    # Open and write the odd integers to the file
                with open("odd.txt", "w") as num_file:
                    num_file.write("ODD INTEGERS\n")
                    for num in odd_int:
                        num_file.write(str(num) + "\n")
                
                # Define the PySimpleGUI layout for the "File Saved" window
                file_saved_layout = [
                    [sg.Text("File saved successfully!", key ="saved")],
                    [sg.Button("OK")]
                ]
                # Create the PySimpleGUI window for the "File Saved" message
                file_saved_window = sg.Window("File Location", file_saved_layout)

                # Wait for the user to close the file saved window
                while True:
                    file_event, values = file_saved_window.read()
                    if file_event in (sg.WINDOW_CLOSED, "OK"):
                        break

                # Define the PySimpleGUI layout for file location
                visit_layout = [
                    [sg.Text(("File saved successfully!")],
                    [sg.Text("The files are located in the following directory:"), sg.Button('Copy Even'), sg.Button('Copy Odd')],
                    [sg.Text("", size=(80,1), key='filepath')],
                    [sg.Button("Visit Save Files", key="visit"), sg.Button("Exit")]
                ]
                
                # Create the PySimpleGUI window for file location
                visit_window = sg.Window('File Location', visit_layout)
                

                # Event loop to handle PySimpleGUI events for file location window
                while True:
                    visit_event, visit_values = visit_window.read()

                    # If the user selects "" button, 
                    if visit_event == sg.WIN_CLOSED or visit_event == "Exit":
                        break

                    elif visit_event == 'Copy Even':
                        path = os.path.dirname(os.path.abspath(__file__))
                        filepath = os.path.join(path, "even.txt")
                        pyperclip.copy(filepath)
                        sg.Popup('File path copied to clipboard!')
                        continue

                    elif visit_event == 'Copy Odd':
                        path = os.path.dirname(os.path.abspath(__file__))
                        filepath = os.path.join(path, "odd.txt")
                        pyperclip.copy(filepath)
                        sg.Popup('File path copied to clipboard!')
                        continue
                    
                    elif visit_event == 'visit':
                        # Open the directory where the files were saved
                        os.startfile(cwd)
                        break

                # Close the file saved window
                file_saved_window.close()
                # Close the output window
                visit_window.close()

        # Close the output window
        output_window.close()

# Close the main window
window.close()