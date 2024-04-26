try:
        with open ("my_file.txt", "w") as file :
                file.write("Hello, my name is Wanjiku line 1.\n") 
                file.write("19 years old is line 2.\n") 
                file.write("Python is Great! line 3.\n")
        print("File 'my_file.txt'created succesfully.")
except IOError:    
        print("Error:File'my_file.txt' not found.") 
except PermissionError:
        print("Error:Permission denied.")       

try:
        with open("non_existence_file.txt", "r")as file :
                content=file.read()
except IOError:
        print("\nError:File 'non_existence_file.txt'not found.") 
finally:
        print("\nScript execution completed.")  

try:
        with open("my_file.txt, 'a'")as file:
                file.write("Appending a new line!.\n") 
                file.write("Adding yet another line.\n")
                file.write("And one more for good measure.\n") 
        print("Additional lines appended succesfully.") 
except IOError:
        print(f"Error:File not found.")                                         
