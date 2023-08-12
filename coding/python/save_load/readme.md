# loaders

## numpy
[detail](https://numpy.org/doc/stable/reference/generated/numpy.save.html)
```
import numpy as np
np.save(file_dir, file)
file = np.load(file_dir)
```
To .npy

## pickle
```
import pickle 
f = open(file_path, 'wb')
pickle.dump(file, f)
f.close()

f = open(file_path, 'rb')
file = pickle.load(f)
f.close()
```
to .pkl

## joblib
[detail](https://joblib.readthedocs.io/en/latest/generated/joblib.dump.html)
```
import joblib
joblib.dump(file, file_dir)
file = joblib(file)
```

## pandas
```
import pandas as pd
file = pd.DataFrame(np.array([1,2,3]))
file.to_csv(file_dir)
file = pd.read_csv(file_dir)

# extra
to_hdf read_hdf
to_json read_json
```

## yaml

```
import yaml
file = dict()

with open(file_dir, 'w') as f:
    yaml.safe_dump(file)

with open(file_dir, 'r') as f:
    file = yaml.safe_load(f)
```


# file operation

* save file
```
def save_file(file_path, file):
    f = open(file_path, 'wb')
    pickle.dump(file, f)
    f.close()
```
* load file
```
def load_file(file_path):
    f = open(file_path, 'rb')
    file = pickle.load(f)
    f.close()
    return file
```
* search file
```
def search_file(file_dir, file_name):
    make_dir(file_dir)
    file_names = os.listdir(file_dir)
    if file_name in file_names:
        return True
    else:
        return False
```

* delete file
```
def delete_file(file_dir, file_name, data_type=''):
    make_dir(file_dir)
    name_space = os.listdir(file_dir)
    if_exist_flag = False
    for names in name_space:
        if file_name in names:
            os.remove(file_dir + '/' + names)
            print('DELETE; TYPE: {};  delete {} in {}'.format(data_type, file_name, file_dir))
            if_exist_flag = True
    if not if_exist_flag:
        print(file_name, 'doet NOT exists in ', file_dir)
```
* make directory
```
def make_dir(file_dir):
     isExists=os.path.exists(file_dir)
     if not isExists:
         os.makedirs(file_dir)
```

# torch model

```
torch.save(model.state_dict(), file_dir)
weights = torch.load(file_dir, map_location=model.device)
model.load_static_dict(weights, strict=strict)
```
