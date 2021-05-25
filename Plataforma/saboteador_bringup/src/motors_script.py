#!/usr/bin/env python
import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay
import rospy
#from std_msgs.msg import Int32
from std_msgs.msg import Float32

GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)			# enable warning from GPIO
AN2 = 13				# set pwm2 pin on MD10-Hat
AN1 = 12				# set pwm1 pin on MD10-hat
DIG_R = 24				# set dir2 pin on MD10-Hat
DIG_L = 26				# set dir1 pin on MD10-Hat
GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG_R, GPIO.OUT)		# set pin as output
GPIO.setup(DIG_L, GPIO.OUT)		# set pin as output
sleep(1)				# delay for 1 seconds
p1 = GPIO.PWM(AN1, 100)			# set pwm for M1
p2 = GPIO.PWM(AN2, 100)			# set pwm for M2

p1.start(0)                     
p2.start(0) 

duty_motor_left = 0
duty_motor_right = 0


def motor_left_callback(msg):
	global duty_motor_left   
    duty_motor_left = msg.data
    #print("motor left callback: ", duty_motor_left)
    
def motor_right_callback(msg):
	global duty_motor_right
    duty_motor_right = msg.data
    #print("motor right callback: ", duty_motor_right)
    
    
def listener():
	global duty_motor_left
	global duty_motor_right
	global p1
	global p2
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("saboteador/motor_left", Float32, motor_left_callback)
    rospy.Subscriber("saboteador/motor_right", Float32, motor_right_callback)
    rate = rospy.Rate(50);

    while not rospy.is_shutdown():
    
        if duty_motor_left >= 0:
            GPIO.output(DIG_L, GPIO.LOW) 
        else:
            GPIO.output(DIG_L, GPIO.HIGH)
            duty_motor_left = -duty_motor_left;
    
        if duty_motor_right >= 0:
            GPIO.output(DIG_R, GPIO.LOW) 
        else:
            GPIO.output(DIG_R, GPIO.HIGH)
            duty_motor_right = -duty_motor_right;
    	
    	print("motor left callback: ", duty_motor_left)
    	print("\n")
    	print("motor right callback: ", duty_motor_right)
    	 
        p1.start(duty_motor_left)                     
        p2.start(duty_motor_right) 
       
        rate.sleep()
    

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
    	GPIO.cleanup()
        pass




