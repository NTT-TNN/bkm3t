int LED = 23;
int inPin = 18;
int val = 0;

void setup(){
        Serial.begin(115200);
        pinMode(LED, OUTPUT);
        pinMode(inPin, INPUT_PULLUP);
}

void loop(){
        Serial.println("test");
        delay(200);
}
