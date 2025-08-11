import numpy as np
import matplotlib.pyplot as plt

# --- 1. Configuration for Academic-Style Plots ---
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "font.size": 10,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "figure.dpi": 300,
})

# --- 2. Generate Synthetic Time-Series Data ---
n_points = 800
t = np.linspace(0, 4, n_points)
trend = 0.8 * (t - 2)**2 + 5
seasonality = 3 * np.sin(2 * np.pi * 2 * t) + 1.5 * np.sin(2 * np.pi * 5 * t)
np.random.seed(42)
noise = 1.2 * np.random.randn(n_points)
combined_signal = trend + seasonality + noise

# --- 3. Create the Multi-Panel Plot ---
fig, axes = plt.subplots(
    nrows=4,
    ncols=1,
    figsize=(8, 6),
    sharex=True
)

axes[0].plot(t, combined_signal, color='k', linewidth=1.5)
axes[0].set_title('Combined Time-Series Signal', fontsize=14)
axes[0].set_ylabel('Value')

axes[1].plot(t, trend, color='C0', linestyle='--', linewidth=2)
axes[1].set_title('Component 1: Long-Term Trend', loc='left', fontsize=11, style='italic')
axes[1].set_ylabel('Value')

axes[2].plot(t, seasonality, color='C1', linestyle='--', linewidth=2)
axes[2].set_title('Component 2: Periodic/Seasonal Patterns', loc='left', fontsize=11, style='italic')
axes[2].set_ylabel('Value')

axes[3].plot(t, noise, color='C2', linewidth=0.8, alpha=0.8)
axes[3].set_title('Component 3: High-Frequency Noise', loc='left', fontsize=11, style='italic')
axes[3].set_ylabel('Value')
axes[3].set_xlabel('Time (arbitrary units)')

# --- 4. Final Touches and Saving ---
plt.tight_layout()
plt.savefig("multi_scale_timeseries_decomposition.pdf", format='pdf', bbox_inches='tight')
plt.savefig("multi_scale_timeseries_decomposition.png", format='png', dpi=300, bbox_inches='tight')
