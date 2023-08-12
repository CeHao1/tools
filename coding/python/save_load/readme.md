# loaders

## numpy
[detail](https://numpy.org/doc/stable/reference/generated/numpy.save.html)
```
import numpy as np
np.save(file_dir, file)
file = np.load(file_dir)
```

## pickle
```
f = open(file_path, 'wb')
pickle.dump(file, f)
f.close()

f = open(file_path, 'rb')
file = pickle.load(f)
f.close()
```


# formats


# operation



* joblib
* pandas