
## copy file
scp user@ip:remote_dir local/dir   
scp local/dir user@ip:remote_dir

## mount driver
[detail](https://qa.1r1g.com/sf/ask/238510121/)

```
sudo apt-get install sshfs

mkdir ~/remote_code # create a target directory
sshfs $USER@remote.example.com:/home/$USER/code ~/remote_code # mount from remote to the current device
```

## white list
hosts.allow