def liftLeftLeg(ser):
	setAngle(ser, 5, 70)
	setAngle(ser, 0, 80)
	time.sleep(.5)
	setAngle(ser, 5, 90)
	setAgnle(ser, 7, 110)
	setAngle(ser, 8, 80)
	setAngle(ser, 6, 105)

def stepLeftForward(ser):
	setAngle(ser, 8, 80)
	setAngle(ser, 7, 100)
	setAngle(ser, 6, 95)
	time.sleep(.5)
	setAngle(ser, 3, 110)
	time.sleep(.5)
	setAngle(ser, 2, 80)
	time.sleep(.5)
	setAngle(ser, 1, 105)
	setAngle(ser, 0, 90)
	time.sleep(.5)