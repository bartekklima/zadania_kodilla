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

    def __repr__(self):
        return '%s' %self.title


class Serial(Film):
    def __init__(self, episode_number, season_number, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        self.number_of_plays += 1
        return "{} S{:02}E{:02}".format(self.title, self.season_number, self.episode_number)




def list_maker(a):                                           # Przypisywaanie danych do film i serial
                                                                 # oraz umieszcznie ich w jednej liscie
    def body_list_maker(lista):
        kind=input('enter kind: ')                                       
        Title = input('Title: ')
        Publication_date = int(input('Publication_date: '))
        Type = input('Type: ')
        Number_of_plays = int(input('Number_of_plays: '))
        
        while kind != 'film' and kind != 'serial':
            kind=input ('wrong kind. Choose between "film" or "serial": ')

        if kind == 'film':
            film = Film(                                    
                title=Title, 
                publication_date=Publication_date, 
                type=Type,
                number_of_plays=Number_of_plays)

            lista.append(film)

        elif kind == 'serial':
            Episode_number=int(input('episode_number: '))
            Season_number=int(input("season_number: "))
            
            serial = Serial(
                title=Title, 
                publication_date=Publication_date, 
                type=Type,
                number_of_plays=Number_of_plays,
                episode_number=Episode_number, 
                season_number=Season_number)
            
            lista.append(serial)
    
    body_list_maker(a)             
    while ""==input('Would you like add one more film - PRESS ENTER (enter something and press enter to skip)'):  # Powtórzenie funkji
        body_list_maker(a)
 



def list_filter(lista):             # Funkcja rozdzielająca bibliotekę filmów i seriali
    films = []
    serials = []
    for i in lista:
        if type(i)==Film:
            films.append(i)
        else:
            serials.append(i)
    
    # try:
    #     for i in films:
    #         print('Films',i)
    # except:
    #     pass
    # try:
    #     for i in serials:
    #         print('Serials',i)
    # except:
    #     pass

    return films, serials
    

def search(lista):                # Szukanie video po nazwie w bibliotece
    name = input("Enter name of looking for video: ")
    for i in lista:
        if i.title == name:
            index = lista.index(i)
            return lista[index]




library=[]                                # Tworzę bibliotekę filmów i seriali
list_maker(library)
print(library)

# for i in a:                           # Odtwarzam wszystkie filmy i serial z biblioteki
#     i.play()
#     print(i, '\n', i.number_of_plays, '\n')


sorted_library = list_filter(library)       # Rozdzielam bibliotekę filmów i seriali
films, serials = sorted_library
print('\n',films, serials)

looking_video = search(library)             # Szukanie video po nazwie w bibliotece
print(looking_video)
