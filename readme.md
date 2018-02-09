# CloudTube

**A Python script that allows you to store files on YouTube**

By encoding the file into a binary sequence, and representing that sequence in a video using a colored circle,
files can be stored as YouTube videos.

**In its present state, this script currently works exclusively on text files!**

Also, I am still working on a good way to select the video to download. You will have to hard-code the video
url every time you want to retrieve for now, but that will be fixed in the future.

## Requirements

* Install youtube-upload tool
	* https://github.com/tokland/youtube-upload
* Install Pytube
	* pip install pytube

## Usage

`python cloudtube --store <file>.txt`

`python cloudtube --retrieve <video name>`
