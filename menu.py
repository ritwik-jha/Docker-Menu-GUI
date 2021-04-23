from tkinter import *
import subprocess as sp

root = Tk()
root.title('Docker')
root.geometry('500x650')

#functions
def imagelist():
    output = sp.getoutput('docker images')
    op_win = Toplevel()
    op_win.title('Output')
    Label(op_win, text=output, font=('arial',10)).pack()

def running_conlist():
    output = sp.getoutput('docker ps')
    op_win = Toplevel()
    op_win.title('Output')
    Label(op_win, text=output, font=('arial',10)).pack()

def all_conlist():
    output = sp.getoutput('docker ps -a')
    op_win = Toplevel()
    op_win.title('Output')
    Label(op_win, text=output, font=('arial',10)).pack()

def image_pull_op():
    output = sp.getoutput('docker pull {}'.format(image_name))
    Label(image_pull_op_win, text=output).grid(row=2, column=0, columnspan=2)

def image_pull():
    global image_pull_op_win
    image_pull_op_win = Toplevel()
    image_pull_op_win.title('Output')
    #image_pull_op_win.geometry('300x200')
    e = Entry(image_pull_op_win)
    Label(image_pull_op_win, text='Enter name of image').grid(row=0, column=0, padx=5, pady=10)
    e.grid(row=0, column=1, pady=10, padx=5)
    global image_name
    image_name = e.get()
    Button(image_pull_op_win, text='Submit', command=image_pull_op).grid(row=1, column=0, columnspan=2, padx=10)

def docker_run_op():
    output = sp.getoutput('docker run -it --name {} {}'.format(con_name, docker_run_image))
    Label(docker_run_op_win, text=output).grid(row=3, column=0, columnspan=2, padx=10)

def docker_run():
    global docker_run_op_win
    docker_run_op_win = Toplevel()
    docker_run_op_win.title('Output')
    #image_pull_op_win.geometry('300x200')
    e1 = Entry(docker_run_op_win)
    Label(docker_run_op_win, text='Enter name of container: ').grid(row=0, column=0, padx=5, pady=10)
    e1.grid(row=0, column=1, pady=10, padx=5)
    global con_name
    con_name = e1.get()
    e2 = Entry(docker_run_op_win)
    Label(docker_run_op_win, text='Enter name of image: ').grid(row=1, column=0, padx=5, pady=10)
    e2.grid(row=1, column=1, pady=10, padx=5)
    global docker_run_image
    docker_run_image = e2.get()
    Button(docker_run_op_win, text='Submit', command=docker_run_op).grid(row=2, column=0, columnspan=2, padx=10)

def docker_run_bg():
    return

def con_fg():
    return

def con_stop():
    return

def con_terminate():
    return

def all_con_stop():
    return

def all_con_terminate():
    return

def delete_image():
    return

def command_run():
    return

def command_run_terminate():
    return

def inspect():
    return

def get_logs():
    return

def getvalue():
    option = value.get()
    if option == 1:
        imagelist()
    elif option == 2:
        running_conlist()
    elif option == 3:
        all_conlist()
    elif option == 4:
        image_pull()
    elif option == 5:
        docker_run()
    elif option == 6:
        docker_run_bg()
    elif opiton == 7:
        con_fg()
    elif option == 8:
        con_stop()
    elif option == 9:
        con_terminate()
    elif option == 10:
        all_con_stop()
    elif option == 11:
        all_con_terminate()
    elif option == 12:
        delete_image()
    elif option == 13:
        command_run()
    elif option == 14:
        command_run_terminate()
    elif option == 15:
        inspect()
    elif option==16:
        get_logs()

Label(root, text='DOCKER MENU', font=('arial',20,'bold')).grid(row=0, column=0, columnspan=3, padx=120, sticky='W')
Label(root, text='').grid(row=1, column=0)
Label(root, text='').grid(row=2, column=0)
Label(root, text='Welcome to Docker menu what would you like to do?', font=('arial', 10)).grid(row=3, column=0, sticky='W',padx=80, pady=10)

global value
value = IntVar()

x=100

Radiobutton(root, text='List the docker images', variable=value, value=1).grid(row=4, column=0, sticky='W', padx=x)
Radiobutton(root, text='List the running docker containers', variable=value, value=2).grid(row=5, column=0, sticky='W', padx=x)
Radiobutton(root, text='List all the docker containers', variable=value, value=3).grid(row=6, column=0, sticky='W', padx=x)
Radiobutton(root, text='Pull a docker image', variable=value, value=4).grid(row=7, column=0, sticky='W', padx=x)
Radiobutton(root, text='Run a docker container with interactive terminal', variable=value, value=5).grid(row=8, column=0, sticky='W', padx=x)
Radiobutton(root, text='Run a docker container in background', variable=value, value=6).grid(row=9, column=0, sticky='W', padx=x)
Radiobutton(root, text='Foreground a container running in background', variable=value, value=7).grid(row=10, column=0, sticky='W', padx=x)
Radiobutton(root, text='Stop a running container', variable=value, value=8).grid(row=11, column=0, sticky='W', padx=x)
Radiobutton(root, text='Terminate a stopped container', variable=value, value=9).grid(row=12, column=0, sticky='W', padx=x)
Radiobutton(root, text='Stop all the containers', variable=value, value=10).grid(row=13, column=0, sticky='W', padx=x)
Radiobutton(root, text='Terminate all the stopped containers', variable=value, value=11).grid(row=14, column=0, sticky='W', padx=x)
Radiobutton(root, text='Delete a docker image', variable=value, value=12).grid(row=15, column=0, sticky='W', padx=x)
Radiobutton(root, text='Run a command in docker container', variable=value, value=13).grid(row=16, column=0, sticky='W', padx=x)
Radiobutton(root, text='Run a command in docker container and then termiate it', variable=value, value=14).grid(row=17, column=0, sticky='W', padx=x)
Radiobutton(root, text='Inspect a running container', variable=value, value=15).grid(row=18, column=0, sticky='W', padx=x)
Radiobutton(root, text='Get logs of running container', variable=value, value=16).grid(row=19, column=0, sticky='W', padx=x)


Button(root, text='Submit', command=getvalue, padx=20, pady=15).grid(row=20, column=0, pady=30)


root.mainloop()

