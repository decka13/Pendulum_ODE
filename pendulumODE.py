from cmath import sin
import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 2 # Length of pendulum stick
g = 9.8 # Gravity
mu = .1 # Air Resistance Coeffient
delta_t = 0.01 # Change in time
t = 0 # Start tiime

  
# ODE Equation
def ODE(theta, theta_dot):
    return -mu*theta_dot - (g/2)*sin(theta) * delta_t # Angular acceration at point (theta, theta_dot)

# Get theta from user
def get_theta0():
    theta = input("Input Theta: ")
    if theta == "0":
        return 0
    try:
        theta = float(theta)
        return theta
    except:
        print("Input numerical value for theta")
        return get_theta0() 
# Get theta_dot from user
def get_theta_dot0():
    theta_dot = input("Input Theta Dot: ")
    if theta_dot == "0":
        return 0
    try:
        theta_dot = float(theta_dot)
        return theta_dot
    except:
        print("Input numerical value for theta dot")
        return get_theta_dot0()
# Check if theta has stopped changing
def check_theta(theta):
    if theta % np.pi < 0.001 and theta % np.pi > -0.001:
        return False
    else:
        return True
# Check if theta_dot has stopped changing
def check_theta_dot(theta):
    if theta < 0.001 and theta > -0.001:
        return False
    else:
        return True
def main():
    global t
    theta = get_theta0()
    theta_dot = get_theta_dot0()
    # Loop to get all of the angular accerations of the system until it stops moving
    while check_theta(theta) == True or check_theta(theta_dot) == True:
        coordinate = (theta, theta_dot) # Original placement of (theta, theta_dot)
        slope = ODE(theta, theta_dot) # Check how (theta, theta_dot) will change
        slope = slope.real 
        theta += theta_dot # Move theta by theta_dot
        theta_dot += slope # Move theta by the slope
        t += delta_t
        plt.plot([coordinate[0], theta], [coordinate[1], theta_dot]) # Plot vector 
    print(t)
    plt.title("Angular Acceleration of Pendulum")
    plt.xlabel("Angle Theta")
    plt.ylabel("Angular Velocity")
    plt.grid(True)
    plt.show()

main()