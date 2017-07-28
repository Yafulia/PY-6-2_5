import os
import subprocess


def convert(files, dir):
	for file in files:
		subprocess.run(["convert", os.path.join(*[dir, 'Source'], file),
		"-resize", "200", os.path.join(*[dir, 'Result'], file)])


def main():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	os.mkdir('Result')
	
	files_to_convert = os.listdir(os.path.join(current_dir, 'Source'))
	convert(files_to_convert, current_dir)


main()