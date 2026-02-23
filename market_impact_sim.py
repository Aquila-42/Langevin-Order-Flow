import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('dark_background')

class PhysicsImpactSimulator:
    def __init__(self, n_steps=400, n_levels=100, tick_size=0.1):
        self.n_steps = n_steps
        self.n_levels = n_levels
        self.tick_size = tick_size
        self.mid_prices = np.zeros(n_steps)
        self.order_books = [] 
        self.stats = []

    def simulate(self):
        current_mid = 100.0
        velocity = 0.0 # Price momentum
        volatility = 0.12
        
        # Wall indices (Fixed support/resistance)
        wall_indices = [25, 75] 
        
        for t in range(self.n_steps):
            # 1. Stochastic Force (Brownian Motion)
            force = np.random.normal(0, volatility)
            
            # 2. "Wall Force" (Repulsion Logic)
            # Calculate price position in grid units
            price_idx = (current_mid - 95) / self.tick_size
            
            for w_idx in wall_indices:
                dist = price_idx - w_idx
                if abs(dist) < 5: # Interaction zone
                    # Inverse square law repulsion (Physics-inspired)
                    repulsion = 0.15 / (dist if abs(dist) > 0.1 else 0.1)
                    force += repulsion

            # 3. Update Velocity and Position (Langevin Dynamics)
            velocity = 0.8 * velocity + force # 0.8 is "friction"
            current_mid += velocity
            self.mid_prices[t] = current_mid
            
            # 4. Generate Order Book with Volumetric Walls
            bid_vols = np.random.gamma(2, 5, self.n_levels)
            ask_vols = np.random.gamma(2, 5, self.n_levels)
            
            for idx in wall_indices:
                # Walls "shimmer" with random institutional activity
                bid_vols[idx] += np.random.uniform(150, 300)
                ask_vols[idx] += np.random.uniform(150, 300)
            
            self.order_books.append((bid_vols, ask_vols))
            
            # Calculate Imbalance
            b_sum, a_sum = np.sum(bid_vols), np.sum(ask_vols)
            self.stats.append({
                'bid_sum': b_sum, 'ask_sum': a_sum,
                'imbalance': (b_sum - a_sum) / (b_sum + a_sum)
            })

class QuantumVisualizer:
    def __init__(self, simulator):
        self.sim = simulator

    def animate(self):
        heatmap = np.zeros((self.sim.n_levels, self.sim.n_steps))
        for t, (b, a) in enumerate(self.sim.order_books):
            heatmap[:, t] = b + a

        fig = plt.figure(figsize=(16, 9), facecolor='#0D1117')
        gs = fig.add_gridspec(1, 2, width_ratios=[5, 1])
        ax_hm = fig.add_subplot(gs[0, 0])
        ax_st = fig.add_subplot(gs[0, 1])

        # Modern Magma/Plasma Hybrid Look
        im = ax_hm.imshow(heatmap, aspect='auto', cmap='magma', origin='lower', interpolation='gaussian')
        line, = ax_hm.plot([], [], color='#00FFFF', lw=2, label='Price Path')
        glow, = ax_hm.plot([], [], color='#00FFFF', lw=6, alpha=0.3) # Neon glow effect

        ax_hm.set_title("ADVANCED ORDER FLOW: PHYSICS-IMPACT ENGINE", color='cyan', loc='left', family='monospace')
        
        # Imbalance bar
        bar = ax_st.bar([0], [0], color='lime')
        ax_st.set_ylim(-1, 1)
        ax_st.set_title("NET PRESSURE", color='white', fontsize=10)
        
        txt = ax_st.text(0, -1.3, '', color='white', ha='center', family='monospace')

        def update(frame):
            im.set_array(heatmap[:, :frame+1])
            im.set_extent([0, frame+1, 0, self.sim.n_levels])
            
            x = np.arange(frame+1)
            y = (self.sim.mid_prices[:frame+1] - self.sim.mid_prices[0]) / self.sim.tick_size + (self.sim.n_levels/2)
            
            line.set_data(x, y)
            glow.set_data(x, y)
            ax_hm.set_xlim(0, max(50, frame+1))
            
            imb = self.sim.stats[frame]['imbalance']
            bar[0].set_height(imb)
            bar[0].set_color('#00FF41' if imb > 0 else '#FF3131')
            
            txt.set_text(f"STEP: {frame}\nIMB: {imb:.4f}\nVOL: {int(self.sim.stats[frame]['bid_sum'])}")
            return [im, line, glow, bar[0], txt]

        ani = animation.FuncAnimation(fig, update, frames=self.sim.n_steps, interval=30, blit=True)
        plt.show()

if __name__ == "__main__":
    sim = PhysicsImpactSimulator()
    sim.simulate()
    view = QuantumVisualizer(sim)
    view.animate()
