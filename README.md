# stable_difussion_scripts
scripts for training and inferring stable diffusion models


## For using the scripts in colab:

```python
!pip install requests
```

```python

import requests

# Save getStyles.py as file to colab working directory
# If you are using GitHub, make sure you get the "Raw" version of the code

url = 'https://raw.githubusercontent.com/ameerfayiz/stable_difussion_scripts/main/getStyles.py'
r = requests.get(url)

# make sure your filename is the same as how you want to import 
with open('getStyles.py', 'w') as f:
    f.write(r.text)

# now we can import
import getStyles as gs
```
