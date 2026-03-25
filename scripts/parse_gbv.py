import csv

with open(r"C:\Users\hamed\Downloads\gbv - raw.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

books = []
current_book = {}
current_field = None
empty_count = 0

for line in lines:
    if line.strip() == '':
        empty_count += 1
        if empty_count >= 4:
            if current_book:
                books.append(current_book)
            current_book = {}
            current_field = None
            empty_count = 0
    elif len(line) > 21 and line[21] == ':':
        empty_count = 0
        current_field = line[:21].strip()
        value = line[23:].strip()
        if current_field in current_book:
            current_book[current_field] += ' | ' + value
        else:
            current_book[current_field] = value
    else:
        empty_count = 0
        value = line.strip()
        if current_field:
            current_book[current_field] += ' ' + value

if current_book:
    books.append(current_book)

all_fields = []
for book in books:
    for field in book.keys():
        if field not in all_fields:
            all_fields.append(field)
print(all_fields)

with open(r"C:\Users\hamed\Downloads\gbv - clean.txt", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_fields)
    writer.writeheader()
    for b in books:
        writer.writerow(b)
print(len(books))


