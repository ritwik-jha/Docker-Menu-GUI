# DOCKER GRAPHICAL MENU

## INTRODUCTION
Docker is a container engine which can be used to launch containers in seconds. Now-a-days containers are used for deploying most of the application. Containers have a lot of 
perks over the traditional bare-metal system. One of the most applauded feature of containers is that it can be launched in seconds. 

In this project we have created a docker menu app which will act as an interface between the user and the docker service. The app connects to the docker daemon running in the system. The user no longer needs to remember the docker commands. 
The user can simply ask the program what he/she wants to do and the program will do it behind the scene. The is graphical in nature so that provides the user releive from the black terminal screen. 

The app is created using python as language and tkinter GUI framework. The app can be run in any os provided that the tkinter module is installed and docker is installed 
and docker service is running. 

## Features
Version 1.0 of the docker menu provides the following features:
1. Image list
2. Running container list
3. All containers list
4. Image pull
5. Container launch
6. Container launch in background
7. Foreground a container running in background
8. Container stop
9. Container terminate
10. All container stop
11. All container terminate
12. Delete docker image
13. Run a command in docker
14. Inspecting a docker container
15. Getting logs of a container

## Working
To run the program clone the repo in local system in which python, tkinter and docker are installed, run the following command in the repo folder:
```bash
python menu.py
```
OR 
```bash
python3 menu.py
```


### Main window
![image](https://user-images.githubusercontent.com/59885389/116812131-c088b580-ab6a-11eb-9355-463b45324846.png)
