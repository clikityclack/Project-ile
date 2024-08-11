import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def projectile(u, angg, gr):
    ang = np.radians(angg)

    st.write(f"The Angle in Radians is = {ang:.2f}")

    vy = u * np.sin(ang)
    vx = u * np.cos(ang)

    st.write(f"The velocity in x is {vx:.2f} m/s and the velocity in y is {vy:.2f} m/s")

    T = 2 * vy / gr
    T = int(100 * T)

    cm_range = int(vx * T) + 1
    cm_height = int(100 * vy * vy / (2*gr)) + 1

    st.write(f"Max Range is {cm_range-1} cm, Max Height is {cm_height-1} cm, and Time of Flight is {T / 100:.2f} s")

    array = np.zeros([cm_height, cm_range])

    for t in range(0, T):
        x = vx * t
        y = vy * t - (gr/2) * t * t / 100
        x = int(x)
        y = cm_height - int(y) - 1
        array[y, x] = 1

    # Plot the trajectory
    plt.figure(figsize=(5, 5))
    plt.imshow(array, 
               cmap='Blues_r', 
               interpolation='none'
               )
    plt.axis('off')  # Hide axes
    st.pyplot(plt)  # Display the plot in Streamlit

# Streamlit interface
st.title('Projectile Motion Simulation')

# Slider for velocity and angle
u = st.slider('Select the velocity of the projectile (m/s)', min_value=0.0, max_value=50.0, value=10.0, step=0.1)
a = st.slider('Select the angle of projection (degrees)', min_value=0.0, max_value=90.0, value=45.0, step=0.1)

# Gravity values for different celestial bodies, including Pluto
gravity_values = {
    "Pluto": 0.62,
    "Mercury": 3.7,
    "Mars": 3.71,
    "Uranus": 8.69,
    "Venus": 8.87,
    "Earth": 9.81,
    "Saturn": 10.44,
    "Neptune": 11.15,
    "Jupiter": 24.79,
    "Sun": 274
}

# Use `select_slider` to display planet names on the slider
planet_name = st.select_slider(
    'Select the celestial body (Gravity in m/s²)',
    options=list(gravity_values.keys()),
    value="Earth"
)

# Get the gravity value for the selected planet
g = gravity_values[planet_name]

# Display the selected planet and gravity
st.write(f"Selected Celestial Body: {planet_name} with gravity {g} m/s²")

# Update the plot continuously
projectile(u, a, g)