from video_out import VideoOut
import os
from pytube import YouTube

class Store:

    def __init__(self, file, retrieve=False):
        self.file       = open(file, 'rb').read()
        self.video_file = file.replace('.txt', '.avi')
        self.video_out  = VideoOut(self.video_file)
        self.data       = ''.join('{0:08b}'.format(ord(x), 'b') for x in file)

    def write(self):
        # Write SOF (start of file) indicator.
        self.video_out.write_sof()

        for d in self.data:
            if d == '0':
                self.video_out.write_zero()
            elif d == '1':
                self.video_out.write_one()

        # Technically the EOF frame, but it's the same
        # color at the moment, so no need to duplicate.
        self.video_out.write_sof()

        command = ''.join([
            'youtube-upload ',
            '--title="',
            self.video_file,
            '" ',
            '--privacy unlisted ',
            self.video_file
        ])

        print(command)
        os.system(command)
