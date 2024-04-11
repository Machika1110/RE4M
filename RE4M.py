# coding: utf-8
# import
import tkinter as tk      # make apps
import tkinter.ttk as ttk
import random             # make random number
import cv2                # show question.png
import sys                # extract outer file

# define parameters
score = 0        # total score
qnum = []        # question number defined by random numbers
qsub = "all"     # mathematical subject
nummin = 1       # minimum of random question number
nummax = 120     # maxmum of random question number
qtime = 3        # question time in 1 try
qwrg = []        # list of questions you mistook
cnum = 0         # number of correct answers
qcount = 0       # count questions
opt_qtime = [3, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]  # qtime selection
asecond = 1000   # [ms] = 1 secnond, interval time for timer
after_id = 0     # for timer
hcount=0         # show hour
mcount=0         # shoe minute
scount=0         # show second
start_flag = False # if true, timer is ON
qnum2 = 0        # in start2, question number solved
exepath = sys.argv[0].replace("RE4M.exe", "")


# define answer of each question
ans = [
    "DUMMY",
    16, 58, 33, 6, 85, 5,     # Q1~6, "formulas and numbers"
    -7, -16, 8, 0, 0, 9,      # Q7~12, "secondary function"
    2, 2, 18, 120, 4, 3.24,   # Q13~18, "Shapes and measurements"
    44.8, 47, 11, 3, 2, 3,      # Q19~24,  "Data and analyze"
    120, 12, 30, 81, 6, 20160, 150, 53, 0.167, 61, 216, 11,   # Q25~36, "probability"
    4, 18, 108, 4, 36, 36, # Q37~42, "properties of shapes"
    1651, 10, 6, 234, 48, 7, 2, 103, 231, 0.384, 90, 37,    #Q43~54, "properties of integer"
    672, 2, 4, 9, 1, 2,       # Q55~60, "formula and proof"
    5, 2, -20, -6, 17, 22,   # Q61~66, "complex number and equations"
    5, -13, 3, 4, 12, 0,      #Q67~72, "shape and equation"
    -3, 4, 2, 3, 4, 3,        #Q73~78, "trigonometric function"
    3, 1, 16, 1575, 188, -28, #Q79~84, "exponential and logarithmic function"
    -4, 4, 1, -13, 2, 1, 0, 3, 1, 44, -9, 9,  #Q85~96, "differentiation and integration"
    135, 2, 7, 1, 5, 3, -4, 11, 2, 60, 1, 1, #Q97~108, "vector"
    14950, 6141, 2, 388310, 3, 0.999, 2, 4, 3, 1, 649539, 7889 #Q109~120, "sequence"
]

# Decide question number 
def randnum(nummin, nummax, qtime): # make random numbers without dubling
      ns = []
      while len(ns) < qtime:
            n = random.randint(nummin, nummax)
            if not n in ns:
                ns.append(n)
      return ns

########## START ##########
def start_menu():
    global frame_start
    global qcount
    global cnum, after_id, hcount, mcount, scount, start_flag

    # initialize parameters
    timestop()                # from pause menu
    cv2.destroyAllWindows()   # from pause menu
    qcount = 0
    cnum = 0
    after_id = 0
    hcount=0
    mcount=0
    scount=0
    start_flag = False

    # delete other menu frame 
    try:
        frame_ques.destroy()
    except NameError:
        pass
    try:
        frame_setting.destroy()
    except NameError:
        pass
    try:
        frame_result.destroy()
    except NameError:
        pass
    try:
        frame_pause.destroy()
    except NameError:
        pass

    try:
        frame_Qselect.destroy()
    except NameError:
        pass

    # make start menu frame
    frame_start = ttk.Frame(root)
    frame_start.pack(fill = tk.BOTH, pady=20)

    scorelbl2 = tk.Label(
        frame_start,
        text = "Score : " + str(score),
        font=("Times", "16", ),
        bg = "#7FFFD4",
        width =24
    )
    scorelbl2.pack()

    LOGO = tk.Label(
        frame_start, 
        bd=20,
        bg="gray",
        text=" RE4M ",
        font=("Times", "140", "bold"),
        relief=tk.RAISED
    )
    LOGO.pack(padx = 30, pady = 20)   # Show LOGO
    
    start1 = tk.Button(
        frame_start,
        bd=5,
        text=" START RANDOMLY ",
        font=("Times", "16", ),
        bg = "#7FFFD4",
        command=ques_menu
    ) 
    start1.pack(pady = 10)

    start2 = tk.Button(
        frame_start,
        bd=5,
        text=" START WITH SELECTION ",
        font=("Times", "16", ),
        bg = "#7FFFD4",
        command=Qselect_menu
    ) 
    start2.pack(pady = 10)

    setting= tk.Button(
        frame_start,
        bd=5,
        text=" SETTINGS ",
        font=("Times", "16", ),
        bg = "#7FFFD4",
        command=setting_menu
    ) 
    setting.pack(pady = 10)

    if len(qwrg)== 0:
        start2["state"] = "disabled"

