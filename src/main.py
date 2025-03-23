import machine
import time
button = machine.Pin(0)

def button_press():    
    f = open('data.txt')
    presses = int(f.read()) + 1
    f.close()
    f = open('data.txt', 'w')
    f.write(str(presses))
    f.close()
    print(presses)
while True:
    if button.value() == 1:
        button_press()
        time.sleep(.2)