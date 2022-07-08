segs_str=input("Por favor, entre com o número de segundos que deseja converter: ")
segs_int=int(segs_str)
dias=segs_int//86400
resto_dias=segs_int%86400
horas=resto_dias//3600
resto_horas=resto_dias%3600
minutos=resto_horas//60
segundos=resto_horas%60
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
