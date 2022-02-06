import bookings.student_booking


# THIS FUNCTION HELP TO 'CANCEL' STUDENT BOOKINGS
def cancel_booking():
    print("CANCELLING BOOKINGS : \n")
   
    print(bookings.student_booking.STUDENT_PIN)
    print(bookings.student_booking.STUDENT_EMAIL)

    if len(bookings.student_booking.STUDENT_NAME) == 0 and len(bookings.student_booking.DATE) == 0 and len(bookings.student_booking.TIME) == 0 and len(
            bookings.student_booking.CAMPUS) == 0 and len(bookings.student_booking.STUDENT_PIN) == 0 and len(bookings.student_booking.PROBLEM) == 0 and len(
            bookings.student_booking.STUDENT_EMAIL) == 0:
                
        print("\t\t\t 'PLEASE FILL SOME INFORMATION DON'T KEEP IT EMPTY\n")
        run = True
        return run
    else:
        
        LOC1 = ""
        print("ENTER STUDENT'S E-MAIL :", end=" ")
        try:
            STUDENT_EMAIL = (input().upper())
            LOC1 = bookings.student_booking.STUDENT_EMAIL.index(STUDENT_EMAIL)
        except ValueError:
            print("\nCANCEL BOOKING WAS UNSUCCESSFULLY : \n")
            run = True
            return run
        
        LOC = ""
        print("ENTER 4 DIGTE CODE:", end=" ")
        try:
            OLD_MOBILE = input()
            LOC = bookings.student_booking.STUDENT_PIN.index(OLD_MOBILE)
        except ValueError:
            print("\nCANCEL BOOKING WAS UNSUCCESSFULLY : \n")
            run = True
            return run
            
        if str(LOC) == str(LOC1):
            bookings.student_booking.DATE.remove(bookings.student_booking.DATE[LOC])
            bookings.student_booking.STUDENT_NAME.remove(bookings.student_booking.STUDENT_NAME[LOC])
            bookings.student_booking.STUDENT_PIN.remove(bookings.student_booking.STUDENT_PIN[LOC])
            bookings.student_booking.TIME.remove(bookings.student_booking.TIME[LOC])
            bookings.student_booking.PROBLEM.remove(bookings.student_booking.PROBLEM[LOC])
            bookings.student_booking.STUDENT_EMAIL.remove(bookings.student_booking.STUDENT_EMAIL[LOC])
            bookings.student_booking.CAMPUS.remove(bookings.student_booking.CAMPUS[LOC])

            print("\n\t\t STUDENT BOOKING CANCELLED SUCCESSFULLY.")
            run = True
            return run