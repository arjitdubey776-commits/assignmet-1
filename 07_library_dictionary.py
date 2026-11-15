library = {
    101: "Python",
    102: "Data Structures",
    103: "Computer Networks"
}

print("Library books:", library)

book_id = int(input("Enter book ID to search: "))

if book_id in library:
    print("Book name:", library[book_id])
else:
    print("Book not found")
