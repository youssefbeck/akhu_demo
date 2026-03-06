current_credits = int(input("Enter your current credit total: "))
if current_credits >= 90: #yani talabani kamida 90 ta kretdi bolishi kerak
    standing = "Honours" #yani u shartni qoniqtirsa honors
else:
    standing = "Standard"  #qoniqtirmasa standart
print("Welcome! Current credits:", current_credits)
print("Standing:", standing)
while True: #yani bu cheksiz davom etadi biz breakni ishlatishimizga qadar
    print("[1] Enrol in module  [2] Drop module  [3] Check credits  [4] Exit") #menularni chqaradi
    choice = input("Your choice: ")
    if choice == "1":
        credits = int(input("Module credits: "))  #kiritgan modul kredtini olamiz
        if credits <= 0:
            print("Error: credit value must be positive.")  #nol yoki manfiy son invalid yani error chiqadi
        else:
            current_credits += credits  #current(total)ga qoshib boramiz
            print("Enrolled. New credit total:", current_credits)  #yani yangilangan total chiqadi
    elif choice == "2": #ayni bu qatordan bir keyingi modulga o'tamiz
        credits = int(input("Module credits to drop: "))  #yana kredit soraymiz
        if credits <= 0:
            print("Error: credit value must be positive.")  
        elif credits > current_credits:
            print(f"Cannot drop {credits} credits. Current total:", current_credits) 
        else:
            current_credits -= credits  
            print("Module dropped. New credit total:", current_credits)  #yangilangan totalni chiqaramiz

    elif choice == "3": #3- modulga o'tish
        print("Current credit total:", current_credits)  #hozirgi totalni chiqaramiz
    elif choice == "4": #4-modulga o'tish
        print("Goodbye! Final credit total:", current_credits)  #final kreditini chiqaramiz
        break  #va endi while ni tark etamiz
    else:
        print("Invalid choice. Please select a valid option.")  #yani agar notog'ri habar kiritilsa yani umuman boshqa narsalar kiritilssa 