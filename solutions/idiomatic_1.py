import os
import glob
import yaml

pattern = os.path.join('sample_data', '*.yaml')
for fname in glob.glob(pattern):
    with open(fname) as fh:
        print fname, len(yaml.safe_load(fh).get('members') or [])
