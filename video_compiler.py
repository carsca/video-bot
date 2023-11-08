from moviepy.editor import *
import random

class TriviaVideoGenerator:
    def __init__(self):
        self.background = VideoFileClip('whitevid.mp4')

    def get_random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def get_text_color(self, bg_color):
        luminance = (0.299 * bg_color[0] + 0.587 * bg_color[1] + 0.114 * bg_color[2]) / 255
        return 'white' if luminance < 0.5 else 'black'

    def generate_trivia_video(self, question):
    

        final_clip = CompositeVideoClip(self.background, self.background)
        final_clip = final_clip.resize

        return final_clip
