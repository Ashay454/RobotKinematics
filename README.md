# 🤖 2-DOF Planar Robotic Arm Kinematics

This repository contains Python scripts demonstrating the **Forward Kinematics (FK)** and **Inverse Kinematics (IK)** for a simple two-degree-of-freedom (2-DOF) planar robotic arm. Both scripts use the `numpy` library for mathematical calculations and `matplotlib` for visualization.

## 🌟 Key Concepts

### 1\. Forward Kinematics (`forward.py`)

Forward Kinematics determines the **end-effector's position** in Cartesian space, given the **lengths of the arm links** and the **angles of the joints**.

### 2\. Inverse Kinematics (`inverse.py`)

Inverse Kinematics determines the **joint angles** required to place the end-effector at a **desired target position** in Cartesian space. This is a crucial aspect of robotics for path planning and control.

## 🛠️ Requirements

To run the scripts, you will need **Python 3** installed, along with the following libraries:

  * **`numpy`**: For numerical operations, especially trigonometric functions.
  * **`matplotlib`**: For plotting and visualizing the robotic arm.

You can install the required libraries using pip:

```bash
pip install numpy matplotlib
```

## 📂 Project Structure

```
RobotKinematics
├── forward.py        # Script for Forward Kinematics calculation and visualization
├── inverse.py        # Script for Inverse Kinematics calculation and visualization
├── README.md         # Project documentation (this file)      
└── requirements.txt
```

## 🚀 Usage

### 1\. Forward Kinematics

The `forward.py` script calculates and plots the end-effector position based on predefined joint angles ($\theta_1$ and $\theta_2$).

#### Example Code Snippet:

```python
# Link lengths
L1 = 100
L2 = 100

# Joint angles (in degrees)
theta1 = 45
theta2 = 30
# ...
# Coordinates are calculated and plotted
```

#### How to Run:

```bash
python forward.py
```

### 2\. Inverse Kinematics

The `inverse.py` script calculates the required joint angles ($\theta_1$ and $\theta_2$) to reach a specified target $(x, y)$ coordinate and plots the resulting arm configuration.

#### Example Code Snippet:

```python
# Link lengths
L1 = 100
L2 = 100

# Target coordinates
x_target = 120
y_target = 80
# ...
# Joint angles (theta1, theta2) are calculated using the law of cosines and plotted.
```

The core IK calculation for the 2-DOF arm uses geometry and the Law of Cosines to find $\theta_2$:

$$
\cos(\theta_2) = \frac{x_{\text{target}}^2 + y_{\text{target}}^2 - L_1^2 - L_2^2}{2 L_1 L_2}
$$

The calculation then finds $\theta_1$ using the angle to the target and a correction angle:

#### How to Run:

```bash
python inverse.py
```

The script will also print the calculated joint angles to the console:

```
Theta1 = 45.41°, Theta2 = -48.19°
```

-----

## ⚙️ Customization

You can easily modify the parameters in both scripts:

  * **Link Lengths (`L1`, `L2`):** Change the size of the robotic arm.
  * **Forward Kinematics:** Adjust `theta1` and `theta2` (in degrees) to see different arm poses.
  * **Inverse Kinematics:** Change `x_target` and `y_target` to test reaching different points in the workspace.

## 🤝 Contribution

Feel free to fork the repository and submit pull requests with any improvements, especially related to handling the two possible solutions (elbow-up/elbow-down) for Inverse Kinematics\!
