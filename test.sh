#!/usr/bin/env bash

# make copy of original directory
cd ./test
cp -R orig/ copy/

# encrypt dir
cd ./orig
echo -e "Running clavis (encryption)."
python3 ../../clavis.py -e

# unencrypt dir
echo -e "\nRunning clavis (decryption)."
python3 ../../clavis.py -d
cd ..

# should be no differences
echo -e "\nFile structure"
diff -r orig copy

echo -e "\n"

# remove possibly clobbered dir unless leave flag specified
rm -r orig

# rename to restore
mv copy orig

