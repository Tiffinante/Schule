def eintritt(alter):
    preis = 12
    if alter < 3:
        preis = 0

    else:
        if alter < 12:
            preis = 6

        else:
            if alter > 67:
                preis = 8

    return preis
