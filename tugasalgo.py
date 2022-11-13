Tinggi = float(input('Masukkan Tinggi badan dalam Meter : '))
Berat = float(input('Masukkan Berat Badan dalam Kilogram : '))

def BMI(Tinggi,Berat):
    bmi=Berat/(Tinggi**2)
    if (bmi < 18 ):
        return 'anda Kekurangan gizi',bmi

    elif (bmi >=18 and bmi <= 25):
        return 'gizi anda sudah cukup',bmi
        
    elif (bmi <25):
        return 'anda kelebihan gizi',bmi

quote, bmi = BMI(Tinggi,Berat)
print('bmi mu adalah: {} dan  {}'.format(bmi, quote))
