import os

# Prevent LSL from using IPv6 and multicast to avoid warnings
os.environ["LSL_NO_IPV6"] = "1"
os.environ["LSL_NO_MULCAST"] = "1"

from frenztoolkit import Streamer
import time
import datetime
from pylsl import StreamInfo, StreamOutlet, cf_string

frenz_device_id = "FRENZXXX"
frenz_product_key = "YYY"

# Initialize StreamInfo & StreamOutlet once only
timeinterval = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

# MARK: EEG raw outlet init
info__raw_eeg = StreamInfo(
    name=f'{frenz_device_id}_EEG_raw',
    type='EEG_raw',
    channel_count=6,
    nominal_srate=125,
    channel_format='float32',
    source_id=f'eeg_raw_{frenz_device_id}_{timeinterval}'
)
outlet_raw_eeg = StreamOutlet(info__raw_eeg)

# MARK: PPG raw outlet init
info__raw_ppg = StreamInfo(
    name=f'{frenz_device_id}_PPG_raw',
    type='PPG_raw',
    channel_count=3,
    nominal_srate=25,
    channel_format='float32',
    source_id=f'ppg_raw_{frenz_device_id}_{timeinterval}'
)
outlet_raw_ppg = StreamOutlet(info__raw_ppg)

# MARK: IMU raw outlet init
info__raw_imu = StreamInfo(
    name=f'{frenz_device_id}_IMU_raw',
    type='IMU_raw',
    channel_count=3,
    nominal_srate=50,
    channel_format='float32',
    source_id=f'imu_raw_{frenz_device_id}_{timeinterval}'
)
outlet_raw_imu = StreamOutlet(info__raw_imu)

# MARK: EEG filtered outlet init
info__filtered_eeg = StreamInfo(
    name=f'{frenz_device_id}_EEG_filtered',
    type='EEG_filtered',
    channel_count=4,
    nominal_srate=125,
    channel_format='float32',
    source_id=f'eeg_filtered_{frenz_device_id}_{timeinterval}'
)
outlet_filtered_eeg = StreamOutlet(info__filtered_eeg)

# MARK: EOG filtered outlet init
info__filtered_eog = StreamInfo(
    name=f'{frenz_device_id}_EOG_filtered',
    type='EOG_filtered',
    channel_count=4,
    nominal_srate=125,
    channel_format='float32',
    source_id=f'eog_filtered_{frenz_device_id}_{timeinterval}'
)
outlet_filtered_eog = StreamOutlet(info__filtered_eog)

# MARK: EMG filtered outlet init
info__filtered_emg = StreamInfo(
    name=f'{frenz_device_id}_EMG_filtered',
    type='EMG_filtered',
    channel_count=4,
    nominal_srate=125,
    channel_format='float32',
    source_id=f'emg_filtered_{frenz_device_id}_{timeinterval}'
)
outlet_filtered_emg = StreamOutlet(info__filtered_emg)

# MARK: Posture outlet init
info_posture = StreamInfo(
    name=f'{frenz_device_id}_POSTURE',
    type='Posture',
    channel_count=1,
    nominal_srate=0.2,
    channel_format='string',
    source_id=f'posture_{frenz_device_id}_{timeinterval}'
)
outlet_posture = StreamOutlet(info_posture)

# MARK: PoAS outlet init
info__poas = StreamInfo(
    name=f'{frenz_device_id}_poas',
    type='PoAS',
    channel_count=1,
    nominal_srate=0.2,
    channel_format='float32',
    source_id=f'poas_{frenz_device_id}_{timeinterval}'
)
outlet_poas = StreamOutlet(info__poas)

# MARK: sleep stage outlet init
info__sleep_stage = StreamInfo(
    name=f'{frenz_device_id}_sleep_stage',
    type='SleepStage',
    channel_count=1,
    nominal_srate=0.2,
    channel_format='float32',
    source_id=f'sleep_stage_{frenz_device_id}_{timeinterval}'
)
outlet_sleep_stage = StreamOutlet(info__sleep_stage)

