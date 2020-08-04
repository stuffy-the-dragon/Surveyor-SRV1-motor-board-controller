from gpiozero import LED

led1 = LED(13)
led2 = LED(12)

userin = ''

while userin != 'q':
    print("Type 'q' to quit")
    userin = input("Type LED nr to toggle it:  ")
    if userin == 'q':
        break
    elif userin == '1':
        led1.toggle()
    elif userin == '2':
        led2.toggle()
    else:
        print("Incorrect command try again")

