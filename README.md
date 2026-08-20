# DeepOPWR

# For using surrogate models in MIDAS, please follow below steps:

## 1. Create a Conda Environment

Create a Conda environment with Python 3.11:

```bash
conda create -n myenv python=3.11.14
conda activate myenv
```

## 2. Install DeepXDE

Install the required version of DeepXDE:

```bash
pip install deepxde==1.14.0
```

## 3. Replace the DeepXDE Package Contents

Clone the following repository:

```bash
git clone https://github.com/nhnkkhang/DeepOnet-Nuclear.git
```

Replace the contents of the installed `deepxde` package directory with the files from the cloned repository.

Typical location of the `deepxde` package inside the Conda environment:

```text
<conda_path>/envs/myenv/lib/python/site-packages/deepxde
```

## 4. Install Required Package Versions

Install the following package versions (install one by one to prevent conflict):

```text
TensorFlow        2.15.0
NumPy             1.26.4
Matplotlib        3.10.8
scikit-learn      1.7.1
scikit-optimize   0.10.2
joblib            1.5.3
```

## 5. Update Absolute Paths

In `midas_data.py`, update the absolute paths used for DeepONet model loading/reloading with the correct paths for your system.

> This step is required for proper DeepONet model loading and reloading functionality.
# Pre-trained Model Paths
