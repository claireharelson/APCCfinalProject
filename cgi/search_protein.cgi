#!/usr/local/bin/python3

import jinja2
import mysql.connector
import cgi

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader( searchpath="/var/www/html/charels1/final/html" )

# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('search.tmpl')

# Get data from html form
form = cgi.FieldStorage()
term = form.getvalue('search')

# Python code to carry out SQL commands
class SearchResults():
	structure_id = None
	name = None
	head = None
	deposition_date = None
	release_date = None
	structure_method = None
	resolution = None
	journal_reference = None
	author = None

results = list()

def main():

	conn = mysql.connector.connect(user='charels1', password='Gobruins44!', host='localhost', database='charels1')
	curs = conn.cursor()

	qry = "SELECT structure_id, name, head, deposition_date, release_date, structure_method, resolution, journal_reference, author FROM pdb WHERE structure_id = %s"
	curs.execute(qry, (term,))

	for (structure_id, name, head, deposition_date, release_date, structure_method, resolution, journal_reference, author) in curs:
		result = SearchResults()
		result.structure_id = structure_id
		result.name = name
		result.head = head
		result.deposition_date = deposition_date
		result.release_date = release_date
		result.structure_method = structure_method
		result.resolution = resolution
		result.journal_reference = journal_reference
		result.author = author
		results.append(result)	

	conn.commit()
	conn.close()


if __name__ == '__main__':
	main()


print("Content-Type: text/html\n\n")
print(template.render(results=results))
            
