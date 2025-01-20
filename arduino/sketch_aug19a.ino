char serialData;


void setup() {
  // put your setup code here, to run once:
pinMode(7, OUTPUT);
pinMode(8, OUTPUT);
pinMode(5, OUTPUT);

}

void loop() {

  if(Serial.available() > 0) {
    serialData = Serial.read();
    Serial.print(serialData);
  }
  
  digitalWrite(8,HIGH);
  
  digitalWrite(7, LOW);
  analogWrite(5, 500);
  delay(1000);
   digitalWrite(8,LOW);
  digitalWrite(7, HIGH);
  analogWrite(5, 500);
  delay(1000);
  

}



