import random
import statistics
import datetime
import time
from tkinter import *
from tkinter import ttk 

### AUTHOR: SALIM DAMERDJI
### TIME: 4/12/2019
#################### GLOBAL VARIABLES ###############################################
FACTOR = None
FILENAME = 'RESULTS.csv'

# From https://www.thebalance.com/do-companies-with-female-executives-perform-better-4586443
TEXT0 = 'The University of California-Davis reported that the top 25 California companies with the highest percentage of women executives and board members saw a 74 percent higher return on assets and equity than the broader set of companies surveyed. This included companies such as William-Sonoma, Yahoo!, and Wells Fargo.'
# From https://www.catalyst.org/wp-content/uploads/2019/02/Women_Take_Care_Men_Take_Charge_Stereotyping_of_U.S._Business_Leaders_Exposed.pdf 
TEXT1 = 'We often think of leaders as dominant and ambitious—as embodying qualities that closely match the stereotype of men. On the other hand, the traits that make up the feminine stereotype (e.g., friendliness and sensitivity) are seen as less vital to leadership. These stereotypes result in women being evaluated less positively than men for leadership positions.' 

leader_stimuli = ['CEO', 'President', 'Manager', 'Figurehead', 'Superior']
supporter_stimuli = ['Assistant', 'Subordinate', 'Helper', 'Follower', 'Aide']
male_stimuli = ['Michael', 'James', 'David', 'John', 'Robert'] # 5 most popular male names from 1970s according to https://www.weddingvendors.com/baby-names/popular/1970/
female_stimuli = ['Jennifer', 'Lisa', 'Kimberly', 'Michelle', 'Amy'] # same as above

instructions_iat='Next, you will use the "e" and "i" computer keys to categorize items into groups as fast as you can. These are the four groups and the items that belong to each: \n \n Category \t \tWords \n Leader \t \t \t' + str(leader_stimuli) + '\n Supporter \t \t' + str(supporter_stimuli) + '\n Female \t \t \t' + str(female_stimuli) + '\n Male \t \t \t' + str(male_stimuli) + '\n \n There are five parts. The instructions change for each part. Pay attention!'

def make_instruction(key, category):
    if key == 'e' or key == 'E':
        return 'Press e for the ' + category + ' category.'
    else:
        return 'Press i for the ' + category + ' category.'

instructions={
        0:make_instruction('e', 'leader'),
        1:make_instruction('i', 'supporter'),
        2:make_instruction('e', 'male'),
        3:make_instruction('i', 'female'),
        4:make_instruction('e', 'leader or male'),
        5:make_instruction('i', 'supporter or female'),
        6:make_instruction('e', 'supporter'),
        7:make_instruction('i', 'leader'),
        8:make_instruction('e', 'supporter or male'),
        9:make_instruction('i', 'leader or female')
        }

###################### PICK FACTOR, 1 through 4 ####################################
# Used by submit_factor() so we know which treatments to apply later 
def set_factor(num):
    global FACTOR
    FACTOR = num

def pick_factor(frame):
    factor = IntVar()
    instr = ttk.Label(frame, text="Pick a factor", wraplength = 1000)
    one = ttk.Radiobutton(frame, text='1 - None', variable=factor, value=1)
    two = ttk.Radiobutton(frame, text='2 - Text0 Only', variable=factor, value=2)
    three = ttk.Radiobutton(frame, text='3 - Text1 Only', variable=factor, value=3)
    four = ttk.Radiobutton(frame, text='4 - Both', variable=factor, value=4)
    submit = ttk.Button(frame, text='Submit', command=lambda: submit_factor(frame, factor.get()))

    # Format all widgets
    i = 1
    for widget in [instr, one, two, three, four, submit]:
        widget.grid(column=0, row=i, padx=2, pady=2, sticky=(E,W))
        i += 1
    
def submit_factor(frame, val):
    set_factor(val)
    with open(FILENAME, "a") as myfile:
        myfile.write(str(val) + ",")
    clear(frame)
    pick_gender(frame)

########################### STUDENT INPUTS GENDER ####################################
def pick_gender(frame):
    gender = StringVar()
    ttk.Label(frame, text="Select your gender:", wraplength = 1000).grid(column=1,row=0)
    ttk.Radiobutton(frame, text='Male', variable=gender, value='Male').grid(column=1, row=1, sticky=(W,E))
    ttk.Radiobutton(frame, text='Female', variable=gender, value='Female').grid(column=1, row=2, sticky=(W,E))
    ttk.Button(frame, text='Submit', command=lambda: submit_gender(frame, gender.get())).grid(column=2, row=3)

def submit_gender(frame, gender):
    with open(FILENAME, "a") as myfile:
        myfile.write(gender + ",")
    clear(frame)
    treatments(frame)

########################### TREATMENT IS APPLIED TO SUBJECT ##########################
def treatments(frame):
    if FACTOR == 1:
        go_to_instructions(frame)
    elif FACTOR == 2:
        display_text(frame, TEXT0, lambda: go_to_instructions(frame))
    elif FACTOR == 3:
        display_text(frame, TEXT1, lambda: go_to_instructions(frame))
    elif FACTOR == 4:
        if random.randint(0,1):
            display_text(frame, TEXT0, lambda: next_text(frame, TEXT1))
        else:
            display_text(frame, TEXT1, lambda: next_text(frame, TEXT0))

