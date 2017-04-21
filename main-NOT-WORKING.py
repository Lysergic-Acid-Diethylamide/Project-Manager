#Author :: Lysergic
import sys
import getopt

def main(argv):
	#Program variables
	project = ""

	try:
		opts, args = getopt.getopt(argv,"ha:d:pc:o:",["help","append=","delete=","purge", "check=", "open="])

	except getopt.GetoptError as e:
		print(str(e))
		print("Use '-h' for usage information")
		sys.exit(2)

	for opt, arg in opts:
			if opt in ("-h", "--help"):		#Each option has its own personal function
				usage()

			elif opt in ("-a", "--append"):
				appendProject(arg)
			
			elif opt in ("-d", "--delete"):
				deleteProject(arg)

			elif opt in ("-p", "--purge"):
				purgeProjects()

			elif opt in ("-c", "--check"):
				checkProject(arg)

			elif opt in ("-o", "--open"):
				openProject(arg)

	displayProjects()

def usage():
	print("Project Lister by Lysergic")
	print
	print("Description: Displays a custom project list and includes some customizable")
	print("features.")
	print
	print("Options:")
	print("-h --help		Displays help information")
	print
	print("-a --append <project-name> 		Add a new project to the list")
	print("-d --delete <project-name> 		Remove a project from the list")
	print("-p --purge 						Remove ALL projects from the list")
	print("-c --check <project-name> 		Check off a project to show completion **UNDER CONSTRUCTION**")
	print("-o --open <project-name> 		Open a project's folder				   **UNDER CONSTRUCTION**")
	print
	print("Usage:")
	print("projects -a Break_IRC_Server -f /root/home/Desktop/Projects/IRC_Breaking")
	print("projects -d completed_Project")
	print
	print("Important:: projects are cAsE sENsitIVE and MUST be typed WITHOUT spaces")

def appendProject(project):
	projectList = open("projects.txt","a")

	project = project.rstrip(" ")

	print("Adding [{}] to project list!").format(project)
	projectList.write((project+"\n"))	#Removing whitespace character because otherwise it gets bitchy
	print("Done!")
	sys.exit(1)

def deleteProject(project):
	projectList = open("projects.txt","r")

	tempFile = open("tmp.txt","w")
	print("Removing [{}] from project list!").format(project)

	for line in projectList:
		if line != project:			#Re-write file without the specified file
			tempFile.write(line)

	os.remove(projectList)
	os.rename("tmp.txt","projects.txt")
	print("Done!")
	sys.exit(1)

def purgeProjects():
	
	print("Are you sure you want to remove all projects?")
	ans = input("WARNING - WILL REMOVE ALL PROJECTS, TYPE 'nah' TO EXIT\n")

	if ans == "nah":
		print("Exiting!")

	else:
		os.remove("projects.txt")	#Delete project file and create a new blank one
		open("projects.txt","r")
		print("Removed all projects!")
		
	sys.exit(1)

def checkProject(project):
	print("Sorry, but this module is")
	print(" ___________________")
	print("|___|___|___|___|___| ")
	print("|_|___|___|___|___|_|")
	print("| UNDER CONSTRUCTION|")	#1337 A5cii 4rt
	print("|___|___|___|___|___|")
	print("|_|___|___|___|___|_|")
	print
	sys.exit(1)

def openProject(project):
	print("Sorry, but this module is")
	print(" ___________________")
	print("|___|___|___|___|___| ")
	print("|_|___|___|___|___|_|")
	print("| UNDER CONSTRUCTION|")
	print("|___|___|___|___|___|")
	print("|_|___|___|___|___|_|")
	print
	sys.exit(1)

def displayProjects():
	#This is where it gets interesting
	projectList = open("projects.txt","r")
	projects = []
	longestProjectName = 0
	longestLine = 24

	for line in projectList:
		line = line.rstrip("\n")
		if len(line) > longestProjectName:	#Get longest name for text formatting
			longestProjectName = len(line)

		projects.append(line)

	print(projects)
	print(str(longestLine))

	print
	print("       //////////////////////////////////////////////////")
	print("       //  ___  ___   ___    _  ___  ___  _____  ____  //")
	print("       // | _ || _ | |   |  | || __||  _||_   _||  __| //")
	print("       // |  _||   \ | | | _| || _| | |_   | |  _\ \   //")	#Fairly self-explainitory
	print("       // |_|  |_|\_\|___||___||___||___|  |_| |____|  //")
	print("       //                                              //")
	print("       //////////////////////////////////////////////////")
	print

	#Here's where it gets complicated
	longestLine += (longestProjectName*2)

	print(longestLine)

	#Head
	#I hate this bit, such a pain to debug
	#ughhhhhhhhh
	longestLine = longestLine / 2

	print(longestLine)
	if longestLine % 2 > 0:	#Odd numbers don't play nice so, remove them
		longestLine += 1
	print(longestLine)
	
	print(" ___"+("_"*(longestLine+16))+"___")
	print("|   "+(" "*(longestLine+16))+"   |")	#Maths, maths and oh glorious maths.
	print("|   "+(" "*(longestLine/2))+"Current Projects"+(" "*(longestLine/2))+"   |")
	print("|___"+("_"*(longestLine+16))+"___|")

	longestLine += 16 	#Don't ask

	#Body
	print("|   "+(" "*longestLine)+"   |")
	projectNo = 0

	for project in projects:
		projectNo += 1	#Counter for project list index, nothing technical

		if len(project) % 2 > 0:
			project = (project + " ")	#Remember this line? I do. Fuck odd numbers.

		print("|   " + (" "*(longestLine/2)) + project  + "   |") #This. Fucking. Line.
	print("|___"+("_"*longestLine)+"___|")
		
if __name__ == "__main__":
	main(sys.argv[1:])
