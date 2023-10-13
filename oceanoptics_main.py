import matplotlib.pyplot as plt
import numpy as np
import time
from seabreeze.spectrometers import Spectrometer, list_devices

devices = list_devices()
print(devices)
spec = Spectrometer(devices[0])

# Set integration time if needed
int_time = spec.integration_time_micros(10000)

wavelengths = spec.wavelengths()
intensities = spec.intensities()

# data = np.column_stack((wavelengths, intensities))
# fname = "bg_spectrum.txt"
# np.savetxt(fname, data, delimiter='\t')

# bg_data = np.loadtxt('bg_spectrum.txt')
# bg_signal = bg_data[:,1]

fig, ax = plt.subplots()
while True:
    intensities = spec.intensities()
    # intensities = intensities-bg_signal
    ax.clear()
    ax.plot(wavelengths,intensities,'r')
    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('Intensity (arb.unit)')
    ax.set_xlim(200,1100)
    # ax.set_ylim(0,7000)
    plt.grid()
    plt.pause(0.1)
    
    if plt.waitforbuttonpress(timeout=0.1):
        break

plt.show()