#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

class b(object):
	def __init__(self):
		self._pub_sound = rospy.Publisher('/Sound', Int16, queue_size=1)

		while(1):
			self._Exe()

	def _Exe(self):
		print "input number"
		number = input()

		sound = Int16()
		sound.data = number
		self._pub_sound.publish(sound)

if __name__=='__main__':
	rospy.init_node('mysound')
	b = b()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass
