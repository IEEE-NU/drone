//hello
//dogs
int escPins[4] =  {27,26,25,24};
const int ledPin = 6;

void setup() {
  //Serial.begin(9600);
  for (int i=0; i<4; i++) {
    pinMode(escPins[i], OUTPUT);
  }
  pinMode(ledPin, OUTPUT);
}

void loop()                     
{
  unsigned long prevMillis = millis();
  unsigned long currentMillis = millis();
  
  while (currentMillis - prevMillis < 2000) {
    for (int i=0; i<4; i++) {
      analogWrite(escPins[i], 255);
    }
    currentMillis = millis();
  }

  prevMillis = millis();
  currentMillis = millis();
  while (currentMillis - prevMillis < 200) {
    for (int i=0; i<4; i++) {
      analogWrite(escPins[i], 0);
    }
    currentMillis = millis();
  }
  
  prevMillis = millis();
  currentMillis = millis();
  while (currentMillis - prevMillis < 200) {
    for (int i=0; i<4; i++) {
      analogWrite(escPins[i], 254);
    }
    currentMillis = millis();
  }
  
  prevMillis = millis();
  currentMillis = millis();
  while (currentMillis - prevMillis < 200) {
    for (int i=0; i<4; i++) {
      analogWrite(escPins[i], 0);
    }
    currentMillis = millis();
  }

  prevMillis = millis();
  currentMillis = millis();
  // should be armed now
  while (currentMillis - prevMillis < 2000) {
    for (int i=0; i<4; i++) {
      analogWrite(escPins[i], 0);
    }
    currentMillis = millis();
  }
  
  while(1) {
    prevMillis = millis();
    currentMillis = millis();
    while (currentMillis - prevMillis < 1500) {
      for (int i=0; i<4; i++) {
        analogWrite(escPins[i], 25);
      }
      currentMillis = millis();
    }
    
    prevMillis = millis();
    currentMillis = millis();
    while (currentMillis - prevMillis < 1500) {
      for (int i=0; i<4; i++) {
        analogWrite(escPins[i], 100);
      }
      currentMillis = millis();
    }
    
    prevMillis = millis();
    currentMillis = millis();
    digitalWrite(ledPin, HIGH);
    while (currentMillis - prevMillis < 1500) {
      for (int i=0; i<4; i++) {
        analogWrite(escPins[i], 175);
      }
      currentMillis = millis();
    }
    digitalWrite(ledPin, LOW);
  }
}

