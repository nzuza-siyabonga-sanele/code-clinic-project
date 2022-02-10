import re, booking_system

# lists of information
STUDENT_NAME = []
STUDENT_EMAIL = []
STUDENT_PIN = []
PROBLEM = []
CAMPUS = [] 
DATE = []
TIME = []

#TODO book a slot for student
def book_a_slot():
    
    print("STUDENT INFORMATION REQUIED FOR BOOKINGS: \n")
    print("ENTER WTC STUDENT USERNAME :", end=" ")
    NAME = input().upper()
    if "HELP" == NAME  or "H" == NAME:
        print(booking_system.help_commands()) 
        
    if "quit" == NAME or "Q" == NAME:
        print("THANK YOU ! VISIT AGAIN.")
        run = False
        return run 
    
    if NAME in STUDENT_NAME:
        print("\n")
        return ("\t STUDENT ALREADY BOOKED.") 
    else:
        STUDENT_NAME.append(NAME)
      
    while "" != NAME and ("QUIT" != NAME or "Q" != NAME):
        print("ENTER WTC STUDENT USERNAME :", end=" ")
        NAME = input().upper()
        if "HELP" == NAME or "H" == NAME:
            print(booking_system.help_commands())

        if "QUIT" == NAME or 'Q' == NAME:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run  
        
        if NAME in STUDENT_NAME:
            print("\n")
            return ("\t STUDENT ALREADY BOOKED.") 
        else:
            STUDENT_NAME.append(NAME)
            break
        
        
    print("ENTER STUDENT E-MAIL ID :", end=" ")
    EMAIL_ID = input().upper()
    if "HELP" == EMAIL_ID or 'H' == EMAIL_ID:
        print(booking_system.help_commands())
        
    if "QUIT" == EMAIL_ID or 'Q' == EMAIL_ID:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run 
         
    if EMAIL_ID.endswith("@STUDENT.WETHINKCODE.CO.ZA"):
        if EMAIL_ID.startswith(STUDENT_NAME[0]):
            if EMAIL_ID in STUDENT_EMAIL:
                print("\n")
                return ("\t STUDENT ALREADY BOOKED.") 
            else:
                STUDENT_EMAIL.append(EMAIL_ID)
            
        else:
            print("\t E-MAIL DOES NOT MATCH STUDENT USERNAME.")
            print("\t PRESS 1 : TO UPDATE STUDENT USERNAME./ level empty TO CHANGE STUDENT E-MAIL")
            OPTIONS = (input("ENTER YOUR OPTION : "))
            if "HELP" == EMAIL_ID or 'H' == EMAIL_ID:
                print(booking_system.help_commands()) 
                
            if "QUIT" == EMAIL_ID or 'Q' == EMAIL_ID:
                print("THANK YOU ! VISIT AGAIN.")
                run = False
                return run 
            
            if OPTIONS == '1':
                print("ENTER 'OLD USERNAME' :", end=" ")
                OLD_NAME = input().upper()
                if "HELP" == EMAIL_ID or 'H' == EMAIL_ID:
                    print(booking_system.help_commands()) 
                    
                if "QUIT" == EMAIL_ID or 'Q' == EMAIL_ID:
                    print("THANK YOU ! VISIT AGAIN.")
                    run = False
                    return run 
                if OLD_NAME in STUDENT_NAME:
                    LOC_NAME = STUDENT_NAME.index(OLD_NAME)
                    print("ENTER 'NEW USERNAME' :", end=" ")
                    NEW_NAME = input().upper()
                    if "HELP" == EMAIL_ID or 'H' == EMAIL_ID:
                        print(booking_system.help_commands()) 
                        
                    if "QUIT" == EMAIL_ID or 'Q' == EMAIL_ID:
                        print("THANK YOU ! VISIT AGAIN.")
                        run = False
                        return run 
                    STUDENT_NAME[LOC_NAME] = NEW_NAME
                    if NEW_NAME in STUDENT_NAME:
                        print("\t 'USERNAME UPDATED SUCCESSFULLY.")
                        print("\n")
                else:
                    print("INPUT DOES NOT MATCH 'OLD USERNAME'!")
                
             
    if "quit" in EMAIL_ID or "Q" in EMAIL_ID:
        print("THANK YOU ! VISIT AGAIN.")
        run = False
        return run 
    
    while EMAIL_ID.startswith(STUDENT_NAME[-1]) == False and EMAIL_ID.endswith("@STUDENT.WETHINKCODE.CO.ZA") == False and ("quit" != EMAIL_ID or 'Q' != EMAIL_ID):
        # print("\t PLEASE ENTER VALID STUDENT E-MAIL.")
        print("ENTER STUDENT E-MAIL ID :", end=" ")
        EMAIL_ID = input().upper()
        if "HELP" == EMAIL_ID or 'H' == EMAIL_ID:
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
                print("\t PRESS 1 : TO UPDATE STUDENT USERNAME./ level empty TO CHANGE STUDENT E-MAIL")
                OPTIONS = (input("ENTER YOUR OPTION : "))
                if OPTIONS == '1':
                    print("ENTER 'OLD USERNAME' :", end=" ")
                    OLD_NAME = input().upper()
                    if OLD_NAME in STUDENT_NAME:
                        LOC_NAME = STUDENT_NAME.index(OLD_NAME)
                        print("ENTER 'NEW USERNAME' :", end=" ")
                        NEW_NAME = input().upper()
                        STUDENT_NAME[LOC_NAME] = NEW_NAME
                        if NEW_NAME in STUDENT_NAME:
                            print("\t 'USERNAME UPDATED SUCCESSFULLY.")
                            print("\n")
                    else:
                        print("INPUT DOES NOT MATCH 'OLD USERNAME'!")
                
        if "QUIT" == EMAIL_ID or 'Q' == EMAIL_ID:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
        
        
    print("ENTER 4 DIGTE CODE :", end=" ")
    PIN = (input())
    if "HELP" == PIN or 'H' == PIN:
        print(booking_system.help_commands()) 
    if len(PIN) == 4:
        if PIN not in STUDENT_PIN:
            STUDENT_PIN.append(PIN)
    if "QUIT" in PIN or "Q" in PIN:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
    while len(PIN) < 4 and ("QUIT" not in PIN  or "Q" not in PIN):
        PIN = input()
        if "HELP" in PIN or "H" in PIN:
            print(booking_system.help_commands()) 
        print("\t PLEASE ENTER VALID 4 DIGIT CODE.")
        if len(PIN) == 4:
            if PIN not in STUDENT_PIN:
                STUDENT_PIN.append(PIN)
                break
        if "QUIT" in PIN or "Q" in PIN:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
        
    # print("\t PLEASE ENTER VALID STUDENT CAMPUS [ DURBAN, CAPE TOWN , JOHANNESBURG ].")
    print("ENTER STUDENT CAMPUS :", end=" ")
    CAMP = ["DURBAN", "CAPE TOWN", "JOHANNESBURG"]
    CLASS = input().upper()
    if "HELP" in CLASS or "H" in CLASS:
        print(booking_system.help_commands()) 
    if CLASS in CAMP:
        CAMPUS.append(CLASS)
    if "QUIT" in CLASS or "Q" in CLASS:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run  
    while CLASS not in CAMP and ("QUIT" not in CLASS or "Q" not in CLASS):
        # print("\t PLEASE ENTER VALID STUDENT CAMPUS.")
        print("ENTER STUDENT CAMPUS :", end=" ")
        CLASS = input().upper()
        if "HELP" in CLASS or "H" in CLASS:
            print(booking_system.help_commands()) 
        if CLASS in CAMP:
            CAMPUS.append(CLASS)
            break
        if "QUIT" in CLASS or "Q" in CLASS:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run    

        
    print("ENTER DATE FOR YOUR BOOKING FORMAT YYYY/MM/DD :", end=" ")
    USER_DATE = (input())
    if "HELP" in USER_DATE or "H" in USER_DATE:
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
        DATE.append(USER_DATE)
    if "QUIT" in USER_DATE or "Q" in USER_DATE:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run 
                
    while len(B) != 3 and "/" in USER_DATE and ("QUIT" != USER_DATE or "Q" != USER_DATE):
        # print("\t PLEASE ENTER VALID DATE FORMAT YYYY/MM/DD.")
        print("ENTER DATE FOR YOUR BOOKING FORMAT YYYY/MM/DD :", end=" ")
        USER_DATE = (input())
        if "HELP" == USER_DATE or "H" == USER_DATE:
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
            DATE.append(USER_DATE)
        if "QUIT" in USER_DATE or "Q" in USER_DATE:
                print("THANK YOU ! VISIT AGAIN.")
                run = False
                return run 
               
    print("ENTER TIME FOR YOUR BOOKING BETWEEN 8:00AM TO 17:30PM (TIME FORMAT 00:00) :", end=" ")
    USER_TIME = (input())
    if "HELP" in USER_TIME or "H" in USER_TIME:
        print(booking_system.help_commands()) 
    
    if len(USER_TIME) < 5:
            matched = re.match("[8-9][:][0-5][0-9]", USER_TIME)
            is_match = bool(matched)
    elif len(USER_TIME) > 4:
            matched = re.match("[0-1][0-7][:][0-5][0-9]", USER_TIME)
            is_match = bool(matched)
        
    if is_match == True:
        if USER_TIME not in TIME:
            TIME.append(USER_TIME)
    if "QUIT" in USER_TIME or "Q" in USER_TIME:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
        
    while len(TIME) < 1 and ("QUIT" not in USER_TIME or "Q" not in USER_TIME):
        print("\t PLEASE ENTER VALID BOOKING TIME BETWEEN 8:00AM TO 17:30PM (TIME FORMAT 00:00) .")
        print("ENTER STUDENT TIME FOR BOOKING :", end=" ")
        USER_TIME = (input())
        if "HELP" in USER_TIME or "H" in USER_TIME:
            print(booking_system.help_commands()) 
        
        if len(USER_TIME) < 5:
            matched = re.match("[8-9][:][0-5][0-9]", USER_TIME)
            is_match = bool(matched)
        elif len(USER_TIME) > 4:
            matched = re.match("[0-1][0-7][:][0-5][0-9]", USER_TIME)
            is_match = bool(matched)
                
        if is_match == True:
            if USER_TIME not in TIME:
                TIME.append(USER_TIME)
        if "QUIT" in USER_TIME or "Q" in USER_TIME:
                print("THANK YOU ! VISIT AGAIN.")
                run = False
                return run
    
   
    print("ENTER MODULE SUPPORT REQUIRED :", end=" ")
    SUPPORT = input().upper()
    if "HELP" in SUPPORT or "H" in SUPPORT:
        print(booking_system.help_commands()) 
    if SUPPORT != '':
        PROBLEM.append(SUPPORT)
    while len(PROBLEM) < 1 and ("QUIT" not in SUPPORT or "Q" not in SUPPORT):
        print("\t PLEASE FILL IN THE MODULE SUPPORT REQUIRED.")
        print("ENTER MODULE SUPPORT REQUIRED :", end=" ")
        SUPPORT = input().upper()
        if "HELP" in SUPPORT or "H" in SUPPORT:
            print(booking_system.help_commands()) 
        if SUPPORT != '':
            PROBLEM.append(SUPPORT)
            break
        if "QUIT" in SUPPORT or "Q" in SUPPORT:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
           
    print("\n")
    return ("\t STUDENT INFORMATION ADDED SUCCESSFULLY FOR BOOKING.") 