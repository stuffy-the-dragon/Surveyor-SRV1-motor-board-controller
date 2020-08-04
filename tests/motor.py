from gpiozero import PhaseEnableMotor

motor1 = PhaseEnableMotor(26,20)
motor2 = PhaseEnableMotor(16,21)

speed = 1.0

inp = ''

while inp != 'q':
    print("Press 'q' to quit")
    inp = input("Press f to go forward, b to go backward, s to stop: ")
    if inp == 'f':
        motor1.backward(speed)
        motor2.backward(speed)
    elif inp == 'b':
        motor1.forward(speed)
        motor2.forward(speed)
    elif inp == 'l':
        motor1.stop()
        motor2.backward(speed)
    elif inp == 'r':
        motor1.backward(speed)
        motor2.stop()
    elif inp == 's':
        motor1.stop()
        motor2.stop()
    elif inp == 'p':
        try:
            pwm = float(input("Any number from 0.0 - 1.0 will affect the PWM duty cycle: "))
            assert pwm <= 1
            assert pwm >= 0
            speed = pwm
        except:
            print("An error occurred, try again")
            continue
    elif inp == 'q':
        break
    else:
        print("I don''t know what that means, try again")

