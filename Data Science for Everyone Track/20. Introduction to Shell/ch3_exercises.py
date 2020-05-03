# Exercise_1 
tail -n 5 seasonal/winter.csv  > last.csv

--------------------------------------------------
# Exercise_2 
#1
tail -n 2 seasonal/winter.csv > bottom.csv
#2
head -n 1 bottom.csv


--------------------------------------------------
# Exercise_3 
cut -d, -f2 seasonal/summer.csv | grep -v Tooth

--------------------------------------------------
# Exercise_4 
cut -d, -f2 seasonal/summer.csv | grep -v Tooth | head -n 1

--------------------------------------------------
# Exercise_5 
grep 2017-07  seasonal/spring.csv | wc -l

--------------------------------------------------
# Exercise_6 
head -n 3 seasonal/*.csv

--------------------------------------------------
# Exercise_7 
cut -d, -f2 seasonal/winter.csv | grep -v Tooth | sort -n -r

--------------------------------------------------
# Exercise_8 
cut -d, -f2 seasonal/winter.csv | grep -v Tooth | sort | uniq -c

--------------------------------------------------
# Exercise_9 
head

--------------------------------------------------
# Exercise_10 
#1
wc -l seasonal/*.csv
#2
wc -l seasonal/*.csv | grep -v  total
#3
wc -l seasonal/*.csv | grep -v  total | sort -n | head -n1


--------------------------------------------------
