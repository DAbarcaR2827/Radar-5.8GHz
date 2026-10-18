from matplotlib.widgets import Slider
import serial
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM4', 9600, timeout=1)

Map = {}

fig, axd = plt.subplot_mosaic(
    [['Full', 'Slice'], 
     ['Slider', 'Slider']], 
    figsize=(15, 8)
)

axFull = fig.add_subplot(axd['Full'].get_subplotspec(), projection='3d')
axSlice = fig.add_subplot(axd['Slice'].get_subplotspec(), projection='3d')
axSlider = axd['Slider']

axFull.set_title('3D Full Map', fontsize=14, fontweight='bold')
axFull.set_xlabel('X'); axFull.set_ylabel('Y'); axFull.set_zlabel('Z')
axFull.set_xlim([-200, 200]); axFull.set_ylim([-200, 200]); axFull.set_zlim([-100, 200])

axSlice.set_title('CORTE TRANSVERSAL', fontsize=14, fontweight='bold')
axSlice.set_xlabel('X'); axSlice.set_ylabel('Y'); axSlice.set_zlabel('Z')
axSlice.set_xlim([-200, 200]); axSlice.set_ylim([-200, 200]); axSlice.set_zlim([-100, 200])

axSlider.set_title('Altura del Corte', fontsize=12)
Zslider = Slider(axSlider, 'Z (cm)', -50, 200, valinit=0, valstep=5) 


ScFull = axFull.scatter([], [], [], c=[], cmap='plasma', s=10, alpha=0.8)
ScSlice = axSlice.scatter([], [], [], c=[], cmap='plasma', s=25, alpha=1.0)
Cbar = fig.colorbar(ScFull, ax=[axFull, axSlice], shrink=0.6, pad=0.1)
Cbar.set_label('Elevación | DEG |')

Allxs, Allys, Allzs, AllColors = [], [], [], []
SliceThickness = 15

plt.ion()


def to_cartesian(azDEG, elDEG, distance):
    if distance <= 0:
        return None, None, None
    azRAD = np.deg2rad(azDEG)
    elRAD = np.deg2rad(elDEG)
    x = distance * np.cos(elRAD) * np.cos(azRAD)
    y = distance * np.cos(elRAD) * np.sin(azRAD)
    z = distance * np.sin(elRAD)
    return x, y, z

def actualizar_corte(val):
    Zobject = Zslider.val
    mask = np.abs(np.array(Allzs) - Zobject) < SliceThickness

    if np.any(mask):
        xsCut = np.array(Allxs)[mask]
        ysCut = np.array(Allys)[mask]
        zsCut = np.array(Allzs)[mask]
        ColorCut = np.array(AllColors)[mask]

        ScSlice._offsets3d = (xsCut, ysCut, zsCut)
        ScSlice.set_array(ColorCut)
    else:
        ScSlice._offsets3d = ([], [], [])
        
    fig.canvas.draw_idle()

Zslider.on_changed(actualizar_corte)
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
                    
                    if dist1 > 0:
                        Map[(azimut, elevation)] = dist1
                    
                    if dist2 > 0:
                        Map[(azimut2, elevation2)] = dist2

                    Allxs, Allys, Allzs, AllColors = [], [], [], []
                    for (az, el), dist in Map.items():
                        x, y, z = to_cartesian(az, el, dist)
                        if x is not None:
                            Allxs.append(x); Allys.append(y); Allzs.append(z)
                            AllColors.append(el)

                    if len(Allxs) > 0:
                        ScFull._offsets3d = (np.array(Allxs), np.array(Allys), np.array(Allzs))
                        ScFull.set_array(np.array(AllColors))

                        actualizar_corte(Zslider.val)


                    fig.canvas.draw_idle()
                    plt.pause(0.01)

                except (ValueError, IndexError) as e:
                    print(f"Parse error: {e} | raw: {raw}") 

except KeyboardInterrupt:
    print("\nAdiosito Gru...\nVector salió del radar")
    ser.close()
