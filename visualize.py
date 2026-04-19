import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/raw/employees.csv")

sns.countplot(x="performance", data=df)
plt.title("Employee Performance Distribution")
plt.show()