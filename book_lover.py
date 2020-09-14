# A booklover regularly buys new books. Unfortunately, she doesn't have much time to read them immediately, 
# so she always has a stack of unread books. When the booklover brings a new book, she puts it on top of the previously bought unread ones. 
# Whenever she feels like reading, she takes a book from the very top of her book stack, finishes it in one go, and puts in on the shelf with the read books.
#
# Given a sequence of the booklover's actions, print out all books that she reads. Books should be printed on separate lines.
#
# The input is as follows. The number n refers to the total number of actions. BUY book_name denotes buying a book called book_name,
# while READ refers to reading the book from the top of the stack.
#
# You can assume that initially, the booklover doesn't have any unread books.
#
# Sample Input 2:
# 
# 8
# BUY Pride and Prejudice
# BUY Anna Karenina
# READ
# BUY Hamlet
# BUY Pride and Prejudice
# BUY Anna Karenina
# READ
# BUY Hamlet
# 
# Sample Output 2:
# 
# Anna Karenina
# Anna Karenina

books = []
for _ in range(int(input())):
    inp = input().split(' ', 1)
    if inp[0] == 'READ':
        if len(books) > 0:
            print(books.pop())
    else:
        books.append(inp[1])
