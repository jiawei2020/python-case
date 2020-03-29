# import modules
import pandas as pd
from matplotlib import pyplot as plt

# Task 1: read the data 
# Read data/coronavirus_dataset.csv into virus_cases_worldwide
virus_cases_worldwide = pd.read_csv("data/coronavirus_dataset.csv")
# See the result
print(virus_cases_worldwide)

# Task 2: get the confirmed cases throughout the world
confirmed_cases_worldwide = virus_cases_worldwide[virus_cases_worldwide.type == "confirmed"]
# See the result
print(confirmed_cases_worldwide)

# Task 3: get the confirmed cases for UK and France
allNativeData = confirmed_cases_worldwide[confirmed_cases_worldwide.Province.isnull()]
ukData = allNativeData[allNativeData.Country == "United Kingdom"]
franceData = allNativeData[allNativeData.Country == "France"]

# See the result
print(ukData)
print(franceData)

# Task 4: Draw a line plot of cumulative cases vs. date
plt.plot(ukData.date, ukData.cases, label="UK")
plt.plot(franceData.date, franceData.cases, label="France")

# Add a title
plt.title("UK and France cases")

# Label the x-axis and y-axis
plt.xlabel("Dates")
plt.ylabel("Case numbers")
plt.legend()

plt.show()
