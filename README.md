## Description
Generate a preview video from a video file. I have seen scripts and applications that make a preview image from a video file, but never found one that makes a short preview video from one. I have been looking to develop a video marketplace very soon, I felt like this would be useful as it provides users with a small preview of what they would be purchasing.

## Installation
video-preview-maker has the following dependencies:
- [opencv-python](https://pypi.org/project/opencv-python/)
- [numpy](https://pypi.org/project/numpy/)

You can install the dependencies listed above using pip:
```
pip install -r requirements.txt
```

## Usage
To simply create a video preview you can run the script with the default settings by using:
```
python app.py --video_path [VIDEO FILE]
```
Specify the number of frames you want to use in the preview video:
```
--frame_count [NUMBER OF FRAMES]
```
Specify the number of seconds you want to skip at the beginning and end of the video:
```
--skip_seconds [NUMBER OF SECONDS]
```
Specify the number of seconds you want each frame to appear in the preview video:
```
--duration_per_frame [NUMBER OF SECONDS]
```
Specify the fps of the preview video:
```
--fps [FRAMES PER SECOND]
```
Specify the path of the output file:
```
--output [OUTPUT VIDEO FILE]
```
