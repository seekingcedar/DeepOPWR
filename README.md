# DeepOPWR

# Installation Instructions on NCSU's HAZEL hpc

## 1. Create a Conda Environment

To install DeepOPWR, users will need to create a conda environment in their personal directories in the 'supplemental group storage'.
This is located at '/usr/local/usrapps/ardor/unityid/' where the unityid is your personal unity ID. If this directory does not already 
exist, then you can navigate to '/usr/local/usrapps/ardor/' and create a directory named after your unity ID. 

for all future commands using the 'supplemental group storage' file path, you will need to replace 'unityid' with your personal unity ID.

Once the directory is created, you will create a conda environment with python3.11:

```bash
conda create --prefix /usr/local/usrapps/ardor/unityid/deepopwr_env -c conda-forge python=3.11.14
conda activate /usr/local/usrapps/ardor/rjmikouc/deepopwr_env
```

## 2. Create a Designated Directory

This directory will hold the DeepOPWR and all associated files. It is best to create this directory in the designated scratch directory.
You can use any name, for this demonstration 'NE512_project' is used to name the directory. Every step from this point forward will 
be conducted from the designated directory.

```bash
cd /gpfs_common/share02/ardor/unityid/
mkdir NE512_project
cd ./NE512_project
```

## 3. Clone this Repository

In the designated directory, clone the following repository:

```bash
git clone https://github.com/nhnkkhang/DeepOnet-Nuclear.git
```

Replace the contents of the installed `deepxde` package directory with the files from the cloned repository.


## 2. Install DeepXDE

The next step is to install the required version of DeepXDE. You may need to install pip before installing DeepXDE:

```bash
conda install pip
pip install deepxde==1.14.0
```

## 3. Replace the DeepXDE Package Contents

Clone the following repository:

```bash
git clone https://github.com/nhnkkhang/DeepOnet-Nuclear.git
```

Replace the contents of the installed `deepxde` package directory with the files from the cloned repository.

```bash
cp -rf /gpfs_common/share02/ardor/unityid/NE512_project/DeepOnet-Nuclear/* /usr/local/usrapps/ardor/unityid/deepopwr_env/lib/python3.11/site-packages/deepxde/
```

## 4. Install Required Package Versions

Run the following command to install the following package:

```bash
python -m pip install TensorFlow==2.15.0
```

## 5. Update Absolute Paths

In `midas_data.py`, update the absolute paths used for DeepONet model loading/reloading with the correct paths for your system.

> This step is required for proper DeepONet model loading and reloading functionality.
# Pre-trained Model Paths
