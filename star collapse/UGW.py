import numpy as np
from scipy.signal import find_peaks

# Simulated signal representing ultrasonic reflections
signal = np.sin(np.linspace(0, 20, 500)) + np.random.normal(0, 0.1, 500)
peaks, _ = find_peaks(signal, height=0)

# Detect significant peaks indicating potential defects
for peak in peaks:
    if signal[peak] > 1.5:  # Threshold for defect
        print(f"Potential defect detected at index {peak}")