from tabula.io import read_pdf, convert_into, convert_into_by_batch


# columns = 4
# pfile = read_pdf("./electrical.pdf", pages="45", output_format="json")

convert_into(input_path = "./electrical.pdf", 
			output_path= "./electrical_json.json",
			output_format='json',
			pages='46-55', lattice=True)

# print(pfile)

# convert_into_by_batch(input_dir="./electrical.pdf",
# 						 output_format="json")
print("Done")