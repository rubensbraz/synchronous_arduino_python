import serial
import time
import sys

# Configuration
ARDUINO_PORT = "COM6"  # Change this to your specific port (e.g., /dev/ttyUSB0 on Linux/Mac)
BAUD_RATE = 9600
TIMEOUT = 1.0  # Seconds to wait for a response

def main():
    try:
        # Initialize Serial Connection
        ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=TIMEOUT)
        print(f"Connected to {ARDUINO_PORT} at {BAUD_RATE} baud.")
        
        # Wait for Arduino to reset after connection is established
        print("Waiting for Arduino to reset...")
        time.sleep(2) 
        
        # Clear buffers
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        print("Ready to send commands.\n")

        while True:
            # 1. Get input from user
            user_input = input("Enter command to Arduino (or 'q' to quit): ")

            if user_input.lower() == 'q':
                print("Exiting...")
                break

            # 2. Send data to Arduino
            # We add a newline character '\n' so the Arduino knows the message ended
            ser.write((user_input + "\n").encode("utf-8"))

            # 3. Wait for response (Synchronous part)
            # The script blocks here until a line is received or timeout occurs
            if ser.in_waiting or True: # We attempt to read immediately
                response = ser.readline().decode("utf-8").strip()
                
                if response:
                    print(f"Arduino replied: {response}")
                else:
                    print("Error: No response from Arduino (Timeout).")

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial connection closed.")

if __name__ == "__main__":
    main()
