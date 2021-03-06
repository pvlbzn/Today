#!/bin/bash


#
# Information about number of days and how much is already done.
#
NDAY=$( ls -ld */ | wc -l )
DONE=$(( ${NDAY}+1-1 ))
PERCENT=$( bc <<< "scale=2; "$DONE" / 3.65" )

echo "Duration"
echo -e "days: \t\t${NDAY:5}"
echo -e "done: \t\t${PERCENT}%\n"


#
# Information about .md files, which is the main used format. Code
# files is not much relevant for stats.
#
MDFILES=$( echo */* | grep .md | wc -w )
# This variable value is a bug-prone because of white space prefix
# which should be cut for calculations.
WORDS=$( cat */*.md | wc -w )

echo "Count:"
echo -e ".md files:\t${MDFILES:5}"
echo -e ".md words:\t${WORDS:3}\n"


#
# Information about averanges. Averange words per each .md file
# and an averange number of words per a day.
#
AVGWORDS=$(( ${WORDS} / ${MDFILES} ))
AVGPERDAY=$(( ${WORDS} / ${NDAY} ))

echo "Words per:"
echo -e "avg per .md:\t${AVGWORDS}"
echo -e "avg per day:\t${AVGPERDAY}"
