

STUDENT_NAME = []
STUDENT_ROLL_NUMBER = []
STUDENT_ADDRESS = []
STUDENT_EMAIL = []
STUDENT_AGE = []
STUDENT_MOBILE_NUMBER = []
STUDENT_CLASS = []



def ADD_STUDENT_INFORMATION():
        
    print("ADDING STUDENT INFORMATION : \n")
    print("ENTER STUDENT USERNAME :", end=" ")
    NAME = input().upper()
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
        print("\t PLEASE ENTER VALID USERNAME.")
        print("ENTER STUDENT USERNAME :", end=" ")
        NAME = input().upper()
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
        
                  
    print("PLEASE ENTER VALID DATE FORMAT YYYY/MM/DD.")
    print("ENTER STUDENT DATE :", end=" ")
    ROLL_NUMBER = (input())
    A = ROLL_NUMBER.split("/")
    B = []
    if len(A) == 3:
        count = 0
        for i in A:
            if count == 0:
                if (len(i) == 4) and (len(A[count])== 4):
                    B.append(i)
            if count == 1:
                if (len(i) >= 1 and len(i)<3) and (len(A[count]) >= 1 and len(i)<3) and int(A[count]) <= 12:
                    B.append(i)
            if count == 2:
                if (len(i) >= 1 and len(i)<3) and (len(A[count]) >= 1 and len(i)<3) and int(A[count]) <= 31:
                    B.append(i) 
            count += 1
    if len(B) == 3 and "/" in ROLL_NUMBER:
        if ROLL_NUMBER in STUDENT_ROLL_NUMBER:
            print("\n")
            return ("\t STUDENT ALREADY BOOKED.") 
        else:
            STUDENT_ROLL_NUMBER.append(ROLL_NUMBER)
    if "EXIT" in ROLL_NUMBER:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run 
                
    while len(A) != 3 and len(B) == 3 and "/" in ROLL_NUMBER and int(A[count]) < 2021 and "EXIT" not in NAME:
        print("PLEASE ENTER VALID DATE FORMAT YYYY/MM/DD.")
        print("ENTER STUDENT DATE :", end=" ") 
        ROLL_NUMBER = (input())
        A = ROLL_NUMBER.split("/")
        B = []
        if len(A) == 3:
            count = 0
            for i in A:
                if count == 0:
                    if (len(i) == 4) and (len(A[count])== 4) and int(A[count]) > 2021:
                        B.append(i)
                if count == 1:
                    if (len(i) >= 1 and len(i)<3) and (len(A[count]) >= 1 and len(i)<3) and int(A[count]) < 12:
                        B.append(i)
                if count == 2:
                    if (len(i) >= 1 and len(i)<3) and (len(A[count]) >= 1 and len(i)<3) and int(A[count]) < 32:
                        B.append(i) 
                count += 1
        if len(B) == 3 and "/" in ROLL_NUMBER:
            if ROLL_NUMBER in STUDENT_ROLL_NUMBER:
                print("\n")
                return ("\t STUDENT ALREADY BOOKED.") 
            else:
                STUDENT_ROLL_NUMBER.append(ROLL_NUMBER)
                break
        if "EXIT" in ROLL_NUMBER:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run  
                
######################################################################################
    print("ENTER STUDENT AGE :", end=" ")
    AGE = int(input())
    STUDENT_AGE.append(AGE)

    print("ENTER STUDENT CAMPUS :", end=" ")
    CAMP = ["DURBAN", "CAPE TOWN", "JOHANNESBURG"]
    CLASS = input().upper()
    if CLASS in CAMP:
        STUDENT_CLASS.append(CLASS)
    if "EXIT" in CLASS:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run  
    while CLASS not in CAMP and "EXIT" not in NAME:
        print("\t PLEASE ENTER VALID STUDENT CAMPUS.")
        print("ENTER STUDENT CAMPUS :", end=" ")
        CLASS = input().upper()
        if CLASS in CAMP:
            if CLASS in STUDENT_CLASS:
                print("\n")
                return ("\t STUDENT ALREADY BOOKED.") 
            else:
                STUDENT_CLASS.append(CLASS)
                break
        if "EXIT" in CLASS:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run    

###########################################################################################
    print("ENTER STUDENT E-MAIL ID :", end=" ")
    EMAIL_ID = input().upper()
    if EMAIL_ID.endswith("@STUDENT.WETHINKCODE.CO.ZA"):
        if EMAIL_ID.startswith(STUDENT_NAME[0]):
            if EMAIL_ID in STUDENT_EMAIL:
                print("\n")
                return ("\t STUDENT ALREADY BOOKED.") 
            else:
                STUDENT_EMAIL.append(EMAIL_ID)
            
        else:
            print("\t PLEASE ENTER VALID STUDENT E-MAIL.")
            print("E-MAIL DOES NOT MATCH STUDENT USERNAME.")
            print("PRESS 1 : TO UPDATE STUDENT USERNAME./ level empty TO CHANGE STUDENT E-MAIL")
            OPTIONS = (input("ENTER YOUR OPTION : "))
            if OPTIONS == '1':
                print("ENTER 'OLD NAME' :", end=" ")
                OLD_NAME = input().upper()
                LOC_NAME = STUDENT_NAME.index(OLD_NAME)
                print("ENTER 'NEW NAME' :", end=" ")
                NEW_NAME = input().upper()
                STUDENT_NAME[LOC_NAME] = NEW_NAME
                print("\t 'NAME UPDATED SUCCESSFULLY.")
                print("\n")
                
        if EMAIL_ID.startswith(STUDENT_NAME[-1]):
            if EMAIL_ID in STUDENT_EMAIL:
                print("\n")
                return ("\t STUDENT ALREADY BOOKED.") 
            else:
                STUDENT_EMAIL.append(EMAIL_ID)
                
            

    if "EXIT" in EMAIL_ID:
        print("THANK YOU ! VISIT AGAIN.")
        run = False
        return run 
    while EMAIL_ID.startswith(STUDENT_NAME[0]) == False and "EXIT" not in NAME:
        print("\t PLEASE ENTER VALID STUDENT E-MAIL.")
        print("ENTER STUDENT E-MAIL ID :", end=" ")
        EMAIL_ID = input().upper()
        if EMAIL_ID.endswith("@STUDENT.WETHINKCODE.CO.ZA") == True:
            if EMAIL_ID.startswith(STUDENT_NAME[-1]):
                if EMAIL_ID in STUDENT_EMAIL:
                    print("\n")
                    return ("\t STUDENT ALREADY BOOKED.") 
                else:
                    STUDENT_EMAIL.append(EMAIL_ID)
                    break
            else:
                print("E-MAIL DOES NOT MATCH STUDENT USERNAME.")
                print("PRESS 1 : TO UPDATE STUDENT USERNAME./ LEVEL EMPTY TO CHANGE STUDENT E-MAIL")
                OPTIONS = (input("ENTER YOUR OPTION : "))
                if OPTIONS == '1':
                    print("ENTER 'OLD NAME' :", end=" ")
                    OLD_NAME = input().upper()
                    LOC_NAME = STUDENT_NAME.index(OLD_NAME)
                    print("ENTER 'NEW NAME' :", end=" ")
                    NEW_NAME = input().upper()
                    STUDENT_NAME[LOC_NAME] = NEW_NAME
                    print("\t 'NAME UPDATED SUCCESSFULLY.")
                    print("\n")
        if EMAIL_ID.startswith(STUDENT_NAME[-1]):
            if EMAIL_ID in STUDENT_EMAIL:
                print("\n")
                return ("\t STUDENT ALREADY BOOKED.") 
            else:
                STUDENT_EMAIL.append(EMAIL_ID)
                break
            
        if "EXIT" in EMAIL_ID:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
        
    ###########################################################################################

    print("ENTER MODULE SUPPORT REQUIRED :", end=" ")
    SUPPORT = input().upper()
    STUDENT_ADDRESS.append(SUPPORT)
    
    print("ENTER STUDENT MOBILE NUMBER :", end=" ")
    MOBILE_NUMBER = (input())
    if len(MOBILE_NUMBER) == 10:
        if MOBILE_NUMBER in STUDENT_MOBILE_NUMBER:
            print("\n")
            return ("\t STUDENT ALREADY BOOKED.") 
        elif MOBILE_NUMBER not in STUDENT_MOBILE_NUMBER:
            STUDENT_MOBILE_NUMBER.append(MOBILE_NUMBER)
    if "EXIT" in EMAIL_ID:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
    while len(MOBILE_NUMBER) < 10 and "EXIT" not in NAME:
        MOBILE_NUMBER = input()
        print("\t PLEASE ENTER VALID TEN DIGIT MOBILE NUMBER.")
        if len(MOBILE_NUMBER) == 10:
            if MOBILE_NUMBER in STUDENT_MOBILE_NUMBER:
                print("\n")
                return ("\t STUDENT ALREADY BOOKED.") 
            elif MOBILE_NUMBER not in STUDENT_MOBILE_NUMBER:
                STUDENT_MOBILE_NUMBER.append(MOBILE_NUMBER)
                break
        if "EXIT" in EMAIL_ID:
            print("THANK YOU ! VISIT AGAIN.")
            run = False
            return run
        
    ###########################################################################################
    print("\n")
    return ("\t STUDENT INFORMATION ADDED SUCCESSFULLY.")


print("\n")

print("' ********** WELCOME TO REORD INFORMATION SYSTEM ********** ' \n")
run = True
while run:
    print("PRESS FROM THE FOLLOWING OPTION : \n")

    print("PRESS 1 : TO ADD STUDENT INFORMATION.")
    print("PRESS 2 : TO DELETE STUDENT INFORMATION.")
    print("PRESS 3 : TO UPDATE STUDENT INFORMATION.")
    print("PRESS 4 : TO DISPLAY STUDENT INFORMATION.")
    print("PRESS 5 : TO EXIT SYSTEM.")

    OPTION = int(input("ENTER YOUR OPTION : "))
    print("\n")
    print(end="\n")

    if OPTION == 1:
        run = ADD_STUDENT_INFORMATION()
        print(run)
        print("\n")
    # elif OPTION == 2:
    #     SMS.DELETE_STUDENT_INFORMATION()
    # elif OPTION == 3:
    #     SMS.UPDATE_STUDENT_INFORMATION()
    # elif OPTION == 4:
    #     SMS.DISPLAY_STUDENT_INFORMATION()
    # elif OPTION == 5:
    #     print("THANK YOU ! VISIT AGAIN.")
    #     run = False
    else:
        print("PLEASE CHOOSE CORRECT OPTION FROM THE FOLLOWING.")
        print("\n")

