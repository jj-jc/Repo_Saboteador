#!/usr/bin/env python3
import RPi.GPIO as GPIO
import os
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32

def talker():
    global contaLF
    global contaLB
    global contaRF
    global contaRB
    pub = rospy.Publisher('chatter', Int32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        
        print(contaLF, "  ", contaLB, "  ", contaRF, "  ", contaRB)
        conL = (contaLF + contaLB) / 2
        conR = (contaRF + contaRB) / 2
        #contaLF=0
        #contaLB=0
        #contaRF=0
        #contaRB=0
        GPIO.cleanup()
        
        informacion_motor1 = conL
        informacion_motor2 = conR
        rospy.loginfo(informacion_motor1, informacion_motor2)
        pub.publish(informacion_motor1, informacion_motor2)
        rate.sleep()
        

contaLF=0
contaLB=0
contaRF=0
contaRB=0

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN) #LF
GPIO.setup(20,GPIO.IN)
GPIO.setup(6,GPIO.IN) #LB
GPIO.setup(5,GPIO.IN)
GPIO.setup(19,GPIO.IN) #RF
GPIO.setup(16,GPIO.IN)
GPIO.setup(11,GPIO.IN) #RB
GPIO.setup(8,GPIO.IN)

#callbacks
def CuentaA_LF(channel):
    global contaLF
#     if GPIO.input(21)==GPIO.input(20):
#         contaLF -= 1
#     else:
#         contaLF += 1
    contaLF+=1

def CuentaB_LF(channel):
    global contaLF
#     if GPIO.input(21)!=GPIO.input(20):
#         contaLF -= 1
#     else:
#         contaLF += 1

def CuentaA_LB(channel):
    global contaLB
#     if GPIO.input(6)==GPIO.input(5):
#         contaLB -= 1
#     else:
#         contaLB += 1
    contaLB+=1

def CuentaB_LB(channel):
    global contaLB
#     if GPIO.input(6)!=GPIO.input(5):
#         contaLB -= 1
#     else:
#         contaLB += 1

def CuentaA_RF(channel):
    global contaRF
#     if GPIO.input(19)==GPIO.input(16):
#         contaRF += 1
#     else:
#         contaRF -= 1
    contaRF+=1

def CuentaB_RF(channel):
    global contaRF
#     if GPIO.input(19)!=GPIO.input(16):
#         contaRF += 1
#     else:
#         contaRF -= 1

def CuentaA_RB(channel):
    global contaRB
#     if GPIO.input(11)==GPIO.input(8):
#         contaRB += 1
#     else:
#         contaRB -= 1
    contaRB+=1

def CuentaB_RB(channel):
    global contaRB
#     if GPIO.input(11)!=GPIO.input(8):
#         contaRB += 1
#     else:
#         contaRB -= 1


#Interrupciones
GPIO.add_event_detect(21,GPIO.RISING, callback=CuentaA_LF)
#GPIO.add_event_detect(20,GPIO.RISING, callback=CuentaB_LF)
GPIO.add_event_detect(6,GPIO.RISING, callback=CuentaA_LB)
#GPIO.add_event_detect(5,GPIO.RISING, callback=CuentaB_LB)
GPIO.add_event_detect(19,GPIO.RISING, callback=CuentaA_RF)
#GPIO.add_event_detect(16,GPIO.RISING, callback=CuentaB_RF)
GPIO.add_event_detect(11,GPIO.RISING, callback=CuentaA_RB)
#GPIO.add_event_detect(8,GPIO.RISING, callback=CuentaB_RB)



#bucle principal
if __name__=='__main__':
    try:           
        talker()
              
    #except rospy.ROSInterruptException:
    except:
        pass
