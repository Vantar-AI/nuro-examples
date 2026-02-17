<div align="center">

# Nuro Examples

**Tutorials, examples, and benchmarks for the [Nuro SDK](https://github.com/Vantar-AI/nuro).**

</div>

---

## Examples

| Example | Description | Backends Tested |
|---------|-------------|-----------------|
| `basics/hello_spikes.py` | Your first spiking network in Nuro | GPU |
| `basics/populations.py` | Working with populations and dynamics | GPU |
| `basics/plasticity.py` | Learning rules — STDP, three-factor, reward-modulated | GPU |
| `vision/dvs_anomaly.py` | DVS camera anomaly detection (industrial IoT) | GPU, Loihi |
| `audio/keyword_spotting.py` | Spiking keyword spotter for edge deployment | GPU, Loihi, Speck |
| `robotics/gesture_control.py` | Gesture recognition for robot control | GPU, SpiNNaker |
| `probabilistic/bayesian_inference.py` | Bayesian inference on thermodynamic hardware | GPU, CN101 |
| `hybrid/vision_reasoning.py` | Multi-backend: vision (Loihi) + reasoning (CN101) | Loihi, CN101 |

## Getting Started

```bash
pip install nuro
git clone https://github.com/Vantar-AI/nuro-examples.git
cd nuro-examples
python basics/hello_spikes.py
```

## Structure

```
basics/          # Start here — fundamentals of the Nuro API
vision/          # Computer vision with event cameras and SNNs
audio/           # Audio processing and keyword spotting
robotics/        # Sensorimotor loops and robot control
probabilistic/   # Bayesian inference, generative models
hybrid/          # Multi-backend workloads
benchmarks/      # Performance comparisons across backends
```

## Current Status

🚧 **Pre-alpha** — Examples will be added as the core SDK develops.

## License

Apache 2.0

---

<div align="center">

**[Nuro SDK](https://github.com/Vantar-AI/nuro)** · **[Research](https://github.com/Vantar-AI/research)** · **[Vantar AI](https://vantar.ai)**

</div>
