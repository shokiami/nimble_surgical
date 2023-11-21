import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

IN_DIR = 'betr_force_vs_disp'

sns.set()

fig1, axs1 = plt.subplots(nrows=2, figsize=(10, 10))
axs1[0].set_title(f'Force vs. Displacement')
axs1[0].set_xlabel('Displacement (mm)')
axs1[0].set_ylabel('Force (mN)')

for csv in sorted(os.listdir(IN_DIR)):
  df = pd.read_csv(os.path.join(IN_DIR, csv))
  displacements = df['Displacement'][1:].to_numpy(dtype=np.float32)
  forces = df['Force'][1:].to_numpy(dtype=np.float32)
  axs1[0].plot(displacements, forces, label=csv)

axs1[0].legend(loc='upper right', fontsize='9')
fig1.savefig('force_vs_displacement.png')
