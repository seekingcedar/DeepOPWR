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

## 3. Clone the DeepOPWR Repository

In the designated directory, clone the following repository:

```bash
git clone https://github.com/JakeMikouchi/DeepOPWR.git
```

A folder should appear in the designated directory named DeepOPWR. This folder contains the entire model but additional
steps are needed in order to run the model.

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

## 4. Install Required Package

Run the following command to install the required package with the correct version:

```bash
python -m pip install TensorFlow==2.15.0
```

## 5. Update Absolute Paths

In the DeepOPWR folder, open the file named `model_paths.py`, you will need to update the update the absolute paths used for DeepONet with 
the correct paths for your system. To do this, replace any instance of the string /home/rjmikouc/scratch_dir/deeponet_midas/Solo_model/ with 
/gpfs_common/share02/ardor/unityid/deeponet_midas/DeepOPWR/

```text
/home/rjmikouc/scratch_dir/deeponet_midas/Solo_model/ --> /gpfs_common/share02/ardor/unityid/deeponet_midas/DeepOPWR/
```

Congratulations, you are now ready to use the DeepOPWR model.


# Running The Code

## 1. Create Your Loading Pattern

In the DeepOPWR directory, there is a file named case.yaml. This file acts as the input to DeepOPWR and is where you will define your loading pattern.  
A simple loading pattern already exists within the file. Notice that the existing loading pattern is in the quarter core configuration, DeepOPWR can 
only accept quarter core loading patterns so please do not alter the current shape of the input (including the number of elements in the pattern). 
To update the loading pattern, you can change the assembly definition at any valid location. Available assembly definitions are '201', '251', '252', 
'321', '322' as defined in your project assignment. Assembly locations that are designated as '10' are reflector locations, and assembly locations 
designated as '00' are void locations DO NOT CHANGE ANY REFLECTORS OR VOIDs IN THE INPUT. 

## 2. Run The Model
To run the model, enter the following command into the command line: 

```bash
python3 run_model.py --input case.yaml 
```
When running the model, please do so through an interactive session on the hpc.



