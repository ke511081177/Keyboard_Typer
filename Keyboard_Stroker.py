import keyboard
from time import sleep
from argparse import ArgumentParser

def save_script(event):
  

  with open('Script.txt', 'a+') as f:
    f.write(str(event))
    f.close()

def main(args):
    if args.m == 'new':
            print("### Press F2 2 Start Record ###")
            keyboard.wait('f2')
            print("Start") 
            print("### Press F2 to Stop Record ###")
            event = keyboard.record(until='f2')
            save_script(event)

        if args.m == 'load':
            
            f = open('keylogger.txt', 'r')
            e = f.read()
            e = list(e)
            print("### Loading Successfully  ###")

    print('### wait 5 sec & Start  ###')
    print("### Press ESC to Stop the Program  ###")
    sleep(5)
    while True:
        keyboard.play(event, speed_factor=1)
        if keyboard.is_pressed('esc'):
            break

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-m", help="positional argument 1",default='new')
    args = parser.parse_args()
    print(args.m)
    
    main(args)
