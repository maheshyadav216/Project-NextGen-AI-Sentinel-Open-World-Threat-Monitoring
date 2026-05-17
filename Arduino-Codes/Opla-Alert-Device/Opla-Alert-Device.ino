//=============================================================================//
// Project/Tutorial       - NextGen AI Sentinel – Open-World Threat Monitoring
// Device                 - Opla Iot Kit
// Author                 - https://www.hackster.io/maheshyadav216
// Hardware               - Arduino Opla Iot Kit, Arduino MKR WiFi 1010   
// Software               - Arduino IDE
// GitHub Repo of Project - https://github.com/maheshyadav216/Project-NextGen-AI-Sentinel-Open-World-Threat-Monitoring 
// Code last Modified on  - 16/05/2026
// Code/Content license   - (CC BY-NC-SA 4.0) https://creativecommons.org/licenses/by-nc-sa/4.0/
//============================================================================//

// AI Sentinel Local Threat Alert System

#include <WiFiNINA.h>
#include <PubSubClient.h>
#include <Arduino_MKRIoTCarrier.h>

// =========================
// WiFi Credentials
// =========================
const char* ssid = "xxxxxxx";
const char* password = "xxxxxxx";

// =========================
// MQTT Broker
// =========================
// Recommended:
// Install Mosquitto broker on Jetson Orin Nano
// and use Jetson local IP here.

const char* mqtt_server = "192.168.0.52"; // CHANGE THIS
const int mqtt_port = 1883;
const char* mqtt_topic = "emergency/alert";

// =========================
// WiFi + MQTT
// =========================
WiFiClient wifiClient;
PubSubClient client(wifiClient);

// =========================
// Oplà Carrier
// =========================
MKRIoTCarrier carrier;

// =========================
// Threat State
// =========================
bool threatActive = false;
unsigned long threatStartTime = 0;

// =========================
// LED Animation Variables
// =========================
int brightness = 0;
int fadeAmount = 2;

// =========================
// Buzzer Variables
// =========================
unsigned long lastBeepTime = 0;
bool buzzerState = false;

// =========================
// WiFi Connection
// =========================
void connectWiFi()
{
    Serial.print("Connecting to WiFi");

    while (WiFi.begin(ssid, password) != WL_CONNECTED)
    {
        Serial.print(".");
        delay(1000);
    }

    Serial.println("\nWiFi Connected!");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
}

// =========================
// MQTT Reconnect
// =========================
void reconnectMQTT()
{
    while (!client.connected())
    {
        Serial.print("Connecting to MQTT...");

        String clientId = "OplaClient-";
        clientId += String(random(0xffff), HEX);

        if (client.connect(clientId.c_str()))
        {
            Serial.println("Connected!");
            client.subscribe(mqtt_topic);
        }
        else
        {
            Serial.print("Failed. Retry in 2 sec. State: ");
            Serial.println(client.state());
            delay(2000);
        }
    }
}

// =========================
// OLED Standby Screen
// =========================
void showStandbyScreen()
{
    carrier.display.fillScreen(ST77XX_BLACK);

    carrier.display.setTextColor(ST77XX_CYAN);
    carrier.display.setTextSize(3);
    carrier.display.setCursor(102, 52);
    carrier.display.println("AI");

    carrier.display.setCursor(48, 82);
    carrier.display.println("SENTINEL");

    carrier.display.setTextColor(ST77XX_GREEN);
    carrier.display.setTextSize(2);
    carrier.display.setCursor(84, 142);
    carrier.display.println("SYSTEM");

    carrier.display.setCursor(90, 168);
    carrier.display.println("ARMED");
}

// =========================
// OLED Threat Screen
// =========================
void showThreatScreen()
{
    carrier.display.fillScreen(ST77XX_RED);

    carrier.display.setTextColor(ST77XX_WHITE);
    carrier.display.setTextSize(3);
    carrier.display.setCursor(60, 55);
    carrier.display.println("WARNING");

    carrier.display.setTextSize(2);
    carrier.display.setCursor(80, 105);
    carrier.display.println("WEAPON");

    carrier.display.setCursor(70, 135);
    carrier.display.println("DETECTED!");

    // Timestamp
    unsigned long seconds = millis() / 1000;

    carrier.display.setTextColor(ST77XX_YELLOW);
    carrier.display.setTextSize(2);
    carrier.display.setCursor(88, 190);
    carrier.display.print("T+");
    carrier.display.print(seconds);
    carrier.display.println("s");
}

// =========================
// LED Standby Animation
// =========================
void standbyLEDs()
{
    for (int i = 0; i < 5; i++)
    {
        carrier.leds.setPixelColor(i, 0, 0, 25);
    }

    carrier.leds.show();
}

// =========================
// Threat LED Animation
// =========================
void threatLEDs()
{
    brightness += fadeAmount;

    if (brightness <= 0 || brightness >= 255)
    {
        fadeAmount = -fadeAmount;
    }

    for (int i = 0; i < 5; i++)
    {
        carrier.leds.setPixelColor(i, brightness, 0, 0);
    }

    carrier.leds.show();
    delay(20);
}

// =========================
// Threat Buzzer Pattern
// =========================
void threatBuzzer()
{
    unsigned long currentMillis = millis();

    if (currentMillis - lastBeepTime >= 250)
    {
        lastBeepTime = currentMillis;

        buzzerState = !buzzerState;

        if (buzzerState)
        {
            carrier.Buzzer.sound(1500);
        }
        else
        {
            carrier.Buzzer.noSound();
        }
    }
}

// =========================
// MQTT Callback
// =========================
void callback(char* topic, byte* payload, unsigned int length)
{
    String message;

    for (unsigned int i = 0; i < length; i++)
    {
        message += (char)payload[i];
    }

    Serial.print("Message Received: ");
    Serial.println(message);

    // =========================
    // Threat Trigger
    // =========================
    if (message == "THREAT")
    {
        threatActive = true;
        threatStartTime = millis();

        showThreatScreen();
    }

    // =========================
    // Clear Alert
    // =========================
    if (message == "CLEAR")
    {
        threatActive = false;

        carrier.Buzzer.noSound();

        showStandbyScreen();
    }
}

// =========================
// Setup
// =========================
void setup()
{
    Serial.begin(115200);

    carrier.begin();

    carrier.display.fillScreen(ST77XX_BLACK);

    carrier.display.setRotation(0);

    carrier.display.setTextWrap(false);

    showStandbyScreen();

    standbyLEDs();

    connectWiFi();

    client.setServer(mqtt_server, mqtt_port);
    client.setCallback(callback);
}

// =========================
// Main Loop
// =========================
void loop()
{
    if (!client.connected())
    {
        reconnectMQTT();
    }

    client.loop();

    // =========================
    // Threat Mode
    // =========================
    if (threatActive)
    {
        threatLEDs();

        threatBuzzer();

        // Auto-clear after 15 seconds
        if (millis() - threatStartTime > 15000)
        {
            threatActive = false;

            carrier.Buzzer.noSound();

            showStandbyScreen();

            standbyLEDs();
        }
    }
    else
    {
        standbyLEDs();
    }
}
//==========================================================================================================//