from typing import Dict, List, TypedDict
import requests as fetch
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn")

Data = TypedDict(
    'Data', {'deformation': List[float], 'sigma': List[float], 'time': List[float]})

for i in range(1, 6):
    e = round(0.2*(i), 2)
    params = {'time': '0:0.1:5',
              'deformation': f'{e}:{e}', 'model': '1'}
    payload: Data = fetch.get(
        "http://localhost:5000", params=params).json()
    print(payload['sigma'][0]-payload['sigma'][-1])
    # print(payload['sigma'][10])

    plt.plot(payload['time'], payload['sigma'],
             label=f'deformación: {e}%')

plt.xlabel('Tiempo')
plt.ylabel('Sigma')
plt.title('Sigma/Tiempo')
plt.legend(loc="lower right", title="Deformaciones", frameon=True)
plt.show()