########## Question ##########
def ques_menu():
    global frame_ques
    global pausebtn
    global inans
    global inans
    global setans
    global correctlbl
    global scorelbl
    global qnum
    global nummin, nummax, qtime
    global hour, min, sec, timeframe
    global processshow

    frame_start.destroy()

    qnum = randnum(nummin, nummax, qtime)
    timestart()

    frame_ques = tk.Frame(root)
    frame_ques.pack()
    frame_ques2=tk.Frame(frame_ques)



    # show time
    timeframe=tk.Frame(frame_ques2,bg = "#7FFFD4", width =18,)

    hour = tk.Label(
        timeframe,
        text = "00",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )

    dot1 = tk.Label(
        timeframe,
        text = ":",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )

    min = tk.Label(
        timeframe,
        text = "00",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )

    dot2 = tk.Label(
        timeframe,
        text = ":",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )

    sec = tk.Label(
        timeframe,
        text = "00",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )


    # show score
    scorelbl = tk.Label(
        frame_ques2,
        text =  "Score : " + str(score),
        font=("Times", "16", ),
        bg = "#7FFFD4",
        width =24
    )

    # pause
    pausebtn = tk.Button(
        frame_ques2,
        text = "PAUSE",
        font=("Times", "16", ),
        bg = "#7FFFD4",
        width =18,
        command=pausefnc
    )

    frame_ques2.pack()
    timeframe.pack(fill="x", padx=10, side = 'left')
    hour.pack(padx=5, side = "left")
    dot1.pack(padx=5, side = "left")
    min.pack(padx=5, side = "left")
    dot2.pack(padx=5, side = "left")
    sec.pack(padx=5, side = "left")
    scorelbl.pack(fill="x", padx=10, side = 'left')
    pausebtn.pack(fill="x", padx=10, side = 'left')

    # Show question
    
    qshow(qnum[qcount])
    

    # Show N/N
    processshow = tk.Label(
        frame_ques,
        text="Question 1/{}".format(qtime),
        font=("Times", "16", "bold")
    )
    processshow.pack(padx=10, pady=10)

    # Input answer 
    inans = tk.Entry(
        frame_ques,
        bd=5,
        width=30,
        justify="center",
        relief="sunken"
    )
    inans.pack(padx=10, pady=10)

    setans = tk.Button(
        frame_ques,
        text=" ANSWER ",
        bd=5,
        relief="raised",
        font=("Times", "16", "bold"),
        command=getans
    )
    setans.pack(padx=10, pady=10)

    correctlbl = tk.Label(
        frame_ques,
        text="Correct/Incorrect showed",
        font=("Times", "16", "bold")
    )
    correctlbl.pack(padx=10, pady=10)

