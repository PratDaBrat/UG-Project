import cv2


def makeVideo(z, n, episode, session, name='animation.mp4'):
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter(name, fourcc, 15.0, (640, 480))
	for i in range(z, n):		#no.of images
		img_path = f'session{session}/stateimages/{episode}_{i}.png'
		# print(img_path)
		frame = cv2.imread(img_path)
		out.write(frame)
	out.release


def makeQTV(z, n, episode, session, name='qt_animation.mp4'):
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	out = cv2.VideoWriter(name, fourcc, 15.0, (1200, 600))
	for i in range(z, n):		#no.of images
		img_path = f'session{session}/qtimages/{episode}_{i}.png'
		# print(img_path)
		frame = cv2.imread(img_path)
		out.write(frame)
	out.release
