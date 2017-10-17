import cv2

size = 1
webcam = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:

	rval = False
	while(not rval):
		(rval, frame) = webcam.read()
		if(not rval):
			print("Failed to open webcam. Trying again...")
	frame = cv2.flip(frame, 1, 0)
	mini = cv2.resize(frame,(int(frame.shape[1] / size), int(frame.shape[0] / size)))
	faces = classifier.detectMultiScale(mini)
	for f in faces:
		(x ,y, w, h) = [v * size for v in f ]
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=4)

	cv2.imshow('OpenCV', frame)
	key = cv2.waitKey(10)
	if key == 27:
		break

webcam.release()
cv2.destroyAllWindows()