from typing import Dict, List, TypedDict
import requests as fetch
import json
import matplotlib.pyplot as plt

plt.style.use("seaborn")

Data = TypedDict(
    'Data', {'deformation': List[float], 'sigma': List[float], 'time': List[float]})

params = {'time': '0:1', 'deformation': '0:0.0005:2'}

data: Data = fetch.get(
    "http://localhost:5000", params=params).json()

print(data)

plt.subplot(1, 3, 1)
plt.plot(data['time'], data['sigma'])
plt.xlabel('Time')
plt.ylabel('Sigma')
plt.title('Sigma/Time')

plt.subplot(1, 3, 2)
plt.plot(data['deformation'], data['sigma'])
plt.xlabel('Deformation')
plt.ylabel('Sigma')
plt.title('Sigma/Deformation')

plt.subplot(1, 3, 3)
plt.plot(data['time'], data['deformation'])
plt.xlabel('Time')
plt.ylabel('Deformation')
plt.title('Deformation/Time')

plt.show()
