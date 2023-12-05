#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'mesaj alindi %s' , data.data)


def dinleyen():
    sub = rospy.Subscriber('dinle', Twist, callback)

if __name__ == '__main__':
    dinleyen()