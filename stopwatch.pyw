from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import time

root=Tk()
root.configure(background=("blue"))
root.title("Stopwatch")
root.geometry("500x379+410+0")
root.minsize(500,379)
root.maxsize(500,704)
root.iconbitmap('stopwatch.ico')
time_elapsed1=00
time_elapsed2=00
time_elapsed3=00
i=00
j=00
time1=00

def create_label(text,_x,_y):
    label = Label(root, text=text,fg='blue', bg="white",font=("System",20,"bold"))
    label.place(x=_x,y=_y,width=100,height=45)

def start():
    start_button.place_forget()
    stop_button.place(x = 0, y = 100, width=100, height=50)
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2
    time2=int(time.time())
    if time2!=time1:
        time1=time2
        if time_elapsed1<59:
            time_elapsed1+=1
            clock_frame.config(text=str(time_elapsed3) + ":" + str(time_elapsed2)+ ":" + str(time_elapsed1))
        else:
            time_elapsed1=0
            if time_elapsed2<59:
                time_elapsed2+=1
                clock_frame.config(text=(str(time_elapsed3) + ":" + str(time_elapsed2)+ ":" + str(time_elapsed1)))
            else:
                time_elapsed2=0
                if time_elapsed3<23:
                    time_elapsed3+=1
                    clock_frame.config(text=(str(time_elapsed3) + ":" + str(time_elapsed2)+ ":" + str(time_elapsed1)))
                else:
                    messagebox.showwarning("Response", "You left it on for too long")
    self_job=root.after(1000,start)

def stop():
    global self_job
    if self_job is not None:
        root.after_cancel(self_job)
        self_job = None
    stop_button.place_forget()
    start_button.place(x = 0, y = 100, width=100, height=50)

def clear():
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2,label,i,j
    try:
        stop()
    except:
        start()
        stop()
    clock_frame.config(text="0:0:0", font=("Helevtica", 100))
    time_elapsed1=0
    time_elapsed2=0
    time_elapsed3=0
    time_1=0
    time_2=0
    i=0
    j=0
    wig=root.winfo_children()
    for b in wig:
        b.place_forget()
    start_button.place(x = 0, y = 100, width=100, height=50)
    lap_button.place(x = 200, y = 100, width=100, height=50)
    reset_button.place(x = 400, y = 100, width=100, height=50)
    clock_frame.place(x = 0, y = 0, width=500, height=100)

def lap():
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2,i,j
    if i<5:
        create_label((str(time_elapsed3)+":"+str(time_elapsed2)+ ":" + str(time_elapsed1)), 0+(101*i),150+(j*46))
    else:
        j+=1
        i=0
        create_label((str(time_elapsed3)+":"+str(time_elapsed2)+ ":" + str(time_elapsed1)), 0+(101*i),150+(j*46))
    i+=1

clock_frame=Label(text="0:0:0",bg="black",fg="white",font=("Helevtica",100))
start_button=Button(text="START",bg="blue",fg="white",command=start,font=("Coral",20,"bold"))
stop_button=Button(text="PAUSE",bg="white",fg="blue",command=stop,font=("Coral",20,"bold"),relief="sunken")
lap_button=Button(text="LAP",bg="blue",fg="white",command=lap,font=("Coral",20,"bold"))
reset_button=Button(text="RESET",bg="blue",fg="white",command=clear,font=("Coral",20,"bold"))

start_button.place(x = 0, y = 100, width=100, height=50)
lap_button.place(x = 200, y = 100, width=100, height=50)
reset_button.place(x = 400, y = 100, width=100, height=50)
clock_frame.place(x = 0, y = 0, width=500, height=100)

root.mainloop()
