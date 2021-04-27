from tkinter import *
import subprocess as sp
from tkinter import messagebox

main = Tk()
main.title('Docker')
main.geometry('500x650')

#functions
def imagelist():
    root.destroy()
    output = sp.getoutput('docker images')
    op_win = LabelFrame(main, padx=80, pady=300)
    op_win.grid(row=0, column=0)
    Label(op_win, text=output, font=('arial',10)).grid(row=0, column=0, pady=50)
    Button(op_win, text='Go Back', command=main_menu).grid(row=1, column=0, pady=50)
def running_conlist():
    root.destroy()
    output = sp.getoutput('docker ps')
    op_win = LabelFrame(main, padx=80, pady=300)
    op_win.grid(row=0, column=0)
    Label(op_win, text=output, font=('arial',10)).grid(row=0, column=0, pady=50)
    Button(op_win, text='Go Back', command=main_menu).grid(row=1, column=0, pady=50)

def all_conlist():
    root.destroy()
    output = sp.getoutput('docker ps -a')
    op_win = LabelFrame(main, padx=80, pady=300)
    op_win.grid(row=0, column=0)
    Label(op_win, text=output, font=('arial',10)).grid(row=0, column=0, pady=50)
    Button(op_win, text='Go Back', command=main_menu).grid(row=1, column=0, pady=50)

def image_pull_op():
    output = sp.getoutput('docker pull {}'.format(image_name))
    image_pull_op_win = Toplevel()
    Label(image_pull_op_win, text=output).grid(row=2, column=0, columnspan=2)

def image_pull():
    root.destroy()
    op_win = LabelFrame(main, padx=80, pady=300)
    op_win.grid(row=0, column=0)
    e = Entry(op_win)
    Label(op_win, text='Enter name of image').grid(row=0, column=0, padx=5, pady=10)
    e.grid(row=0, column=1, pady=10, padx=5)
    global image_name
    image_name = e.get()
    Button(op_win, text='Submit', command=image_pull_op).grid(row=1, column=0, columnspan=2, padx=10)
    Button(op_win, text='Go Back', command=main_menu).grid(row=1, column=0, pady=50)

def docker_run_op():
    output = sp.getoutput('docker run -it --name {} {}'.format(con_name, docker_run_image))
    docker_run_op_win = Toplevel()
    Label(docker_run_op_win, text=output).grid(row=3, column=0, columnspan=2, padx=10)

def docker_run():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    e1 = Entry(op_win)
    Label(op_win, text='Enter name of container: ').grid(row=0, column=0, padx=5, pady=10)
    e1.grid(row=0, column=1, pady=10, padx=5)
    global con_name
    con_name = e1.get()
    e2 = Entry(op_win)
    Label(op_win, text='Enter name of image: ').grid(row=1, column=0, padx=5, pady=10)
    e2.grid(row=1, column=1, pady=10, padx=5)
    global docker_run_image
    docker_run_image = e2.get()
    Button(op_win, text='Submit', command=docker_run_op).grid(row=2, column=0, padx=10, pady=20)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)

def docker_run_bg_op():
    output = sp.getoutput('docker run -dit --name {} {}'.format(con_name, docker_run_image))
    docker_run_op_win = Toplevel()
    Label(docker_run_op_win, text=output).grid(row=3, column=0, columnspan=2, padx=10)    

def docker_run_bg():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    e1 = Entry(op_win)
    Label(op_win, text='Enter name of container: ').grid(row=0, column=0, padx=5, pady=10)
    e1.grid(row=0, column=1, pady=10, padx=5)
    global con_name
    con_name = e1.get()
    e2 = Entry(op_win)
    Label(op_win, text='Enter name of image: ').grid(row=1, column=0, padx=5, pady=10)
    e2.grid(row=1, column=1, pady=10, padx=5)
    global docker_run_image
    docker_run_image = e2.get()
    Button(op_win, text='Submit', command=docker_run_bg_op).grid(row=2, column=0, padx=10, pady=20)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)

def docker_fg_op():
    output = sp.getoutput('docker attach {}'.format(con_name))
    docker_run_op_win = Toplevel()
    Label(docker_run_op_win, text=output).grid(row=3, column=0, columnspan=2, padx=10)

def con_fg():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    e1 = Entry(op_win)
    Label(op_win, text='Enter name/id of container: ').grid(row=0, column=0, padx=5, pady=10)
    e1.grid(row=0, column=1, pady=10, padx=5)
    global con_name
    con_name = e1.get()
    Button(op_win, text='Submit', command=docker_fg_op).grid(row=2, column=0, padx=10, pady=20)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)

