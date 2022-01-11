def main():

    print ('Nama planet : ')

    ListPlanet = ['Mercury' , 'Venus', 'Mars', 'Pluto', 'Jupiter', 'Neptune', 'Saturn', 'Uranus']

    while ListPlanet:
        print(ListPlanet.pop(0))

    Planet = input('Cari tahu berat badan anda diplanet ').lower()

    Berat = int(input('Masukkan berat badan anda : '))

    MERCURY = int(float(Berat * 0.38))
    VENUS = int(float(Berat * 0.91))
    MARS = int(float(Berat * 0.38))
    PLUTO = int(float(Berat * 0.04))
    JUPITER = int(float(Berat * 2.34))
    NEPTUNE = int(float(Berat * 1.12))
    SATURN = int(float(Berat * 0.93))
    URANUS = int(float(Berat * 0.92))

    if (Planet == "mercury"):
        print('Berat badan anda di Mercury: ',MERCURY)
            
    elif (Planet == "venus"):
        print('Berat badan anda di Venus: ', VENUS)

    elif (Planet == "mars"):
        print('Berat badan anda di Mars:', MARS)

    elif (Planet == "pluto"):
        print('Berat badan anda di Pluto:', PLUTO)

    elif (Planet == "jupiter"):
        print('Berat badan anda di Jupiter', JUPITER)

    elif (Planet == "neptune"):
        print('Berat badan anda di Neptune', NEPTUNE)

    elif (Planet == "saturn"):
        print('Berat badan anda di Saturn', SATURN)

    elif (Planet == "uranus"):
        print('Berat badan anda di Uranus', URANUS)

    elif (Berat < 0):
        print('Berat badan tidak memenuhi')

    else:    
        print('Planet tidak termasuk dalam list')

    restart = input('Ingin cobain lagi?\n' ).lower()
    if restart == "ya":
        main()

    else:
        print('Terimakasih')
        exit()

main()

