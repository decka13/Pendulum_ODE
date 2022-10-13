from cmath import sin
import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 2
g = 9.8
mu = .1
delta_t = 0.01
t = 0

  
# ODE Equation
def ODE(theta, theta_dot):
    return -mu*theta_dot - (g/2)*sin(theta) * delta_t


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

def check_theta(theta):
    if theta % np.pi < 0.001 and theta % np.pi > -0.001:
        return False
    else:
        return True

def check_theta_dot(theta):
    if theta < 0.001 and theta > -0.001:
        return False
    else:
        return True
def main():
    global t
    theta = get_theta0()
    theta_dot = get_theta_dot0()
    while check_theta(theta) == True or check_theta(theta_dot) == True:
        coordinate = (theta, theta_dot)
        slope = ODE(theta, theta_dot)
        slope = slope.real
        theta += theta_dot
        theta_dot += slope
        t += delta_t
        plt.plot([coordinate[0], theta], [coordinate[1], theta_dot])
    print(t)
    plt.title("Angular Acceleration of Pendulum")
    plt.xlabel("Angle Theta")
    plt.ylabel("Angular Velocity")
    plt.grid(True)
    plt.show()

main()