# Author: Carlo Scarpa
# Description: Program that helps run both the video compiler and question class to export 10 different YouTube shorts
import os
from video_compiler import TriviaVideoGenerator
from moviepy.editor import *
import random



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

    def get_question(self):
        '''
        Purpose of this getter is to avoid questions from going off the edge of the screen
        
        '''
        MAX_CHARACTERS = 40
        # Check if the text exceeds the maximum character count
        if len(self.question) > MAX_CHARACTERS:
            # Find the position of the last space before the maximum character count
            last_space = self.question.rfind(' ', 0, MAX_CHARACTERS)
            if last_space != -1:  # If a space is found within the limit
                question_text = self.question[:last_space] + '\n' + self.question[last_space + 1:]
            else:  # If no space found within the limit, insert newline directly
                question_text = self.question[:MAX_CHARACTERS] + '\n' + self.question[MAX_CHARACTERS:]
        else:
            question_text = self.question
        return question_text

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
        
        # Create clips array
        clips = []
        clips.append(TextClip(Trivia.get_question(), color='white', stroke_color='black', stroke_width=2, fontsize=70, font="Bernard-MT-Condensed", size=(1080,1920), align="center").set_position((0,-700)).set_duration(1).set_start(0))

        # Loop through all options, adjusting their positions accordingly
        ypos = -500
        for op in Trivia.options:
            clips.append(TextClip(op, color='white', stroke_color='black', stroke_width=2, fontsize=100, font="Bernard-MT-Condensed", size=(1080,1920), align="center").set_position((0,ypos)).set_duration(1).set_start(0))
            ypos += 250

        # add the answer to the array
        answer_text = TextClip(Trivia.answer, color='white', stroke_color='black', stroke_width=3, fontsize=200, font="Bernard-MT-Condensed", size=(1080,1920), align="center").set_position((0,0)).set_duration(1).set_start(0)


        # The backgrround clip
        background = VideoFileClip(self.background).subclip(0, 1)
        # The initial text clips
        final_text_clip = CompositeVideoClip(clips)
        # Initial text on top of background
        final_clip = CompositeVideoClip([background, final_text_clip])
        
        # Revealed answer clip
        answer_clip = CompositeVideoClip([background, answer_text])
        
        # The actual final video
        final_clip = concatenate_videoclips([final_clip, answer_clip])
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