# Exercise_1 
echo $OSTYPE

--------------------------------------------------
# Exercise_2 
#1
testing=seasonal/winter.csv
#2
head -n1 $testing


--------------------------------------------------
# Exercise_3 
for filetype in docx odt pdf; do echo $filetype; done

--------------------------------------------------
# Exercise_4 
for filename in people/*; do echo $filename; done

--------------------------------------------------
# Exercise_5 
for file in seasonal/*.csv; do grep 2017-07 $file | tail -n1; done

--------------------------------------------------
