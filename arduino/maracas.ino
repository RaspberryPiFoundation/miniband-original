int newState;
int states[] = {-1,-1};
const int wait = 500;

void setup() {
  Serial.begin(9600);
}
void loop() {
  for (int i = 0; i < 3; i+=2) {
    newState = digitalRead(i);
    if (newState != states[i]) {
      Serial.print(i);
      Serial.print(",1023");
      Serial.println();
      states[i] = newState;
      delay(wait);
    } 
  }
}