from pylsl import StreamInlet
from pylsl.resolve import resolve_stream
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ======= Configuration for each signal type =======
stream_types = {
    'EEG_raw': {'channels': 7, 'buffer_size': 500},  # Updated from 6 to 7 channels (timestamp + 6 EEG channels)
    'PPG_raw': {'channels': 4, 'buffer_size': 500},  # Updated from 3 to 4 channels (timestamp + 3 PPG channels)
    'IMU_raw': {'channels': 4, 'buffer_size': 500},  # Updated from 3 to 4 channels (timestamp + 3 IMU channels)
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
    # 'Delta': {'channels': 5, 'buffer_size':100},
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
            if stype == 'EEG_raw':
                if ch == 0:
                    ax.set_ylabel(f"{stype} Timestamp", fontsize=8)
                elif ch == 1:
                    ax.set_ylabel(f"{stype} LF", fontsize=8)
                elif ch == 2:
                    ax.set_ylabel(f"{stype} OTEL", fontsize=8)
                elif ch == 3:
                    ax.set_ylabel(f"{stype} REF1", fontsize=8)
                elif ch == 4:
                    ax.set_ylabel(f"{stype} RF", fontsize=8)
                elif ch == 5:
                    ax.set_ylabel(f"{stype} OTER", fontsize=8)
                elif ch == 6:
                    ax.set_ylabel(f"{stype} REF2", fontsize=8)
            elif stype == 'PPG_raw':
                if ch == 0:
                    ax.set_ylabel(f"{stype} Timestamp", fontsize=8)
                elif ch == 1:
                    ax.set_ylabel(f"{stype} GREEN", fontsize=8)
                elif ch == 2:
                    ax.set_ylabel(f"{stype} RED", fontsize=8)
                elif ch == 3:
                    ax.set_ylabel(f"{stype} INFRARED", fontsize=8)
            elif stype == 'IMU_raw':
                if ch == 0:
                    ax.set_ylabel(f"{stype} Timestamp", fontsize=8)
                elif ch == 1:
                    ax.set_ylabel(f"{stype} X", fontsize=8)
                elif ch == 2:
                    ax.set_ylabel(f"{stype} Y", fontsize=8)
                elif ch == 3:
                    ax.set_ylabel(f"{stype} Z", fontsize=8)
            else:
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

