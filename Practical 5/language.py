# step 1: Create a dictionary with programming languages and their usage percentages
# step 2: languages = list of keys in the dictionary
#         Percentages = list of values in the dictionary
# step 3: Create a bar chart using matplotlib
#           Set the title and labels for the chart  (plt.title, plt.xlabel, plt.ylabel)
#           Add data labels to each bar in the chart (plt.text)
#           Set the y-axis limit to 100 (better visualization) (plt.ylim)
# step 4: Check if a specific language is in the dictionary and print its usage percentage 
#           If not, print that the language is not in the list

#create a dictionary with programming languages and their usage percentages
language_usage = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}
print(language_usage)

import matplotlib.pyplot as plt

#use the keys and values of the dictionary to create lists for languages and percentages
languages = list(language_usage.keys())
percentages = list(language_usage.values())

plt.figure(figsize=(10,6))

# Create a bar chart using matplotlib
# Set the title and labels for the chart
bars = plt.bar(languages, percentages,color='skyblue',edgecolor='black',linewidth=1.2,width=0.5)
plt.title("Programming Language Popularity (Feb 2024)", fontsize=16, fontweight='bold')
plt.xlabel("Programming Languages", fontsize=12)
plt.ylabel("Percentage of Developers", fontsize=12)

# Add data labels to each bar in the chart
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height}%', ha='center', fontsize=10)

# Set the y-axis limit to 100 for better visualization
plt.ylim(0,100)
plt.show()

# Pseudocode: You can change the value of 'language' below to enter different languages
language = "Python"  # Change this variable to the language you want to enter

if language in language_usage:
    print(f"{language}: {language_usage[language]}% of developers use this language.")#f{language} means the content of language
else:
    print(f"{language} is not in the list.")

