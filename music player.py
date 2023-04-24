#-------> Coded by Dhanu <-----
# A Simple Music player in python using pygame and os modules!

import pygame
import os

# Initialize Pygame
pygame.init()

# Set the window title and size
pygame.display.set_caption("Music Player")
screen = pygame.display.set_mode((300, 100))

# Set the music directory
music_dir = input("Enter the path of .mp3 file to play: ")

# Get a list of music files in the directory
music_files = [file for file in os.listdir(music_dir) if file.endswith(".mp3")]

# Initialize the music player
pygame.mixer.music.load(os.path.join(music_dir, music_files[0]))
pygame.mixer.music.play()

# Loop through the music files
index = 0
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Display the song name
    font = pygame.font.Font(None, 36)
    text = font.render(music_files[index], 1, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()

    # Check if the current song has ended
    if not pygame.mixer.music.get_busy():
        index += 1
        if index >= len(music_files):
            index = 0
        pygame.mixer.music.load(os.path.join(music_dir, music_files[index]))
        pygame.mixer.music.play()
