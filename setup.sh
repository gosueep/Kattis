
# if [ $1 == 'e' ]; then
#   cd Easy
# elif [ $1 == 'm' ]; then
#   cd Medium
# elif [ $1 == 'c' ]; then
#   cd Challenge
# fi

mkdir $1
cd $1
touch $1.py

if [ $# == 2 ]; then
    n=$2
else
  n=1
fi

for (( i = 0; i < n; i++ )); do
    touch "input$i.txt"
done
