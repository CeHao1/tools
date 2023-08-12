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


# torch model


