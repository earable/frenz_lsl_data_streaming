# 🧠 FRENZ Streaming Toolkit

The **Frenz Streaming Toolkit** enables researchers and developers to stream real-time brain data from the **Frenz Brainband** to their computer. This facilitates the development of custom neuroscience applications and provides access to clean, distinct brain signals — serving as a practical alternative to PSG (Polysomnography), the clinical gold standard.

---

## 🚀 Getting Started

### 📦 Installation

Install via `pip`:

```bash
pip install frenztoolkit
```

Or build from source by downloading this repository.

### 🔑 Product Key Required

To activate the toolkit, a valid **product key** is required.  
Please contact **Earable's sales department** to obtain one.

---

## 🖥️ System Requirements

Before using the toolkit, ensure you have the following:

- A Frenz Brainband
- A laptop/desktop (MacOS, Windows 64) with Bluetooth and internet connectivity
- A product key (contact Earable's sales department if you don't have one)
- Python 3.9 environment:

Goto page: https://www.python.org/downloads/release/python-3913/

Choose your OS setup file:

MacOS: https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg

Windows 64: https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe

### Check if Python 3.9 is installed
```bash
python3.9 --version
```
or

```bash
python --version
```

Result:

Python 3.9.xx

### Create new virtual environment
```bash
python3.9 -m venv vir_name
```
or

```bash
python -m venv vir_name
```

### Environment activation:
### MacOS
```bash
source vir_name/bin/activate  
```

### Windows 64 OS
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

```bash
.\vir_name\Scripts\Activate.ps1
```

---

## 🌐 Lab Streaming Layer (LSL) Integration


The toolkit supports **real-time data streaming** through the **Lab Streaming Layer (LSL)**.

https://labstreaminglayer.readthedocs.io/info/getting_started.html

### 📥 Installing Requirements

Navigate to your project directory and install dependencies:

```bash
pip install -r requirements.txt
```

### 🛠️ Installing LSL Library if error

You can install `liblsl` using either `conda` or `homebrew`:

#### Using Conda

```bash
conda install -c conda-forge liblsl
```

#### Using Homebrew

```bash
brew install labstreaminglayer/tap/lsl
```

### 🧭 Set Environment Variable (macOS ≥ 10.15)

```bash
export DYLD_LIBRARY_PATH=/opt/homebrew/lib
```

> 🔁 Replace the path if your LSL library is installed elsewhere.

---

## 🧬 Sample Code

> ⚠️ **Make sure all dependencies are installed and the environment is activated.**

### 📤 Streaming Data

File: `lsl_data_streaming.py`

To stream new brainwave data:

```python
from pylsl import StreamInfo, StreamOutlet, cf_string, cf_double64

info = StreamInfo(
    name='brainwave_stream',
    type='EEG',
    channel_count=7,
    nominal_srate=125,
    channel_format=cf_double64,
    source_id='brainband_001'
)

outlet = StreamOutlet(info)

# Send data
outlet.push_sample(data)    # Send single sample
outlet.push_chunk(data)     # Send a batch (chunk) of samples
```

---

### 📥 Reading and Plotting Data

File: `lsl_data_reader.py`

- Reads LSL data streams
- Plots the real-time brain signals

Make sure the `stream_types` match those defined in your `lsl_data_streaming.py` (name, type, channels).

---

## 📚 License & Support

For licensing and support inquiries, please contact **Earable’s sales department**.
