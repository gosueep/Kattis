
if [ $1 == 'e' ]; then
  cd Easy
elif [ $1 == 'm' ]; then
  cd Medium
fi

cd $2

if [ $# == 3 ]; then
    cat "input$3.txt" | py $2.py
else
    cat input.txt | $2.py
fi

