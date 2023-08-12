# How to set up mujoco
1. download and copy to .mujoco, also install mujoco_py. import mujoco_py and get path to add.
2. and the path to .bashrc, but when using conda, we need to update the .zshrc
https://blog.csdn.net/thinszx/article/details/104601606
3. we need to activate and source ~/.zshrc


# pyproject.toml-based
which is required to install pyproject.toml-based projects
for mpi4py;  https://stackoverflow.com/questions/28440834/error-when-installing-mpi4py
sudo apt-get install libopenmpi-dev

# gcc
fatal error: GL/glew.h: No such file or directory  #include <GL/glew.h>
distutils.errors.CompileError: command '/usr/bin/gcc' failed with exit code 1  

solution： https://github.com/openai/mujoco-py/issues/745
``` 
sudo apt-get install libglew-dev
```
