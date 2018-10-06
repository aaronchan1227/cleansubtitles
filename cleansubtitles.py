## @author: Chanakya Varma
## Written for IND ENG 135, Fall 2018, UC Berkeley
## Team: The Jokestor


from bs4 import BeautifulSoup
import argparse

def cleanFile(file_name):
	#Reading dirty file
	dirty_file = open(file_name, "r")
	dirty_text = dirty_file.read()
	soup = BeautifulSoup(dirty_text, "lxml")
	dirty_file.close()

	#Write into clean file
	clean_file_name = "[CLEANED] " + file_name
	clean_file = open(clean_file_name, "w")
	clean_file.write(soup.get_text())
	clean_file.close()

	print("Cleaning is complete.")

def main(file_name):
    print("File '" + file_name + "' has been read. ")
    cleanFile(file_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Enter the file name without quotations')
    parser.add_argument('file_name', help='enter the name of the .srt file')
    args = parser.parse_args()

    main(args.file_name)

