//hello
//dogs=cute

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

  freq_change(2000, 255);
  freq_change(200, 0);
  freq_change(200, 254);
  freq_change(200, 0);
  // should be armed now
  freq_change(2000, 0);

  
  while(1) {
 
    freq_change(1500, 25);
    freq_change(1500, 100);
    digitalWrite(ledPin, HIGH);
    freq_change(1500, 175);
    digitalWrite(ledPin, LOW);
    
  }
}


void freq_change(int comp, int freq)
{
  unsigned long prevMillis = millis();
  unsigned long currentMillis = millis();

  while (currentMillis - prevMillis < comp) {
    for (int i=0; i<4; i++) {
      analogWrite(escPins[i], freq);
    }
    currentMillis = millis();
  }
}

