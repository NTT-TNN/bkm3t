#include <IRremote.h> // thư viện hỗ trợ IR remote

const int receiverPin = 8; // chân digital 8 dùng để đọc tín hiệu
IRrecv irrecv(receiverPin); // tạo đối tượng IRrecv mới
decode_results results;// lưu giữ kết quả giải mã tín hiệu

const int RED = 7;// LED đỏ
const int YELLOW = 6;// LED vàng
const int GREEN = 5;// LED xanh
/* trạng thái của các LEDs*/
boolean stateRED = false;
boolean stateYELLOW = false;
boolean stateGREEN = false;
void setup()
{
  Serial.begin(9600);// serial 
  irrecv.enableIRIn(); // start the IR receiver
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
}
// translate IR signals
void translateIR()
{
  switch(results.value)
  {
    case 0x143226DB:  stateRED = !stateRED; 
                digitalWrite(RED, stateRED); 
                break;
    case 0xA32AB931: stateYELLOW = !stateYELLOW; 
                digitalWrite(YELLOW, stateYELLOW); 
                break;
    case 0x39D41DC6: stateGREEN = !stateGREEN; 
                digitalWrite(GREEN, stateGREEN);  
                break;

  }
}
void loop()
{
  if (irrecv.decode(&results)) // nếu nhận được tín hiệu
  {
//    translateIR();
    Serial.println(results.value, HEX);
    delay(200);
    irrecv.resume(); // nhận giá trị tiếp theo
  }
}
