# Step 1:create a list of countries and their populations
#        uk_countries = [57.11, 3.13, 1.91, 5.45]
#        uk_names = ["England", "Wales", "Northern Ireland", "Scotland"]
# Step 2:create a list of provinces and their populations
#        china_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
#        china_names = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]
# Step 3:draw a pie chart for the UK countries
#        use matplotlib.pyplot to create a pie chart （plt.pie）
#        Set the title and labels for the chart （plt.title, plt.xlabel, plt.ylabel）
#        Set the colors for each section of the pie chart （colors）
# Step 4:draw a pie chart for the China provinces
#        use matplotlib.pyplot to create a pie chart （plt.pie）
#        Set the title and labels for the chart （plt.title, plt.xlabel, plt.ylabel）
#        Set the colors for each section of the pie chart （colors）
# Step 5:show the pie charts

# create a list of countries and their populations
uk_countries = [57.11, 3.13, 1.91, 5.45]
uk_names = ["England", "Wales", "Northern Ireland", "Scotland"]

# create a list of provinces and their populations
china_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]
china_names = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]

import matplotlib.pyplot as plt

# Draw a pie chart for the UK countries
colors = ['#4db6ac', '#ffb74d', '#9575cd', '#f06292']  # Define colors for each section of the pie chart
plt.figure(figsize=(8, 6))
plt.pie(uk_countries, labels=uk_names, autopct='%1.1f%%', startangle=140 ,colors=colors ,) # Create pie chart  
plt.title("Population Distribution in UK Countries (2022)") # Set title for the pie chart
plt.axis('equal')  # Ensure the pie chart is a circle
plt.show()

# Draw a pie chart for the China provinces
colors = ['#4db6ac', '#ffb74d', '#9575cd', '#f06292', '#64b5f6'] # Define colors for each section of the pie chart
plt.figure(figsize=(8, 6))
plt.pie(china_provinces, labels=china_names, autopct='%1.1f%%', startangle=140 ,colors=colors ,) # Create pie chart
plt.title("Population Distribution in China Provinces (2022)") # Set title for the pie chart
plt.axis('equal') # Ensure the pie chart is a circle
plt.show()
