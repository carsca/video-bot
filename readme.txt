Authors: Carlo Scarpa

Description: This program uses chatgpt and other python libraries like moviepy to automate the creation of short form content

My first focus will be making simple trivia videos for YT shorts, and TikTok

Programs needed:
- video editor that takes footage, and question then outputs a video sound for youtube shorts
- object that contains all information to plug in to the video editor file
- file that generates csv file in form Question, option1, option2, option3, option4, answer
        - (will start with manual before attempting to plug chat gpt in)



11/7 -
6:22PM
Left trying to solve why text only shows above y = 50
What works:
        randomly picking background video
        the assingment of elements of the Question object
        exports video
        stuff shows up on the screen



Still needed to work -
        text config (animation, sizing, wrapping cases for length of q)
        voice over (text2speech)
        music (will probably make a folder similar to backgrounds of trending sounds)
        timer animation



11/8 -
5:55PM
What works:
        everything from last entry
        text appears and reveals answer after x time
        random background is selected
        works if iterating the list from the csv file
        wraps question text if too long

Still needs work:
        bigO is really long (idk if this is fixable)
        Need to animate text transition
        animate timer
        voice over
        music
        

Later improvements -
        ChatGPT api implementation
        Generate 100 quickly