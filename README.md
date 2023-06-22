# Text-To-Speech Vits Model based
Mengubah text menjadi voice berdasarkan Vits Model
## Installation
Pastikan sudah menginstall VLC dan Python.
### VLC
<p>Install VLC melalui tautan <a href="https://www.videolan.org" target="_blank">ini</a></p>
<p>Setelah itu, konfigurasikan VLC kedalam PATH sistem.</p>
<p>Gunakan perintah di bawah untuk memeriksa apakah VLC sudah terkonfigurasi kedalam PATH sistem</p>

```sh
vlc --help
```

### Python
<p>Install Python melalui tautan <a href="https://www.python.org" target="_blank">ini</a></p>
<p>Setelah itu, konfigurasikan Python kedalam PATH sistem.</p>
<p>Gunakan perintah di bawah untuk memeriksa apakah Python sudah terkonfigurasi kedalam PATH sistem</p>
<p>Linux</p>

```sh
python --version
```

<p>Windows</p>

```sh
py --version
```

## Usage

```sh
python tts.py -t "Teks kamu di sini"
```

Untuk mengubah suara karakter, gunakan flag <code>-va</code>.

```sh
python tts.py -t "Hallo" -va "herta"
```
