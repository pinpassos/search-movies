# Import modules
from functions import function

# Main
while True:
    movie_name = str(input('Type a movie name in english: ')).strip()
    movie = function.requisition(movie_name)
    if movie['Response'] == 'False':
        print('Error: ' + movie['Error'])
    else:
        function.movie_details(movie)
        flag = ' '
        while flag not in 'YN':
            flag = str(input('Do you wanna continue?[Y/N]: ')).upper()
            if flag == 'N':
                print('Closing application...')
                function.sleep(2)
                exit()
            elif flag == 'Y':
                print('Here we again!')
                break
            else:
                print('Please choose between Y or N.')
