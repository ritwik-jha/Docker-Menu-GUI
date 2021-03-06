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
    op_win = LabelFrame(main,pady=250)
    op_win.grid(row=0, column=0)
    Label(op_win, text=output, font=('arial',10)).grid(row=0, column=0, pady=50)
    Button(op_win, text='Go Back', command=main_menu).grid(row=1, column=0, pady=50)

def all_conlist():
    root.destroy()
    output = sp.getoutput('docker ps -a')
    op_win = LabelFrame(main, pady=250)
    op_win.grid(row=0, column=0)
    Label(op_win, text=output, font=('arial',10)).grid(row=0, column=0, pady=50)
    Button(op_win, text='Go Back', command=main_menu).grid(row=1, column=0, pady=50)

def image_pull_op():
    image_name = e.get()
    print(image_name)
    output = sp.getoutput('docker pull {}'.format(image_name))
    image_pull_op_win = Toplevel()
    Label(image_pull_op_win, text=output).grid(row=2, column=0, columnspan=2)

def image_pull():
    root.destroy()
    op_win = LabelFrame(main, padx=120, pady=300)
    op_win.grid(row=0, column=0)
    global e
    e = Entry(op_win)
    Label(op_win, text='Enter name of image').grid(row=0, column=0, padx=5, pady=10)
    e.grid(row=0, column=1, pady=10, padx=5)
    Button(op_win, text='Submit', command=image_pull_op).grid(row=1, column=0, padx=10)
    Button(op_win, text='Go Back', command=main_menu).grid(row=1, column=1, pady=50,padx=10)


def docker_run():
    root.destroy()
    op_win = LabelFrame(main,padx=10,pady=250)
    op_win.grid(row=0, column=0)
    Label(op_win, text='''To launch a container with interactive mode run the following command in the terminal: 
    \n docker   run   -it   --name     con_name     image_to_be_used''').grid(row=0,column=0)
    Button(op_win, text='Go Back', command=main_menu).grid(row=1, column=0, pady=50)

def docker_run_bg_op():
    con_name = e3.get()
    docker_run_image = e4.get()
    output = sp.getoutput('docker run -dit --name {} {}'.format(con_name, docker_run_image))
    docker_run_op_win = Toplevel()
    Label(docker_run_op_win, text=output).grid(row=3, column=0, columnspan=2, padx=10)    

def docker_run_bg():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=250)
    op_win.grid(row=0, column=0)
    global e3
    e3 = Entry(op_win)
    Label(op_win, text='Enter name of container: ').grid(row=0, column=0, padx=5, pady=10)
    e3.grid(row=0, column=1, pady=10, padx=5)
    global e4
    e4 = Entry(op_win)
    Label(op_win, text='Enter name of image: ').grid(row=1, column=0, padx=5, pady=10)
    e4.grid(row=1, column=1, pady=10, padx=5)
    

    Button(op_win, text='Submit', command=docker_run_bg_op).grid(row=2, column=0, padx=10, pady=20)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)


def con_fg():
    root.destroy()
    op_win = LabelFrame(main,pady=250, padx=10)
    op_win.grid(row=0, column=0)
    Label(op_win, text='''To attach a container running in background run the following command in the terminal: 
    \n docker  attach  con_name ''').grid(row=0,column=0)
    Button(op_win, text='Go Back', command=main_menu).grid(row=1, column=0, pady=50)

def con_stop_op():
    con_name = e6.get()
    output = sp.getoutput('docker stop {}'.format(con_name))
    docker_run_op_win = Toplevel()
    tex = 'container stopped successfully \n name/id:  {}'.format(output)
    Label(docker_run_op_win, text=tex).grid(row=3, column=0, columnspan=2, padx=10)


def con_stop():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=250)
    op_win.grid(row=0, column=0)
    global e6
    e6 = Entry(op_win)
    Label(op_win, text='Enter name/id of container: ').grid(row=0, column=0, padx=5, pady=10)
    e6.grid(row=0, column=1, pady=10, padx=5)

    Button(op_win, text='Submit', command=con_stop_op).grid(row=2, column=0, padx=10, pady=20)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)

def con_ter_op():
    con_name = e7.get()
    output = sp.getoutput('docker rm {}'.format(con_name))
    docker_run_op_win = Toplevel()
    tex = 'Container terminated successfully \n Name/Id:  {}'.format(output)
    Label(docker_run_op_win, text=tex).grid(row=3, column=0, columnspan=2, padx=10)

def con_terminate():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=250)
    op_win.grid(row=0, column=0)
    global e7
    e7 = Entry(op_win)
    Label(op_win, text='Enter name/id of container: ').grid(row=0, column=0, padx=5, pady=10)
    e7.grid(row=0, column=1, pady=10, padx=5)
    
    Button(op_win, text='Submit', command=con_ter_op).grid(row=2, column=0, padx=10, pady=20)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)


