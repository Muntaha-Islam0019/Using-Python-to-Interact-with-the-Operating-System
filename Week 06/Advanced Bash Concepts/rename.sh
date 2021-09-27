# for loop example

# what we're doing here is, changing renaming all the files with .HTM extension to .html extension
for file in *.HTM; do
    name=$(basename "$file" .HTM)
    mv "$file" "$name.html"
done