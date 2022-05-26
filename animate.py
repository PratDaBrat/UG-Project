import cv2

def makeVideo():
	fourcc  = cv2.VideoWriter_fourcc('M','J','P','G')
	out = cv2.VideoWriter('animation.mp4', fourcc, 1.0, (640,480))
	for i in range(10): #no.of images
		img_path = f'stateimages/{i}.png'
		print(img_path)
		frame = cv2.imread(img_path)
		out.write(frame)
	out.release

makeVideo()