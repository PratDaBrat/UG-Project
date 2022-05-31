import cv2

def makeVideo(z,n,episode,name='animation.mp4'):
	fourcc  = cv2.VideoWriter_fourcc('M','J','P','G')
	out = cv2.VideoWriter(name, fourcc, 10.0, (640,480))
	for i in range(z,n): #no.of images
		img_path = f'stateimages_alt/{episode}_{i}.png'
		# print(img_path)
		frame = cv2.imread(img_path)
		out.write(frame)
	out.release
