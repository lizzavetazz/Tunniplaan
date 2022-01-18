from tkinter import*

tp=Tk()
Label(text=" ").grid(row=0, column=0)
Label(text="Esmaspäev", borderwidth=2).grid(row=1, rowspan=2, column=0, columnspan=2)
Label(text="Teisipäev", borderwidth=2).grid(row=2, rowspan=2, column=0, columnspan=2)
Label(text="Kolmapäev", borderwidth=2).grid(row=3, rowspan=2, column=0, columnspan=2)
Label(text="Neljapäev", borderwidth=2).grid(row=4, rowspan=2, column=0, columnspan=2)
Label(text="Reede", borderwidth=2).grid(row=5, rowspan=2, column=0, columnspan=2)
#esmaspäev
tugiest2=Button(text="Tugiõpe\nEesti keel").grid(row=1, rowspan=2, column=3)
log=Button(text="Logistikateenuse\nja varude juhtimine").grid(row=1, rowspan=2, column=4, columnspan=2)
mat=Button(text="Matemaatika").grid(row=1, rowspan=2, column=6, columnspan=2)
Label(text="   ").grid(row=1, rowspan=2, column=8)
kjak=Button(text="Keel ja\n kirjandus").grid(row=1, rowspan=2, column=9, columnspan=2)
tugimat=Button(text="Tugiõpe\nmatemaatika").grid(row=1, rowspan=2, column=11)
#teisipäev
tugihim=Button(text="Tugiõpe\nKeemia").grid(row=3, rowspan=2, column=2)
progm=Button(text="Programmerimise alused").grid(row=3, rowspan=2, column=4, columnspan=3)
Label(text="   ").grid(row=3, rowspan=2, column=5)
füs=Button(text="Füüsika").grid(row=3, rowspan=2, column=6, columnspan=2)
#kolmapäev
tugiest1=Button(text="Tugiõpe\nEsti keel").grid(row=5, rowspan=2, column=1)
kunst=Button(text="Kunstiained").grid(row=5, rowspan=2, column=2, columnspan=2)
Label(text="   ").grid(row=5, rowspan=2, column=4)
kk=Button(text="Kehaline kasvatus").grid(row=5, rowspan=2, column=5, columnspan=2)
#neljapäev
log_=Button(text="Logistikateenused\nja varude juhtimine").grid(row=7, column=1, columnspan=2)
Label(text="   ").grid(row=4, column=2, columnspan=2)
progm_=Button(text="Programmerimise alused").grid(row=7, rowspan=2, column=3, columnspan=2)
eng1=Button(text="Inglise keel").grid(row=7, column=5, columnspan=2)
merk_=Button(text="Arenduskeskkonna\nloomine").grid(row=8, column=5, columnspan=2)
merk=Button(text="Arenduskeskkonna\nloomine").grid(row=7, rowspan=2, column=5, columnspan=2)
ek2=Button(text="Eesti keel").grid(row=8, column=5, columnspan=2)
alina=Button(text="Rühmajuhataja\ntund").grid(row=7, rowspan=2, column=9)
#reede
ek1=Button(text="Eesti keel").grid(row=9, column=1, columnspan=2)
merk1=Button(text="Arenduskeskkonna\nloomine").grid(row=10, column=1, columnspan=2)
progmr=Button(text="Programmerimise alused").grid(row=9, rowspan=2, column=3, columnspan=5)
merk2=Button(text="Arenduskeskkonna\nloomine").grid(row=9, column=8, columnspan=2)
eng2=Button(text="Inglise keel").grid(row=10, column=8, columnspan=2)

tp.mainloop()