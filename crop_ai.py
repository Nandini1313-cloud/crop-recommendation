import serial
import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("Crop_recommendation.csv")

X = data[['N','P','K','temperature','humidity','rainfall']]
y = data['label']

model = RandomForestClassifier()
model.fit(X,y)

# Connect Arduino
arduino = serial.Serial('COM12',9600)
time.sleep(2)

N = 90
P = 40
K = 40
rainfall = 100

while True:

    line = arduino.readline().decode().strip()
    print(line)

    if "Temperature" in line:
        temp = float(line.split(":")[1])

    if "Humidity" in line:
        hum = float(line.split(":")[1])

        prediction = model.predict([[N,P,K,temp,hum,rainfall]])

        print("Recommended Crop:",prediction[0])
        print("------------------------")