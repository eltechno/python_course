#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 26/04/19

#Feature:  #Enter feature name here
# Enter feature description here

#Scenario:  # Enter scenario name here
# Enter steps here

import matplotlib.pyplot as plt
"""
The matplotlib.pyplot module contains the Matplotlib library’s graphing capabilities that we use. This module typically is imported with the name plt.
"""
import numpy as np
"""
The NumPy (Numerical Python) library includes the function unique that we’ll use to summarize the die rolls. The numpy module typically is imported as np.
"""
import random
"""
The random module contains Python’s random-number- generation functions
"""
import seaborn as sns
"""
The seaborn module contains the Seaborn library’s graphing capabilities we use. This module typically is imported with the name sns. Search for why this curious abbreviation was chosen.
"""

rolls = [random.randrange(1,7) for i in range(600)]
#print(rolls)
values, frecuencies = np.unique(rolls, return_counts=True)
#print(values)
#print(frecuencies)
title = f'Rolling a six-sided die {len(rolls):,} Times'
sns.set_style() #sns = Seaborn
axes= sns.barplot(x=values, y=frecuencies, palette='bright')

axes.set_title(title)
axes.set(xlabel='Die Value',   ylabel='Frequency')

axes.set_ylim(top=max(frecuencies) * 1.10)

for bar, frequency in zip(axes.patches, frecuencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11,   ha='center', va='bottom')

plt.show()