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
        return "{} ({})".format(self.title, self.publication_date)

class Serial(Film):
    def __init__(self, episode_number, season_number, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        self.number_of_plays += 1
        return "{} S{:02}E{:02}".format(self.title, self.season_number, self.episode_number)



def list_maker(lista):                                           # Przypisywaanie danych do film i serial
                                                                 # oraz umieszcznie ich w jednej liscie
    kind=input('enter kind: ')                                       
    Title = input('Title: ')
    Publication_date = int(input('Publication_date: '))
    Type = input('Type: ')
    Number_of_plays = int(input('Number_of_plays: '))
    
    while kind != 'film' and kind != 'serial':
        kind=input ('wrong kind. Choose between "film" or "serial": ')

    if kind == 'film':
        Title = Film(                                    
            title=Title, 
            publication_date=Publication_date, 
            type=Type,
            number_of_plays=Number_of_plays)

        lista.append(Title)

    elif kind == 'serial':
        Episode_number=int(input('episode_number: '))
        Season_number=int(input("season_number: "))
        
        Title = Serial(
            title=Title, 
            publication_date=Publication_date, 
            type=Type,
            number_of_plays=Number_of_plays,
            episode_number=Episode_number, 
            season_number=Season_number)
        
        lista.append(Title)

    return lista

# film = Film(                                   
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

a=[]
list_maker(a)

for i in a:
    i.play()
    print(i, '\n', i.number_of_plays)
