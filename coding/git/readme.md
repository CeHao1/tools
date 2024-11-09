# recursive clone submodules

```
git clone xxx --recursive
```

## edit .gitmodules
```
[submodule "lisdf"]
	path = lisdf
	url = https://github.com/Learning-and-Intelligent-Systems/lisdf
```
need to specify the name, path and url

## sync
```
git submodule sync
git submodule update --init --recursive
```