########## Question with selection ##########
def Qselect_menu():
    global frame_Qselect
    global qselect, inans2, selectset, setans2, pausebtn2
    global qwrg
    global hour, min, sec, timeframe2

    frame_start.destroy()

    frame_Qselect = tk.Frame(root)
    frame_Qselect.pack()

    qwrg = list(set(qwrg))
    qwrg = sorted(qwrg)

    frame_Qselect2 = tk.Frame(frame_Qselect)
    timeframe2=tk.Frame(frame_Qselect2,bg = "#7FFFD4", width =18,)

    hour = tk.Label(
        timeframe2,
        text = "00",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )

    dot1 = tk.Label(
        timeframe2,
        text = ":",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )

    min = tk.Label(
        timeframe2,
        text = "00",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )

    dot2 = tk.Label(
        timeframe2,
        text = ":",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )

    sec = tk.Label(
        timeframe2,
        text = "00",
        bg = "#7FFFD4",
        font=("Times", "16", "bold")
    )


    # show score
    scorelbl2 = tk.Label(
        frame_Qselect2,
        text =  "Score : " + str(score),
        font=("Times", "16", ),
        bg = "#7FFFD4",
        width =24
    )

    # pause
    pausebtn2 = tk.Button(
        frame_Qselect2,
        text = "QUIT",
        font=("Times", "16", ),
        bg = "#7FFFD4",
        width =18,
        command=start_menu
    )

    frame_Qselect2.pack()
    timeframe2.pack(fill="x", padx=10, side = 'left')
    hour.pack(padx=5, side = "left")
    dot1.pack(padx=5, side = "left")
    min.pack(padx=5, side = "left")
    dot2.pack(padx=5, side = "left")
    sec.pack(padx=5, side = "left")
    scorelbl2.pack(fill="x", padx=10, side = 'left')
    pausebtn2.pack(fill="x", padx=10, side = 'left')

    qselect = ttk.Combobox(
        frame_Qselect,
        justify="center",
        textvariable= tk.IntVar(),
        height=20,
        values=qwrg,
        state = "readonly"
    )
    qselect.pack()

    selectset = tk.Button(
        frame_Qselect,
        text="SELECT",
        command=selectQ
    )
    selectset.pack()
    

    # Input answer 
    inans2 = tk.Entry(
        frame_Qselect,
        bd=5,
        width=30,
        justify="center",
        relief="sunken",
        state="disable"
    )
    inans2.pack(padx=10, pady=10)

    setans2 = tk.Button(
        frame_Qselect,
        text=" ANSWER ",
        bd=5,
        relief="raised",
        font=("Times", "16", "bold"),
        command=getans2,
        state="disable"
    )
    setans2.pack(padx=10, pady=10)


########## Result ##########
def result_menu():
    global frame_result
    global cnum

    frame_ques.destroy()
    timestop()

    frame_result = ttk.Frame(root)
    frame_result.pack(fill = tk.BOTH, pady=20)
    
    if float(cnum)/float(qtime) >= 0.7 and float(cnum)/float(qtime) < 1.0:
        resultcmmt = tk.Label(frame_result,bd=5,text=" Congulaturation !! ",font=("Times", "32", ))
        resultcmmt.pack()
    
    elif float(cnum)/float(qtime) == 1.0:
        resultcmmt = tk.Label(frame_result,bd=5,text=" Incredible !!! ",font=("Times", "32", ))
        resultcmmt.pack()
    else:
        resultcmmt = tk.Label(frame_result,bd=5,text=" Well done ! ", font=("Times", "32", ))
        resultcmmt.pack()
    
    ratiocorrect = tk.Label(frame_result, bd=5, text="Your ratio of correct : {:02} %".format(int(float(cnum) * 100 / float(qtime))), font=("Times", "32", ))
    ratiocorrect.pack()
    cnum = 0 

    timetaken = tk.Label(frame_result, bd=5, text="Time you took : {:02}:{:02}:{:02}".format(hcount, mcount, scount), font=("Times", "32", ))
    timetaken.pack()    

    backstart2 = tk.Button(
        frame_result,
        bd=5,
        text=" Back ",
        font=("Times", "16", ),
        bg = "#7FFFD4",  
        command=start_menu
        )
    backstart2.pack(pady = 10)


