import sublime
import sublime_plugin
import re
import os

# class TestMotherFuckOnSave(sublime_plugin.EventListener):
# 	def on_selection_modified(self,view):
# 		# if(None != tempSel and tempSel == view.sel()[0]):
# 			print(view.sel()[0])

def findNextChar(view,point,findPrev = False):
	point = (findPrev and point - 1) or  point ;
	char = view.substr(point);
	if char == None:
		return -1;
	if re.match("\S",char):
		return char,point;
	else:
		point = (findPrev and point - 1) or  point + 1;
		return findNextChar(view,point,findPrev);

def isLuaFunc(view,wordRegion):
	findNextCharReturn = findNextChar(view,wordRegion.end());
	if(isinstance(findNextCharReturn,(tuple))):
		return view.substr(wordRegion)[0];
	else:
		return -1;

def tryToFindCaller(view,wordRegion):
	point = wordRegion.begin();
	if point == 0:
		return -1;
	prevChar = findNextChar(view,point,True);
	if(prevChar == -1):
		return -1;
	if (prevChar[0] == "." or prevChar[0] == ":"):
		return view.substr(view.word(prevChar[1]-1));
	else:
		return "can't find a caller maybe global";


def TryToFindDef(view,className,FuncName):
	pass


class ExampleCommand(sublime_plugin.TextCommand):


	# def testPrint(index,arg2):
	# 	print(arg2)

	def run(self, edit):

		outRootPath = r"E:\Test\out\L7Utils";
		rootPath = self.view.window().folders();
		print(rootPath[2]);

		# filePath = r"E:\UnityWorkSpace\github\UnityUtility\Assets\L7Utils\AlwaysFaceCamera.cs";
		# file = open(filePath, 'r', encoding="utf-8")

		# newFileText = '';
		# try:
		# 	lines = file.readlines()
		# 	# print(lines[0]);
		# 	for i in range(len(lines)-1):
		# 		print(len(lines[i]));
		# 		# print(i)

		# finally:
		# 	file.close();



		# find all lua files. include subdirectory
		for root, dirs, files in os.walk(rootPath[2]):
			for fileName in files:
				if fileName.endswith(".cs"):
					filePath = os.path.join(root,fileName)
					print("now deal with  " + fileName);
					file = open(filePath, 'r', encoding="utf-8")

					outDirName = root.replace(rootPath[2],outRootPath);
					if not os.path.exists(outDirName):
						os.makedirs(outDirName);

					outFilePath = os.path.join(outDirName,fileName);
					# print(outFilePath);
					outFile = open(outFilePath,'w',encoding = "utf-8")

					try:
						lines = file.readlines()
						newFileText = lines[0];
						for i in range(1, len(lines)-1):
							if(len(lines[i]) > 1 or len(lines[i-1]) <= 1):
								newFileText = newFileText+lines[i];

						outFile.write(newFileText);
					finally:
						file.close();
						outFile.close();

		print("finish");

		# writeFile = open(rootPath[0] + "/.jump_definition.tags", 'wt')
		# try:
		# 	global JSON_DATA
		# 	JSON_DATA = allFuncData
		# 	writeFile.write(json.dumps(allFuncData, indent=4))
		# finally:
		# 	writeFile.close()

		# test = self.view.window().project_data();
		# print(type(test))
		# print(len(test))
		# for key in test.keys():
		# 	print(key);
		# print(test[1])
		# for proj_subdir in self.view.window().project_data()["folders"]:
		# 	print(proj_subdir);
		# self.view.window().show_quick_panel([["a","b","e"],["c","d","e"],["cfewr","d","e"],["c","d","e"],["c","d","e"],["c","d","e"],["c","d","e"],["c","d","e"],["c","d","e"],["c","d","e"],["c","d","e"]], self.testPrint);
		# print(sublime.executable_path());
		# print(self.view.sel()[0])
		# print(tryToFindCaller(self.view,self.view.word(self.view.sel()[0])));


