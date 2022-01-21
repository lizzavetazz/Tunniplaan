from tkinter import*

tp=Tk()

#tunnide viited
Label(text=" ").grid(row=0,column=0)
Label(text="0\n7.40-8.25",borderwidth=1,relief="solid").grid(row=0, column=2, sticky=N+S+W+E)
Label(text="1\n8.30-9.15",borderwidth=1,relief="solid").grid(row=0, column=3, sticky=N+S+W+E)
Label(text="2\n9.20-10.05",borderwidth=1,relief="solid").grid(row=0, column=4, sticky=N+S+W+E)
Label(text="3\n10.10-10.55",borderwidth=1,relief="solid").grid(row=0, column=5, sticky=N+S+W+E)
Label(text="4\n11.00-11.45",borderwidth=1,relief="solid").grid(row=0, column=6, sticky=N+S+W+E)
Label(text="5\n11.50-12.35",borderwidth=1,relief="solid").grid(row=0, column=7, sticky=N+S+W+E)
Label(text="6\n12.40-13.25",borderwidth=1,relief="solid").grid(row=0, column=8, sticky=N+S+W+E)
Label(text="7\n13.30-14.15",borderwidth=1,relief="solid").grid(row=0, column=9, sticky=N+S+W+E)
Label(text="8\n14.20-15.05",borderwidth=1,relief="solid").grid(row=0, column=10, sticky=N+S+W+E)
Label(text="9\n15.10-15.55",borderwidth=1,relief="solid").grid(row=0, column=11, sticky=N+S+W+E)
Label(text="10\n16.00-16.45",borderwidth=1,relief="solid").grid(row=0, column=12, sticky=N+S+W+E)

#nädalapäevad
Label(text="").grid(row=0, column=0)
Label(text="Esmaspäev", borderwidth=1, relief="solid").grid(row=1, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
Label(text="Teisipäev", borderwidth=1, relief="solid").grid(row=3, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
Label(text="Kolmapäev", borderwidth=1, relief="solid").grid(row=5, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
Label(text="Neljapäev", borderwidth=1, relief="solid").grid(row=7, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
Label(text="Reede", borderwidth=1, relief="solid").grid(row=9, rowspan=2, column=0, columnspan=2, sticky=N+S+W+E)
#esmaspäev
tugiest2=Button(text="Tugiõpe\nEesti keel", bg="#8A726B", borderwidth=1, relief="solid").grid(row=1, column=3, sticky=N+S+W+E)
Label(text="").grid(row=2, column=3, sticky=N+S+W+E)
log=Button(text="Logistikateenused ja\n varude juhtimine", bg="lightgreen", borderwidth=1, relief="solid").grid(row=1, rowspan=2, column=4, columnspan=2, sticky=N+S+W+E)
mat=Button(text="Matemaatika", bg="pink", borderwidth=1, relief="solid").grid(row=1, rowspan=2, column=6, columnspan=2, sticky=N+S+W+E)
Label(text="   ", borderwidth=1, relief="solid").grid(row=1, rowspan=2, column=8, sticky=N+S+W+E)
kjak=Button(text="Keel ja\n kirjandus", bg="#8FEA67", borderwidth=1, relief="solid").grid(row=1, rowspan=2, column=9, columnspan=2, sticky=N+S+W+E)
tugimat=Button(text="Tugiõpe\nmatemaatika", bg="pink", borderwidth=1, relief="solid").grid(row=1, rowspan=2, column=11, sticky=N+S+W+E)
#teisipäev
tugihim=Button(text="Tugiõpe\nKeemia", bg="#B104C3", borderwidth=1, relief="solid").grid(row=3, rowspan=2, column=3, sticky=N+S+W+E)
progm=Button(text="Programmerimise alused", bg="lightblue", borderwidth=1, relief="solid").grid(row=3, rowspan=2, column=4, columnspan=3, sticky=N+S+W+E)
Label(text="   ", borderwidth=1, relief="solid").grid(row=3, rowspan=2, column=7, sticky=N+S+W+E)
füs=Button(text="Füüsika", bg="pink", borderwidth=1, relief="solid").grid(row=3, rowspan=2, column=8, columnspan=2, sticky=N+S+W+E)
#kolmapäev
tugiest1=Button(text="Tugiõpe\nEesti keel", bg="#DC29EE", borderwidth=1, relief="solid").grid(row=5, column=3, sticky=N+S+W+E)
Label(text="", borderwidth=1, relief="solid").grid(row=6, column=3, sticky=N+S+W)
kunst=Button(text="Kunstiained", bg="#AE4A8A", borderwidth=1, relief="solid").grid(row=5, rowspan=2, column=4, columnspan=2, sticky=N+S+W+E)
Label(text="   ", borderwidth=1, relief="solid").grid(row=5, rowspan=2, column=6, sticky=N+S+W+E)
kk=Button(text="Kehaline kasvatus", bg="#A94E88", borderwidth=1, relief="solid").grid(row=5, rowspan=2, column=7, columnspan=2, sticky=N+S+W+E)
#neljapäev
log_=Button(text="Logistikateenused\nja varude juhtimine", bg="lightgreen", borderwidth=1, relief="solid").grid(row=7, rowspan=2, column=3, columnspan=2, sticky=N+S+W+E)
Label(text="   ", borderwidth=1,relief="solid").grid(row=7, rowspan=2, column=5, sticky=N+S+W+E)
progm_=Button(text="Programmerimise alused", bg="lightblue", borderwidth=1,relief="solid").grid(row=7, rowspan=2, column=6, columnspan=2, sticky=N+S+W+E)
eng1=Button(text="Inglise keel", bg="lightyellow", borderwidth=1,relief="solid").grid(row=7, column=8, columnspan=2, sticky=N+S+W+E)
merk_=Button(text="Arenduskeskkonna\nloomine", bg="#CF4141", borderwidth=1,relief="solid").grid(row=8, column=8, columnspan=2, sticky=N+S+W+E)
merk=Button(text="Arenduskeskkonna\nloomine", bg="#CF4141", borderwidth=1,relief="solid").grid(row=7, column=10, columnspan=2, sticky=N+S+W+E)
ek2=Button(text="Eesti keel", bg="#8A726B", borderwidth=1,relief="solid").grid(row=8, column=10, columnspan=2, sticky=N+S+W+E)
alina=Button(text="Rühmajuhataja\ntund", bg="#DC29EE", borderwidth=1,relief="solid").grid(row=7, rowspan=2, column=12, sticky=N+S+W+E)
#reede
ek1=Button(text="Eesti keel", bg="#DC29EE", borderwidth=1,relief="solid").grid(row=9, column=3, columnspan=2, sticky=N+S+W+E)
merk1=Button(text="Arenduskeskkonna\nloomine", bg="#CF4141", borderwidth=1,relief="solid").grid(row=10, column=3, columnspan=2, sticky=N+S+W+E)
progmr=Button(text="Programmerimise alused", bg="lightblue", borderwidth=1,relief="solid").grid(row=9, rowspan=2, column=5, columnspan=5, sticky=N+S+W+E)
merk2=Button(text="Arenduskeskkonna\nloomine", bg="#CF4141", borderwidth=1,relief="solid").grid(row=9, column=10, columnspan=2, sticky=N+S+W+E)
eng2=Button(text="Inglise keel", bg="#8FEA67", borderwidth=1,relief="solid").grid(row=10, column=10, columnspan=2, sticky=N+S+W+E)

tp.mainloop()

#Выходи из гитхаба плез