########## Settings ##########
def setting_menu():
    global frame_setting
    global qtimebox
    global qtimeshow
    global scorelbl4

    frame_start.destroy()

    frame_setting = ttk.Frame(root)
    frame_setting.pack(fill = tk.BOTH, pady=20)

    scorelbl4 = tk.Label(
        frame_setting,
        text = "Score : " + str(score),
        font=("Times", "16", ),
        bg = "#7FFFD4",
        width =24
    )
    scorelbl4.pack(side=tk.TOP)

    RESETSCORE = tk.Button(
        frame_setting, 
        bd=5,
        text=" Reset your score ",
        font=("Times", "16", ),
        bg = "#7FFFD4",
        command = score0
        )
    
    qtimeshow = tk.Label(
        frame_setting,
        bd=5,
        text = "Question number in 1 try : " + str(qtime),
        font=("Times", "16", ),
        bg = "#7FFFD4",
    )


    qtimebox = ttk.Combobox(
        frame_setting,
        height = 20,
        values= opt_qtime,
        textvariable= tk.IntVar(),
        justify = "center",
        state = "readonly"
    )
    
    qtimeset = tk.Button(
        frame_setting,
        bd = 5,
        command=qtimechange,
        text="Question number in 1 try SET ",
        font=("Times", "16", ),
        bg = "#7FFFD4"
    )

    backstart = tk.Button(
        frame_setting,
        bd=5,
        text=" Back ",
        font=("Times", "16", ),
        bg = "#7FFFD4",  
        command=start_menu
        )

    # 各種ウィジェットの設置
    RESETSCORE.pack(pady = 30)
    qtimeshow.pack(pady=10)
    qtimebox.pack(pady=10)
    qtimeset.pack(pady=10)
    backstart.pack(pady = 10)

# Pause
def pause_menu():
    global frame_pause

    frame_pause = tk.Frame(
        root,
        bd = 5,
        width=600,
        height=400, 
        bg="gray",
        relief=tk.RAISED
    )
    frame_pause.place(relx=0.125, rely=0.1)

    backbtn = tk.Button(
        frame_pause,
        text = " Back to START menu ",
        font=("Times", "16", ),
        bd=5,
        command = start_menu
    )
    backbtn.place(relx=0.35, rely=0.3)

    resumebtn = tk.Button(
        frame_pause,
        text = " Resume ",
        font=("Times", "16", ),
        bd=5,
        command = resumefnc
    )
    resumebtn.place(relx=0.45, rely=0.6)

def resume():
    try:
        frame_pause.destroy()
    except NameError:
        pass

def disable_pause():
    pausebtn["state"] = "disable"
    inans["state"] = "disable"
    setans["state"] = "disable"

def able_pause():
    pausebtn["state"] = "normal"
    inans["state"] = "normal"
    setans["state"] = "normal"

def pausefnc():
    pause_menu()
    disable_pause()

def resumefnc():
    resume()
    able_pause()

def qtimechange():
    global qtime
    qtime = int(qtimebox.get())
    qtimeshow["text"] = "Question number in 1 try : " + str(qtime)

def score0():
    global score
    score = 0
    scorelbl4["text"] = "Score : " + str(score)

def getans():
    global cnum
    global score
    global qcount
    global qtime 
    global qwrg



    if is_num(inans.get()) == float(ans[qnum[qcount]]):  # correctans input
            score += 10
            cnum = cnum + 1
            scorelbl["text"] = "Score : " + str(score)
            correctlbl["text"] = " Correct ! "

    else: # incorrect answer
            correctlbl["text"] = " Incorrect "
            qwrg.append(qnum[qcount])
    

    
    inans.delete(0, tk.END) # delete former answer
    qcount = qcount + 1

    if qcount == qtime: # final question
        #reset parameters             
        qcount = 0
        cv2.destroyAllWindows()
        disable_pause()
        toresult= tk.Button(
            frame_ques,
            bd=5,
            text="See your result ",
            font=("Times", "16", ),
            bg = "#7FFFD4",
            anchor= tk.S,
            command=result_menu
        ) 
        toresult.pack()
    else:
        processshow["text"] = "Question {}/{}".format(qcount+1, qtime)
        qshow(qnum[qcount])

