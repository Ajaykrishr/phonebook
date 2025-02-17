

universal = {}

while 1:
    
    print("\n***** Please select an option *****\n")
    print("\n***** 1. Add    2. Update    3.View    4.View all    5.Delete User    6.Exit *****\n")
    choice = int(input("\nChoice: "))
    print("\n")
    
    if choice == 1:
        name = input("Enter the name of the person: ").lower()
        if not name.strip():
            continue
        universal.update({name:{}})
        copy = universal[name]
        copy.update({"name":name})
        
    
        email_count = int(input("How many email ids are going to be provided: "))

        
        copy.update({"email_ids":[]})
        
        for i in range(email_count):
            email = input(f"Enter email id {i+1}: ")
            copy["email_ids"].append(email)
            
        ph_count = int(input("Enter the number of phone numbers to be provided: "))
        copy.update({"contact_info":[]})
        
        for i in range(ph_count):
            phone = input(f"Enter phone number {i+1}: ")
            copy["contact_info"].append(phone)
            
        
        
    elif choice == 2:
           name_update = input("Enter the name of the person whose details you wish to change: ").lower()
           print("\n***** What detail would you like to update? *****\n")
           print("\n 1.Name   2.Email    3.Phone number \n")
           change_choice = int(input("\nChoice: "))
           print("\n")
           while 1:
               if change_choice == 0:
                   break
               if change_choice == 1:
                   
                   name_change = input("Enter new name: ").lower()
                   universal[name_update].update({"name":name_change})
                   universal[name_change] = universal[name_update] 
                   universal.pop(name_update)
                   name_update = name_change
                   break
           
               elif change_choice == 2:
                   while 1:
                    print("\n 1. Add another email \n")
                    print("\n 2. Modify an existing email id \n")
                    print("\n 3. Delete an existing email \n")
                    print("\n 4. Done \n")
                    email_choice = int(input("\nChoice: "))
                    print("\n")
                    
                    if email_choice == 1:
                        new_mail = input("Enter new email id: ")
                        universal[name_update].get("email_ids").append(new_mail)
                        
                    
                    elif email_choice == 4:
                        change_choice = 0
                        break
                    
                    elif email_choice == 3:
                        
                        while 1:
                            print("\n Which one of the following emails would you like to delete? \n")
                            
                            print("\n type -2 if you wish to cancel the operation. \n")
                            
                            for i in range(len(universal[name_update].get("email_ids"))):
                                emails = universal[name_update]["email_ids"][i]
                                print(f"{i+1}.{emails}")
                            email_choice1 = int(input("\nChoice: "))
                            print("\n")
                            
                            if email_choice1 > 0 and email_choice1 <= len(universal[name_update].get("email_ids")):
                                popped = universal[name_update]["email_ids"][email_choice1 - 1]
                                universal[name_update]["email_ids"].pop(email_choice1 - 1)
                                print(f"Deleted email id: {popped}")
                                break
                            
                            elif email_choice1 == -2:
                                break
                            break
                    
                    elif email_choice == 2:
                        while 1:
                            print("\n Which of the following emails would you like to edit? \n")
                            
                            print("\n type -2 if you wish to cancel the operation. \n")
                            
                            for i in range(len(universal[name_update].get("email_ids"))):
                                emails = universal[name_update]["email_ids"][i]
                                print(f"{i+1}.{emails}")
                            email_choice1 = int(input("\nChoice: "))
                            print("\n")
                            
                            if email_choice1 > 0 and email_choice1 <= len(universal[name_update].get("email_ids")):
                                new_mail1 = input(f"Enter new mail id to replace mail id {email_choice1}: ")
                                universal[name_update]["email_ids"][email_choice1 - 1] = new_mail1
                                break
                            
                            elif email_choice1 == -2:
                                break
                    
                               
                                
               elif change_choice == 3:
                   while 1:
                    print("\n 1. Add another phone number \n")
                    print("\n 2. Modify an existing phone number \n")
                    print("\n 3. Delete an existing phone number \n")
                    print("\n 4. Done \n")
                    phone_choice = int(input("\nChoice: "))
                    print("\n")
                    
                    if phone_choice == 1:
                        new_phone = input("Enter new phone number: ")
                        universal[name_update].get("contact_info").append(new_phone)
                        
                    
                    elif phone_choice == 4:
                        change_choice = 0
                        break
                    
                    elif phone_choice == 3:
                        
                        while 1:
                            print("\n Which one of the following phone numbers would you like to delete? \n")
                            
                            print("\n type -2 if you wish to cancel the operation. \n")
                            
                            for i in range(len(universal[name_update].get("contact_info"))):
                                phonezz = universal[name_update]["contact_info"][i]
                                print(f"{i+1}.{phonezz}")
                            phone_choice1 = int(input("\nChoice: "))
                            print("\n")
                                
                            if phone_choice1 > 0 and phone_choice1 <= len(universal[name_update].get("contact_info")):
                                popped = universal[name_update]["contact_info"][phone_choice1 - 1]
                                universal[name_update]["contact_info"].pop(phone_choice1 - 1)
                                print(f"Deleted phone number: {popped}")
                                break
                                
                            elif phone_choice1 == -2:
                                break
                            
                    
                    elif phone_choice == 2:
                        while 1:
                            print("\n Which of the following phone numbers would you like to edit? \n")
                            
                            print("\n type -2 if you wish to cancel the operation. \n")
                            
                            for i in range(len(universal[name_update].get("contact_info"))):
                                phonezz = universal[name_update]["contact_info"][i]
                                print(f"{i+1}.{phonezz}")
                                
                            phone_choice1 = int(input("\nChoice: "))
                            print("\n")
                                
                            if phone_choice1 > 0 and phone_choice1 <= len(universal[name_update].get("contact_info")):
                                    new_phone1 = input(f"Enter new phone number to replace phone number id {phone_choice1}: ")
                                    universal[name_update]["contact_info"][phone_choice1 - 1] = new_phone1
                                    break
                                
                            elif phone_choice1 == -2:
                                break
                    
                            
                                    
    elif choice == 3:
        print("\n Whose details would you like to view: \n")
        count = 1
        uni = list(universal)
        for i in range(len(universal)):
            print(f"{i+1}. {uni[i]}")
            count += 1
        person_choice = int(input("\nChoice: "))
        print("\n")
        if person_choice > 0 and person_choice <= len(universal):
            persona = uni[person_choice - 1]
            print(f"Name: {universal[persona]['name']}\n")
            email_list = universal[persona]["email_ids"]
            phone_list = universal[persona]["contact_info"]
            print("Email ids: ", end=" ")
            for i in email_list:
                print(i, end=",")
            print("\n")
            print("Phone numbers: ", end=" ")
            for i in phone_list:
                print(i, end=",")
            
        
    elif choice == 4:
        for i in universal.items():
            print("\n ***** \n")
            print(f"Name: {i[0]} \n")
            email_list = i[1]["email_ids"]
            phone_list = i[1]["contact_info"]
            
            print("Email ids: ", end=" ")
            for j in email_list:
                print(j, end=",")
            print("\n")
            print("phone numbers: ", end=" ")
            for k in phone_list:
                print(k, end=",")
            print("\n")
            print("\n ***** \n")
            print("\n")
            
    elif choice == 5:
        users = [i for i in universal]       
        print("Which of the following users do you wish to delete: ")
        for i in range(len(users)):
            print(f"{i+1}.{users[i]}")
        user_choice = int(input("Choice: "))
        if user_choice > 0 and user_choice <= len(universal):
            popped_user = users[user_choice - 1]
            universal.pop(users[user_choice - 1])
            print(f"Popped user {popped_user}.")
            
        
    else:
        break
                    
                
        
                           
                   
                      
        
    
        
        
