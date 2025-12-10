/*
 * Synchronous Serial Communication - Arduino Side
 * Reads a string from Python, processes it, and sends a response back.
 */

void setup() {
  // Initialize serial communication at 9600 bits per second
  Serial.begin(9600);
  
  // Optional: Wait for the serial port to connect (needed for native USB boards like Leonardo)
  while (!Serial) {
    ; 
  }
}

void loop() {
  // Check if data is available in the serial buffer
  if (Serial.available() > 0) {
    
    // 1. Read the incoming data until a newline character is found
    // The trim() function removes any whitespace/newline characters from the ends
    String receivedString = Serial.readStringUntil('\n');
    receivedString.trim();

    // 2. Process the data (Example logic)
    // You can add logic here to control LEDs or motors based on 'receivedString'
    String responseStatus = "OK";
    
    // 3. Send the response back to Python
    // We construct a single string to send back
    Serial.print("Command '");
    Serial.print(receivedString);
    Serial.print("' received. Status: ");
    Serial.println(responseStatus); // println adds the '\n' Python is waiting for
  }
}