def display_text(frame, text, fn):
    ttk.Label(frame, text=text, wraplength=1000).grid(column=0,row=0)
    ttk.Button(frame, text='Done Reading', command=fn).grid(column=0,row=1)

def next_text(frame, text):
    clear(frame)
    display_text(frame, text, lambda: go_to_instructions(frame))

def go_to_instructions(frame):
    clear(frame)
    iat_instructions(frame)

########################## STUDENT GETS IAT INSTRUCTIONS ##############################
def instructions_i(frame, i):
    if 0 <= i <= 4:
        clear(frame)
        instruction_helper(frame, i)
        ttk.Button(frame, text='Done Reading', command=lambda: stage_i(frame, i)).grid(column=1,row=1)
    else:
        finish(frame)

def iat_instructions(frame):
    ttk.Label(frame, text=instructions_iat, wraplength = 1000).grid(column=0,row=0)
    ttk.Button(frame, text='Done Reading', command=lambda: instructions_i(frame, 0)).grid(column=0,row=1)

def instruction_helper(frame, i):
    left = ttk.Label(frame, text=instructions[2*i], wraplength = 200)
    left.grid(column=0,row=0, sticky=W,padx=(100,0))
    left.config(font=('Arial', 18))
    right = ttk.Label(frame, text=instructions[2*i+1], wraplength = 200)
    right.grid(column=2,row=0, sticky=E,padx=(0,100))
    right.config(font=('Arial', 18))
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)

########################## STAGE i, for i in {1,2,3,4,5} ################################
def get_labels_i(i):
    e_labels, i_labels = [], []
    if i in [0,2]:
        e_labels.extend(leader_stimuli)
        i_labels.extend(supporter_stimuli)
    if i in [1,2,4]:
        e_labels.extend(male_stimuli)
        i_labels.extend(female_stimuli)
    if i in [3,4]:
        e_labels.extend(supporter_stimuli)
        i_labels.extend(leader_stimuli)
    return e_labels, i_labels

def stage_i(frame, i):
    clear(frame)

    e_labels, i_labels = get_labels_i(i)
    random_labels = random.sample(e_labels+i_labels, len(e_labels)+len(i_labels))  

    cur_label = StringVar()
    cur_label.set(random_labels.pop(0))

    instruction_helper(frame, i)
    center = ttk.Label(frame, text=cur_label.get(), wraplength=500)
    center.grid(column=1,row=1,sticky='N')
    center.config(font=('Arial',18))

    def new_center(new):
        center['text'] = new

    times = [time.time()]
    if cur_label.get() in e_labels:
        frame.focus_set()
        frame.bind('e', lambda x: next_label(frame, cur_label, random_labels, i, e_labels, times, new_center))
    else:
        frame.focus_set()
        frame.bind('i', lambda x: next_label(frame, cur_label, random_labels, i, e_labels, times, new_center))
        
def unbind_both(frame):
    frame.unbind('e')  
    frame.unbind('i')  

def next_label(frame, cur_label, labels, i, e_labels, times, new_center):
    times.append(time.time())
    unbind_both(frame)
    if labels:
        cur_label.set(labels.pop(0))
        new_center(cur_label.get())
        if cur_label.get() in e_labels: 
            frame.bind('e', lambda x: next_label(frame, cur_label, labels, i, e_labels, times, new_center))
        else:
            frame.bind('i', lambda x: next_label(frame, cur_label, labels, i, e_labels, times, new_center))
    else:
        write_times(times)
        instructions_i(frame, i+1)

def write_times(times):
    durations = [round(j-i,5) for i, j in zip(times[: -1], times[1 :])]

    with open(FILENAME, 'a') as myfile:
        for dur in durations:
            myfile.write(str(dur) + ',')

def clear(container):
    for widgets in container.winfo_children():
        widgets.destroy()

############################ THANK YOU #############################################
def finish(frame):
    clear(frame)
    ttk.Label(frame, text='Thank you for completing this experiment!', wraplength = 1000).grid(column=1,row=0)

############################ MAIN ##################################################

def col_maker_helper(stage_num):
    if stage_num in [1,2,4]:
        return [str(stage_num) + '_' + str(word) for word in list(range(10))]
    elif stage_num in [3,5]:
        return [str(stage_num) + '_' + str(word) for word in list(range(20))]
try:
    open(FILENAME, 'r')
except:
    with open(FILENAME, 'w') as myfile:
        myfile.write('time,factor,gender,')
        for i in range(1,6):
            for header in col_maker_helper(i):
                myfile.write(header + ',')

with open(FILENAME, 'a') as myfile:
    myfile.write('\n' + datetime.datetime.now().strftime('%H:%M:%S') + ',')

root = Tk() 
root.title("Experiment")
root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1) 

mainframe = ttk.Frame(root, padding=(10,10)) # create a frame widget
mainframe.grid(column=0,row=0,sticky=(N,E,W,S))
#mainframe.grid_columnconfigure(index=0,pad=100)
s = ttk.Style()
pick_factor(mainframe)
root.mainloop()
