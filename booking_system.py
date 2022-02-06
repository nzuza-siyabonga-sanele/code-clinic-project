import sys


valid_commands = ['h', 'help', 'q','quit', 'v','volunteer', 'b', 'book', 'c','cancel', 'u', 'update']


#TODO list all available commands
def help_commands():
    commands ="""These are all valid comands:
h or help - outputs a list of available commnads\n
q or quit - quits and exits booking system\n
v or volunteer - books a volunteer slot in the code clinics calendar\n
b or book - books a available slot for student in the code clinics calendar\n
c or cancel - cancels a volunteer slot or student booking"""

    return commands


#TODO get commands from user here
def get_command(OPTION):
    
    import bookings.student_booking
    import bookings.update_information
    import bookings.cancel_booking
    
    
    if OPTION.lower() == "book" or "b":
        return bookings.student_booking.book_a_slot()
        
    elif OPTION.lower() == "cancel" :
        return bookings.cancel_booking.cancel_booking()

    elif OPTION.lower() == ("update" or "u") : 
        return bookings.update_information.update_bookings_volunteer()
            
    elif OPTION.lower() == "view" :
        print("work in progress")
    elif OPTION.lower() == "exit"  :
        print("THANK YOU ! VISIT AGAIN.")
        run = False
    elif OPTION.lower() == ("help" or 'h') :
        outprint = help_commands()
        print(outprint)
        run = True
        return run
    else:
        print("PLEASE CHOOSE CORRECT OPTION FROM THE FOLLOWING.\n")
        run = True
        return run
    pass


#TODO call all functions here
def start_booking():
    
    print("\n")
    print("' ********** WELCOME TO CODE CLINIC ********** ' \n")
    
    print("""Open 7 days, Weekends and public holidays are counted in the 7 days.
The duration for each section is half hour long.
Student can volunteer or book their time in the coding clinic.

You can Enter Help to display all the commands needed for the code clinic.
""")
    
    run = True
    
    if len(sys.argv)>1:
        if len(sys.argv) > 2:
            if sys.argv[1].lower() == ("book" or "b") and sys.argv[2].lower() == ("cancel" or "c"):
                OPTION = "cancel"
                run = get_command(OPTION)
            elif sys.argv[1] == ("book" or "b") and sys.argv[2].lower() == ("update" or "u"):
                OPTION = "update"
                run = get_command(OPTION)
        elif sys.argv[1] == ("book" or "b"):
            OPTION = "book"
            run = get_command(OPTION)
            
    # MESSAGE = output_one()
    # print(MESSAGE)
    else:
        OPTION = (input("ENTER YOUR OPTION : "))
        print("\n")
        print(end="\n")
        run = get_command(OPTION)
        print(run)
    
    while run:
        
        # MESSAGE = output_one()
        # print(MESSAGE)
        OPTIONS = (input("ENTER YOUR OPTION : "))
        print("\n")
        print(end="\n")
        run = get_command(OPTION)
        print(run)
    
if __name__ =="__main__":
    start_booking()