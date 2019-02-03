#!/usr/bin/env python
# -#- coding: utf-8 _*_
import rospy
import time
import subprocess
from std_msgs.msg import Int16


class a(object):
	def __init__(self):
		self._sub_number = rospy.Subscriber('/Sound', Int16, self._callback_sound)

	def _callback_sound(self, message):
		self._number = message.data
		print self._number
		for num in range(self._number):
			m = self._number % 3
			cmd = "mpg321 ~/sound/" + str(m) + ".mp3"
			subprocess.call(cmd, shell=True)

if __name__=='__main__':
	rospy.init_node('Sound')
	a = a()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		pass
