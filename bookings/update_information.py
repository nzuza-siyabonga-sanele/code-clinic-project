import bookings.student_booking



# THIS FUNCTION HELP TO 'UPDATE' DATA OF STUDENT.
def update_bookings_volunteer():
    print("UPDATE STUDENT INFORMATION : \n")

    if len(bookings.student_booking.STUDENT_NAME) == 0 and len(bookings.student_booking.DATE) == 0 and len(bookings.student_booking.TIME) == 0 and len(
            bookings.student_booking.CAMPUS) == 0 and len(bookings.student_booking.STUDENT_PIN) == 0 and len(bookings.student_booking.PROBLEM) == 0 and len(
            bookings.student_booking.STUDENT_EMAIL) == 0:
        # print("\n")
        print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY\n")
        run = True
        return run
    else:
        print("ENTER STUDENT ATTRIBUTE YOU WANT TO update :", end="\n")
        print("LIKE 'USERNAME, ROLL NUMBER, AGE, MOBILE NUMBER, ADDRESS, EMAIL, CLASS.")
        print("ENTER HERE :", end=" ")
        ATTRIBUTE = input().upper()

        if ATTRIBUTE == 'NAME':
            print("ENTER 'OLD NAME' :", end=" ")
            OLD_NAME = input().upper()
            LOC_NAME = bookings.student_booking.STUDENT_NAME.index(OLD_NAME)

            print("ENTER 'NEW NAME' :", end=" ")
            NEW_NAME = input().upper()
            bookings.student_booking.STUDENT_NAME[LOC_NAME] = NEW_NAME
            print("\t 'NAME UPDATED SUCCESSFULLY.\n")


        elif ATTRIBUTE == 'ROLL NUMBER':
            print("ENTER 'OLD ROLL NUMBER' :", end=" ")
            OLD_USER_DATE = int(input())
            LOC_ROLL = bookings.student_booking.DATE.index(OLD_USER_DATE)

            print("ENTER 'NEW ROLL NUMBER' :", end=" ")
            NEW_ROLL = int(input())
            bookings.student_booking.DATE[LOC_ROLL] = NEW_ROLL
            print("\t 'ROLL NUMBER UPDATED SUCCESSFULLY.\n")

        elif ATTRIBUTE == 'AGE':
            print("ENTER 'OLD AGE' :", end=" ")
            OLD_AGE = int(input())
            LOC_ROLL = bookings.student_booking.TIME.index(OLD_AGE)

            print("ENTER 'NEW AGE' :", end=" ")
            NEW_AGE = int(input())
            bookings.student_booking.TIME[LOC_ROLL] = NEW_AGE
            print("\t 'AGE UPDATED SUCCESSFULLY.\n")

        elif ATTRIBUTE == 'ADDRESS':
            print("ENTER 'OLD ADDRESS' :", end=" ")
            OLD_ADDRESS = input()
            LOC_ADDRESS = bookings.student_booking.PROBLEM.index(OLD_ADDRESS)

            print("ENTER 'NEW ADDRESS' :", end=" ")
            NEW_ADDRESS = input()
            bookings.student_booking.PROBLEM[LOC_ADDRESS] = NEW_ADDRESS
            print("\t 'ADDRESS UPDATED SUCCESSFULLY.\n")


        elif ATTRIBUTE == 'EMAIL':
            print("ENTER 'OLD EMAIL' :", end=" ")
            OLD_EMAIL = input()
            LOC_EMAIL = bookings.student_booking.STUDENT_EMAIL.index(OLD_EMAIL)

            print("ENTER 'NEW EMAIL' :", end=" ")
            NEW_EMAIL = input()
            bookings.student_booking.STUDENT_EMAIL[LOC_EMAIL] = NEW_EMAIL
            print("\t 'EMAIL - ID UPDATED SUCCESSFULLY.\n")


        elif ATTRIBUTE == 'CLASS':
            print("ENTER 'OLD CLASS' :", end=" ")
            OLD_CLASS = input()
            LOC_CLASS = bookings.student_booking.CAMPUS.index(OLD_CLASS)

            print("ENTER 'NEW CLASS' :", end=" ")
            NEW_CLASS = input()
            bookings.student_booking.CAMPUS[LOC_CLASS] = NEW_CLASS
            print("\t 'CLASS UPDATED SUCCESSFULLY.\n")


        elif ATTRIBUTE == 'MOBILE NUMBER':
            print("ENTER 'OLD MOBILE NUMBER' :", end=" ")
            OLD_MOBILE = input()

            print("ENTER 'NEW MOBILE NUMBER' :", end=" ")
            NEW_MOBILE = input()
            STUDENT_PIN_LEN = len(OLD_MOBILE)
            M_N_LEN = len(NEW_MOBILE)

            if STUDENT_PIN_LEN < 4:
                print(end="\n")
                print("PLEASE ENTER TEN DIGIT MOBILE NUMBER.")
                print("SYSTEM HAS STOP, PLEASE TRY AGAIN.")
                exit()
            elif M_N_LEN < 4:
                print(end="\n")
                print("\t PLEASE ENTER VALID TEN DIGIT MOBILE NUMBER.")
                print("\t SYSTEM WORKING HAS STOP PLEASE TRY AGAIN.")
                exit()
            else:
                LOC_MOBILE = bookings.student_booking.STUDENT_PIN.index(OLD_MOBILE)
                bookings.student_booking.STUDENT_PIN[LOC_MOBILE] = NEW_MOBILE
                print("\t 'MOBILE NUMBER UPDATED SUCCESSFULLY.\n")

        run = True
        return run