def all_con_stop():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    output = sp.getoutput('docker stop $(docker ps -aq)')
    tex = 'Successfully stopped the following containers: \n' + output
    Label(op_win, text=tex).grid(row=1, column=0)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=0, pady=50)


def all_con_terminate():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=200)
    op_win.grid(row=0, column=0)
    output = sp.getoutput('docker rm $(docker ps -aq)')
    tex = 'Successfully terminated the following containers: \n' + output
    Label(op_win, text=tex).grid(row=1, column=0)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)


def delete_image_op():
    image_delete_name = e7.get()
    output = sp.getoutput('docker rmi {}'.format(image_delete_name))
    op_win = Toplevel()
    Label(op_win, text='Image deleted successfully \n {}'.format(output)).grid(row=1, column=0, columnspan=2, padx=110, pady=200)


def delete_image():
    root.destroy()
    op_win = LabelFrame(main, padx=130, pady=250)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter name of image: ').grid(row=0, column=0)
    global e7
    e7 = Entry(op_win)
    e7.grid(row=0, column=1)

    Button(op_win, text='Submit', command=delete_image_op).grid(row=2, column=0, padx=10, pady=20)
    Button(op_win, text='Go Back', command=main_menu).grid(row=2, column=1, pady=50)


def command_run_op():
    image_to_use = e8.get()
    command = e9.get()
    output = sp.getoutput('docker run {}  {}'.format(image_to_use, command))
    op_win = Toplevel()
    Label(op_win, text=output).grid(row=2, column=0, columnspan=2)

def command_run():
    root.destroy()
    op_win = LabelFrame(main, padx=130, pady=250)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter the name of image: ').grid(row=0, column=0, pady=20)
    global e8
    e8=Entry(op_win)
    e8.grid(row=0, column=1)
    Label(op_win, text='Command to run: ').grid(row=1, column=0, pady=20)
    global e9
    e9 = Entry(op_win)
    e9.grid(row=1, column=1)
    
    Button(op_win, text='Submit', command = command_run_op).grid(row=2, column=0)
    Button(op_win, text='Back', command=main_menu).grid(row=2, column=1)


def command_run_ter_op():
    image_to_use_ter = e10.get()
    command_ter = e11.get()
    output = sp.getoutput('docker run --rm {}  {}'.format(image_to_use_ter, command_ter))
    op_win = Toplevel()
    Label(op_win, text=output).grid(row=2, column=0, columnspan=2)


def command_run_terminate():
    root.destroy()
    op_win = LabelFrame(main, padx=120, pady=250)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter the name of image: ').grid(row=0, column=0, pady=20)
    global e10
    e10=Entry(op_win)
    e10.grid(row=0, column=1)
    Label(op_win, text='Command to run: ').grid(row=1, column=0, pady=20)
    global e11
    e11 = Entry(op_win)
    e11.grid(row=1, column=1)
    
    Button(op_win, text='Submit', command = command_run_ter_op).grid(row=2, column=0)
    Button(op_win, text='Back', command=main_menu).grid(row=2, column=1)

def inspect_op():
    inspect_con = e12.get()
    output = sp.getoutput('docker inspect {}'.format(inspect_con))
    op_win = Toplevel()
    Label(op_win, text=output).grid(row=2, column=0, columnspan=2)


def inspect():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=250)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter the name/id of container: ').grid(row=0, column=0, pady=20)
    global e12
    e12=Entry(op_win)
    e12.grid(row=0, column=1)
    
    Button(op_win, text='Submit', command = inspect_op).grid(row=2, column=0)
    Button(op_win, text='Back', command=main_menu).grid(row=2, column=1)

def logs_op():
    logs_con = e13.get()
    output = sp.getoutput('docker logs {}'.format(logs_con))
    op_win = Toplevel()
    Label(op_win, text=output).grid(row=2, column=0, columnspan=2)

def get_logs():
    root.destroy()
    op_win = LabelFrame(main, padx=110, pady=250)
    op_win.grid(row=0, column=0)
    Label(op_win, text='Enter the name/id of container: ').grid(row=0, column=0, pady=20)
    global e13
    e13=Entry(op_win)
    e13.grid(row=0, column=1)
    
    Button(op_win, text='Submit', command = logs_op).grid(row=2, column=0)
    Button(op_win, text='Back', command=main_menu).grid(row=2, column=1)

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
    widgets = main.winfo_children()
    for widget in widgets:
        widget.destroy()
    #op_win.destroy()
    #main.destroy()
    root = LabelFrame(main, pady=30)
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

