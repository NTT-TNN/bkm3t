

#include <IRremote.h>

int RECV_PIN = 13;
int ledPin1 = 25;
int ledPin2 = 26;
int ledPin3 = 27;

IRrecv irrecv(RECV_PIN);

decode_results results;

void setup()
{
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, HIGH);
  digitalWrite(ledPin3, HIGH);

  Serial.begin(9600);
  // In case the interrupt driver crashes on setup, give a clue
  // to the user what's going on.
  Serial.println("Enabling IRin");
  irrecv.enableIRIn(); // Start the receiver
  Serial.println("Enabled IRin");

  delay(1000);
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, LOW);
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    if(results.value == 2576){
      Serial.println("up");
      digitalWrite(ledPin1, HIGH);
      delay(300);
      digitalWrite(ledPin1, LOW);
    }
    else if(results.value == 2592){
      Serial.println("down");
      digitalWrite(ledPin2, HIGH);
      delay(300);
      digitalWrite(ledPin2, LOW);
    }
    else if(results.value == 2608){
      Serial.println("left");
      digitalWrite(ledPin3, HIGH);
      delay(300);
      digitalWrite(ledPin3, LOW);
    }
    else if(results.value == 2624){
      Serial.println("right");
    }
    else if(results.value == 2640){
      Serial.println("walking");
    }
    else if(results.value == 2656){
      Serial.println("running");
    }
    else if(results.value == 2672){
      Serial.println("standing");
    }
    else if(results.value == 2688){
      Serial.println("sitting");
    }
    else {
      Serial.println("Not recognize code!");
      digitalWrite(ledPin1, HIGH);
      digitalWrite(ledPin2, HIGH);
      digitalWrite(ledPin3, HIGH);

      delay(300);

      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin2, LOW);
      digitalWrite(ledPin3, LOW);
    }
    
    irrecv.resume(); // Receive the next value
  }
  delay(100);
}
