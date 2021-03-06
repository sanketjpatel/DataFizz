# Solution to AllMyBooksArePacked

Please check out 'books.json' which is the output of my python program.

The source files can be found inside 'src/main/python/' folder.
* bookparser.py
    Contains methods to make a book object (dictionary) from parsed HTML.
* extract.py
    Parses each HTML file. Makes a list of books by using bookparser.
* collect.py
    Given a list of books, collects some of them to put in a box.
    Modifies the original list to contain only the remaining books.
* allocate.py
    Allocates a given list of books to N boxes of capacity 10 pounds each.
    Writes the list of boxes to a json file named 'books.json'
    
EXTENSION PROBLEMS:

1. Domains beyond Amazon.com
    This parser will mostly not work, unless the other domain uses the same tags and attributes, and similar tree structure. We will need to implement a different parse method. Something that could work; Use Machine Learning and give lots of sample data so the parser can improve over time to 'learn' where the information of the book resides.

2. Products beyond just simply books.
    Parsers need to change. Although, collect and allocate to boxes should work well with minor modifications. The basic problem is a variation of the 0-1 Knapsack with weight=value. Slightly different from 'subset-sum' problem. We want to maximize our value of the knapsack.
    
3. Parse and ship 2,000,000 books:
    This solution uses Dynamic Programming, and a few optimization techniques to keep the runtime polynomial. Few of them are as follows:
    - Calculation of values in DP table stops as soon as the box is filled. Worst case for calculating DP table is O(N*W), where N is the number of books and W is the capacity of box. Will have big constant factor if the scaling factor to make all weights integers is large.
    - The list of books is reduced every time a book is put into the box. So the next iterations for calculating DP table will take less time. Worst case is we extract one book per iteration, so O(N)
    - Overall runtime complexity is O(W*N^2)
    
    However, if we don't want to maximize weights in each box, we can employ a greedy algorithm. This will take O(N log N) time.
    Greedy approach - Sort the book list. Keep iterating through the book list from both sides. If we can put it in the box, remove from the list and add to box contents.

    Even less optimal approach would take O(N) time. Starting from the first element in the list, keep adding books to a box. If you can't add a book to the current box, append box to the box_list. Take a new box, and repeat.
