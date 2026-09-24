#define LEFT_BUTTON  25
#define RIGHT_BUTTON 26
#define START_BUTTON 27

void setup() {
  Serial.begin(115200);

  pinMode(LEFT_BUTTON, INPUT_PULLUP);
  pinMode(RIGHT_BUTTON, INPUT_PULLUP);
  pinMode(START_BUTTON, INPUT_PULLUP);
}

void loop() {

  if (digitalRead(LEFT_BUTTON) == LOW) {
    Serial.println("LEFT");
    delay(50);
  }

  if (digitalRead(RIGHT_BUTTON) == LOW) {
    Serial.println("RIGHT");
    delay(50);
  }

  if (digitalRead(START_BUTTON) == LOW) {
    Serial.println("START");
    delay(200);
  }
}