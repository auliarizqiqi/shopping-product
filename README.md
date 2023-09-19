Nama : Aulia Rizqi Hidayatunnisa

Kelas : PBP B

NPM : 2206817881

Tautan aplikasi Adaptable : https://my-app-shopping-product.adaptable.app

Tautan repository : https://github.com/auliarizqiqi/shopping-product.git


TUGAS 3 - PBP

1. Apa perbedaan antara form POST dan form GET dalam Django?
Jawab: form POST adalah metode untuk mengirim data dari browser ke server menggunakan metode HTTP POST. Form GET adalah metode untuk mengirim data dari browser ke server menggunakan metode HTTP GET. Terdapat perbedaan antara keduanya, yaitu:

- Data yang dikirimkan dengan metode GET akan terlihat di URL sehingga tidak cocok untuk data sensitif seperti kata sandi atau informasi pribadi. Sedangkan metode POST lebih aman untuk mengirim data sensitif karena data tersebut tidak terlihat di URL

- Metode GET biasanya digunakan ketika ingin mengambil data dari server tanpa mengubah data tersebut. Sedangkan metode POST digunakan ketika kita ingin mengirim data ke server untuk membuat, memperbaru, atau menghapus data. 

- Metode POST tidak dibatasi panjang string, sedangkan metode GET dibatasi panjang string

- Data yang dikirim dengan metode POST tidak tersimpan dalam riwayat penelusuran oleh browser, sedangkan metode GET dapat menyimpan data yang dikirim dalam riwayat penelusuran.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Jawab: 
- HTML atau HyperText Markup Language merupakan sebuah markup language yang berfokus pada penyajian data dalam bentuk halaman web dan tidak digunakan secara umum untuk pertukaran data.
- XML atau Extensible Markup Language merupakan suatu markup language yang menyimpan data dalam format teks dan tag sederhana. Digunakan untuk pertukaran data antara berbagai sistem yang memiliki struktur data yang berbeda.
- JSON atau JavaScript Object Notation merupakan suatu format yang dibuat di atas JavaScript untuk merepresentasikan data dalam bentuk key dan value. Cocok untuk pertukaran data antara server dan klien web.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Jawab: Karena JSON merupakan format pertukaran data yang sangat ringan serta lebih mudah dibaca dan ditulis oleh manusia, sehingga mudah untuk diterjemahkan dan dibuat (generate) oleh komputer.


4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab: 

- Membuat input form untuk menambahkan objek model pada app sebelumnya
Membuat berkas baru pada direktori main dengan nama forms.py dan menambahkan kode ke dalam berkas tersebut. Buka berkas views.py yang ada pada folder main dan menambahkan beberapa import. Lalu membuat fungsi baru pada berkas tersebut yang menerima parameter request dan menambahkan kode untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form. Kemudian mengubah fungsi show_main dengan menambahkan kode, import fungsi create-product di urls.py, dan menambahkan path url. Lalu membuat berkas HTML baru pada direktori main/templates isi dengan beberapa kode, buka main.html dan tambahkan kode untuk menampilkan data produk dalam bentuk tabel serta tombol yang akan redirect ke halaman form.

- Menambahkan 5 Fungsi Views
Membuat view baru dalam django untuk melihat objek yang sudah ditambahkan dalam berbagai format seperti HTML, XML, JSON, XML by ID, dan JSON by ID. Tambahkan fungsi dan path url untuk membuat view baru di urls.py

-  Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
Konfigurasikan URL routing di Django untuk setiap view yang telah dibuat dengan import modul-modul yang diperlukan dan desfinisikan pola URL di dalam berkas urls.py

- Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
Buka berkas README.md pada direktori lokal dan jawab pertanyaan-pertanyaan di berkas tersebut.

- Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.


Gambar Postman - HTML 
![Alt Text](/Gambar_Postman/Postman_HTML_AuliaRizqi.png)



Gambar Postman - XML
![Alt Text](/Gambar_Postman/Postman_XML_AuliaRizqi.png)



Gambar Postman - XML by ID 1
![Alt Text](/Gambar_Postman/Postman_XML_ID1_AuliaRizqi.png)



Gambar Postman - XML by ID 2
![Alt Text](/Gambar_Postman/Postman_JSON_ID2_AuliaRizqi.png)



Gambar Postman - XML by ID 3
![Alt Text](/Gambar_Postman/Postman_XML_ID3_AuliaRizqi.png)



Gambar Postman - XML by ID 4
![Alt Text](/Gambar_Postman/Postman_XML_ID4_AuliaRizqi.png)



Gambar Postman - JSON 
![Alt Text](/Gambar_Postman/Postman_JSON_AuliaRizqi.png)



Gambar Postman - JSON by ID 1
![Alt Text](/Gambar_Postman/Postman_JSON_ID1_AuliaRizqi.png)



Gambar Postman - JSON by ID 2
![Alt Text](/Gambar_Postman/Postman_JSON_ID2_AuliaRizqi.png)



