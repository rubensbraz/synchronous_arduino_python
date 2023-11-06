void setup()
{
    Serial.begin(9600);
}

int movement;

void loop()
{
    if (Serial.available())
    {
        // Receive from Python
        String receivedString = Serial.readStringUntil('\n');
        Serial.println("Arduino received: " + receivedString);

        // Send to Python
        Serial.print("Arduino sends: ");
        Serial.print(response); // ENTER YOUR RESPONSE HERE
        Serial.println();
    }
}
