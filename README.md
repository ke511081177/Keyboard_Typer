# Keyboard_Stroker

## Intro

- A program that can record keyboard event scripts and read stored scripts and run automated.


## Requirement

    pip install keyboard
    
    
## Run
- Can choose mode
    - new **(defult)**
    - load 

python keyboard_stroker.py -m new

## Pipeline

- new

    1.  `python keyboard_stroker.py -m new `  
    
    2.  Press `f2` to start record keyboard event script.
    3.  Press `f2` to stop and store the script to a txt file. `ex.Script.txt`
    4.  Wait 5 sec to start the Script.
    5.  Press `esc` to stop.

- load
    1. `python keyboard_stroker.py -m load `
    2. load Script file and run. Can change file path&name in code. 


## Notice

Recommend execute as system administrator when you use it because some software will block background event.
