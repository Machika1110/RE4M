# RE4M (**R**andom **E**xercises **for** **M**athematics)
This is the application based on Python & Tkinter for outputting randomly math questions.  
Math questions are included in "Questions".  
Answers are included in "ANSWER.txt".


## install modules
The following modules are need for pyinstaller

    python -m venv .venv
    pip install tkinter
    pip install opencv-python
    pip install opencv-contrib-python


## script for pyinstaller
Prepare "RE4M.py" and "icon1.ico"
    pyinstaller RE4M.py --onefile --noconsole --icon==icon1.ico
