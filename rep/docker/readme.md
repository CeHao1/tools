# jupyter

直接进去就是root，建议用这个  
docker run -itd --name=ipy --user root -p 8888:8888 -v /home/tusimple/work:/home/jovyan/work jupyter/datascience-notebook:latest bash

然后用 jupyter notebook --allow-root

进入后允许sudo  
docker run -itd --name=ipy -e GRANT_SUDO=yes  -p 8888:8888 -v /home/tusimple/work:/home/jovyan/work jupyter/datascience-notebook:latest bash
