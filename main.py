from Bio.Align import substitution_matrices

import numpy as np


m = substitution_matrices.load("BLOSUM62")


data = m.tolist()

data = np.asarray(data)

data = data + 10
data = np.log10(data)

aa = [c for c in m.alphabet]

import plotly.express as px

xlabel = "Amino Acid"
labels = dict(color="Similarity", x=xlabel, y=xlabel)
fig = px.imshow(data, labels=labels, color_continuous_scale="viridis",
                x=aa, y=aa,                
                template="plotly_dark")

fig.write_html("visual.html")

