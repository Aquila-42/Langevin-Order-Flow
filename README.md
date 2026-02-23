# 🌊 Physics-Impact Engine: Order Flow Simulation

This repository contains a market microstructure simulator that treats price movement as a particle moving through a force field. I built this to experiment with applying **Classical Mechanics** and **Langevin Dynamics** to financial order books.

## 🚀 The Concept
Most market simulators use simple random walks. I wanted to build something more "physical." In this engine:
* **The Price** is a particle with momentum and friction.
* **Liquidity Walls** act as repulsive force fields.
* **The Order Book** is a dynamic volumetric heatmap.

---

## 🛠️ Technical Features

### 1. Langevin Dynamics Logic
The price update isn't just random; it follows a velocity-based momentum model:
$$v_{t+1} = \gamma v_t + F_{stochastic} + F_{repulsion}$$
This creates a more "organic" price path that exhibits inertia, rather than the jittery movement of a standard Wiener process.

### 2. Inverse-Square Repulsion
When the price approaches "Institutional Walls" (large limit orders), the engine applies a repulsion force inspired by **Coulomb's Law**. The closer the price gets to the wall, the harder it is pushed back, simulating the difficulty of "breaking" a massive support or resistance level.



### 3. Dynamic Heatmap Visualization
The simulator generates a real-time "Order Flow" heatmap. 
* **Vertical Axis:** Price levels.
* **Horizontal Axis:** Time.
* **Intensity:** Liquidity volume (using a Gamma distribution to simulate realistic order sizes).

---

## 🧰 Tech Stack
* **Language:** Python 3.x
* **Math/Sim:** NumPy, SciPy
* **Visualization:** Matplotlib (Animation & Heatmap)

## 🧪 The "Fun" Part
The coolest part of this project is the **shimmer effect** on the walls. The "institutional" volume isn't static; it fluctuates randomly to simulate high-frequency traders pulling and adding liquidity near key price levels, creating a "pulsing" effect in the order flow.

---
*Built for the fun of deconstructing the physics of finance.*
