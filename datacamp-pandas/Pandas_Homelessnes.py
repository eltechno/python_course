import pickle
import pandas as pd
with open('homeless_data.pkl', 'rb') as f:
    data = pickle.load(f)

homelessness = pd.DataFrame(data)

print(homelessness.info)
print(homelessness.index)
print(homelessness.values)
print(homelessness.columns)

# Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals")
homelessness_fam = homelessness.sort_values("family_members", ascending=[False])
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])
# Print the top few rows
#print(homelessness_ind)
print(homelessness_ind[["state", "individuals"]].head(), end="\n\n")
print(homelessness_fam.head(), end="\n\n")
print(homelessness_reg_fam, end="\n\n")


# Select the individuals column
individuals = homelessness["individuals"]
# Print the head of the result
print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[["state","family_members"]]
# Print the head of the result
print(state_fam.head())

# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]
# Print the head of the result
print(ind_state.head())

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]
# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]
# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]
# See the result
print(fam_lt_1k_pac)

#adding updates