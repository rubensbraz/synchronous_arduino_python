import serial  # You need to install pyserial, use "pip install pyserial" in your terminal

arduino_port = "COM6"  # Change for your Arduino Port
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

ser.flushInput()
ser.flushOutput()

while True:
    data_to_send = input("Send to Arduino: ")
    ser.write((data_to_send + "\n").encode("utf-8"))

    response = ser.readline().decode("utf-8").strip()
    print(response)

ser.close()
