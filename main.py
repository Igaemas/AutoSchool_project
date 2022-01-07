import os

# -- user configuration --
projectPath = ""
userName = os.getlogin()
userPath = "c:/Users/" + userName + "/Documents/AutoCode/"

def Start_Choice():
  print("que voulez vous faire ? : ")
  print("1 -> executer un cours\n2 -> configurer le logiciel")
  userChoice = int(input("Que choisissez-vous ? :"))
  match userChoice:
    case 1:
      Start_Code()
    case 2:
      File_Configuration()

def File_Configuration():
  if os.path.exists(userPath) == False :
    os.mkdir(userPath) 
  if os.path.exists(userPath + "config/") == False :
    os.mkdir(userPath + "config/")
    localConfig = open(userPath + "config/file_config.txt", "w+")
    localConfig.write("0")
    localConfig.close
  print("  \nFichier de configuration créé\n  ")
  Start_Choice()

def Start_Code():
  
  print("sur quoi voulez-vous travailler ? : ")
  print("1 -> HTML")
  userChoice = int(input("Que choisissez-vous ? :"))

  match userChoice:
    case 1:
      projectPath = userPath + "html/"
      print(projectPath)
    case 2:
      projectPath = userPath + "python/"

# ----------------------------------------------------------------

Start_Choice()

# -- dir project creation --
if os.path.exists(projectPath) == True :
  print("this directory already exist.")  
else :
  localConfig = open(userPath + "config/file_config.txt", "w+")
  filename = localConfig.read() + ".html"
  localConfig.write("1")
  localConfig.close
  os.mkdir(projectPath)
  