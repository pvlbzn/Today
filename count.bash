#!/bin/bash

# Number of folders equals to number of days.
NDAY=$(ls -ld */ | wc -l)
MDFILES=$(echo */* | grep .md | wc -w)
WORDS=$(cat */*.md | wc -w)

echo -e "Days total:\t$NDAY"
echo -e ".md files:\t$MDFILES"
echo -e ".md words:\t$WORDS"
