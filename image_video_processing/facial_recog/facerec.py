import cv2, sys, numpy, os
size = 1
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'att_faces'

print('Training...')

(images, lables, names, id) = ([], [], {}, 0)

for (subdirs, dirs, files) in os.walk(fn_dir):

    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)

        for filename in os.listdir(subjectpath):

            f_name, f_extension = os.path.splitext(filename)
            if(f_extension.lower() not in
                    ['.png','.jpg','.jpeg','.gif','.pgm']):
                print("Skipping "+filename+", wrong file type")
                continue
            path = subjectpath + '/' + filename
            lable = id

            # Add to training data
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (112, 92)

(images, lables) = [numpy.array(lis) for lis in [images, lables]]

model = cv2.createFisherFaceRecognizer()
model.train(images, lables)




haar_cascade = cv2.CascadeClassifier(fn_haar)
webcam = cv2.VideoCapture(0)
while True:

    rval = False
    while(not rval):
        # Put the image from the webcam into 'frame'
        (rval, frame) = webcam.read()
        if(not rval):
            print("Failed to open webcam. Trying again...")

    frame=cv2.flip(frame,1,0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

    faces = haar_cascade.detectMultiScale(mini)
    for i in range(len(faces)):
        face_i = faces[i]

        # Coordinates of face after scaling back by `size`
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))

        prediction = model.predict(face_resize)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.putText(frame,
           '%s - %.0f' % (names[prediction[0]],prediction[1]),
           (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))

    cv2.imshow('OpenCV', frame)
    key = cv2.waitKey(10)
    if key == 27:
        break