import typer


def linear_search():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    search = typer.prompt("what number are you looking for")
    search = int(search)
    num_searches = 0
    print('performing linear search')    
    for x in prime_numbers:
        num_searches += 1
        print(f'is {search} equal to {x}?')
        if search == x:
            print(f'found {search}, took me {num_searches} searches')
            return
    
    print('couldn\'t find {search} in the array')

linear_search()

def binary_search():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    search = typer.prompt("what number are you looking for")
    search = int(search)
    num_searches = 0
    print('performing binary search')    