# MARK: focus outlet init
info__focus = StreamInfo(
    name=f'{frenz_device_id}_focus',
    type='Focus',
    channel_count=1,
    nominal_srate=0.5,
    channel_format='float32',
    source_id=f'focus_{frenz_device_id}_{timeinterval}'
)
outlet_focus = StreamOutlet(info__focus)

# MARK: signal quality check outlet init
info__signal_quality = StreamInfo(
    name=f'{frenz_device_id}_signal_quality',
    type='SignalQuality',
    channel_count=4,
    nominal_srate=0.2,
    channel_format='float32',
    source_id=f'signal_quality_{frenz_device_id}_{timeinterval}'
)
outlet_signal_quality = StreamOutlet(info__signal_quality)

# MARK: alpha outlet init
info__alpha = StreamInfo(
    name=f'{frenz_device_id}_alpha',
    type='Alpha',
    channel_count=5,
    nominal_srate=0.5,
    channel_format='float32',
    source_id=f'alpha_{frenz_device_id}_{timeinterval}'
)
outlet_alpha = StreamOutlet(info__alpha)

# MARK: beta outlet init
info__beta = StreamInfo(
    name=f'{frenz_device_id}_beta',
    type='Beta',
    channel_count=5,
    nominal_srate=0.5,
    channel_format='float32',
    source_id=f'beta_{frenz_device_id}_{timeinterval}'
)
outlet_beta = StreamOutlet(info__beta)

# MARK: theta outlet init
info__theta = StreamInfo(
    name=f'{frenz_device_id}_theta',
    type='Theta',
    channel_count=5,
    nominal_srate=0.5,
    channel_format='float32',
    source_id=f'theta_{frenz_device_id}_{timeinterval}'
)
outlet_theta = StreamOutlet(info__theta)

# MARK: gamma outlet init
info__gamma = StreamInfo(
    name=f'{frenz_device_id}_gamma',
    type='Gamma',
    channel_count=5,
    nominal_srate=0.5,
    channel_format='float32',
    source_id=f'gamma_{frenz_device_id}_{timeinterval}'
)
outlet_gamma = StreamOutlet(info__gamma)

# MARK: delta outlet init
info__delta = StreamInfo(
    name=f'{frenz_device_id}_delta',
    type='Delta',
    channel_count=5,
    nominal_srate=0.5,
    channel_format='float32',
    source_id=f'delta_{frenz_device_id}_{timeinterval}'
)
outlet_delta = StreamOutlet(info__delta)

# Start streaming from Frenz
streamer = Streamer(
    device_id=frenz_device_id,
    product_key=frenz_product_key,
    data_folder="./recorded_data",
    turn_off_light=True # Turn off the light on Frenz Band, default is True
)
streamer.start()

# MARK: Streaming loop
# Channel description:
# LF: left forehead
# OTEL: over the ear right
# REF1: left reference
# REF2: right reference
# RF: right forehead
# OTER: over the ear left
# GREEN: green LED
# RED: red LED
# INFRARED: infrared LED
# X: x-axis
# Y: y-axis
# Z: z-axis
# AVG: average

