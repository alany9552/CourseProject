# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# Data
df=pd.DataFrame({'x': range(1,11), 'y1111': np.random.randn(10), 'y2222': np.random.randn(10)+range(1,11), 'y3333': np.random.randn(10)+range(11,21) })
 
# multiple line plot
plt.plot( 'x', 'y1111', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
plt.plot( 'x', 'y2222', data=df, marker='', color='olive', linewidth=2)
plt.plot( 'x', 'y3333', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
plt.legend()
plt.show()