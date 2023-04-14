## Comparison between mean field and fluctuation

mu = 0.0
param = jl.Parameters(κ=0.01)
trange = np.linspace(0.1,2.5,100)
pressure_mean = [jl.pressure_MF(t,mu,param,norm=True) for t in trange]
pressure_sigma = [ jl.pressure(jl.phaser_σ,temp,mu,param) + jl.pressure(jl.phasesc_σ,temp,mu,param) for temp in trange ]
pressure_tot = np.array(pressure_mean) + np.array(pressure_sigma)

plt.plot(trange,pressure_mean,label='Mean Field')
plt.plot(trange,pressure_sigma,label='fluctuation')
plt.plot(trange,pressure_tot,label='Total')
plt.legend()
plt.xlabel('T')
plt.ylabel(r'$P/T^3$');