isim="Gökdeniz"
soyisim='KAPLAN'
SinifNumarasi='0000'
Sınıf='ATP10A'




ad=input('Lütfen İsim Giriniz ')

if isim == ad: 
    print(' Giriş Yapıldı Yönlendiriliyorsunuz ')

else:
    print(' Sistemde Böyle Bir Öğrenci Kayıtlı Değil')
   
    
 
 

soyad=input('Lütfen Soyisim Giriniz ')

if soyisim==soyad:

        print(' Yönlendiriliyorsunuz... ')

else:
 print(' Sistemde  Böyle  Bir Öğrenci Bulunmamaktadır Lütfen Numaranızı Tekrardan Giriniz ')

sınıf=input('Lütfen Sınıfınızı Girin ')

if sınıf==Sınıf:
    print(' Sistemde Böyle Bir Kayıtlı Öğrenci Bulundu Son İşlem Sınıf Numarasıdır ')

else:
    print(' Sistemde Bu Sınıfa Kayıtlı Böyle Bir Öğrenci Bulunmamaktadır ')


numara=input(' Lütfen Okul Numaranızı Giriniz ')
if(SinifNumarasi==numara):
         print('Giriş Başarılı  Hoşgeldin ' + Sınıf  + "Sınıfından" + numara  + " Lı " +  isim + soyisim   )






    


     
        