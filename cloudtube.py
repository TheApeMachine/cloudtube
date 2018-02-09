import numpy as np
import cv2
import sys
import os
from pytube import YouTube

STORE = False

for arg in sys.argv:
    if arg == '--store':
        STORE = True

FILE = sys.argv[2]

if STORE:
    print 'STORING ', FILE, '...'

    file       = open(FILE, 'rb').read()
    video_file = FILE.replace(".txt", ".avi")
    fourcc     = cv2.VideoWriter_fourcc('M','J','P','G')
    out        = cv2.VideoWriter(video_file, fourcc, 30, (640, 480))
    img        = np.zeros((480, 640, 3), np.uint8)
    data       = ''.join('{0:08b}'.format(ord(x), 'b') for x in file)

    # Render a blue circle, and write a frame to signal the
    # start of our file.
    cv2.circle(img, (10, 10), 10, (255, 0, 0), -1)
    out.write(img)

    for d in data:
        if d == '0':
            # Render a red circle, and write a frame
            cv2.circle(img, (10, 10), 10, (0, 0, 255), -1)
            out.write(img)
        elif d == '1':
            # Render a green circle and write a frame.
            cv2.circle(img, (10, 10), 10, (0, 255, 0), -1)
            out.write(img)

        # For now we will just render a black frame, to detect
        # if there is a sequence of identical bits.
        cv2.circle(img, (10, 10), 10, (0, 0, 0), -1)
        out.write(img)

    # Render a blue circle, and write a frame to signal the
    # end of our file.
    cv2.circle(img, (10, 10), 10, (255, 0, 0), -1)
    out.write(img)

    command = ''.join(["youtube-upload ", '--title="', video_file, '" ', '--privacy unlisted ', video_file])

    print command
    os.system(command)

    print 'ALL DONE!'
else:
    print 'RETRIEVING ', FILE, '...'

    YouTube('https://www.youtube.com?v=nr00F3PHwYc').streams.first().download()

    cap  = cv2.VideoCapture(FILE + 'avi.mp4')
    out  = FILE + '-out.txt'
    file = open(out, 'wb')
    data = []

    while(cap.isOpened()):
        ret, frame = cap.read()

        try:
            roi = frame[10, 10]

            if roi[1] > 200:
                data.append(1)
            elif roi[2] > 200:
                data.append(0)

        except TypeError:
            cap.release()

    file.write(''.join([chr(sum(bit << abs(idx - 8) - 1 for idx, bit in enumerate(y)))
        for y in zip(*[data[x::8] for x in range(8)])
    ]))

    print 'ALL DONE!'
