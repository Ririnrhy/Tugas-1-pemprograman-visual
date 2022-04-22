
print('operasi matematika')
print(' 1. Jumlah \t[+]')
print(' 2. pengurangan\t [-]')
print(' 3. perkalian\t [*]')
print(' 4. pembagian\t [/]')
pil = int(input("\nmasukkan pilihan operasi : "))
x= int(input("bilangan 1 : "))
y= int(input("bilangan 2 : "))
if pil == 1:
    hasil = x+y
elif pil == 2:
    hasil = x-y
elif pil == 3:
    hasil = x*y
elif pil == 4:
    hasi = x/y
print("\nHasil :%d" %hasil)
    

    

