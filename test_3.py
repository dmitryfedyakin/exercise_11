from solution_3 import Track, Album

print('Введите данные, чтобы добавить новый трек')
name = input('Введите название трека: ')
duration = int(input('Введите длительность трека в секундах: '))
singer = input('Введите имя исполнителя: ')
alb_name = input('Введите название альбома: ')
date = input('Введите год выпуска: ')

track_1 = Track('The less i know the better',
                '216','Tame Impala', date, alb_name)
track_2 = Track('Let it happen', '467', 'Tame Impala', date, alb_name)
track_3 = Track(name, duration, singer, date, alb_name)
alb = Album(alb_name, date, singer)
alb.add_track(track_1)
alb.add_track(track_2)
alb.add_track(track_3)
print(alb)
alb.del_track(track_2)

while True:
    print(alb)
    print('Выберите трэк:') 
    number = int(input())
    track = alb.tracks[number - 1]

    while True:
        print('\nВыберите действие:')
        print('1. Воспроизвести трек')
        print('2. Поставить на паузу')
        print('3. Остановить трек')
        print('4. Выйти')

        choice = input("Введите номер действия: ")
        if choice == '1':
            track.play()
        elif choice == '2':
            track.pause()
        elif choice == '3':
            track.stop()
        elif choice == '4':
            break
