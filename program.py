# Author: Carlo Scarpa
# Description: Program that helps run both the video compiler and question class to export 10 different YouTube shorts
import os
from video_compiler import TriviaVideoGenerator
from moviepy.editor import *
import random


# Left off trying to solve why text only appears above y = 50

class Trivia:
    def __init__(self, question, options, answer):
        '''
        Question object: 
        This object stores all the data grabbed from the csv file

        question: Question string 
        Options: Array of 4 different options
        answer: the correct answer in those options
        '''
        self.question = question
        self.options = options
        self.answer = answer

    def __repr__(self):
        return f"text output: {self.question} {', '.join(self.options)} {self.answer}"

class TriviaVideoGenerator:
    '''
    Object that generates the video
    '''

    def __init__(self, background):
        '''
        Passes background for the constructor, it is the random video from the folder
        'background_videos'
        '''
        self.background = background


    def generate_trivia_video(self, Trivia):
        # create clips array
        clips = []
        # add a TextClip of the question to the array
        clips.append(TextClip(Trivia.question, fontsize=50, color='white').set_position((100, 100)).set_start(0).set_duration(5))


        # Loop through all options, adjusting their positions accordingly
        ypos = 960
        for op in Trivia.options:
            clips.append(TextClip(op, fontsize=40, color='white').set_position((540, 40)).set_start(0).set_duration(5))
            ypos -= 20
        # add the answer to the array
        clips.append(TextClip(Trivia.answer, fontsize=30, color='black').set_position((0, 960)).set_start(0).set_duration(5))
        
        # convert array into all the clips concatenated
        final_text_clip = CompositeVideoClip(clips)
        # get background
        background = VideoFileClip(self.background).subclip(0, 5)
        # merge these clips together 
        final_clip = CompositeVideoClip([background, final_text_clip])

        return final_clip

def create_questions():
    with open('trivia_questions.csv', 'r') as file:
        lines = file.readlines()

    question_arr = []
    for line in lines[1:]:

        components = line.strip().split(',')
        question = components[0]
        options = components[1:-1]
        answer = components[-1]
        question_arr.append(Trivia(question, options, answer))

    return question_arr

def get_random_background():
    '''
    Had help generating this, essentially gets the path to my folder 'background_videos' and picks a random video to use
    '''

    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, 'background_videos')

    file_list = os.listdir(folder_path)
    background = os.path.join(folder_path, random.choice(file_list))

    return background


def main():
    video_generator = TriviaVideoGenerator(get_random_background())
    questions = create_questions()

    curr_question = questions[0]

    video = video_generator.generate_trivia_video(curr_question)
    video.write_videofile("new_video.mp4")

if __name__ == "__main__":
    main()