try:
    while True:
        # Check if the session duration is greater than 30 minutes
        # You can change the duration as needed
        if streamer.session_dur > 30 * 60:
            break

        # EEG raw data
        # Channel order: LF, OTEL, REF1, RF, OTER, REF2 (REF1 = REF2 = 0 not used)
        eeg_raw = streamer.DATA["RAW"]["EEG"]
        if eeg_raw.shape[0] > 0:
            outlet_raw_eeg.push_chunk(eeg_raw.copy()[-125:, :].tolist())
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | EEG raw: {eeg_raw.shape}")

        # PPG raw data
        # Channel order: GREEN, RED, INFRARED
        ppg_raw = streamer.DATA["RAW"]["PPG"]
        if ppg_raw.shape[0] > 0:
            outlet_raw_ppg.push_chunk(ppg_raw.copy()[-25:, :].tolist())
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | PPG raw: {ppg_raw.shape}")

        # IMU raw data
        # Channel order: X, Y, Z
        imu_raw = streamer.DATA["RAW"]["IMU"]
        if imu_raw.shape[0] > 0:
            outlet_raw_imu.push_chunk(imu_raw.copy()[-50:, :].tolist())
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | IMU raw: {imu_raw.shape}")

        # EEG filtered data
        # Channel order: LF, OTEL, RF, OTER
        # unit: uV
        eeg_filtered = streamer.DATA["FILTERED"]["EEG"].T
        if eeg_filtered.shape[0] > 0:
            outlet_filtered_eeg.push_chunk(eeg_filtered.copy()[-125:, :].tolist())
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | EEG filtered: {eeg_filtered.shape}")

        # EOG filtered data
        # Channel order: LF, OTEL, RF, OTER
        # unit: uV
        eog_filtered = streamer.DATA["FILTERED"]["EOG"].T
        if eog_filtered.shape[0] > 0:
            outlet_filtered_eog.push_chunk(eog_filtered.copy()[-125:, :].tolist())
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | EOG filtered: {eog_filtered.shape}")

        # EMG filtered data
        # Channel order: LF, OTEL, RF, OTER
        # unit: uV
        emg_filtered = streamer.DATA["FILTERED"]["EMG"].T
        if emg_filtered.shape[0] > 0:
            outlet_filtered_emg.push_chunk(emg_filtered.copy()[-125:, :].tolist())
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | EMG filtered: {emg_filtered.shape}")

        # Posture data
        # value: prone, supine, left, right, head dropped
        posture = streamer.SCORES.get("posture")
        if posture is not None:
            outlet_posture.push_sample([posture])
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | Posture: {posture}")

        # PoAS data
        # value: 0-1
        poas = streamer.SCORES.get("poas")
        if poas is not None:
            outlet_poas.push_sample([poas])
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | PoAS: {poas}")

        # Sleep stage data
        # value < 0: undefined, value = 0: awake, value = 1: light, value = 2: deep, value = 3: REM
        sleep_stage = streamer.SCORES.get("sleep_stage")
        if sleep_stage is not None:
            outlet_sleep_stage.push_sample([sleep_stage])
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | Sleep stage: {sleep_stage}")

        # Focus data
        # value: 0-100
        focus = streamer.SCORES.get("focus_score")
        if focus is not None:
            outlet_focus.push_sample([focus])
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | Focus: {focus}")

        # Signal quality data
        # Channel order: LF, OTEL, RF, OTER
        # value 0 - not good; value 1 - good
        signal_quality = streamer.SCORES.get("sqc_scores")
        if signal_quality is not None:
            outlet_signal_quality.push_chunk(list(signal_quality))
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | Signal quality: {signal_quality}")

        # Alpha data
        # Channel order: LF, OTEL, RF, OTER, AVG
        # unit: dB
        alpha = streamer.SCORES.get("alpha")
        if alpha is not None:
            outlet_alpha.push_chunk(list(alpha))
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | Alpha: {alpha}")

        # Beta data
        # Channel order: LF, OTEL, RF, OTER, AVG
        # unit: dB
        beta = streamer.SCORES.get("beta")
        if beta is not None:
            outlet_beta.push_chunk(list(beta))
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | Beta: {beta}")

        # Theta data
        # Channel order: LF, OTEL, RF, OTER, AVG
        # unit: dB
        theta = streamer.SCORES.get("theta")
        if theta is not None:
            outlet_theta.push_chunk(list(theta))
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | Theta: {theta}")

        # Gamma data
        # Channel order: LF, OTEL, RF, OTER, AVG
        # unit: dB
        gamma = streamer.SCORES.get("gamma")
        if gamma is not None:
            outlet_gamma.push_chunk(list(gamma))
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | Gamma: {gamma}")

        # Delta data
        # Channel order: LF, OTEL, RF, OTER, AVG
        # unit: dB
        delta = streamer.SCORES.get("delta")
        if delta is not None:
            outlet_delta.push_chunk(list(delta))
        print(f"[{datetime.datetime.now()}] Duration: {streamer.session_dur:.2f}s | Delta: {delta}")
        

        time.sleep(1)
except KeyboardInterrupt:
    print("Keyboard interrupt")
    streamer.stop()
except Exception as e:
    print(f"Error: {e}")
    streamer.stop()
    
streamer.stop()
