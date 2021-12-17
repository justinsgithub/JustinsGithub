from constants import my_vars

def login_title(wdriver):

    if wdriver.title == my_vars["login_title"]:

        wdriver.quit()

        quit()   

def count_200(wdriver, count):

    if count >= 200:

        print("HIT 200 QUITTING NOW")

        wdriver.quit()

        quit()

def unknown_err(wdriver):

    print("UNKNOWN ERR")

    wdriver.quit()

    quit()