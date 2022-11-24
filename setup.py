pixray_version = "latest release" #@param ["latest release", "next planned release"]
branch = "release"
if pixray_version == "next planned release":
  branch = "master"
git clone --recursive --branch $branch https://github.com/pixray/pixray
pip install -r pixray/requirements.txt
pip install basicsr
pip uninstall -y tensorflow 
git clone https://github.com/pixray/diffvg
%cd diffvg
git submodule update --init --recursive
python setup.py install
%cd ..
!pip freeze | grep torch

import sys
sys.path.append("pixray")
import pixray
