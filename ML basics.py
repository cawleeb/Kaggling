# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:43:06 2024

@author: caleb
"""
#%% Gradient descent
a = # alpha

for j in range (1:len(n)):
    for i in range(1:len(m)):
        Theta[1:j] = theta[j]-a*(h_theta(x[i])-y[i])*x[i][j]
        # Signal gets noisy with multiple dimensions, but it will eventually 
        # get close to the global minimum, but might overfit a bit
        # 
# linear regression has no local minimum
        