import numpy as np
import matplotlib.pyplot as plt

L1 = 100
L2 = 100

x_target = 120
y_target = 80

cos_theta2 = (x_target**2 + y_target**2 - L1**2 - L2**2) / (2 * L1 * L2)
cos_theta2 = np.clip(cos_theta2, -1.0, 1.0)
theta2 = np.arccos(cos_theta2)


theta1 = np.arctan2(y_target, x_target) - np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))

x0, y0 = 0, 0
x1 = L1 * np.cos(theta1)
y1 = L1 * np.sin(theta1)
x2 = x1 + L2 * np.cos(theta1 + theta2)
y2 = y1 + L2 * np.sin(theta1 + theta2)

plt.figure()
plt.plot([x0, x1, x2], [y0, y1, y2], '-o', linewidth=3)
plt.plot(x_target, y_target, 'rx', markersize=10, label='Target')
plt.xlim(-200, 200)
plt.ylim(0, 200)
plt.title("2-DOF Robotic Arm - Inverse Kinematics")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)


theta1_deg = np.degrees(theta1)
theta2_deg = np.degrees(theta2)
plt.text(-190, 180, f'Theta1 = {theta1_deg:.2f}°', fontsize=12, color='black')
plt.text(-190, 160, f'Theta2 = {theta2_deg:.2f}°', fontsize=12, color='black')

plt.show()

print(f"Theta1 = {np.degrees(theta1):.2f}°, Theta2 = {np.degrees(theta2):.2f}°")