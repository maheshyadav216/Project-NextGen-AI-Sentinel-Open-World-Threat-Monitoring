# Project : NextGen AI Sentinel
NextGen AI Sentinel – Open-World Threat Monitoring &amp; Zero-Shot Detection using Vision Transformers on the Edge
  
<img src="/Images/AI-sentinel-git-thumb.jpg" height="200"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <img src="/Images/AI-sentinel-git-thumb2.jpg" height="200">  
  
**Next Gen AI Sentinel** is an AI-powered real-time surveillance and threat response system built on the **NVIDIA Jetson Orin Nano** platform using Vision Transformer–based Open-Vocabulary Detection. Unlike traditional CCTV analytics systems that are restricted to fixed object classes, this project uses NanoOWL and Zero-Shot Learning to detect threats dynamically through natural language prompts such as “weapon,” “rifle,” “gun,” or “masked person” without requiring custom dataset training for every new category. The system processes CCTV video feeds locally on the edge device using CUDA-accelerated inference, enabling low-latency, privacy-focused real-time monitoring. To reduce false alarms, a custom multi-frame threat confirmation logic verifies detections across consecutive frames before triggering alerts.  
  
Once a threat is confirmed, the AI Sentinel automatically captures evidence snapshots, sends instant Telegram alerts with images, and activates a physical IoT-based emergency response system using the Arduino Oplà IoT Kit over MQTT communication. The Oplà device acts as a local smart emergency console by turning all onboard RGB LEDs red, displaying warning messages on the OLED screen, and activating an audible buzzer alarm. By combining Edge AI, Vision Transformers, Open-Vocabulary Detection, IoT communication, and embedded hardware response into a single integrated workflow, this project demonstrates a modern cyber-physical security system capable of intelligent real-time threat monitoring and response.  
  
  
## Documentation

Refer the [Blog on Hackster](https://www.hackster.io/maheshyadav216/) for more information.  

**Hardware**
- [NVIDIA JETSON ORIN NANO SUPER DEVELOPER KIT](https://www.nvidia.com/en-in/autonomous-machines/embedded-systems/jetson-orin/nano-super-developer-kit/)  
  
**Hardware**
- Jetson Orin Nano Developer Kit  
    [Getting Started Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit) 
- Arduino Opla IoT Kit  
    [Getting Started Guide](https://opla.arduino.cc/)  

**Software**
- Jetson Orin Nano Developer Kit Setup  
    [Setup GUIDE](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)  
    [Initial Setup](https://www.jetson-ai-lab.com/tutorials/initial-setup-jetson-orin-nano/)     
    [Jetpack SDK Manager](https://developer.nvidia.com/sdk-manager)     
- Arduino Opla Iot Kit   
    [Carrier Board](https://opla.arduino.cc/opla/module/carrier/lesson/discovering-the-mkr-iot-carrier)  
    [Cloud](https://opla.arduino.cc/opla/module/cloud/lesson/getting-started-with-the-cloud-short)    
  
------------------------------------------------------------------------------------------------------

📕 **YouTube Video Links**  
  
▶️  NextGen AI Sentinel – Open-World Threat Monitoring - 🔗 https://youtu.be/sMybIUDKJOM   
  
-------------------------------------------------------------------------------------------------------
📒 **Important Links**  
 
🌐 NVIDIA SDK Manager - 🔗 https://developer.nvidia.com/sdk-manager   
📒 GitHub Documentation  
🌐 NVIDIA AI IOT - 🔗 https://github.com/nvidia-ai-iot  
  
🔑 Arduino Resources 🔗 https://github.com/arduino-libraries/Arduino_OplaUI    
⚙️ Demos 🔗 https://opla.arduino.cc/   

🛒 Hardware Purchase Links -  
NVIDIA Store - 🔗 https://developer.nvidia.com/embedded/buy-jetson?product=all&location=IN  
Arduino Store - 🔗 https://store-usa.arduino.cc/products/arduino-opla-iot-kit  

   
------------------------------------------------------------------------------------------------------

📜 Source Code, Circuit Diagrams and Documentation : 

🌐 GitHub Repository - 🔗 https://github.com/maheshyadav216/Project-NextGen-AI-Sentinel-Open-World-Threat-Monitoring     
  
🌐 Hackster Blog -  
🔗 https://www.hackster.io/maheshyadav216/nexgen-ai-sentinel-open-world-threat-detection-system-8e5775  
  
------------------------------------------------------------------------------------------  

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

