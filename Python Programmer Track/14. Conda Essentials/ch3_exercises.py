# Exercise_1 
#1
conda activate course-env
#2
conda activate pd-2015
#3
conda deactivate


--------------------------------------------------
# Exercise_2 
conda env remove --name deprecated

--------------------------------------------------
# Exercise_3 
#1
conda create --name conda-essentials attrs=19.1.0 cytoolz
#2
conda activate conda-essentials
#3
conda list


--------------------------------------------------
# Exercise_4 
conda env export  -n course-env --file course-env.yml

--------------------------------------------------
# Exercise_5 
#1
conda env create --file environment.yml
#2
conda env create --file shared-config.yml


--------------------------------------------------
