# Infant Cry Classification System

This project aims to develop a deep learning-based system to classify and identify the reasons behind an infant's cry. It integrates temperature and pulse sensors alongside a microphone to analyze the infant’s cry and predict whether the cry is caused by tiredness, pain, burping, hunger, or discomfort. 

## Features:
- **Cry Detection**: Detects if the sound input is a cry.
- **Cry Classification**: Identifies the reason behind the cry using the pitch and intensity.
- **Sensor Integration**: Uses a temperature sensor and a pulse sensor to measure additional health data.
- **Alerts**: Sends a customized message to caregivers with the reason for the cry using a Telegram chatbot.

## Components:
- **DS18B20 Temperature Sensor**: Reads and sends temperature data.
- **Super Debug Heart Pulse Sensor**: Monitors the pulse rate of the infant.
- **Microphone**: Records 5 seconds of audio every minute to detect cries.
- **Raspberry Pi**: Used as the core hardware to process the data and make predictions.

## Dataset:
The model is trained using the [Donate a Cry Corpus Dataset](https://asmp-eurasipjournals.springeropen.com/articles/10.1186/s13636-021-00197-5), which consists of 250 audio files labeled with different reasons such as:
- Tiredness
- Pain
- Burping
- Hungry
- Discomfort

## How It Works:
1. The microphone records 5 seconds of audio at one-minute intervals.
2. A deep learning model detects if the audio contains infant crying.
3. If crying is detected, a second deep learning model analyzes the cry to determine its cause.
4. Additional data from the temperature and pulse sensors are sent alongside the cry classification.
5. The system sends an alert to the parent via a Telegram bot with the detected reason for the cry.



## Model:
Two convolutional neural networks (CNN) are used:
- **Cry Detection Model**: Identifies whether the input audio contains a baby cry.
- **Cry Classification Model**: Classifies the reason for the cry based on the characteristics of the audio.

## Results:
- Cry Detection Accuracy: 95%
- Cry Classification Accuracy: 90%


### Software Setup:
1. Clone this repository.
   ```bash
   git clone https://github.com/username/infant-cry-classification.git
   cd infant-cry-classification
