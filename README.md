# Synchronous Serial Communication (Python & Arduino)

This project demonstrates a synchronous communication handshake between a computer (running Python) and an Arduino microcontroller. The Python script sends a command, and the Arduino processes it and returns a response.

## 📂 Project Structure

* `synchronous.py`: The Python script that acts as the "Master". It sends input commands and waits for a reply.
* `synchronous.ino`: The Arduino firmware that acts as the "Slave". It listens for commands and echoes a status back.

## 🛠 Prerequisites

### Hardware

* Arduino Board (Uno, Nano, Mega, etc.) 
* USB Cable

### Software

* [Python 3.x](https://www.python.org/)
* [Arduino IDE](https://www.arduino.cc/en/software)

### Python Libraries

You need the `pyserial` library to access the USB ports.
```bash
pip install pyserial
```

## ⚙️ Configuration

### 1. Arduino Setup

1.  Open `synchronous.ino` in the Arduino IDE.
2.  Connect your Arduino to the computer.
3.  Select your Board and Port in **Tools > Board** and **Tools > Port**.
4.  **Upload** the code.
5.  *Important:* Note the Port name (e.g., `COM6` or `/dev/ttyUSB0`) shown in the IDE.

### 2. Python Setup

1.  Open `synchronous.py` in your code editor.
2.  Locate the configuration section at the top:
    ```python
    # Configuration
    ARDUINO_PORT = "COM6"  # <-- Change this to your Port
    BAUD_RATE = 9600
    ```
3.  Update `ARDUINO_PORT` to match the port you found in the Arduino IDE.

## 🚀 How to Run

1.  **Close the Arduino IDE Serial Monitor**.
    * *Note:* The serial port can only be used by one program at a time. If the IDE is connected, Python cannot connect.
2.  Run the Python script via terminal:
    ```bash
    python synchronous.py
    ```
3.  Wait for the initialization message:
    ```text
    Connected to COM6 at 9600 baud.
    Waiting for Arduino to reset...
    Ready to send commands.
    ```
4.  Type a command (e.g., "Hello") and press Enter.

## 🐛 Troubleshooting

| Error | Solution |
| :--- | :--- |
| **`SerialException: Access is denied`** | Another program (like Cura or Arduino Serial Monitor) is using the port. Close them. |
| **`No response from Arduino`** | Check if the `BAUD_RATE` in Python (9600) matches `Serial.begin(9600)` in the Arduino code. |
| **Garbage characters (`?`)** | Baud rate mismatch. Ensure both are set to 9600. |

## 📄 License

This project is open-source. Feel free to modify it for your own needs.

**Author:** Rubens Braz.
