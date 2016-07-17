#!/bin/bash

# Declare variable
Var="value"
# Var = "value" is a mistake, Var will be threated like a command to execute.

echo $Var
# > value
echo ${Var/va/G}
# > Glue

n="file.jpeg"
echo ${n:4}
# > .jpeg
echo ${n:0:4}
# > file

echo "PID: $$"
# > XXXXX

suffix=${n:4}
if [ $suffix == ".jpeg" ] && [ "" != true ]
then
    echo "Ok $((10 + 15))"
else
    echo "Not ok"
fi
# > Ok 25

# Prints file descriptor
echo <(echo "")
# > /dev/fd/63

# Item count
items="$(ls | wc -l)"
case "$items" in
    "0") echo "zero";;
    "1") echo "one";;
    "2") echo "two";;
    *) echo "many";;
esac

function foo() {
    echo "Function! Argument: $1"
    return 0
}
foo "15"
# > Function! Argument: 15

