# Write a program to find len os string input from user and save the length to the file data.txt.
file = open("data.txt", 'a')
file.write("\n")
User_Input = input("Enter the String- ")
data = User_Input+","+str(len(User_Input))
file.write(data)
print("Data successfully written  :)")
file.close()
