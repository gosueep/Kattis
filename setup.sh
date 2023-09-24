mkdir $1
cd $1
touch $1.py

if [ $# == 2 ]; then
    n=$2
else
  n=1
fi

for (( i = 0; i < n; i++ )); do
    touch "$i.txt"
done
