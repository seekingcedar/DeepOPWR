# DeepOPWR

# Installation Instructions on NCSU's HAZEL hpc

## 1. Create a Conda Environment

To install DeepOPWR, users will need to create a conda environment in their personal directories in the 'supplemental group storage'.
This is located at '/usr/local/usrapps/ardor/unityid/' where the unityid is your personal unity ID. If this directory does not already 
exist, then you can navigate to '/usr/local/usrapps/ardor/' and create a directory named after your unity ID. 

for all future commands using the 'supplemental group storage' file path, you will need to replace 'unityid' with your personal unity ID.

Once the directory is created, you will need to create a conda environment with python3.11:

```bash
conda create --prefix /usr/local/usrapps/ardor/unityid/deepopwr_env -c conda-forge python=3.11.14
conda activate /usr/local/usrapps/ardor/rjmikouc/deepopwr_env
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
