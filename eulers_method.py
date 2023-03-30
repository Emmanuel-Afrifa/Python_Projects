# In this code, I used the Euler's method to solve an ordinary differential equation
# Using Euler's formular, dy/dx = f(x,y)
# The Euler's method is given by y(i+1) = y(i) + f(x(i),y(i))h
# In this example, the differential equation give is dP/dt = -2.2067x10^-12(P^4 - 81x10^8)

# Import hte necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# An array containing the step sizes
h_array = np.array([480,240,120,60,30])


def arrays(h):
    n = int(480/h)
    thet = np.zeros(n+1)
    thet[0] = 1200
    time = np.zeros(n+1)
    
    return thet, time, h

# The right hand side of the differemtial equation
def func(time, thet):
    return -2.2067e-12*(thet**4 - 81e8)

# Function that computes the Euler's method
def soln(thet,time,h):
    for i in range(int(480/h)):
        thet[i+1] = thet[i] + (func(time[i], thet[i]))*h
        time[i+1] = time[i] + h

    return np.array(thet), np.array(time)


thet_approx = list()
for i in range(len(h_array)):    
    tht, tt, h = arrays(h_array[i])
    answers, time = soln(tht,tt,h)
    thet_approx.append(answers[-1])

# An array containing the approximate solutions at t = 480
np.array(thet_approx)

#An array containing the exact solutions at t = 480
thet_exact = np.array([1635.4,537.26,100.80,32.607,14.806])

# the time components on the the graph
time = np.array([30,60,120,240,480])


#print(f"The solutions are \n{answers} \n\n and the various times are an \n{time}")

# Plotting the exact solution against the approximate solution
plt.figure(figsize=(10,6))
plt.plot(time,thet_approx,color='blue',lw=2, label='Approximate')
plt.plot(time,thet_exact,color='red',lw=2, label='Exact')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Approximate Vs Exact solutions')
plt.xticks(ticks=time ,labels=time)
plt.grid()
plt.legend()

plt.show()