from fileReader import FileReader
from gpt import Gpt
import csv
import ast

f = FileReader("test_textbook.pdf")
excerpts = f.contents_list

flashcards_deck = []
for excerpt in excerpts:
    try:
        flashcards = ast.literal_eval(Gpt.query_gpt(excerpt))
        flashcards_deck.extend(flashcards)
    except:
        pass

csv_file = "sample.csv"

# Write the 2D array to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in flashcards_deck:
        cleaned_row = [row[0].replace(',', ''), row[1].replace(',', '')]
        writer.writerow(cleaned_row)

print(f"Data has been written to {csv_file}")