#define LED_PIN 2  // usually GPIO 2 on ESP32 Dev Modules
const int cycle_time = 80;
void setup() {
  pinMode(2, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  while (Serial.available()) {
    int on_time = Serial.parseInt();
    if (on_time == 0) {
      delay(cycle_time);
      Serial.println("DONE");
    }
    else {
      digitalWrite(LED_PIN, HIGH);
      delay(on_time);
      digitalWrite(LED_PIN, LOW);
      delay(cycle_time - on_time);
      Serial.println("DONE");
    }
  }
}
