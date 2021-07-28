from ds_store import DSStore
import argparse
import requests
import os
import sys

def read_file(file):
	dsstore = DSStore.open(file, 'r+')
	for data in dsstore:
		data = str(data)
		content = data.replace("<","")
		content = content.replace(">","")
		content = content.split(" b")
		if len(content) > 0:
			print(f"[+] {content[0]}")

def download(url):
	name = url.replace("://","_")
	name = name.replace(":","_")
	name = name.replace("/.DS_Store","")
	name = name.replace(".","_")
	name = "/tmp/"+name

	try:
		r = requests.get(url)
		if r.status_code == 200:
			try:
				open(name,"wb").write(r.content)
			except:
				print(f"[i] Large file in: {url}")
				print("[i] Please do to download the manual and use -f for single file analysis...")
	except:
		pass
	
	return name

def main():
	if args.file:
		read_file(args.file)

	if args.urllist:
		urls = open(args.urllist).readlines()
		for url in urls:
			url = url.replace("\n","")
			print(f"\n> {url}\n")
			dsfile = download(url)
			try:
				read_file(dsfile)
				os.remove(dsfile)
			except:
				pass
			

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", help="Path to the DS_Store file", required=False)
	parser.add_argument("-l", "--urllist", help="List of urls", required=False)
	args = parser.parse_args()

	print("""
\u001b[33;1m
	+-+-+-+-+-+-+-+-+-+-+-+
	|d|s|_|a|n|a|l|y|s|e|r|
	+-+-+-+-+-+-+-+-+-+-+-+
\u001b[0m    
\u001b[31m[?] Search files and paths in .DS_Store\u001b[0m""")
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
