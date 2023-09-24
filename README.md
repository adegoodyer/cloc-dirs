# cloc-dirs

## Overview
- execute cloc . on all directories in current directory and output sorted report.

```bash
# cloc dirs
cloc-dirs # report only
cloc-dirs --data-analytics # report and perform data analysis

# cloc-dirs-data-analysis
cloc-dirs-data-analysis /Users/adriangoodyer/dt/cloc-dir-report-20230924112500

```

## Install package dependencies
```bash
# install globally
pip install pandas
pip install matplotlib

# or use virtual environment
# (will have to activate/deactivate before/after each use)
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

## Install
Download/clone and add cloned repo location to PATH as you normally would for you shell or OS distribution.

```bash
# edit file
vim ~/.bash_profile
vim ~/.bashrc

# add paths
export PATH="$PATH:/Users/adriangoodyer/src/adegoodyer/cloc-dirs"
export PATH="$PATH:/Users/adriangoodyer/src/adegoodyer/cloc-dirs-data-analysis"

# dot source
source ~/.bashrc  # If you added the line to ~/.bashrc
source ~/.bash_profile  # If you added the line to ~/.bash_profile
```

> Instructions are for vim/bash, feel free to add your own and create a pull request.
