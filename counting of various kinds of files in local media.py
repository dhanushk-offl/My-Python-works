# Hi! Takes long time to check you media storage, why the fear? Where python is here!  Check you local media in less than 30 lines of code!
#Coded by: Dhanush K
import glob
import os

# First, we define file types to count
video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
audio_extensions = ['.mp3', '.wav', '.wma']
text_extensions = ['.txt', '.pdf', '.doc', '.docx']
programming_extensions = ['.py', '.java', '.cpp', '.c', '.h']

# Then, initialize counters along with their perspective sizes sizes
video_count = 0
video_size = 0
audio_count = 0
audio_size = 0
text_count = 0
text_size = 0
programming_count = 0
programming_size = 0

# walk through the entire file system and count file types for the next process
# Here, you can make an input to get the path of specific folder to this count process, by replacing the /**/ by the input function!
for extension in video_extensions:
    for file in glob.glob(f"/**/*{extension}", recursive=True):
        video_count += 1
        video_size += os.path.getsize(file)
        
for extension in audio_extensions:
    for file in glob.glob(f"/**/*{extension}", recursive=True):
        audio_count += 1
        audio_size += os.path.getsize(file)
        
for extension in text_extensions:
    for file in glob.glob(f"/**/*{extension}", recursive=True):
        text_count += 1
        text_size += os.path.getsize(file)
        
for extension in programming_extensions:
    for file in glob.glob(f"/**/*{extension}", recursive=True):
        programming_count += 1
        programming_size += os.path.getsize(file)

#Finally, print the results
print(f"Number of video files: {video_count}, Total size: {video_size} bytes")
print(f"Number of audio files: {audio_count}, Total size: {audio_size} bytes")
print(f"Number of text files: {text_count}, Total size: {text_size} bytes")
print(f"Number of programming files: {programming_count}, Total size: {programming_size} bytes")
