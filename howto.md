//create conda env named nameofenv with python 3.7 or any other desired library

conda create --name nameofenv python=3.7 

list all envs - conda env list

1.// activate conda (base)
conda activate

2.//activate particular environment
source activate nameofenv

//insatlling new packages
conda install packagename

//list packages in env while env NOT running
conda list -n myenv

//list packages in env while env running
conda list

vim ~/. bashrc to open home bashrc file

DEACTIVATE CONDA TERMINAL - conda deactivate

display environment file path - echo $CONDA_PREFIX

## ADD ENV VARIABLES AND UNSET THEM ON EXIT
cd $CONDA_PREFIX
mkdir -p ./etc/conda/activate.d
mkdir -p ./etc/conda/deactivate.d
touch ./etc/conda/activate.d/env_vars.sh
touch ./etc/conda/deactivate.d/env_vars.sh
