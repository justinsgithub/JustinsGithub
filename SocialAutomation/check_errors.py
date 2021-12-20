from secrets import my_vars


def login_title(wdriver):

    if wdriver.title == my_vars["login_title"]:

        wdriver.quit()

        quit()


def count_400(wdriver, count):

    if count >= 400:

        print(f"HIT {count} QUITTING NOW")

        wdriver.quit()

        quit()


def count_300(wdriver, count):

    if count >= 300:

        print(f"HIT {count} QUITTING NOW")

        wdriver.quit()

        quit()


def unknown_err(wdriver):

    print("UNKNOWN ERR")

    wdriver.quit()

    quit()
