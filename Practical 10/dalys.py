import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/ziten/IBI1_2024-25/Practical 10")
print(os.getcwd())      # 当前目录，像 Unix 的 pwd
print(os.listdir())     # 当前目录下的所有文件，像 Unix 的 ls
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")


# Dataframe just like a table in a database
# Each column can be of different data types
# Each row is an observation
# Each column is a variable
# The first row is the header, which contains the names of the columns
print(dalys_data.head(5)) # Display the first 5 rows of the dataframe、
dalys_data.info() # Display the information of the dataframe
print(dalys_data.describe()) # Display the statistics of the dataframe


# as always in Python, counting begins at zero
# dalys_data.iloc [row, column] # iloc is used to access a group of rows and columns by integer position(s)
print(dalys_data.iloc[0,3]) # Access the first row and the fourth column of the dataframe

# how several rows and columns
# dalys_data.iloc [row_start:row_end, column_start:column_end]

print(dalys_data.iloc[2,0:5]) # Access the third row and the first five columns of the dataframe
print(dalys_data.iloc[0:2,:]) # Access the first two rows and all columns of the dataframe
print(dalys_data.iloc[0:10:2,0:5]) # Access the first ten rows and the first five columns of the dataframe, with a step of 2

# Answer the question:
print(dalys_data.iloc[0:10, 2])
# Your output should contain 10 rows in total. What was the 10th year for which DALYs were recorded in Afghanistan?
# The 10th year for which DALYs were recorded in Afghanistan is 1999.

# We can also use the Booleans to filter the data
my_columns = [True, True, False, True] # Select the first, second and fourth columns
dalys_data.iloc[0:3,my_columns] # Access the first three rows and the first, second and fourth columns of the dataframe

# What happens if my_columns is shorter than the number of columns of your data frame?
# What happens if it’s longer?
    # my_columns = [True, True, False, True, False] # Select the first, second and fourth columns
    # dalys_data.iloc[0:3,my_columns] # Access the first three rows and the first, second and fourth columns of the dataframe
    # #IndexError: Boolean index has wrong length: expected 4, got 5

    # my_columns = [True, True, False] # Select the first and second columns
    # dalys_data.iloc[0:3,my_columns] # Access the first three rows and the first and second columns of the dataframe
    # #IndexError: Boolean index has wrong length: expected 4, got 3

# We can also use the loc method to access the data by label
print(dalys_data.loc[2:4, "Year"])
# Access the third to fifth rows and the "Year" column of the dataframe

# we can actually look for rows that interest us without having to know the row numbers
# dalys_data.loc[every row where Year is 1990,"DALYs"]
print(dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"])


# Examining the situation across countries
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]] #  Select the "DALYs" and "Year" columns for the UK
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]] #  Select the "DALYs" and "Year" columns for France

# compare the mean DALYs between the UK and France
print("UK Mean DALYs:", uk["DALYs"].mean())
print("France Mean DALYs:", france["DALYs"].mean())
if uk["DALYs"].mean() > france["DALYs"].mean():
    print("UK has more DALYs than France")
else:
    print("France has more DALYs than UK")


plt.plot(uk.Year, uk.DALYs, 'b+') 
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
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]

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
