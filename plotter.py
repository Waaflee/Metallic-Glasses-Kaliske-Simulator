from typing import Dict, List, TypedDict
import requests as fetch
import json
import matplotlib.pyplot as plt

plt.style.use("seaborn")

Data = TypedDict(
    'Data', {'deformation': List[float], 'sigma': List[float], 'time': List[float]})

params = {'time': '0:1', 'deformation': '0:0.0005:2', 'model': '1'}

data: Data = fetch.get(
    "http://localhost:5000", params=params).json()

params = {'time': '0:1', 'deformation': '0:0.0005:2', 'model': '2'}

data_second: Data = fetch.get(
    "http://localhost:5000", params=params).json()

# print(data)

plt.subplot(3, 1, 1)
# plt.plot(data['time'], data['sigma'], label="model 0")
plt.plot(data_second["time"], data_second['sigma'], label="model 1")
plt.xlabel('Time')
plt.ylabel('Sigma')
plt.title('Sigma/Time')
plt.legend(loc="lower right", title="Modelos", frameon=True)

plt.subplot(3, 1, 2)
# plt.plot(data['deformation'], data['sigma'], label="model 0")
plt.plot(data_second['deformation'], data_second['sigma'], label="model 1")
plt.xlabel('Deformation')
plt.ylabel('Sigma')
plt.title('Sigma/Deformation')
plt.legend(loc="lower right", title="Modelos", frameon=True)


plt.subplot(3, 1, 3)
# plt.plot(data['time'], data['deformation'], label="model 0")
plt.plot(data_second['time'], data_second['deformation'], label="model 1")
plt.xlabel('Time')
plt.ylabel('Deformation')
plt.title('Deformation/Time')
plt.legend(loc="lower right", title="Modelos", frameon=True)

plt.subplots_adjust(hspace=0.5)
plt.show()
