
#define THRESHOLD 64
#define PADNUM 4
#define PINLIMIT 500

int val;
int pinDelay;
int pinDelays[4] = { 0, 0, 0, 0 };

void setup() {
  Serial.begin(57600);
}

void loop() {
  for(int i = 0; i < PADNUM; i++) {
    val = analogRead(i);
    pinDelay = pinDelays[i];
    
    if(val >= THRESHOLD && pinDelay < 1) {
      Serial.print(i);
      Serial.print(",");
      Serial.print(val);
      Serial.println();
      pinDelays[i] = PINLIMIT;
    }
    
    if (pinDelay > 0) {
      pinDelays[i] = pinDelay - 1;
    }
  }
}
  
