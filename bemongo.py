#!/usr/bin/env python3
import os, sys
sysArgList, command, doc, collection = sys.argv, "", "", ""
try:
	command = sysArgList[1].lower()
	if command == "add":
		try:
			doc = sysArgList[2]
			print("WARNING: Please make sure your json value quotes are escaped: {test:\\\"escape me\\\"}")
			try:
				collection = sysArgList[3]
			except:
				collection = "test"
			os.system("mongo 127.0.0.1/" + collection + " --eval 'var document=" + doc + ";db." + collection + ".insert(document);'")
		except:
			print("Please specify document to add. For help, enter \"bemongo help\"")
	elif command == "read":
		try:
			collection = sysArgList[2]
		except:
			collection = "test"
		os.system("mongo 127.0.0.1/" + collection + " --eval 'db." + collection + ".find();'")
	else:
		print("bemongo <add | read>\n\nbemongo add <json_document>\nbemongo add <json_document> <collection>\n\nbemongo read\nbemongo read <collection>")
except:
	print("Please specify command (add | read). For help, enter \"bemongo help\"")