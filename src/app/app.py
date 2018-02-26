from extract import extract
from collect import collect_to
import json
import os

out_dir = os.environ.get('OUT_DIR')

books = extract(20)
scaled_weights = [int(book['shipping_weight']*10) for book in books]

boxes = []

i=1
while(len(scaled_weights)):
    (box, books, scaled_weights) = collect_to(i, books, scaled_weights)
    boxes.append(box)
    i+=1

with open('%s/books.json' % out_dir, 'w') as outfile:
    json.dump({'boxes': boxes}, outfile, sort_keys=True, indent=4, separators=(',', ': '))

print open('%s/books.json' % out_dir, 'r').read()
outfile.close()
