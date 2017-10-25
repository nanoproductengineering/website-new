a=1
for i in *.pdf; do
  new=$(printf "../papers/%d.pdf" "$a")
  mv -- "$i" "$new"
  let a=a+1
done
