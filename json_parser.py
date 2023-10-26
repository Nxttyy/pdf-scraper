import json

js = open("./electrical_json.json")

tables_data = json.load(js)

# get single table data among many tables across pages
for table_data in tables_data:

	# get rows wrapped in extra "[]" if there are multiple (means table_data["text"][0])
	for every_data in table_data["data"]:

		# loop through all the rows
		for row in every_data:
			cell_text = row["text"] 

			if (cell_text):
				if "\r" in cell_text:
					# print("*")
					cell_text = cell_text.replace("\r", " ")
				print(cell_text)
		print("\n")

js.close()
print("Done")