import requests
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip

url = "https://yt-api.p.rapidapi.com/dl"

querystring = {"id":"6r2Kbaai22s"}

headers = {
	"x-rapidapi-key": "3442d23a1cmsh1210fe872a8c3dep106b17jsn5b06b9186471",
	"x-rapidapi-host": "yt-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()

# print(response["adaptiveFormats"][-1]["url"])

# def merge_video_and_audio(video_path, audio_path, output_path):
#   video_clip = VideoFileClip(video_path)
#   audio_clip = AudioFileClip(audio_path)
#   final_clip = CompositeVideoClip([video_clip, audio_clip])
#   final_clip.write_videofile(output_path)

# # Example usage:
# video_path = response["adaptiveFormats"][0]["url"]
# audio_path = response["adaptiveFormats"][-1]["url"]
# output_path = "merged_video.mp4"

# merge_video_and_audio(video_path, audio_path, output_path)

