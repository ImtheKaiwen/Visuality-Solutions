#  Bir Anahtarın Sözlükte Zaten Mevcut Olup Olmadığını Kontrol Eden Python Programı
a = {"kerem" : 19, "mehmet" : 21}

x = "mehmet"
for key in a.keys():
    if key == x:
        print("var")
        break

