import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from pcap_manipulation import load_pcap_data_non_hot
SAMPLE_SIZE = 20

features, labels = load_pcap_data_non_hot(SAMPLE_SIZE)
pca = PCA(n_components=2)
features = np.reshape(features, (len(features), SAMPLE_SIZE))

labels = np.reshape(labels, (len(labels), 1))

principalComponents = pca.fit_transform(features)
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
labelsDf = pd.DataFrame(data=labels, columns=['quality'])

finalDf = pd.concat([principalDf, labelsDf], axis=1)

fig = plt.figure(figsize = (8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 Component PCA', fontsize=20)

# targets = ['small', 'large', 'hd720']
targets = ['tiny', 'small', 'medium', 'large', 'hd720', 'hd1080']
colors = ['r', 'g', 'b', 'm', 'b', 'y']
for target, color in zip(targets, colors):
    indicesToKeep = (finalDf['quality'] == target)
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c=color
               , s=15)
ax.legend(targets)
ax.grid()
plt.show()