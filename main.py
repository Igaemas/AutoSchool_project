import os

# -- user configuration --
projectPath = ""

userName = os.getlogin()
userPath = "c:/Users/" + userName + "/Documents/AutoCode/"

# -- user choice --
print("sur quoi voulez-vous travailler ? : ")
print("1 -> HTML")
userChoice = int(input("Que choisissez-vous ? :"))

match userChoice:
  case 1:
    projectPath = userPath + "html/"
  case 2:
    projectPath = userPath + "python/"

# -- dir project creation --
if os.path.exists(projectPath) == True :
  print("this directory already exist.")
  
else :
  print(projectPath)
  