# %% [markdown]
# # FIDELFOLIO INVESTMENT PRIVATE LIMITED ASSIGNMENT

# %% [markdown]
# ### STEP 1: IMPORT ALL THE NECESARY PYTHON LIBRARIES

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ### STEP 2: READ DATA FROM THE CSV USING PANDAS AND CHECK

# %%
df=pd.read_csv("NiftyReturnData.csv")

# %%
df.head()

# %% [markdown]
# ### STEP 3: CREATE A DICTIONARY(color_map) TO BE USED LATER FOR THE PURPOSE OF LEGEND

# %%
color_map = {
    'Red': 'Before 2005', 
    'Blue': 'Between 2005 and 2015', 
    'Green': 'After 2015'
}

# %% [markdown]
# ### STEP 4: CREATE A COLUMN "Color" BASED ON THE CONDITIONS IN ORDER TO BE PLOTTED ON SCATTERPLOT

# %%
df['Date'] = pd.to_datetime(df['Date']);

# %%
df['Color'] = 'Green'  # default color
df.loc[df['Date'].dt.year < 2005, 'Color'] = 'Red'  # for dates before 2005
df.loc[(df['Date'].dt.year >= 2005) & (df['Date'].dt.year <= 2015), 'Color'] = 'Blue'  # for dates between 2005 and 2015

# %%
df

# %% [markdown]
# ### STEP 5: PLOT THE SCATTERPLOT AND SAVE IT IN THE FORM OF PNG

# %%
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Period', y='NiftyReturn', hue='Color', palette={'Red': 'red', 'Green': 'green', 'Blue': 'blue'}, s=100);
plt.grid(False, which='both', axis='both')
plt.title('Scatter Plot of Nifty Returns by Period')
plt.yscale('log')
plt.xlabel('Period')
plt.ylabel('Nifty Return')
legend_labels = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in color_map.items()]
plt.legend(handles=legend_labels, title='Color', loc='best')
plt.savefig('scatter_plot2.png');


# %%



