language_usage = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}
print(language_usage)

import matplotlib.pyplot as plt

languages = list(language_usage.keys())
percentages = list(language_usage.values())

bars = plt.bar(languages, percentages,color='skyblue',edgecolor='black',linewidth=1.2,width=0.5)
plt.title("Programming Language Popularity (Feb 2024)", fontsize=16, fontweight='bold')
plt.xlabel("Programming Languages", fontsize=12)
plt.ylabel("Percentage of Developers", fontsize=12)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height}%', ha='center', fontsize=10)

plt.ylim(0,100)
plt.show()

# Pseudocode: You can change the value of 'language' below to enter different languages
language = "Python"  # Change this variable to the language you want to enter

if language in language_usage:
    print(f"{language}: {language_usage[language]}% of developers use this language.")
else:
    print(f"{language} is not in the list.")

