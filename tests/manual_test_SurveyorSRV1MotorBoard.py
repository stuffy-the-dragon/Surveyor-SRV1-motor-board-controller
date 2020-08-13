from SurveyorSRV1MotorBoard import SurveyorSRV1MotorBoard as board

mb = board()

inp = ''
while inp != 'q':
    inp = input("Enter a command ['f', 'b', 'l', 'r', 's', 'lon', 'loff']: ")

    if inp == 'f':
        mb.motorsMove('forward')
    elif inp == 'b':
        mb.motorsMove('backward')
    elif inp == 'l':
        mb.motorsMove('left')
    elif inp == 'r':
        mb.motorsMove('right')
    elif inp == 's':
        mb.motorsStop()
    elif inp == 'lon':
        mb.lasersOn()
    elif inp == 'loff':
        mb.lasersOff()
    elif inp == 'q':
        break
    else:
        print("That is not a valid command. Try again.")
        continue
