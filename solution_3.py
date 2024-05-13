import time

class Track:
    '''
    Represents operations with audiotrack.
    '''

    def __init__(self, name, duration, artist, year, album):
        '''
        Initializes information about track.

        :param name: Track name
        :param duration: Track duration
        :param artist: Track singer
        :param year: Year when track was released
        :param album: Album which consists track
        '''

        self.name = name
        self.duration = int(duration)
        self.artist = artist
        self.year = year
        self.album = album
        self.is_playing = False
        self.start_time = None
        self.pause_time = None
        self.stop_time = 0

    def play(self):
        '''
        Represents track play.
        '''

        if not self.is_playing:
            self.is_playing = True
            self.start_time = time.time() - self.stop_time
            print(f'{self.name}, {self.format_time(self.stop_time)}-' \
                  f'{self.format_time(self.duration)}' \
                  f', до конца трека ' \
                  f'{self.format_time(self.duration - self.stop_time)}')
        
    def pause(self):
        '''
        Represents track pause.
        '''

        if self.is_playing:
            self.is_playing = False
            self.pause_time = time.time()
            self.stop_time = self.pause_time - self.start_time
            if self.stop_time >= self.duration:
                self.stop_time = 0
                self.is_playing = False
                print(f'Трек {self.name} закончился')
            else:
                print(f'ПАУЗА: {self.name} на '\
                      f'{self.format_time(self.stop_time)}')

    def stop(self):
        '''
        Represents stop of playing the track.
        '''

        if self.is_playing:
            self.is_playing = False
            self.stop_time = 0
            print(f'ОСТАНОВКА: Трек {self.name}')

    @staticmethod
    def format_time(seconds):
        '''
        Returns time in necessary format.

        :param seconds: Amount of seconds
        '''
        minutes = int(seconds // 60)
        remnant_seconds = int(seconds % 60)

        return f'{str(minutes).zfill(2)}:{str(remnant_seconds).zfill(2)}'
    
    def __str__(self):
        '''
        Returns string representation of an object (for users).
        '''

        return f'Трек: {self.name}, {self.duration}, '\
            f'{self.artist}, {self.album}'
    

class Album:
    '''
    Represetns album with tracks.
    '''
    
    def __init__(self, name, year, artist):
        '''
        Initializes album atributes.

        :param name: Album name
        :param year: Year when album was released
        :param artist: Creator of the album
        '''
        
        self.name = name
        self.year = year
        self.artist = artist
        self.tracks = []

    def add_track(self, track):
        '''
        Adding new track to the album.

        :param track: Name of the track
        '''

        print(f'Добавление трека {track}')
        self.tracks.append(track)

    def del_track(self, track):
        '''
        Removing track from the album.

        :param track: Name of the track
        '''

        print(f'Удаление трека {track}')
        self.tracks.remove(track)

    def __str__(self):
        '''
        Returns string representation of an object (for users).
        '''

        result = '\n'
        count = 0
        for track in self.tracks:
            count += 1
            result += f'{count}) {track.name} \n'
        return f'\nСписок треков: {result}'
    