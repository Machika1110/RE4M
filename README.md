# RE4M (**R**andom **E**xercises **for** **M**athematics)
This is the application based on Python & Tkinter for outputting randomly math questions.  
Math questions are included in "Questions".  
Answers are included in "ANSWER.txt".

## Installation
### 1. Install modules
The following modules are need for pyinstaller

    python -m venv .venv
    pip install tkinter
    pip install opencv-python
    pip install opencv-contrib-python


### 2. Script for pyinstaller
Prepare "RE4M.py" and "icon1.ico"  


    pyinstaller RE4M.py --onefile --noconsole --icon==icon1.ico


### 3. Set paths for RE4M.exe & Questions
Place RE4M.exe and Questions folder in "same" folders.   
The suggestion is making shortcuts in Desktop.


## The explanation of files and directory
### Questions 
All questions for RE4M. All files are .png format

### ANSWER.txt  
Include number of question and answer

### RE4M.py  
Main program for RE4M.

### README.md
This document.

### answer_list.py
Make answer list from RE4M.py

### icon1.ico
Original icon for RE4M.   
If use other icon, make icons and change scripts for pyinstaller.
