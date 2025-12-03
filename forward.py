import numpy as np
import matplotlib.pyplot as plt

L1 = 100
L2 = 100


theta1 = 45
theta2 = 30


t1 = np.radians(theta1)
t2 = np.radians(theta2)

x0, y0 = 0, 0
x1 = L1 * np.cos(t1)
y1 = L1 * np.sin(t1)

x2 = x1 + L2 * np.cos(t1 + t2)
y2 = y1 + L2 * np.sin(t1 + t2)

plt.figure()
plt.plot([x0, x1, x2], [y0, y1, y2], '-o', linewidth=3)
plt.xlim(-200, 200)
plt.ylim(0, 200)
plt.title("2-DOF Robotic Arm - Forward Kinematics")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.show()