### jupyter

直接进去就是root，建议用这个  
docker run -itd --name=ipy --user root -p 8888:8888 -v /home/**tusimple**/work:/home/jovyan/work jupyter/datascience-notebook:latest bash


然后用 jupyter notebook --allow-root

进入后允许sudo  
docker run -itd --name=ipy -e GRANT_SUDO=yes  -p 8888:8888 -v /home/tusimple/work:/home/jovyan/work jupyter/datascience-notebook:latest bash

### 镜像源
（1）中科大（亲测好用）：https://www.jianshu.com/p/6172f03a24ff
（2）阿里：https://blog.csdn.net/educast/article/details/89954496
（3）自带镜像（不太好用）:https://www.jb51.net/article/147925.htm