Gambar Postman - JSON by ID 3
![Alt Text](/Gambar_Postman/Postman_JSON_ID3_AuliaRizqi.png)



Gambar Postman - JSON by ID 4
![Alt Text](/Gambar_Postman/Postman_JSON_ID4_AuliaRizqi.png)



- Melakukan add-commit-push ke GitHub.
Tambahkan semua perubahan ke repositori Github menggunakan perintah git add, git commit, dan git push. Pastikan projek di Github sudah terupdate.

TUGAS 2 

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:
- Membuat Proyek Django baru:

Setelah membuat repository baru di github dan menjalankan proses konfigurasi dan sebagainya, selanjutnya untuk membuat proyek django yang baru adalah dengan membuka terminal atau command prompt dan buat proyek Django baru dengan perintah: django-admin startproject namaprojek.

- Membuat Aplikasi dengan nama 'main':

Untuk membuat aplikasi main, buka terminal dan masuk ke direktori proyek Django yang baru dibuat.
Lalu jalankan terminal dengan perintah: python manage.py startapp main, lalu mendaftarkan aplikasi main ke dalam proyek pada berkas settings.py

- Melakukan Routing pada proyek:

Membuat berkas urls.py dalam proyek Django dan tambahkan routing untuk aplikasi 'main'dengan menambahkan beberapa kode pada berkas urls.py
Pastikan telah menghubungkan URL dengan tampilan main dengan mengimpor fungsi include dari django.urls

- Membuat Model dengan nama 'Item':

Membuka berkas models.py dalam aplikasi 'main' lalu buat model item dengan atribut yang sesuai dengan permintaan checklist, seperti name, amount, description. Isi berkas tersebut dengan kode untuk mengimpor models dari django.db. Seetelah itu, membuat dan mengaplikasikan migrasi model dengan menjalankan perintah python manage.py makemigrations dan python manage.py migrate.


- Membuat Fungsi pada 'views.py':

Buka berkas views.py dalam berkas aplikasi 'main' dan menambahkan baris-baris impor from django.shortcuts import render di bagian paling atas berkas untuk mengintegrasikan komponen MVT. Lalu tambahkan fungsi show_main di bawah impor untuk mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.

- Membuat sebuah Routing Aplikasi 'main':

Buat berkas urls.py dalam direktori 'main'dan isi dengan barisan kode yang sesuai. Tambahkan rute url untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
Lalu jalankan proyek Django dengan perintah python manage.py runserver. Buka website loca;host di browser untuk melihat halaman yang sudah dibuat.

- Deployment ke Adaptable:

Login pada akun Adaptable dan klik tombol New App untuk membuat aplikasi. Lalu hubungkan dengan repository pada github yang akan digunakan, pilih template deployment, dan pilih tipe baris data yang akan digunakan. Sesuaikan versi python, masukkan perintah pada bagian start command, dan masukkan nama aplikasi yang akan menjadi nama domain situs web aplikasi. Kemudian klik Deploy App untuk memulai proses deployment aplikasi.

- Membuat README.md:

Buat berkas README.md yang berisi tautan menuju aplikasi yang telah di-deploy ke Adaptable.
Jawab pertanyaan-pertanyaan yang tercantum dalam checklist dengan jelas.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawab: ![Gambar Bagan Aulia Rizqi](Bagan_AuliaRizqi.jpg)


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Jawab: Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Virtual environment ini juga berguna untuk memastikan kalau versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lain-nya. Tanpa virtual environment, mungkin ada kesulitan dalam mengelola dependensi proyek yang berbeda.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Jawab: MVT adalah singkatan dari Model-View-Template. MVT adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.


MVC adalah singkatan dari Model-View-Controller yaitu pola desain yang memisahkan aplikasi menjadi tiga komponen utama: Model (logika bisnis dan data), View (tampilan yang diperlihatkan kepada pengguna), dan Controller (menerima input dari pengguna dan mengirimkannya ke Model atau View).


MVVM adalah singkatan dari Model-View-ViewModel yaitu pola desain yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI). Model mengurus data, View adalah tampilan yang diperlihatkan kepada pengguna, dan ViewModel adalah perantara antara Model dan View yang mengatur tampilan dan pembaruan data.


Perbedaan utama antara MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah dalam cara mereka mengatur dan mengelola komponen-komponen inti dalam pengembangan perangkat lunak. MVC memisahkan aplikasi menjadi Model (logika bisnis), View (tampilan), dan Controller (pengendali) dengan pengendali yang menghubungkan Model dan View. MVT, yang umumnya digunakan dalam kerangka kerja web Django, memisahkan Model (data), View (logika tampilan), dan Template (tampilan) dengan Template sebagai pengganti Controller. Sedangkan MVVM, yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), memisahkan Model (data), View (tampilan), dan ViewModel (logika tampilan) dengan ViewModel berperan sebagai perantara antara Model dan View.

