from tkinter import*

tp=Tk()
Label(text=" ").grid(row=0, column=0)
Label(text="Esmaspäev", borderwidth=2).grid(row=1, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
Label(text="Teisipäev", borderwidth=2).grid(row=3, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
Label(text="Kolmapäev", borderwidth=2).grid(row=5, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
Label(text="Neljapäev", borderwidth=2).grid(row=7, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
Label(text="Reede", borderwidth=2).grid(row=9, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
#esmaspäev
tugiest2=Button(text="Tugiõpe\nEesti keel", bg="#8A726B").grid(row=1, column=3, sticky=N+S+W+E)
Label(text="").grid(row=2, column=3, sticky=N+S+W+E)
log=Button(text="Logistikateenused ja\n varude juhtimine", bg="lightgreen").grid(row=1, rowspan=2, column=4, columnspan=2, sticky=N+S+W+E)
mat=Button(text="Matemaatika", bg="pink").grid(row=1, rowspan=2, column=6, columnspan=2, sticky=N+S+W+E)
Label(text="   ").grid(row=1, rowspan=2, column=8, sticky=N+S+W+E)
kjak=Button(text="Keel ja\n kirjandus", bg="#8FEA67").grid(row=1, rowspan=2, column=9, columnspan=2, sticky=N+S+W+E)
tugimat=Button(text="Tugiõpe\nmatemaatika", bg="pink").grid(row=1, rowspan=2, column=11, sticky=N+S+W+E)
#teisipäev
tugihim=Button(text="Tugiõpe\nKeemia", bg="#B104C3").grid(row=3, rowspan=2, column=3, sticky=N+S+W+E)
progm=Button(text="Programmerimise alused", bg="lightblue").grid(row=3, rowspan=2, column=4, columnspan=3, sticky=N+S+W+E)
Label(text="   ").grid(row=3, rowspan=2, column=7, sticky=N+S+W+E)
füs=Button(text="Füüsika", bg="pink").grid(row=3, rowspan=2, column=8, columnspan=2, sticky=N+S+W+E)
#kolmapäev
tugiest1=Button(text="Tugiõpe\nEesti keel", bg="#DC29EE").grid(row=5, column=3, sticky=N+S+W+E)
Label(text="").grid(row=6, column=3, sticky=N+S+W)
kunst=Button(text="Kunstiained", bg="#AE4A8A").grid(row=5, rowspan=2, column=4, columnspan=2, sticky=N+S+W+E)
Label(text="   ").grid(row=5, rowspan=2, column=6, sticky=N+S+W+E)
kk=Button(text="Kehaline kasvatus", bg="#A94E88").grid(row=5, rowspan=2, column=7, columnspan=2, sticky=N+S+W+E)
#neljapäev
log_=Button(text="Logistikateenused\nja varude juhtimine", bg="lightgreen").grid(row=7, rowspan=2, column=3, columnspan=2, sticky=N+S+W+E)
#Label(text="   ").grid(row=4, column=3, sticky=N+S+W+E)
progm_=Button(text="Programmerimise alused", bg="lightblue").grid(row=7, rowspan=2, column=5, columnspan=2, sticky=N+S+W+E)
eng1=Button(text="Inglise keel", bg="lightyellow").grid(row=7, column=7, columnspan=2, sticky=N+S+W+E)
merk_=Button(text="Arenduskeskkonna\nloomine", bg="#CF4141").grid(row=8, column=7, columnspan=2, sticky=N+S+W+E)
merk=Button(text="Arenduskeskkonna\nloomine", bg="#CF4141").grid(row=7, column=11, columnspan=2, sticky=N+S+W+E)
ek2=Button(text="Eesti keel", bg="#8A726B").grid(row=8, column=11, columnspan=2, sticky=N+S+W+E)
alina=Button(text="Rühmajuhataja\ntund", bg="#DC29EE").grid(row=7, rowspan=2, column=14, sticky=N+S+W+E)
#reede
ek1=Button(text="Eesti keel", bg="#DC29EE").grid(row=9, column=3, columnspan=2, sticky=N+S+W+E)
merk1=Button(text="Arenduskeskkonna\nloomine", bg="#CF4141").grid(row=10, column=3, columnspan=2, sticky=N+S+W+E)
progmr=Button(text="Programmerimise alused", bg="lightblue").grid(row=9, rowspan=2, column=5, columnspan=5, sticky=N+S+W+E)
merk2=Button(text="Arenduskeskkonna\nloomine", bg="#CF4141").grid(row=9, column=10, columnspan=2, sticky=N+S+W+E)
eng2=Button(text="Inglise keel", bg="#8FEA67").grid(row=10, column=10, columnspan=2, sticky=N+S+W+E)

tp.mainloop()

#Выходи из гитхаба плез