# doc to show how to use argparse 

## basic code
```
parser = argparse.ArgumentParser()
parser.add_argument('--argname', default=0, type=int, help="help info")
parser.add_argument('--boolean_arg', action='store_true')
args = parser.parse_args()

print(args.argname)
```

## how to call in command line
```
python file_name.py --argname 1 --boolean_arg
```

`store_true` means when call it, this variable is true, else false

## how to use debugger in the vscode
1. first switch to the debug mode in the left column  
2. add the launch.json  
3. set the "python" to be the address of interpreter, e.g. `/anaconda3/envs/py37/bin/python`  
4. add "args" : ["--argname", "1"]  


## problems 
this method has to change args everytime, not as easy as the terminal