# output question.png by cv2
def qshow(qnum): # show questions with png
    qimg = cv2.imread(exepath + "Questions\Question" + str(qnum) + ".png") 
    #qimg = cv2.resize(qimg, (900, 1000))
    cv2.imshow("Question", qimg)
    cv2.moveWindow("Question", 0, 0 ) #DEsktop : 1000, 0  NotePC : 550, 0
    cv2.waitKey(1)

def is_num(t):  # check input is number or not
    try:
        return float(t)
    except ValueError:
        inans.delete(0, tk.END)

# for timer
def update_time():
    global timeframe, hour, min, sec, hcount, mcount, scount
    global after_id

    after_id = root.after(asecond, update_time)

    scount = scount + 1

    if scount == 60:
        scount = 0
        mcount = mcount + 1
        sec["text"] = "{:02}".format(scount)
        min["text"] = "{:02}".format(mcount)
    else: 
        sec["text"] = "{:02}".format(scount)

    if mcount == 60:
        mcount = 0
        hcount = hcount + 1
        min["text"] = "{:02}".format(mcount)
        hour["text"] = "{:02}".format(hcount)

# start timer
def timestart():
    global root
    global start_flag
    global after_id

    if not start_flag:
        start_flag = True

        after_id = root.after(asecond, update_time)

# stop timer
def timestop():
    global start_flag
    global after_id

    if start_flag:
        root.after_cancel(after_id)

        start_flag = False

# in start2, select question
def selectQ():
    global qnum2
    qnum2 = qselect.get()

    if qnum2 != "":
        qselect["state"] = "disable"
        selectset["state"] = "disable"
        inans2["state"] = "normal"
        setans2["state"] = "normal"
        qshow(qnum2)
        timestart()

# in start2, check coorect or incorrect answer
def getans2():

    inans2["state"] = "disable"
    setans2["state"] = "disable"

    timestop()
    if is_num(inans2.get()) == float(ans[int(qnum2)]):  # correctans input
        selectlbl = tk.Label(
            frame_Qselect,
            text="Correct !"
        )
        selectlbl.pack()
        qwrg.remove(int(qnum2))

    else:
        selectlbl = tk.Label(
            frame_Qselect,
            text="Incorrect"
        )
        selectlbl.pack()
    
    pausebtn2["state"] = "disable"
    backstart2 = tk.Button(
        frame_Qselect,
        bd=5,
        text=" Back ",
        font=("Times", "16", ),
        bg = "#7FFFD4",  
        command=start_menu
        )
    backstart2.pack(pady = 10)


# MAIN LOOP
if __name__ == "__main__":
    
    global frame_start


    #Base
    root = tk.Tk()
    root.geometry('800x600')  # Size
    root.title('RE4M')        # Title

    frame_start = ttk.Frame(root)
    frame_start.pack(fill = tk.BOTH, pady=20)

    scorelbl3 = tk.Label(
        frame_start,
        text = "Score : " + str(score),
        font=("Times", "16", ),
        bg = "#7FFFD4",
        width =24
    )
    scorelbl3.pack(side=tk.TOP)

    LOGO = tk.Label(
        frame_start, 
        bd=20,
        bg="gray",
        text=" RE4M ",
        font=("Times", "140", "bold"),
        relief=tk.RAISED
    )
    LOGO.pack(padx = 30, pady = 20)   # Show LOGO
    
    # Randomly
    start1 = tk.Button(
        frame_start,
        bd=5,
        text=" START RANDOMLY ",
        font=("Times", "16", ),
        bg = "#7FFFD4",
        command=ques_menu
    ) 
    start1.pack(pady = 10)

    # with selection
    start2 = tk.Button(
        frame_start,
        bd=5,
        text=" START WITH SELECTION ",
        font=("Times", "16", ),
        bg = "#7FFFD4",
        state = "disabled",
        command=Qselect_menu
    ) 
    start2.pack(pady = 10)

    # config
    setting= tk.Button(
        frame_start,
        bd=5,
        text=" SETTINGS ",
        font=("Times", "16", ),
        bg = "#7FFFD4",
        command=setting_menu
    ) 
    setting.pack(pady = 10)


    root.mainloop()