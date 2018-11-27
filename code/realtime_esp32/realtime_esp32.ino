#include <NTPClient.h>
#include <WiFi.h>
#include <WiFiUdp.h>
// WiFi details
const char *ssid     = "Tenda_4CA1E0";
const char *password = "heodaugau";

// NTP
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "2.asia.pool.ntp.org", 7*3600);
// RTC Libraries
#include <Wire.h> 
#include <RtcDS3231.h>
RtcDS3231<TwoWire> Rtc(Wire);

void WiFi_Setup(){

  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected!");
}

// ************************************
// ** RTC Setup
// ************************************
void RTC_Update(){
  // Do udp NTP lookup, epoch time is unix time - subtract the 30 extra yrs (946684800UL) library expects 2000
  timeClient.update();
  unsigned long epochTime = timeClient.getEpochTime()-946684800UL;
  Rtc.SetDateTime(epochTime); 
}
bool RTC_Valid(){
  bool boolCheck = true; 
  if (!Rtc.IsDateTimeValid()){
    Serial.println("RTC lost confidence in the DateTime!  Updating DateTime");
    boolCheck = false;
    RTC_Update();    
  }
  if (!Rtc.GetIsRunning())
  {
    Serial.println("RTC was not actively running, starting now.  Updating Date Time");
    Rtc.SetIsRunning(true);
    boolCheck = false;
    RTC_Update();
  }
}



// Utility print function
#define countof(a) (sizeof(a) / sizeof(a[0]))
void printDateTime(const RtcDateTime& dt)
{
    char datestring[20];
    snprintf_P(datestring, 
            countof(datestring),
            PSTR("%02u/%02u/%04u %02u:%02u:%02u"),
            dt.Month(),
            dt.Day(),
            dt.Year(),
            dt.Hour(),
            dt.Minute(),
            dt.Second() );
    Serial.println(datestring);
}



void setup(){
  Serial.begin(115200);
  WiFi_Setup();
  // Start NTP Time Client
  timeClient.begin();
  delay(2000);
  timeClient.update();
  Rtc.Begin();
  RTC_Update();
}

void loop() {
  if (!RTC_Valid()){
    RTC_Update();
  }
  RtcDateTime currTime = Rtc.GetDateTime();
  printDateTime(currTime);
  Serial.println(timeClient.getFormattedTime());
  delay(10000);
}
