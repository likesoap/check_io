def sun_angle(localtime: str):
    localtime1 = localtime.split(sep=':')
    print(localtime1)
    if 360 <= int(localtime1[0])*60+int(localtime1[1]) <= 1080:
        return(((int(localtime1[0])-6)*60+int(localtime1[1]))/4)
    else:
        return("I don't see the sun!")


sun_angle("12:15")
sun_angle("07:00")
