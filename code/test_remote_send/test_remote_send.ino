#include <IRremote.h>
IRsend irsend;// gửi tín hiệu hồng hoại

const int receiverPin = 8; // chân digital 8 dùng để đọc tín hiệu
IRrecv irrecv(receiverPin); // tạo đối tượng IRrecv mới
decode_results results;// lưu giữ kết quả giải mã tín hiệu

const int CH4 = 10; //Send IR



void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // start the IR receiver
  /* điện trở nội kéo lên cho tất cả nút bấm*/
//  pinMode(CH1, INPUT_PULLUP);
//  pinMode(CH2, INPUT_PULLUP);
//  pinMode(CH3, INPUT_PULLUP);
//  pinMode(POWER, INPUT_PULLUP);
  pinMode(CH4, OUTPUT);
}

void loop()
{
//  irsend.sendSony(0x10, 12);
  
  if (irrecv.decode(&results)) // nếu nhận được tín hiệu
  {
    Serial.println(results.value, HEX);
//    delay(200);
    irrecv.resume(); // nhận giá trị tiếp theo
  }
  
  
  delay(200);
}
