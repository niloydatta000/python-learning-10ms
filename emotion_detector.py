"""Install deeface, tf-keras, opencv-python properly. The deepface is a pre-trained python library."""

import cv2
from deepface import DeepFace

capture = cv2.VideoCapture(0) # primary camera number 0

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
# .xml file should be in the same directory. Otherwise full directory must be inputted.


while True:
	(bool_value, frame) = capture.read()
	
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # opencv2 works with RGB
	
	
	
	faces = face_cascade.detectMultiScale(rgb_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
	
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 225) thickness=2) # color always takes (B, G, R) format
		
		result = DeepFace.analyze(rgb_frame[x: x + w, y: y + h], actions=("emotion"), enforce_detection=False)
		cv2.putText(frame, text=result[0]['dominant_emotion'], org=(x, y - 20), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.9, color=(0, 0, 225), thickness=3)
		print(result[0]['dominant_emotion']) # Optional
		
	cv2.imshow("Emotion Detector", frame)
	
	if cv2.waitKey(1) and oxFF == ord('q')
	break

capture.release()
cv2.destroyAllWindows()