import pandas as pd
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
             label=f'(numérico) deformación: {e}%')


df = pd.read_csv("analitical_results.csv")
plt.plot(df.t_02, df.sigma_02, 'X', label=f'(analítico) deformación: 0.2%')
plt.plot(df.t_04, df.sigma_04, 'X', label=f'(analítico) deformación: 0.4%')
plt.plot(df.t_06, df.sigma_06, 'X', label=f'(analítico) deformación: 0.6%')
plt.plot(df.t_08, df.sigma_08, 'X', label=f'(analítico) deformación: 0.8%')
plt.plot(df.t_10, df.sigma_10, 'X', label=f'(analítico) deformación: 1.0%')


plt.xlabel('Tiempo')
plt.ylabel('Sigma')
plt.title('Sigma/Tiempo')
plt.legend(loc="upper right", title="Deformaciones", frameon=True)
plt.show()
