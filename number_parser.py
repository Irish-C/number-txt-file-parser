# import module
import PySimpleGUI as sg

# Define the PySimpleGUI layout
layout = [
    [sg.Text("Hi! I will process your selected file and sort numbers within it.")],
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

    # When the user clicks the "Exit" button or closes the window, exit the loop   
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    
    # If the user clicks the "Process File" button, execute the file
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
        output_window = sg.Window("File Processor Output", output_layout)

        # Wait for the user to close the output window
        while True:
            event, values = output_window.read()
            if event == sg.WINDOW_CLOSED or event == "OK":
                break

            # If the user clicks the "Save File" button, write the output to a file
            if event == "Save File":   

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

                # Display a message to the user that the file has been saved
                sg.popup("File saved successfully!", title="Save File")

        # Close the output window
        output_window.close()

# Close the main window
window.close()