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

##################################################################################################


def list_maker(a):                                           # Przypisywaanie danych do film i serial
                                                                 # oraz umieszcznie ich w jednej liscie
    def body_list_maker(lista):
        kind=input('enter kind ("film" or "serial"): ')                                       
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
 



def get_movies(lista):             # Funkcja zwracajáca listę filmów 
    films = []
    for i in lista:
        if type(i)==Film:
            films.append(i)
    return sorted(films, key=lambda element: element.title)

def get_series(lista):             # Funkcja zwracajáca listę seriali
    serials = []
    for i in lista:
        if type(i)==Serial:
            serials.append(i)
    return sorted(serials, key=lambda element: element.title)


    

def search(lista):                # Szukanie video po nazwie w bibliotece
    name = input("Enter name of looking for video: ")
    for i in lista:
        if i.title == name:
            index = lista.index(i)
            return lista[index]

import random

def generate_views(lista):                # funkcja wybiera losowy film i odtwarzam go losową ilość razy
    a = random.choice(lista)
    for i in range(random.randint(1,100)):
        a.play()
    print(a.number_of_plays)
    

def do_10_times(lista):             # 10 razy wykonuje funkcje generate_views
    for i in range(10):
        generate_views(lista)

def top_titles(lista):
    n=int(input("how many top viewed films do you want?: "))                    # funkcja zwraca liste n filmów 
    a=sorted(lista, key=lambda element: element.number_of_plays, reverse=True)  # najwięcej razy oglądanych

    content_type=input('Do you want to show films or serials? ("films"/"serials"): ')
    while content_type != 'films' and content_type != 'serials':
        content_type = input('You wrote wrong kind. Enter "films" or "serials": ')
        
    if content_type=='films':
        return sorted(get_movies(a[:n]), key=lambda element: element.number_of_plays, reverse=True)
    else:
        return sorted(get_series(a[:n]), key=lambda element: element.number_of_plays, reverse=True)


library=[]                                # Tworzę bibliotekę filmów i seriali
list_maker(library)

sorted_library = get_movies(library)       # Rozdzielam bibliotekę filmów i seriali
print('\n',sorted_library)

looking_video = search(library)             # Szukanie video po nazwie w bibliotece
print(looking_video)

do_10_times(library)             # wybieram losowy film i odtwarzam go losową ilość razy

top_n = top_titles(library)         # lista n filmów najwięcej razy oglądanych
print(top_n)