# Hayate

## I. Pendahuluan
Hayate adalah sebuah LINE *official account* yang bertujuan untuk hiburan semata berupa tanya-jawab dan hal-hal lain yang absurd. Hayate berbentuk bot yang berbasis bahasa Python (versi 3.7) dan di-*deploy* melalui Heroku.



## II. Versi dan *Changelog*
1.1.0
- Add renderZero to renderer module
- Remove trailing '.0' in sumnation result

1.0.0
- Initial Release

## III. Dokumentasi (Modul Renderer)
Modul renderer merupakan modul yang dapat menerjemahkan pesan yang dikirim pengguna pada bot menjadi perentilan objek.

### 1. createArray
  createArray merupakan fungsi untuk membuat *array/list* dengan jumlah komponen sebanyak n.
  
  ```
  createArray(5)
  OUT : [0, 1, 2, 3, 4]
  ```
  
  
### 2. renderText
  renderText merupakan fungsi yang mem-*breakdown* serangkaian *text* menjadi objek-objek yang dibutuhkan dan memberikan bendera *true* bahwa prosedur dapat dieksekusi, jika *text* memenuhi syarat. Objek akan diidentifikasi sebagai objek terpisah jika dipisahkan oleh spasi
  
  ```
  text = "!sum 30 40"
  renderText(text,"!sum",2)
  OUT : [True, ['30', '40']]
  
  text = "!list 30 40 70 good bad"
  renderText(text,"!list",5)
  OUT : [True, ['30', '40', '70', 'good', 'bad']]

  text = "!list 30 40 70 good"
  renderText(text,"!list",5)
  OUT : [False, 0]
  ```
  
### 3. renderList
  renderList merupakan fungsi yang meng-*import list* dari sebuah berkas `.txt` (berada pada folder list) yang kemudian mengambil nilai acak dari list tersebut.
  
  ```
  # Apakah.txt
  Ya
  Tidak
  <grup>Mungkin...
  <grup>Gatau sih
  ```
  
  ```
  renderList("Apakah","none")
  OUT : 'Ya'
  
  renderList("Apakah","none")
  OUT : 'Mungkin...\nGatau sih'
  ```
  
### 4. renderList Exception
  Sama seperti renderList, namun jika hasil yang diinginkan diluar dari *list*, maka pada *list* cukup ditambahkan kolom *exception* dan hasil akan mengacak *list* pada kolom *exception* sesuai kriteria *exception* yang diinginkan.
  
  ```
  # Apakah.txt
  Ya
  Tidak
  <grup>Mungkin...
  <grup>Gatau sih
  
  [EXCEPTION] text=Hayate bodoh?
  Tidak
  Mustahil
  
  [EXCEPTION] text=Hayate manusia?
  Bukan, Hayate hanya sebuah bot
  ```
  
  ```
  renderList("Apakah","none")
  OUT : 'Ya'
  
  renderList("Apakah","Hayate bodoh?")
  OUT : 'Mustahil'
  
  renderList("Apakah","Hayate manusia?")
  OUT : 'Bukan, Hayate hanya sebuah bot'
  ```
  
### 5. renderPhrase2 & renderPhrase3
  renderPhrase2 dan renderPhrase3 merupakan fungsi untuk mem-*breakdown* objek dari *text*. Fungsinya hampir sama dengan renderText.
  
  ```
  text = "Siapakah Fulan bin Fulan sebenarnya?"
  renderPhrase2(text,"Siapakah","sebenarnya?")
  OUT : [True, 'Fulan bin Fulan']
  
  text = "Bagaimanakah hubungan cinta Fulan bin Fulan dan Fulanah binti Fulan?"
  renderPhrase3(text,"Bagaimanakah hubungan cinta","dan","?")
  OUT : [True, 'Fulan bin Fulan', 'Fulanah binti Fulan']
  ```

### 6. renderZero
  renderZero berfungsi menghapus '.0' pada ujung bilangan tipe *float* dengan keluaran tipe *string*.
  
  ```
  a = float(20)
  b = float(30)
  a + b
  OUT : 50.0
  
  renderZero(a + b)
  OUT : '50'
  ```
  
## IV. Pekerjaan ke Depan
Hayate merupakan purwarupa sekaligus bot eksperimental yang diujicoba untuk membuat LINE bot lain yang lebih bermanfaat. Hayate merupakan ajang untuk belajar dan melakukan kesalahan, sebelum pembuat mengerjakan proyek lain yang serupa (LINE bot).
