# TP4 - Ej2 - Phy Numérique
# Verification of Central Limit Theorem

# There is a mistake in the code, check later, as for bigger N the gaussian is more spread when it should be sharper (probably just to label mistake)

import numpy as np
import matplotlib.pyplot as plt

N = np.array([10, 50, 100])

Ns = 5000 # We are going to compute each sum Ns times for our histogram

def sumS(Ns, N, j):
    S = np.zeros(Ns)
    for i in range(Ns):
        S[i] = sum(np.random.uniform(-1,1,N[j]))    
    return S

def gauss(x, mu, sigma):
    return np.exp(-0.5*(x-mu)**2/sigma**2) / np.sqrt(2*np.pi) / sigma

def gauss_plot(S):
    """
    inputs :
        -S : 
    outputs :
        x 
    """
    x = np.linspace(S.min(),S.max(),100)
    mu = np.mean(S)
    sigma = np.std(S)
    y = gauss(x, mu, sigma)
    return x, y

S_tab = np.zeros((len(N),Ns))
for j in range(len(N)): 
    S_tab[j,:] = sumS(Ns, N, j)
    x, y = gauss_plot(S_tab[j,:])
    
    plt.hist(S_tab[j,:], bins = int(np.sqrt(Ns)), density = True, alpha =0.4)
    plt.plot(x,y, label = f"Gauss - {N[j]} sample")
    plt.title(f"Histogram for {Ns} sums of sample of {N[0], N[1], N[2]} random values UF[-1,1]")
    plt.xlabel("x"), plt.ylabel(r"$S_x$")
    # in S_tab each element is an array which has S computed Ns times 
    # and in each element of S_tab the sample for the sum is of N values
plt.legend(), plt.show()    

# X=np.random.uniform(-1,1,(Ns,3)) would produce an array of random unif [-1,1]
# of Ns rows and 3 columns so what i could have done is to do (Ns,N[i]) in the loop 
# Then I would have summed each row for loop with sum (X[i,:]) inside
# Basically the same as I did but saving breaking my mind over the shape of my S_tab matrix
# What I did is also cool though 

#2
N = 1

def gen_random_uniform(N, R = 10000):
    title = "exp (Uniform law between 0 and 1)"
    random_tab = np.random.uniform(0,1,size=(R, N)) # Create tab of random uniform values between -1 and 1 with R rows and N N columns (so for N = 1 we have a column with R rows meaning R times drawn the value
    random_tab2 = np.exp(random_tab)
    draw_and_plot_exp(random_tab2, N, R, title)

def draw_and_plot_exp(random_tab2, N, R, title):
# N sample of values, R times sample is drawn
    tab = np.sum(random_tab2, axis=1)
    plt.figure()
    plt.hist(tab, bins = int(np.sqrt(R)), range = [tab.min(), tab.max()], density = True, label = "Histogram")
    plt.plot(neg_exp_function(tab)[0], neg_exp_function(tab)[1], label = "Exponential" )
    plt.plot(gauss_plot(tab)[0], gauss_plot(tab)[1], label = "Gaussian")
    plt.title(f"{title}")
    plt.legend()
    
def neg_exp_function(tab):
    x = np.linspace(tab.min(), tab.max(), 100)
    y = np.exp(-x)
    return x, y

gen_random_uniform(N)

# It makes sense that the law of probability for e^-x is doesn't follow a probability density of e^-x as x follow gaussian prob density (since x are random numbers of unifom distribution) and x---> e^-x is a 1:1 correspondence
# As we were asked about e^-x with x being the uniform rand sample [0,1] we did not use np.random.exponential which directly generates the sample of exp distribution 

#3
# Now we are asked to draw following prob law of p(x) = e^-x
def gen_random_exp(N, R = 10000):
    random_tab = np.random.exponential(size = (R,N))
    draw_and_plot_exp(random_tab, N, R, title = "Exponential law")

gen_random_exp(N)

#4 We could do the curve_fit but since we are working with gaussians where we know the std and mean of the sample we already did the fit by sending the sample, mean and sigma to our gauss_plot
