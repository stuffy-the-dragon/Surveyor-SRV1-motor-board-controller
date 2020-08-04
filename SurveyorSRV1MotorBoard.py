from gpiozero import LED, PhaseEnableMotor

""" A class that controls the motor board on the Surveyor SRV-1 tracked robot """
class SurveyorSRV1MotorBoard:
    """ Constuctor """
    def __init__(self):
        # A factor that can be adjusted to fine tune motor speed
        self.__left_speed = 1.0 
        self.__right_speed = 1.0

        # The actual motor objects
        self.__left_motor = PhaseEnableMotor(26, 20)
        self.__right_motor = PhaseEnableMotor(16, 21)

        # The laser objects
        self.__left_laser = LED(13)
        self.__right_laser = LED(12)

    """ Turn on both lasers """
    def lasersOn(self):
        self.__left_laser.on()
        self.__right_laser.on()

    """ Turn off both lasers """
    def lasersOff(self):
        self.__left_laser.off()
        self.__right_laser.off()

    """ Get the motor speed factors 
        Output: {'left': float, 'right': float}
    """
    @property
    def motorsSpeedFactors(self):
        return {'left': self.__left_speed, 'right': self.__right_speed}

    """ Tune the motor speed factors
        Input: Keyword parameters => left = 1.0 and right = 1.0
    """
    @motorsSpeedFactors.setter
    def motorsSpeedFactors(self, left = 1.0, right = 1.0):
        try:
            assert left <= 1.0 and left >= 0.0
            assert right <= 1.0 and right >= 0.0
        except AssertionError:
            print("The speed parameters should be between 0.0 and 1.0")
            print("Setting both speed factors to default (1.0)")
            left = 1.0
            right = 1.0
        finally:
            self.__left_speed = left
            self.__right_speed = right


    """ Command the motors to move
        Input: direction = ['left', 'right', 'forward', 'backward']
               speed = float => 0.0 to 1.0
    """
    def motorsMove(self, direction, speed = 1.0):
        try:
            assert speed <= 1.0
            assert speed >= 0.0
            assert direction in ['left', 'right', 'forward', 'backward']
        except AssertionError:
            # How to log errors?
            print("Speed parameters should be between 0.0 and 1.0")
            print("Not affecting any motor changes")

        left_speed_adj = speed * self.__left_speed
        right_speed_adj = speed * self.__right_speed

        if direction == 'forward':
            # Backward is forward on our robot
            self.__left_motor.backward(left_speed_adj) 
            self.__right_motor.backward(right_speed_adj) 
        elif direction == 'backward':
            # Forward is backward on our robot
            self.__left_motor.forward(left_speed_adj) 
            self.__right_motor.forward(right_speed_adj) 
        elif direction == 'left':
            self.__left_motor.stop() 
            self.__right_motor.backward(right_speed_adj) 
        elif direction == 'right':
            self.__left_motor.backward(left_speed_adj) 
            self.__right_motor.stop() 
        else:
            print("This shouldn't happen... seems like a direction command slipped through")

    """ Command the motors to stop """
    def motorsStop(self):
        self.__left_motor.stop()
        self.__right_motor.stop()

    """ The status of the SRV1 motor board
        Output: {'L Laser': Boolean, 'R Laser': Boolean, 'L Motor': Boolean, 'R Motor': Boolean}
    """
    def boardStatus(self):
        return {'L Laser': self.__left_laser.is_lit, 
                'R Laser': self.__right_laser.is_lit,
                'L Motor': self.__left_motor.value,
                'R Motor': self.__right_motor.value}


    """ Let the __str__ method indicate the status of the board """
    def __str__(self):
        return str(self.boardStatus())

            
""" If this module is run as stand alone, do some tests """
if __name__ == "__main__":
    mb = SurveyorSRV1MotorBoard()

    mb.lasersOn()
    assert mb.boardStatus()['L Laser']
    assert mb.boardStatus()['R Laser']

    mb.lasersOff()
    assert not mb.boardStatus()['L Laser']
    assert not mb.boardStatus()['R Laser']

    mb.motorsMove('forward')
    assert mb.boardStatus()['L Motor'] == -1.0
    assert mb.boardStatus()['R Motor'] == -1.0

    mb.motorsMove('backward')
    assert mb.boardStatus()['L Motor'] == 1.0
    assert mb.boardStatus()['R Motor'] == 1.0

    mb.motorsMove('left')
    assert mb.boardStatus()['L Motor'] == 0.0
    assert mb.boardStatus()['R Motor'] == -1.0

    mb.motorsMove('right')
    assert mb.boardStatus()['L Motor'] == -1.0
    assert mb.boardStatus()['R Motor'] == 0.0

    print("All tests done!")







