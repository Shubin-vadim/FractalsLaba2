import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

t = np.arange(0.0, 1.0, 0.001)

a0 = 6
f0 = 3
s = a0 * np.sin(2 * np.pi * f0 * t)


pl, = plt.plot(t, s, lw=3, color='green')
plt.axis([0, 1, -10, 10])
axcolor = 'White'

frequency_axis = plt.axes(
    [0.25, 0.1, 0.65, 0.03],
    facecolor=axcolor
)

amplitude_axis = plt.axes(
    [0.25, 0.15, 0.65, 0.03],
    facecolor=axcolor
)

frequency_slider = Slider(frequency_axis, 'Freq', 0.1, 30.0, valinit=f0)
amplitude_slider = Slider(amplitude_axis, 'Amp', 0.1, 10.0, valinit=a0)


def update(val):
    amp = amplitude_slider.val
    freq = frequency_slider.val
    pl.set_ydata(amp * np.sin(2 * np.pi * freq * t))

frequency_slider.on_changed(update)
amplitude_slider.on_changed(update)

plt.show()