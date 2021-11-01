import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./e_sections/some_data.csv")
df.plot('age', 'salary', 'scatter')

plt.show()
