#!/bin/sh

path="$(cygpath $1)"
old="$(cygpath --mixed --absolute "$2")"
new="$(cygpath --mixed --absolute "$5")"

if [ $2 == "/dev/null" ]; then
    echo "no old version for $1"
elif [ $5 == "/dev/null" ]; then
    echo "no new version for $1"
else 
    "/d/tools/DiffMerge_3_3_0_18513/DiffMerge.exe" "$old" "$new" --title1="Old" --title2="New $path"
fi
# "/d/tools/DiffMerge_3_3_0_18513/DiffMerge.exe" "$old" "$new" --title1="Old" --title2="New $path"
