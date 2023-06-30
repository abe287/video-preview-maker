import cv2
import argparse

def get_video_details() -> dict:
    #Open video for processing
    video = cv2.VideoCapture(args.video_path)

    video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)

    video_details = {
        "video_width": video_width,
        "video_height": video_height,
        "total_frames": total_frames,
        "fps": fps
    }

    return video_details

def get_frames(video_details: dict) -> list:
    #Offset for getting next frame
    frame_offset = int(video_details['total_frames'] / args.frame_count)

    #Get list of frames from the video
    frames = []
    for x in range(args.frame_count):
        frame = (frame_offset * x) + frame_offset
        frames.append(frame)
    
    #Calculate seconds to skip at start and end of video
    skip_frames = int(video_details['fps'] * args.skip_seconds)

    #Update first and last frames (skipping x seconds)
    frames[0] = frames[0] + skip_frames
    frames[-1] = frames[-1] - skip_frames

    return frames

def read_frame_from_video(frame_number: int):
    #Open the video file
    video = cv2.VideoCapture(args.video_path)

    #Get the desired frame
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    #Read the frame
    ret, frame = video.read()

    #Release the video capture
    video.release()

    return frame

def compile_frames_to_video(frames: list, output_filename: str, fps: int, frame_width: int, frame_height: int, duration_per_frame: float) -> None:
    #Define the codec and create the VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

    #Convert frame locations to images and write them to video
    for frame in frames:
        #Create an image frame from int value
        image_frame = read_frame_from_video(frame)

        num_frames = int(duration_per_frame * fps)
        for _ in range(num_frames):
            #Write the image frame to the video
            video.write(image_frame)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--frame_count", type=int, help="Number of frames to use in the preview", default=12)
    parser.add_argument("--skip_seconds", type=int, help="Number of seconds to skip at start and end of video", default=10)
    parser.add_argument("--duration_per_frame", type=float, help="Duration each frame will show for (in seconds)", default=0.5)
    parser.add_argument("--output", type=str, help="Path to output file", default="output.mp4")
    parser.add_argument("--fps", type=int, help="fps of output video file", default=30)
    parser.add_argument("--video_path", help="Path to video file")
    args = parser.parse_args()
    
    #Get video details from input video
    video_details = get_video_details()

    #Get preview frames from video
    frames = get_frames(video_details)
    
    #Make video file from preview frames
    compile_frames_to_video(frames, args.output, args.fps, video_details['video_width'], video_details['video_height'], args.duration_per_frame)