import mysql.connector
from Bio.PDB import PDBParser
import os


# Parse PDB files for relevant information and organize into MySQL database


def main():

	conn = mysql.connector.connect(user='charels1', password='Gobruins44!', host='localhost', database='charels1')
	curs = conn.cursor()


	qry = "INSERT INTO pdb(structure_id, name, deposition_date, release_date, structure_method, resolution, journal_reference, author, head) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

	parser = PDBParser(PERMISSIVE=1)

	directory = '/var/www/html/charels1/final/pdb_files'

	for file in os.listdir(directory):
		structure_id = file[0:4]
		file_name = file
		file_path = directory + '/' + file
		structure = parser.get_structure(structure_id, file_path)

		name = structure.header["name"]
		head = structure.header["head"]
		deposition_date = structure.header["deposition_date"]
		release_date = structure.header["release_date"]
		structure_method = structure.header["structure_method"]
		resolution = structure.header["resolution"]
		journal_reference = structure.header["journal_reference"]
		author = structure.header["author"]
	
		curs.execute(qry, (structure_id, name, deposition_date, release_date, structure_method, resolution, journal_reference, author, head))

	conn.commit()
	conn.close()

main()
