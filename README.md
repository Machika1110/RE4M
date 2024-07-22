# RE4M (**R**andom **E**xercises **for** **M**athematics)
This is the application based on Python & Tkinter for outputting randomly math questions.  
Math questions are included in "Questions".  
Answers are included in "ANSWER.txt".

## Installation
### 1. Install modules
The following modules are need for RE4M app.

    python -m venv .venv
    pip install tkinter
    pip install opencv-python
    pip install opencv-contrib-python
    pip install pyinstaller


### 2. Script for pyinstaller
Prepare "RE4M.py" and "icon1.ico" and execute the following command.  


    pyinstaller RE4M.py --onefile --noconsole --icon==icon1.ico

You can get "RE4M.exe" app !

### 3. Set paths for RE4M.exe & Questions
Place RE4M.exe and Questions folder in "same" folders.   
※ The suggestion is making shortcuts in Desktop !


## The explanation of files and directory
### Questions 
&emsp;120 questions in Japanese for RE4M. All files are .png format.

### ANSWER.txt  
&emsp;Include number of question and answer.

### RE4M.py  
&emsp;Main program for RE4M.

### README.md
&emsp;This document.

### answer_list.py
&emsp;Make answer list from RE4M.py

### icon1.ico
&emsp;Original icon for RE4M.   
&emsp;If use other icon, make icons and change scripts for pyinstaller.
