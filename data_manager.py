import pandas as pd
import numpy as np
import csv
import sys
sys.path.append("home/Documents/Dev/Work/infiniteus")

#
#
#
# Python Script to automate management of various aspects of the data
#   - Get Unique Ingredient Items
#
#

recipes = pd.read_csv("recipes.csv", header=0)
yields = recipes[["Yield"]]

#*****Get Unique Ingredients*****#
# ingredients = recipes["Ingredients"]
# ingredients = ingredients.dropna()
# unique = []
#
# for row in ingredients:
#     temp = row.split(" ")
#     unique.extend(temp)
#
# unique = np.unique(unique)
# unique = pd.DataFrame(unique)
# unique.to_csv("ingredients.csv", header="Ingredients", index=False, index_label=False)



#*****Find Missing Data*****#
# purchases_missing = ""
# unit_per_purchase_missing = ""
# conversion_needed = ""
#
# ingredients = pd.read_csv("ingredients.csv", header=0)
#
# ingredients = np.array(ingredients)


# for row in ingredients:
#     #Missing a Purchase Entirely
#     if(row[1] != row[1]):
#         purchases_missing += row[0] + " "
#     #Missing the per unit purchase (NOT purchase unit)
#     elif(row[3] != row[3]):
#         unit_per_purchase_missing += row[0] +" "
#     #If conversion between unit per purchase Unit and recipe standard unit needed
#     if(row[5] == "CONVERSION"):
#         conversion_needed += row[0] + " "
#
# purchases_missing.strip()
# unit_per_purchase_missing.strip()
# conversion_needed.strip()
#
# print(purchases_missing[len(purchases_missing)-1])
# with open ("missing_data.txt", "w") as f:
#     f.write("Missing Purchases:\n")
#     for n in purchases_missing.split(" "):
#         f.write("-" + n + ":        \n\n")
#
#     f.write("!!! Missing Unit Per Purchases:\n")
#     for n in unit_per_purchase_missing.split(" "):
#         f.write("-" + n + ":        \n\n")
#
#     f.write("Conversions Needed:\n----")
#     for n in conversion_needed.split(" "):
#             f.write("-" + n + ":        \n\n")

# print("Missing Purchases:\n----" + purchases_missing + "\n\n")
# print("Missing Unit Per Purchases:\n----" + unit_per_purchase_missing + "\n\n")
# print("Conversions Needed:\n----" + conversion_needed + "\n\n")
