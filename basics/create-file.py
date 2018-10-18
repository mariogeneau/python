# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
def start_setup():
    # ¬¬¬¬¬¬¬¬¬¬¬
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
    prompt = '>>> '
    # ¬¬¬¬¬¬¬¬¬¬¬
    print("MAD PYTHON TEXT FILE CREATOR")
    print("To get started, give a name to your file without extension...")
    # ¬¬¬¬¬¬¬¬¬¬¬
    filename = input(prompt)
    # ¬¬¬¬¬¬¬¬¬¬¬
    print("Now provide the content of the file...")
    # ¬¬¬¬¬¬¬¬¬¬¬
    content = input(prompt)
    # ¬¬¬¬¬¬¬¬¬¬¬
    confirm = input(">>> Do you want to continue with the creation of " + filename + ".txt? (Yes/No)").lower()
    # ¬¬¬¬¬¬¬¬¬¬¬
    if confirm in yes:
        text_file = open(filename + ".txt", "w")
        text_file.write(content)
        text_file.close()
        print("File succesfully created!")
        return True
    elif confirm in no:
        print("Ok, nothing will happen!")
        return False
    else:
       print("Please answer yes or no!, the setup will start again")
       start_setup()
# ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
start_setup()
