# Task

## Number 1
Buatlah program untuk menghitung `DIV` (hasil bagi) dan `MOD` (sisa hasil bagi). Inputan operator tidak boleh diisi dengan simbol `/` atau `%`. lihat ilustrasi dibawah ini:
```
Input
    Masukkan bil 1 = 5
    Masukkan bil 2 = 2
    Operator  = modulo

Output 
     Hasil = 1	
```
```
Input
    Masukkan bil 1 = 5
    Masukkan bil 2 = 2
    Operator  = division

Output 
     Hasil = 2
```
## Number 2
Buatlah program utama untuk mencari banyaknya kombinasi, dengan ketentuan sebagai berikut:
* Buatlah fungsi untuk menghitung faktorial
* Buatlah fungsi untuk menghitung kombinasi, di dalam fungsi kombinasi, panggil fungsi faktorial untuk menghitung nilai kombinasi, dengan parameter fungsi `n` (banyak elemen dalam himpunan) dan `r` (rasio).  

Rumus kombinasi sebagai berikut:  
![Combination](http://www.sciweavers.org/tex2img.php?eq=C_r%5En%3D%5Cfrac%7B%5C%20n%21%7D%7B%5C%28r%21%28n-r%29%21%29%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=mathpple&edit=0)  

Perhatikan contoh berikut:
```
Input
     Masukkan n : 3
     Masukkan r : 2
Output
     Hasil kombinasi  : 3    
```
## Number 3
Buatlah program untuk menghitung nilai suhu dari skala Celcius, ke skala Reamur, Fahrenheit, dan Kelvin. Dengan instruksi sebagai berikut:
* Buatlah 3 fungsi, masing-masing untuk perhitungan ke skala Reamur, Fahreinheit, dan Kelvin.
* Kemudian buatlah satu prosedur yang mengambil nilai suhu dari inputan program utama. Di dalam prosedur, gunakan fungsi-fungsi yang sudah dibuat pada instruksi nomor 1 untuk mengubah nilai suhu ke skala Reamur, Fahrenheit, dan Kelvin. Prosedur diakhiri dengan menampilkan hasil konversi dari Celcius ke skala lainnya.  

Contoh run program seperti dibawah ini:
```
Input
     Masukkan nilai suhu : 25
Output
     Nilai suhu dalam skala Reamur : 20 R
     Nilai suhu dalam skala Fahrenheit : 77 F
     Nilai suhu dalam skala Kelvin : 298 K
```
## BONUS
Buatlah program untuk menghitung nilai suhu dari suatu skala ke tiga skala lainnya. Dengan instruksi sebagai berikut:
* Buatlah 4 fungsi, masing-masing untuk melakukan konversi suhu dari skala Celcius, Reamur, Fahreinheit, dan Kelvin.
* Kemudian buatlah satu prosedur yang mengambil nilai suhu dari inputan program utama. Di dalam prosedur, inputan dari user dipisah menjadi dua, yaitu nilai suhu dan jenis skala suhu.
* Pada program utama, buatlah format inputan berupa NILAI_SUHU (spasi) JENIS_SKALA.
* Program utama tidak boleh memiliki variabel input lebih dari satu.
* Program utama MAKSIMAL 2 BARIS.

# Rumus Konversi Suhu
Berikut rumus konversi nilai suhu ke masing-masing skala:
* Dari Celcius  
![CReamur](http://www.sciweavers.org/tex2img.php?eq=Reamur%3D%284%2F5%29%2ACelcius%0A&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)  
![CFahrenheit](http://www.sciweavers.org/tex2img.php?eq=Fahrenheit%20%3D%20%289%2F5%29%2ACelcius%20%2B%2032%20%0A&bc=White&fc=Black&im=jpg&fs=12&ff=mathpple&edit=0)  
![CKelvin](http://www.sciweavers.org/tex2img.php?eq=Kelvin%3DCelcius%2B273%20%0A&bc=White&fc=Black&im=jpg&fs=12&ff=mathpple&edit=0)  
* Dari Reamur  
![RCelcius](http://www.sciweavers.org/tex2img.php?eq=Celcius%20%3D%20%285%2F4%29%2AReamur&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)  
![RFahrenheit](http://www.sciweavers.org/tex2img.php?eq=Fahrenheit%20%3D%20%289%2F4%29%2AReamur%20%2B%2032%0A&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)  
![RKelvin](http://www.sciweavers.org/tex2img.php?eq=Kelvin%20%3D%20Celcius%20%2B%20273%20%3D%20%285%2F4%29%2AReamur%20%2B%20273&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)
* Dari Fahrenheit  
![FCelcius](http://www.sciweavers.org/tex2img.php?eq=Celcius%20%3D%20%285%2F9%29%2A%28Fahrenheit-32%29&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)  
![FReamur](http://www.sciweavers.org/tex2img.php?eq=Reamur%20%3D%20%284%2F9%29%2A%28Fahrenheit-32%29%0A&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)  
![FKelvin](http://www.sciweavers.org/tex2img.php?eq=Kelvin%20%3D%20%285%2F9%29%2A%28Fahrenheit-32%29%20%2B%20273%0A&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)
* Dari Kelvin  
![KCelcius](http://www.sciweavers.org/tex2img.php?eq=Celcius%20%3D%20Kelvin-273&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)  
![KReamur](http://www.sciweavers.org/tex2img.php?eq=Reamur%20%3D%20%284%2F5%29%2A%28Kelvin-273%29%0A&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)  
![KFahrenheit](http://www.sciweavers.org/tex2img.php?eq=Fahrenheit%20%3D%20%289%2F5%29%2A%28Kelvin-273%29%20%2B%2032%0A&bc=White&fc=Black&im=jpg&fs=12&ff=mathpazo&edit=0)
