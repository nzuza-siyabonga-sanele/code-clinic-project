import re, booking_system

# lists of information
STUDENT_NAME = []
STUDENT_EMAIL = []
STUDENT_PIN = []
CAMPUS = [] 
DATE = []
TIME = []

#TODO book a slot for student
def book_a_slot():
    
    # print('''FOR CAMPUS CHOOSE FROM THE FOLLOWING CAMPUSES :
    # [DURBAN, CAPE TOWN , JOHANNESBURG]''')
    
    print("STUDENT INFORMATION : \n")
    print("ENTER WTC STUDENT USERNAME :", end=" ")
    NAME = input().upper()
    if "HELP" in NAME:
        print(booking_system.help_commands()) 
    if "021" in NAME:
        if NAME in STUDENT_NAME:
            print("\n")
            return ("\t STUDENT ALREADY BOOKED.") 
        else:
            STUDENT_NAME.append(NAME)
    if "EXIT" in NAME:
        print("THANK YOU ! VISIT AGAIN.")
        run = False
        return run   
    while "021" not in NAME and "EXIT" not in NAME:
        # print("\t PLEASE ENTER VALID USERNAME.")
        print("ENTER WTC STUDENT USERNAME :", end=" ")
        NAME = input().upper()
        if "HELP" in NAME:
            print(booking_system.help_commands())
        if "021" in NAME:
            if NAME in STUDENT_NAME:
                print("\n")
                return ("\t STUDENT ALREADY BOOKED.") 
            else:
                STUDENT_NAME.append(NAME)
                break
        if "EXIT" in NAME:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run  
        
    print("ENTER STUDENT E-MAIL ID :", end=" ")
    EMAIL_ID = input().upper()
    if "HELP" in NAME:
        print(booking_system.help_commands()) 
    if EMAIL_ID.endswith("@STUDENT.WETHINKCODE.CO.ZA"):
        if EMAIL_ID.startswith(STUDENT_NAME[0]):
            if EMAIL_ID in STUDENT_EMAIL:
                print("\n")
                return ("\t STUDENT ALREADY BOOKED.") 
            else:
                STUDENT_EMAIL.append(EMAIL_ID)
            
        else:
            # print("\t PLEASE ENTER VALID STUDENT E-MAIL.")
            print("\t E-MAIL DOES NOT MATCH STUDENT USERNAME.")
            print("\t PRESS 1 : TO UPDATE STUDENT USERNAME./ level empty TO CHANGE STUDENT E-MAIL")
            OPTIONS = (input("ENTER YOUR OPTION : "))
            if OPTIONS == '1':
                print("ENTER 'OLD USERNAME' :", end=" ")
                OLD_NAME = input().upper()
                LOC_NAME = STUDENT_NAME.index(OLD_NAME)
                print("ENTER 'NEW USERNAME' :", end=" ")
                NEW_NAME = input().upper()
                STUDENT_NAME[LOC_NAME] = NEW_NAME
                print("\t 'USERNAME UPDATED SUCCESSFULLY.")
                print("\n")
                
             
    if "EXIT" in EMAIL_ID:
        print("THANK YOU ! VISIT AGAIN.")
        run = False
        return run 
    
    while EMAIL_ID.startswith(STUDENT_NAME[-1]) == False and "EXIT" not in NAME:
        # print("\t PLEASE ENTER VALID STUDENT E-MAIL.")
        print("ENTER STUDENT E-MAIL ID :", end=" ")
        EMAIL_ID = input().upper()
        if "HELP" in NAME:
            print(booking_system.help_commands()) 
        if EMAIL_ID.endswith("@STUDENT.WETHINKCODE.CO.ZA") == True:
            if EMAIL_ID.startswith(STUDENT_NAME[-1]):
                if EMAIL_ID in STUDENT_EMAIL:
                    print("\n")
                    return ("\t STUDENT ALREADY BOOKED.") 
                else:
                    STUDENT_EMAIL.append(EMAIL_ID)
                    break
            else:
                print("\t E-MAIL DOES NOT MATCH STUDENT USERNAME.")
                print("\t PRESS 1 : TO UPDATE STUDENT USERNAME./ LEVEL EMPTY TO CHANGE STUDENT E-MAIL")
                OPTIONS = (input("ENTER YOUR OPTION : "))
                if OPTIONS == '1':
                    print("ENTER 'OLD USERNAME' :", end=" ")
                    OLD_NAME = input().upper()
                    LOC_NAME = STUDENT_NAME.index(OLD_NAME)
                    print("ENTER 'NEW USERNAME' :", end=" ")
                    NEW_NAME = input().upper()
                    STUDENT_NAME[LOC_NAME] = NEW_NAME
                    print("\t 'USERNAME UPDATED SUCCESSFULLY.")
                    print("\n")
            
        if "EXIT" in EMAIL_ID:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
        
        
    print("ENTER 4 DIGTE CODE :", end=" ")
    PIN = (input())
    if "HELP" in NAME:
        print(booking_system.help_commands()) 
    if len(PIN) == 4:
        if PIN not in STUDENT_PIN:
            STUDENT_PIN.append(PIN)
    if "EXIT" in PIN:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
    while len(PIN) < 4 and "EXIT" not in NAME:
        PIN = input()
        if "HELP" in NAME:
            print(booking_system.help_commands()) 
        print("\t PLEASE ENTER VALID 4 DIGIT CODE.")
        if len(PIN) == 4:
            if PIN not in STUDENT_PIN:
                STUDENT_PIN.append(PIN)
                break
        if "EXIT" in EMAIL_ID:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
        
    # print("\t PLEASE ENTER VALID STUDENT CAMPUS [ DURBAN, CAPE TOWN , JOHANNESBURG ].")
    print("ENTER STUDENT CAMPUS :", end=" ")
    CAMP = ["DURBAN", "CAPE TOWN", "JOHANNESBURG"]
    CLASS = input().upper()
    if "HELP" in NAME:
        print(booking_system.help_commands()) 
    if CLASS in CAMP:
        CAMPUS.append(CLASS)
    if "EXIT" in CLASS:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run  
    while CLASS not in CAMP and "EXIT" not in NAME:
        # print("\t PLEASE ENTER VALID STUDENT CAMPUS.")
        print("ENTER STUDENT CAMPUS :", end=" ")
        CLASS = input().upper()
        if "HELP" in NAME:
            print(booking_system.help_commands()) 
        if CLASS in CAMP:
            CAMPUS.append(CLASS)
            break
        if "EXIT" in CLASS:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run    

        
    print("ENTER DATE FOR YOUR BOOKING FORMAT YYYY/MM/DD :", end=" ")
    USER_DATE = (input())
    if "HELP" in NAME:
        print(booking_system.help_commands()) 
    A = USER_DATE.split("/")
    B = []
    if len(A) == 3:
        count = 0
        for i in A:
            if count == 0:
                if (len(i) == 4) and (len(A[count])== 4) and int(A[count]) > 2021 and int(A[count]) < 2023 :
                    B.append(i)
            if count == 1:
                if (len(i) >= 1 and len(i)<3) and (len(A[count]) >= 1 and len(i)<3) and int(A[count]) <= 12:
                    B.append(i)
            if count == 2:
                if (len(i) >= 1 and len(i)<3) and (len(A[count]) >= 1 and len(i)<3) and int(A[count]) <= 31:
                    B.append(i) 
            count += 1
    if len(B) == 3 and "/" in USER_DATE:
        if USER_DATE in DATE:
            DATE.append(USER_DATE)
    if "EXIT" in USER_DATE:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run 
                
    while len(B) != 3 and "/" in USER_DATE and "EXIT" not in USER_DATE:
        # print("\t PLEASE ENTER VALID DATE FORMAT YYYY/MM/DD.")
        print("ENTER DATE FOR YOUR BOOKING FORMAT YYYY/MM/DD :", end=" ")
        USER_DATE = (input())
        if "HELP" in NAME:
            print(booking_system.help_commands()) 
        A = USER_DATE.split("/")
        B = []
        if len(A) == 3:
            count = 0
            for i in A:
                if count == 0:
                    if (len(i) == 4) and (len(A[count])== 4) and int(A[count]) > 2021 and int(A[count]) < 2023:
                        B.append(i)
                if count == 1:
                    if (len(i) >= 1 and len(i)<3) and (len(A[count]) >= 1 and len(i)<3) and int(A[count]) <= 12:
                        B.append(i)
                if count == 2:
                    if (len(i) >= 1 and len(i)<3) and (len(A[count]) >= 1 and len(i)<3) and int(A[count]) <= 31:
                        B.append(i) 
                count += 1
        if len(B) == 3 and "/" in USER_DATE:
            if USER_DATE in DATE:
                DATE.append(USER_DATE)
        if "EXIT" in USER_DATE:
                print("THANK YOU ! VISIT AGAIN.")
                run = False
                return run 
               
    print("ENTER TIME FOR YOUR BOOKING BETWEEN 8:00AM TO 17:30PM (TIME FORMAT 00:00) :", end=" ")
    USER_TIME = (input())
    if "HELP" in NAME:
        print(booking_system.help_commands()) 
    
    if len(USER_TIME) < 5:
            matched = re.match("[8-9][:][0-5][0-9]", USER_TIME)
            is_match = bool(matched)
    elif len(USER_TIME) > 4:
            matched = re.match("[0-1][0-7][:][0-5][0-9]", USER_TIME)
            is_match = bool(matched)
        
    if is_match == True:
        if USER_TIME in TIME:
            TIME.append(USER_TIME)
    if "EXIT" in USER_TIME:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
        
    while len(TIME) < 1 and "EXIT" not in USER_TIME:
        print("\t PLEASE ENTER VALID BOOKING TIME BETWEEN 8:00AM TO 17:30PM (TIME FORMAT 00:00) .")
        print("ENTER STUDENT TIME FOR BOOKING :", end=" ")
        USER_TIME = (input())
        if "HELP" in NAME:
            print(booking_system.help_commands()) 
        
        if len(USER_TIME) < 5:
            matched = re.match("[8-9][:][0-5][0-9]", USER_TIME)
            is_match = bool(matched)
        elif len(USER_TIME) > 4:
            matched = re.match("[0-1][0-7][:][0-5][0-9]", USER_TIME)
            is_match = bool(matched)
                
        if is_match == True:
            if USER_TIME in TIME:
                TIME.append(USER_TIME)
        if "EXIT" in USER_TIME:
                print("THANK YOU ! VISIT AGAIN.")
                run = False
                return run
    
           
    print("\n")
    return ("\t STUDENT INFORMATION ADDED SUCCESSFULLY FOR BOOKING.")