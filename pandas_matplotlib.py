import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("data.csv")
type_count=df["Type 1"].value_counts(ascending=True)
plt.barh(type_count.index,type_count.values,color="red",edgecolor="black",alpha=0.7)
plt.title("# of Pokemon Types")
plt.xlabel("Count")
plt.ylabel("Pokemon Types")
plt.tight_layout()

plt.show()