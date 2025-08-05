import serial
import time 

ser = serial.Serial('COM5', 115200, timeout = 1)
time.sleep(2)

while True:
    burst = input("Burst? ")
    if burst == "y":
        init = time.time() * 1000 
        ser.write(b'70\n')
        response = None
        while response != "DONE":
            response = ser.readline().decode().strip()
            print(response)
        print(f"command time taken {(time.time() * 1000) - init}")