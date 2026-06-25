import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('rising_waters_data.csv')
print(data)

plt.plot(data['Date'], data['Water_Level'])
plt.title('Rising Waters')
plt.show()