#Sushant Sushant
#22077514

phoneDirectory= {}
#phoneDirectory is a dictionary.


#printing the greeting message.
print("WELCOME TO THE GRANN'S PHONE DIRECTORY.")

option=0
#taking the options for the menu.
while(option!=4):
  print("MENU")
  print("1. Add a Record. ")
  print("2. Search a Record. ")
  print("3. Update a Record.")
  print("4. Delete a Record.")
  print("5. Quit.")


  option = int(input("Enter your choice: "))
  
#giving the commands for the working of options.
  
  if option == 1:
      #name = input for name  :  phone =  input for phone number.
        
        name = input("Enter Name: ") 
  #making sure that the user enters the name in alphabetical methods.
        if not name.isalpha():
          print("Error: Your name is not correct.")
        phone = input("Enter your 10-digit phone number: ")
      #adding the contact details to the dictionary.
        phoneDirectory[name] = phone
        print("Record added.")
      
    
  elif option == 2:
     #search = input for name to be searched.
       search= input("Enter name to search: ")
     #searching the products in the cart 
       if search in phoneDirectory:
            b= phoneDirectory[search]
     #printing the output
            print(search,":",phoneDirectory[name])
  #if contact enterted is not in the phone directory then it will show
       else:
            print("No contact exists with this name.")
         
  
  elif option == 3:
    
      #cn= input for contact's name to be changed. 
        cn= input("Enter name: ")
      #entering the new 10-digit phone number.
        change = int(input("Enter new 10-digit phone number: "))
      #updating the contact number in phoneDirectory.
        phoneDirectory[change] = cn
        print("Record updated.")
       
  elif option == 4:

    #delete= input for the name which ius to be deleted from dictionary.
         delete = input("Enter name: ")
    #finding the name of the contact to be deleted in dictionary.
         if delete in phoneDirectory:
    #deleting the contact from the dictionary.
            del phoneDirectory[delete]
            print("Record deleted")
#if the given name is not in the dictionary then print Record not found.
         else:
            print("Record not found")

#quitting the program
  elif option == 5:
      print("Quitting")
