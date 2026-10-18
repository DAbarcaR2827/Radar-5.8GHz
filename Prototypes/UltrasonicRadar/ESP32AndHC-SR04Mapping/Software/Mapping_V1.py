import serial
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

ser = serial.Serial('COM4', 9600, timeout=1)

Xpoints = deque(maxlen=500)
Ypoints = deque(maxlen=500)
Zpoints = deque(maxlen=500)


plt.ion()

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim([-200, 200])
ax.set_ylim([-200, 200])
ax.set_zlim([-50, 200])
#[Limit, Limit]


def to_cartesian(azDEG, elDEG, distance):
    if distance <= 0:
        return None, None, None
    azRAD = np.deg2rad(azDEG)
    elRAD = np.deg2rad(elDEG)
    x = distance * np.cos(elRAD) * np.cos(azRAD)
    y = distance * np.cos(elRAD) * np.sin(azRAD)
    z = distance * np.sin(elRAD)
    return x, y, z


sc = ax.scatter([], [], [], c='blue', s=10, alpha=0.7)

print("Waiting data...")

try:
    while True:
        if ser.in_waiting > 0:
            raw = ser.readline().decode('utf-8', errors='ignore').strip()

            if "Azimut:" in raw and "Elevation:" in raw and "distance:" in raw and "Second distance:" in raw:
                try:
                    argument = raw.split('|')
                    azimut = int(argument[0].split(':')[1].strip())
                    elevation = int(argument[1].split(':')[1].strip())
                    dist1 = float(argument[2].split(':')[1].strip())
                    dist2 = float(argument[3].split(':')[1].strip())

                    azimut2 = (azimut + 180) % 360
                    elevation2 = (elevation * -1)
                    x1, y1, z1 = to_cartesian(azimut, elevation, dist1)
                    x2, y2, z2 = to_cartesian(azimut2, elevation2, dist2)


                    if x1 is not None:
                        Xpoints.append(x1)
                        Ypoints.append(y1)
                        Zpoints.append(z1)
                    
                    if x2 is not None:
                        Xpoints.append(x2)
                        Ypoints.append(y2)
                        Zpoints.append(z2)

                    sc._offsets3d = (
                        np.array(Xpoints),
                        np.array(Ypoints),
                        np.array(Zpoints)
                    )
                    fig.canvas.draw_idle()
                    plt.pause(0.01)

                except (ValueError, IndexError) as e:
                    print(f"Parse error: {e} | raw: {raw}") 

except KeyboardInterrupt:
    print("\nAdiosito Gru...\nVector salió del radar")
    ser.close()
