from itertools import chain, islice
print "\n                              RooT HaXor \n                  Usage python split.py your_file.txt \n         Everyfile will contain 300*100 lines after execution"
def chunks(iterable, n):
   "chunks(ABCDE,2) => AB CD E"
   iterable = iter(iterable)
   while True:
       # store one line in memory,
       # chain it to an iterator on the rest of the chunk
       yield chain([next(iterable)], islice(iterable, n-1))

l = 300*1000
file_large = raw_input()
with open(file_large) as bigfile:
    for i, lines in enumerate(chunks(bigfile, l)):
        file_split = '{}.{}'.format(file_large, i)
        with open(file_split, 'w') as f:
            f.writelines(lines)
