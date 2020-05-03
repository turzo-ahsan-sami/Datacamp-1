# Exercise_1 
nano names.txt

--------------------------------------------------
# Exercise_2 
#1
cp seasonal/spring.csv seasonal/summer.csv /home/repl/
#2
grep -h -v Tooth spring.csv summer.csv > temp.csv
#3
history | tail -n3 > steps.txt


--------------------------------------------------
# Exercise_3 
#1
nano dates.sh
#2
bash dates.sh


--------------------------------------------------
# Exercise_4 
#1
nano teeth.sh
#2
bash teeth.sh > teeth.out
#3
cat teeth.out


--------------------------------------------------
# Exercise_5 
#1
nano count-records.sh
#2
bash count-records.sh seasonal/*csv > num-records.out


--------------------------------------------------
# Exercise_6 
#1
nano range.sh
#2
nano range.sh
#3
nano range.sh
#4
bash range.sh seasonal/*.csv > range.out


--------------------------------------------------
# Exercise_7 
#1
nano date-range.sh
#2
bash date-range.sh seasonal/*.csv
#3
bash date-range.sh seasonal/*.csv | sort


--------------------------------------------------
