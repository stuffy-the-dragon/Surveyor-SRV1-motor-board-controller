from gpiozero import PhaseEnableMotor


def clamp(value, min_, max_):
    return min(max_, max(min_, value))


motor1 = PhaseEnableMotor(26, 20)
motor2 = PhaseEnableMotor(16, 21)

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
        pwm = float(input("Any number from 0.0 - 1.0 will affect the \
            PWM duty cycle: "))
        speed = clamp(pwm, 0.0, 1.0)
    elif inp == 'q':
        break
    else:
        print("I don''t know what that means, try again")
