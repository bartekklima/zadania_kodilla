class Film:                                                                 # Tworzenie klas
    def __init__(self, title, publication_date, type, number_of_plays):
        self.title = title
        self.publication_date = publication_date
        self.type = type
        self.number_of_plays = number_of_plays
    
    def play(self):
        self.number_of_plays += 1
    
    def __str__(self):
        self.number_of_plays += 1
        return "{} ({})".format(serial.title, serial.publication_date)

class Serial(Film):
    def __init__(self, episode_number, season_number, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        self.number_of_plays += 1
        return "{} S{:02}E{:02}".format(serial.title, serial.season_number, serial.episode_number)

def lista(kind):
    Title = input('Title: '), 
    Publication_date = input('Publication_date: '), 
    Type = input('Type: '), 
    Number_of_plays = input('Number_of_plays: ')
    
    if kind == 'film':
        film = Film(                                    # Przypisywanie klas do zmiennych
            title=Title, 
            publication_date=Publication_date, 
            type=Type,
            number_of_plays=Number_of_plays)

    elif kind == 'serial':
        # serial = Serial(
        #     title=input('Title: '), 
        #     publication_date=input('Publication_date: '), 
        #     type=input('Type: '),
        #     number_of_plays=input('Number_of_plays: '), 
        #     episode_number=input('episode_number: '), 
        #     season_number=input("season_number: "))
        pass
    else:
        raise NameError ('wroeng kind. Choose between "film" or "serial"')


# film = Film(                                    # Przypisywanie klas do zmiennych
#     title="The Simpsons", 
#     publication_date=2013, 
#     type="comedy",
#     number_of_plays= 2) 

# serial = Serial(
#     title ="The Simpsons", 
#     episode_number=5, 
#     season_number=1,
#     publication_date=1903, 
#     type="comedy",
#     number_of_plays= 2)

lista(input('enter kind: '))