def con_stop_op():
    output = sp.getoutput('docker stop {}'.format(con_name))
    docker_run_op_win = Toplevel()
    Label(docker_run_op_win, text=output).grid(row=3, column=0, columnspan=2, padx=10)


def con_stop():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    e1 = Entry(op_win)
    Label(op_win, text='Enter name/id of container: ').grid(row=0, column=0, padx=5, pady=10)
    e1.grid(row=0, column=1, pady=10, padx=5)
    global con_name
    con_name = e1.get()
    Button(op_win, text='Submit', command=con_stop_op).grid(row=2, column=0, padx=10, pady=20)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)

def con_ter_op():
    output = sp.getoutput('docker rm {}'.format(con_name))
    docker_run_op_win = Toplevel()
    Label(docker_run_op_win, text=output).grid(row=3, column=0, columnspan=2, padx=10)

def con_terminate():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    e1 = Entry(op_win)
    Label(op_win, text='Enter name/id of container: ').grid(row=0, column=0, padx=5, pady=10)
    e1.grid(row=0, column=1, pady=10, padx=5)
    global con_name
    con_name = e1.get()
    Button(op_win, text='Submit', command=con_ter_op).grid(row=2, column=0, padx=10, pady=20)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)


def all_con_stop():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    output = sp.getoutput('docker stop $(docker ps -aq)')
    Label(op_win, text=output).grid(row=1, column=0)

def all_con_terminate():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    output = sp.getoutput('docker rm $(docker ps -aq)')
    Label(op_win, text=output).grid(row=1, column=0)

def delete_image():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter name of image: ').grid(row=0, column=0, padx=110, pady=200)
    e = Entry(op_win)
    e.grid(row=0, column=1, padx=110, pady=200)
    image_delete_name = e.get()
    output = sp.getoutput('docker rmi {}'.format(image_delete_name))
    Label(op_win, text='Image deleted successfully \n {}'.format(output)).grid(row=1, column=0, columnspan=2, padx=110, pady=200)

def command_run_op():
    output = sp.getoutput('docker run {}  {}'.format(image_to_use, command))
    op_win = Toplevel()
    Label(op_win, text=output).grid(row=2, column=0, columnspan=2)

def command_run():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter the name of image: ').grid(row=0, column=0, pady=20)
    e1=Entry(op_win)
    e1.grid(row=0, column=1)
    global image_to_use
    image_to_use = e1.get()
    Label(op_win, text='Command to run: ').grid(row=1, column=0, pady=20)
    e2 = Entry(op_win)
    e2.grid(row=1, column=1)
    global command
    command = e2.get()
    Button(op_win, text='Submit', command = command_run_op).grid(row=2, column=0)
    Button(op_win, text='Back', command=main_menu).grid(row=2, column=1)


def command_run_ter_op():
    output = sp.getoutput('docker run --rm {}  {}'.format(image_to_use_ter, command_ter))
    op_win = Toplevel()
    Label(op_win, text=output).grid(row=2, column=0, columnspan=2)


def command_run_terminate():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter the name of image: ').grid(row=0, column=0, pady=20)
    e1=Entry(op_win)
    e1.grid(row=0, column=1)
    global image_to_use_ter
    image_to_use_ter = e1.get()
    Label(op_win, text='Command to run: ').grid(row=1, column=0, pady=20)
    e2 = Entry(op_win)
    e2.grid(row=1, column=1)
    global command_ter
    command_ter = e2.get()
    Button(op_win, text='Submit', command = command_run_ter_op).grid(row=2, column=0)
    Button(op_win, text='Back', command=main_menu).grid(row=2, column=1)

def inspect_op():
    output = sp.getoutput('docker inspect {}'.format(inspect_con))
    op_win = Toplevel()
    Label(op_win, text=output).grid(row=2, column=0, columnspan=2)


def inspect():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter the name/id of container: ').grid(row=0, column=0, pady=20)
    e1=Entry(op_win)
    e1.grid(row=0, column=1)
    global inspect_con
    inspect_con = e1.get()
    Button(op_win, text='Submit', command = inspect_op).grid(row=2, column=0)

def logs_op():
    output = sp.getoutput('docker logs {}'.format(logs_con))
    op_win = Toplevel()
    Label(op_win, text=output).grid(row=2, column=0, columnspan=2)

def get_logs():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter the name/id of container: ').grid(row=0, column=0, pady=20)
    e1=Entry(op_win)
    e1.grid(row=0, column=1)
    global logs_con
    logs_con = e1.get()
    Button(op_win, text='Submit', command = logs_op).grid(row=2, column=0)

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
    elif option == 7:
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
    else:
        messagebox.showerror(message='Please select a task')

def main_menu():
    global root
    root = LabelFrame(main)
    root.grid(row=0, column=0)
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

main_menu()
main.mainloop()

