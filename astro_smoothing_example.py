%pylab inline
from astropy.convolution import convolve, Box1DKernel

N = 1000 # number of samples we're dealing with
dt = 1.0 / 100.0 # 100 samples / sec

timesteps=np.arange(0,10,dt)

noise_ts = 3 * (np.random.rand(N) - 0.5) # center at 0
plot(timesteps, noise_ts, 'b.')
ylim(-8, 8)




A = 5.0
frequency = 0.5 # Hz
omega = 2 * np.pi * frequency
timesteps = np.linspace(0.0, N*dt, N)
signal = A * np.sin(omega * timesteps)


plot(timesteps, signal)
ylim(-8, 8)

noisy_signal = noise_ts + signal

plot(timesteps, noisy_signal, 'b.')
ylim(-8, 8)



### smooth noisy signal


smoothed_signal = convolve(noisy_signal, Box1DKernel(11))

plot(timesteps, noisy_signal, 'b.', alpha=0.5, label="Noisy")
plot(timesteps, smoothed_signal, 'r', label="Smoothed")
ylim(-8, 8)





figure(figsize=(12,4))
ax = subplot(121)
title("Noisy Signal")
plot(timesteps, noisy_signal)
xlim(0, 4)
subplot(122, sharey=ax)
title("Nice, Smooth Signal")
plot(timesteps, smoothed_signal, 'r', label="Smoothed")
xlim(0, 4)