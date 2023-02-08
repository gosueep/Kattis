
if [ $1 == 'e' ]; then
  cd Easy
elif [ $1 == 'm' ]; then
  cd Medium
elif [ $1 == 'c' ]; then
  cd Challenge
fi

mkdir $2
cd $2
touch $2.py

if [ $# == 3 ]; then
    n=$3
else
  n=1
fi

for (( i = 0; i < n; i++ )); do
    touch "input$i.txt"
done
