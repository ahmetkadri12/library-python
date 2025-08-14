class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

    def set_borrowed_status(self, status):
        self.is_borrowed = bool(status)

    def __str__(self):
        return self.display_info()
