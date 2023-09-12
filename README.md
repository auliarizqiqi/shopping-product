Nama : Aulia Rizqi Hidayatunnisa

Kelas : PBP B

NPM : 2206817881

Tautan aplikasi Adaptable : 


1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:
- Membuat Proyek Django Baru:

Setelah membuat repository baru di github dan menjalankan proses konfigurasi dan sebagainya, selanjutnya untuk membuat proyek django yang baru adalah dengan membuka terminal atau command prompt dan buat proyek Django baru dengan perintah: django-admin startproject namaprojek.

- Membuat Aplikasi 'main':

Untuk membuat aplikasi main, buka terminal dan masuk ke direktori proyek Django yang baru dibuat.
Lalu jalankan terminal dengan perintah: python manage.py startapp main, lalu mendaftarkan aplikasi main ke dalam proyek pada berkas settings.py

- Melakukan Routing:

Membuat berkas urls.py dalam proyek Django dan tambahkan routing untuk aplikasi 'main'dengan menambahkan beberapa kode pada berkas urls.py
Pastikan telah menghubungkan URL dengan tampilan main dengan mengimpor fungsi include dari django.urls

-Membuat Model 'Item':

Membuka berkas models.py dalam aplikasi 'main' lalu buat model item dengan atribut yang sesuai dengan permintaan checklist, seperti name, amount, description. Isi berkas tersebut dengan kode untuk mengimpor models dari django.db. Seetelah itu, membuat dan mengaplikasikan migrasi model dengan menjalankan perintah python manage.py makemigrations dan python manage.py migrate.


-Membuat Fungsi di 'views.py':

Buka berkas views.py dalam berkas aplikasi 'main' dan menambahkan baris-baris impor from django.shortcuts import render di bagian paling atas berkas untuk mengintegrasikan komponen MVT. Lalu tambahkan fungsi show_main di bawah impor untuk mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai.

-Melakukan Routing Aplikasi 'main':

Buat berkas urls.py dalam direktori 'main'dan isi dengan barisan kode yang sesuai. Tambahkan rute url untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
Lalu jalankan proyek Django dengan perintah python manage.py runserver. Buka website loca;host di browser untuk melihat halaman yang sudah dibuat.

-Deployment ke Adaptable:

Login pada akun Adaptable dan klik tombol New App untuk membuat aplikasi. Lalu hubungkan dengan repository pada github yang akan digunakan, pilih template deployment, dan pilih tipe baris data yang akan digunakan. Sesuaikan versi python, masukkan perintah pada bagian start command, dan masukkan nama aplikasi yang akan menjadi nama domain situs web aplikasi. Kemudian klik Deploy App untuk memulai proses deployment aplikasi.

-Membuat README.md:

Buat berkas README.md yang berisi tautan menuju aplikasi yang telah di-deploy ke Adaptable.
Jawab pertanyaan-pertanyaan yang tercantum dalam checklist dengan jelas.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawab: 

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Jawab: Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Virtual environment ini juga berguna untuk memastikan kalau versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lain-nya. Tanpa virtual environment, mungkin ada kesulitan dalam mengelola dependensi proyek yang berbeda.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Jawab: MVT adalah singkatan dari Model-View-Template. MVT adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.
MVC adalah singkatan dari Model-View-Controller yaitu pola desain yang memisahkan aplikasi menjadi tiga komponen utama: Model (logika bisnis dan data), View (tampilan yang diperlihatkan kepada pengguna), dan Controller (menerima input dari pengguna dan mengirimkannya ke Model atau View).
MVVM adalah singkatan dari Model-View-ViewModel yaitu pola desain yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI). Model mengurus data, View adalah tampilan yang diperlihatkan kepada pengguna, dan ViewModel adalah perantara antara Model dan View yang mengatur tampilan dan pembaruan data.
Perbedaan utama antara ketiganya terletak pada peran dan tanggung jawab dari komponen View. Dalam MVC, View memiliki sejumlah logika presentasi. Dalam MVT (terutama dalam konteks Django), View memiliki kemiripan dengan Template dalam MVC. Sementara dalam MVVM, View tidak memiliki tanggung jawab dalam hal logika bisnis, dan ViewModel berfungsi sebagai penghubung yang mengatur tampilan serta pembaruan data. MVVM biasanya diterapkan dalam pengembangan antarmuka pengguna yang lebih kompleks, seperti aplikasi berbasis SPA (Single Page Application).
