from pylsl import StreamInlet
from pylsl.resolve import resolve_stream
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ======= Configuration for each signal type =======
stream_types = {
    # 'EEG_raw': {'channels': 6, 'buffer_size': 500},
    # 'PPG_raw': {'channels': 3, 'buffer_size': 500},
    # 'IMU_raw': {'channels': 3, 'buffer_size': 500},
    # 'EEG_filtered': {'channels': 4, 'buffer_size': 500},
    # 'EOG_filtered': {'channels': 4, 'buffer_size': 500},
    # 'EMG_filtered': {'channels': 4, 'buffer_size': 500},
    # 'Posture': {'channels': 1, 'buffer_size': 1},
    # 'PoAS': {'channels': 1, 'buffer_size': 100},
    # 'SleepStage': {'channels': 1, 'buffer_size':100},
    # 'Focus': {'channels': 1, 'buffer_size':100},
    # 'SignalQuality': {'channels': 4, 'buffer_size':100},
    # 'Alpha': {'channels': 5, 'buffer_size':100},
    # 'Beta': {'channels': 5, 'buffer_size':100},
    # 'Gamma': {'channels': 5, 'buffer_size':100},
    'Delta': {'channels': 5, 'buffer_size':100},
    # 'Theta': {'channels': 5, 'buffer_size':100},
}

# ======= Find and connect to streams =======
inlets = {}
buffers = {}
lines = {}
axes_dict = {}

for i, (stype, config) in enumerate(stream_types.items()):
    print(f"Looking for {stype} stream...")
    stream = resolve_stream('type', stype)[0]
    inlets[stype] = StreamInlet(stream)

    # Buffer initialization
    buffers[stype] = np.zeros((config['buffer_size'], config['channels']))

# ======= Create graphical interface =======
total_plots = sum([v['channels'] for v in stream_types.values()])
fig, axes = plt.subplots(total_plots, 1, figsize=(10, 8), sharex=True)
fig.suptitle("Real-time EEG, PPG, IMU Signals, Processed data from FRENZ band", fontsize=14)

plot_idx = 0
for stype, config in stream_types.items():
    axes_dict[stype] = []
    lines[stype] = []

    for ch in range(config['channels']):
        ax = axes[plot_idx]
        if stype == 'Posture':
            text = ax.text(0.5, 0.5, 'Waiting...', ha='center', va='center', fontsize=14, transform=ax.transAxes)
            ax.set_yticks([])
            ax.set_xticks([])
            ax.set_frame_on(False)
            lines[stype].append(text)
        else:
            line, = ax.plot(buffers[stype][:, ch])
            ax.set_ylabel(f"{stype} Ch{ch+1}", fontsize=8)
            axes_dict[stype].append(ax)
            lines[stype].append(line)
        plot_idx += 1

# ======= Function to update data for animation =======
def update(frame):
    for stype, inlet in inlets.items():
        chunk, _ = inlet.pull_chunk(timeout=0.0)
        if chunk:
            chunk = np.array(chunk)
            if stype == 'Posture':
                latest_text = chunk[-1][0]  # lấy chuỗi cuối cùng
                lines[stype][0].set_text(f'{stype}: {latest_text}')
            else:
                buffers[stype] = np.vstack((buffers[stype], chunk))[-stream_types[stype]['buffer_size']:]
                for ch in range(stream_types[stype]['channels']):
                    data = buffers[stype][:, ch]
                    lines[stype][ch].set_ydata(data)
                    axes_dict[stype][ch].relim()
                    axes_dict[stype][ch].autoscale_view()
    return sum(lines.values(), [])  # flatten list

ani = animation.FuncAnimation(fig, update, interval=100)
plt.tight_layout()
plt.show()

