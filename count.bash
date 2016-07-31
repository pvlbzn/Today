#!/bin/bash


#
# Information about number of days and how much already done.
#
NDAY=$( ls -ld */ | wc -l )
DONE=$(( ${NDAY}+1-1 ))
echo -e "done ${DONE}"
PERCENT=$( bc <<< "scale=2; "$DONE" / 3.65" )

echo -e "days:\t\t${NDAY}"
echo -e "done: \t\t${PERCENT}%\n"


#
# Information about .md files, which are main used format. Code
# files is not much relevant for stats.
#
MDFILES=$( echo */* | grep .md | wc -w )
# This variable value is a bug-prone because of white space prefix
# which should be cut for calculations.
WORDS=$( cat */*.md | wc -w )

echo -e ".md files:\t${MDFILES}"
echo -e ".md words:\t${WORDS}\n"


#
# Information about averanges. Averange words per each .md file
# and averange number of words per day.
#
AVGWORDS=$(( ${WORDS} / ${MDFILES} ))
AVGPERDAY=$(( ${WORDS} / ${NDAY} ))

echo -e "avg per .md:\t${AVGWORDS}"
echo -e "avg per day:\t${AVGPERDAY}"
