# make copy of original directory
cd ./test && cp -R orig copy

# encrypt dir
cd ./test/orig && python ../../clavis.py -e

# unencrypt dir
cd ./test/orig && python ../../clavis.py -d

# should be no differences
cd ./test && diff orig copy