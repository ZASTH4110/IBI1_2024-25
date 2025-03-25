uk_countries = [57.11, 3.13, 1.91, 5.45]
uk_names = ["England", "Wales", "Northern Ireland", "Scotland"]

china_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
china_names = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]

import matplotlib.pyplot as plt

colors = ['#4db6ac', '#ffb74d', '#9575cd', '#f06292']  
plt.figure(figsize=(8, 6))
plt.pie(uk_countries, labels=uk_names, autopct='%1.1f%%', startangle=140 ,colors=colors ,)     
plt.title("Population Distribution in UK Countries (2022)")
plt.axis('equal')  
plt.show()

colors = ['#4db6ac', '#ffb74d', '#9575cd', '#f06292', '#64b5f6'] 
plt.figure(figsize=(8, 6))
plt.pie(china_provinces, labels=china_names, autopct='%1.1f%%', startangle=140 ,colors=colors ,)
plt.title("Population Distribution in China Provinces (2022)")
plt.axis('equal')
plt.show()
