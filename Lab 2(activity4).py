def format_table(column_titles, data):
    column_width = 20

    for title in column_titles:
        print(f"{title:{column_width}}", end='')
    print()

    print("=" * (column_width * len(column_titles)))

    for row in data:
        for value in row:
            print(f"{value:{column_width}}", end='')
        print()

column_titles = []
num_columns = int(input("Enter the number of columns: "))
for i in range(num_columns):
    title = input(f"Enter title for column {i + 1}: ")
    column_titles.append(title)

data = []
num_rows = int(input("Enter the number of rows: "))
for _ in range(num_rows):
    row_data = []
    for title in column_titles:
        value = input(f"Enter {title}: ")
        row_data.append(value)
    data.append(row_data)

format_table(column_titles, data)
