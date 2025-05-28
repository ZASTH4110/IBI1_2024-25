import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/ziten/IBI1_2024-25/Practical 10")
print(os.getcwd())    
print(os.listdir())    
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#showing the third column (the year) for the first 10 rows
print(dalys_data.iloc[0:10,2])
# the 10th year with DALYs data recorded in Afghanistan: 1999

#show DALYs for all countries in 1990
print(dalys_data.loc[dalys_data['Year'] == 1990, 'DALYs'])

#computed the mean DALYs in the UK and France
uk_dalys = dalys_data.loc[dalys_data.Entity=="United Kingdom", "DALYs"]
france_dalys = dalys_data.loc[dalys_data.Entity=="France", "DALYs"]
mean_DALYs_uk = uk_dalys.describe().loc['mean']
mean_DALYs_france = france_dalys.describe().loc['mean']
print(f"Mean DALYs in the UK: {mean_DALYs_uk}") 
print(f"Mean DALYs in France: {mean_DALYs_france}")
#the mean DALYs in the UK was greater than France

uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["Year", "DALYs"]]
plt.plot(uk.Year, uk.DALYs, 'ro') 
# 'b+' means blue plus sign 
# 'r+' means red plus sign
# 'bo' means blue circle  
plt.xticks(uk.Year, rotation=-90) # Rotate the x-axis labels to avoid overlap
plt.title("DALYs in the UK over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.tight_layout()
plt.show()



# Comparing DALYs trend between China and UK
china = dalys_data.loc[dalys_data["Entity"] == "China", ["DALYs", "Year"]]
# Plotting
plt.figure(figsize=(10, 5))
plt.plot(china.Year, china.DALYs, 'r-o', label='China')
plt.plot(uk.Year, uk.DALYs, 'b--s', label='United Kingdom')
plt.title("DALYs over Time: China vs United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(china.Year, rotation=-90 )
plt.legend()
plt.tight_layout()
plt.show()



