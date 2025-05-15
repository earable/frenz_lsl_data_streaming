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

Before using the toolkit, ensure the following:

- A **Frenz Brainband**
- A **MacOS** laptop or desktop with **Bluetooth** and **internet**
- A **valid product key**
- A **Python 3.9** environment

---

## 🧪 Setting Up the Python Environment

### 1. Check Python 3.9

```bash
python3.9 --version
```

### 2. Create a Virtual Environment

```bash
python3.9 -m venv myenv
```

### 3. Activate the Environment (macOS)

```bash
source myenv/bin/activate
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
    channel_count=6,
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
