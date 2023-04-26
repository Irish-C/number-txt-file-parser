# import module
import PySimpleGUI as sg

# Define the PySimpleGUI layout

# Create the PySimpleGUI window

# Create a loop to process events and update the GUI

    # When the user clicks the "Process File" button, execute the file processing code

    # When the user clicks the "Exit" button or closes the window, exit the loop

        # Open the selected file in read mode

        # Split the contents into a list of integers

        # Initialize two empty lists to store odd and even integers

        # Sort each integer into the appropriate list based on parity

        # Create a string to display the even integers

        # Create a string to display the odd integers

        # Update the file path text element with the selected file path

        # Create a PySimpleGUI pop-up window to display the output

        # Wait for the user to close the output window

        # Close the output window

            # If the user clicks the "Save File" button, write the output to a file
            
                # Open a new file for writing
                
                    # Write the even integers to the file

                    # Write the odd integers to the file

                # Display a message to the user that the file has been saved



# CODE FOR THE MAIN OBJECTIVES
# # Open the text file "numbers.txt" in read mode
# with open("numbers.txt", "r") as num_file:
#     content = num_file.read()

# #split content into list of integers
# numbers = [int(i) for i in content.split()]

# # Create two empty lists to store: odd and even integers
# odd_int = []
# even_int = []

# # Check and sort each integer into the two empty lists
# for num in content:
#     if num % 2 == 0:
#         even_int.append(str(num))
#     else:
#         odd_int.append(str(num))

# # Create a text file "odd.txt" to write even integers
# with open("even.txt", "w") as num_file:
#     num_file.write("EVEN INTEGERS\n")
#     for num in even_int:
#         num_file.write(str(num) + "\n")

# # Create a text file "even.txt" to write odd integers
# with open("odd.txt", "w") as num_file:
#     num_file.write("ODD INTEGERS\n")
#     for num in odd_int:
#         num_file.write(str(num) + "\n")