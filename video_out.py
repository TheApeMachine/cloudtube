class VideoOut:

    def __init__(self, video_file):
        self.fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        self.out    = cv2.VideoWriter(video_file, fourcc, 30 (640, 480))
        self.img    = np.zeros((480, 640, 3), np.uint8)

    # Start of file indicator.
    def write_sof(self):
        self.write_frame((255, 0, 0))

    def write_zero(self):
        self.write_frame((0, 0, 255))

    def write_one(self):
        self.write_frame((0, 255, 0))

    def write_frame(self, color):
        cv2.circle(self.img, (10, 10), 10, color, -1)
        self.out.write(self.img)
