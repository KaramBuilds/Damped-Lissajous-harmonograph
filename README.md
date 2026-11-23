# Damped Lissajous Harmonograph

A physics-based parametric curve generator written in Python using `NumPy` and `Matplotlib`. It simulates two perpendicular damped pendulums losing energy over time to friction—capable of generating both high-contrast static profile artwork (**V1**) and real-time looping animations (**V2**).

![Static Harmonograph V1](Figure_1.png) ![Animated Harmonograph V2](harmonograph_anim.gif)

## Mathematical Model

The simulation computes the $x$ and $y$ positions of a damped pendulum system over time $t$:

$$x(t) = e^{-d \cdot t} \sin(f_1 \cdot t + p)$$

$$y(t) = e^{-d \cdot t} \sin(f_2 \cdot t)$$

Where $e^{-d \cdot t}$ models exponential energy decay due to friction, $f_1$ and $f_2$ define the perpendicular oscillation frequencies, and $p$ sets the phase offset.

## Project Versions (V1 & V2)

| Feature | Version 1 (Static Generator) | Version 2 (Animation Engine) |
| :--- | :--- | :--- |
| **Output** | High-contrast static PNG (`Figure_1.png`, `Figure_2.png`) | Smooth looping GIF (`harmonograph_anim.gif`) |
| **Rendering** | Direct `Matplotlib` line plot (`Agg` backend) | Blitted `FuncAnimation` via `PillowWriter` |
| **Use Case** | Custom GitHub profile avatar & static prints | Real-time visualization of harmonic decay |

### Version 1: Static Avatar Generator
* Renders the complete 5,000-point curve instantaneously on a `#0d1117` GitHub dark background with `#39ff88` neon green line styling.
* Ideal for generating crisp, scalable geometric avatars and wallpapers.

### Version 2: Animated Simulation Engine
* Uses `matplotlib.animation.FuncAnimation` with `blit=True` to progressively trace the curve frame by frame.
* Locks axis limits (`-1.1` to `1.1`) and a `1:1` aspect ratio so the spiral remains centered without camera jitter as it decays inward.
* Exports directly to `harmonograph_anim.gif` at `100 DPI` using `PillowWriter` without requiring external FFmpeg dependencies.

## Prerequisites

Install the required Python libraries (`pillow` is required for V2 GIF export):
```bash
pip install numpy matplotlib pillow
```

## How to Run

1. Run either the V1 (static) or V2 (animated) script in your terminal:
   ```bash
   python harmonograph.py
   ```
   *(Replace `harmonograph.py` with your exact V1 or V2 `.py` filename.)*
2. The script renders silently in the background (`Agg` backend) and saves either the PNG image (V1) or `harmonograph_anim.gif` (V2) directly into your working directory.

## Variables You Can Customize

### Physics & Styling Parameters (V1 & V2)

| Variable | Default | What It Controls | Try Changing It To |
| :--- | :--- | :--- | :--- |
| **`f1`** | `3` | Horizontal oscillation frequency (speed along the X-axis) | `4`, `5`, or `7` |
| **`f2`** | `2` | Vertical oscillation frequency (speed along the Y-axis) | `3`, `4`, or `6` |
| **`d`** | `0.02` | Damping factor (how quickly friction shrinks the spiral inward) | `0.01` (more loops) or `0.05` (tighter spiral) |
| **`p`** | `1.57` | Phase shift in radians ($\approx \pi/2$), which opens up the loops | `0`, `0.78`, or `3.14` |
| **`t`** | `0` to `40` | Total simulation time and resolution (`5000` points) | Increase `40` to `60` if you lower `d` |
| **`color`** | `'#39ff88'` | Line color in hex format (neon green) | `'#58a6ff'` (electric blue) or `'#ff7b72'` (coral) |
| **`linewidth`** | `2.5` | Thickness of the plotted curve | `1.5` (delicate) or `3.5` (bold) |

### Animation Parameters (V2 Only)

| Variable | Default | What It Controls | Try Changing It To |
| :--- | :--- | :--- | :--- |
| **`total_frames`** | `100` | Total number of frames rendered in the animation | `150` or `200` (longer, more detailed trace) |
| **`fps`** | `30` | Playback speed in frames per second | `24` (cinematic) or `60` (ultra-smooth) |
| **`dpi`** | `100` | Output resolution of `harmonograph_anim.gif` (`5x5` inches) | `150` (sharper lines, larger file size) |

### Fun Frequency Ratios (`f1 : f2`) to Try
* **`3 : 2`** — Classic trefoil weave (default)
* **`4 : 3`** — Dense geometric knot
* **`5 : 4`** — Intricate mesh ribbon
