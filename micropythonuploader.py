import serial, sys,time, os
from pathlib import Path

def sendByte(openPort, c):
    data = c
    line = "b = {} \r\nm.write(b)\r\n".format(data)
    openPort.write(line.encode())
    return

def showDisplay(filesize, current):
    os.system('cls')
    print("{} of {} bytes sent.".format(current, filesize))
    pass

def sendFile(com,baud,filename):
    port = serial.Serial(com, baud)
    port.write(b'x04\r\n')
    command = 'm = open("{}", "wb")\r\n'.format(filename)
    port.write(command.encode())
    filesize = os.path.getsize(filename)
    counter = 0
    with open(filename, 'rb') as f:
        while True:
            a = f.read(1024)
            if not a:
                print("Uploading {} finished.".format(filename))
                break
            counter += len(a)
            sendByte(port, a)
            showDisplay(filesize, counter)
            time.sleep(0.1)

    port.write(b'm.close()\r\n')
    port.close()
    
    
    pass


def main():
    if len(sys.argv) < 3:
        print("No Valid Argument")
        print("Use: micropythonuploader.py <port> <file>")
        return
    

    port = sys.argv[1]
    filetoupload = sys.argv[2]
    sendFile(port, 115200, filetoupload)
    



main()