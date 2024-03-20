### 1. 安装搜狗输入法  
（1）按照官网安装  
（2）安装依赖： https://www.jb51.net/article/139515.htm  
（3）可选，清理之前的fcitx：https://blog.csdn.net/qq_33159059/article/details/85019467  
（4）在系统中设置选择新的输入法：https://blog.csdn.net/github_39533414/article/details/85211012  


### 2. 安装docker  
（1）安装： https://www.runoob.com/docker/ubuntu-docker-install.html  
（2）添加permission：https://blog.csdn.net/gavinclc/article/details/104735127/  

### 3.安装显卡驱动英伟达  
（1）在系统里选择其他显卡，https://ywnz.com/linux/4573.html  
（2）注意不要选版本太高的，除非跑程序。或者先去英伟达官网查看一下驱动版本是否兼容。  

### 4. ubuntu 18.04 字体调整软件  
（1）安装软件：https://jingyan.baidu.com/article/cbf0e50056a6f52eaa28931c.html  
（2）调整显示位置：https://jingyan.baidu.com/article/60ccbceba520e164cab1972c.html  

### 5. v2ray 安装  
（1）安装教程：https://www.bjjem.com/article-8234-1.html  
https://my.oschina.net/u/4437065/blog/3153449  

### 6. electron-ssr 安装  
（1）安装：https://www.jianshu.com/p/fba8637da1e3?from=timeline&isappinstalled=0  

### 7. proxychains 安装
（1）下载安装：https://www.oneone.moe/576.html  
（2）测试：https://blog.csdn.net/lan120576664/article/details/100784380  
（3）git clone 问题：https://blog.csdn.net/baidu_36482169/article/details/82818490

## Install Ubuntu by Udisk
(this link) https://gcore.com/learning/how-to-install-ubuntu-on-windows/
Enter BIOS, select boot sequence. Disable security boot is necessary.
Change the free space type and install.


## 安装Nvidia driver 后网络消失
进入上一个版本的内核，下载对应的一些组件。
进入recover模式后安装对应 dpkg 即可完成修复。

其实因为英伟达显卡需要更高版本的内核，但是他只下载了 N卡的部分，ubuntu 的内核没有被下载。所以需要手动下载。
https://blog.csdn.net/weixin_44420419/article/details/133592805
