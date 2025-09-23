# Create book list
favorite_books = [
    ("Illiad", "Homer"),
    ("C programming language", "Dennis Ritchie"),
    ("Software design for flexibility", "Chris Hanson"),
    ("Structure and Interpretation of computer programs", "Harold Abelson"),
    ("Let over Lambda", "Doug Hoyte")
]

# Create dictionary of students
students = {"Logan": 100,
            "Mason": 101,
            "Jeff": 102,
            "Hamilton": 103,
            "Cade": 104,
            "Linus": 105
            }

def print_first_3_books() : 
    "Prints the first 3 books that are in my favorite book list"
    for name,author in favorite_books[0:3] : 
        print(author+":",name)

