#!/bin/bash

### prerequisite
# sudo apt-get install freeglut3-dev

## create and activate custom conda env
conda update --all
conda create -n same_1 python=3.8
conda activate same_1

## torch 2.3 stable, Cuda 11.8
conda install pytorch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1 pytorch-cuda=11.8 -c pytorch -c nvidia
#pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 --no-cache-dir
pip3 install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.3.0+cu118.html --no-cache-dir
pip3 install torch_geometric --no-cache-dir
pip3 install pyyaml --no-cache-dir
pip3 install scipy tqdm IPython tensorboard matplotlib plotly pyyaml --no-cache-dir
pip3 install pynvml gputil --no-cache-dir
pip3 install scikit-learn --no-cache-dir
pip3 install glfw --no-cache-dir
pip3 install imgui --no-cache-dir
pip3 install opencv-python --no-cache-dir

python3 setup.py develop

# submodule: fairmotion (https://github.com/sunny-Codes/fairmotion)
git submodule init
git submodule update
cd src/fairmotion
python3 setup.py develop

