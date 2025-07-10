Harika! Aşağıda projen **"VertoX"** için tam özellikli, profesyonel bir GitHub `README.md` örneği bulacaksın. İçerik hem kullanıcıyı bilgilendiriyor, hem de kurulumu ve kullanım şeklini açıkça gösteriyor.

---

### ✅ `README.md`


# VertoX 🔒

**VertoX**, gelişmiş bir Python tabanlı Discord bot destekli araçtır. Kullanıcıya özel araçlar oluşturabilir, webhook mesajları gönderebilir, ve bazı otomatikleştirilmiş işlevler sunar. Ayrıca kurulum sonrası kendini temizleyen bir sistemle çalışır.

---

## 🚀 Özellikler

- ✅ Kullanıcıdan Discord token ve kanal bilgisi alarak keylogger oluşturur.
- 🧠 Akıllı `token` ve `channel ID` doğrulaması.
- 🔐 Discord’a özel mesaj atan bot ile kontrol.
- 🧩 PyInstaller ile .exe dosyası oluşturur.
- 🧼 Kurulum sonrası `setup.bat` ve `requirements.txt` kendini siler.
- 🎨 Terminal arayüzü `colorama` ile renkli ve şık.

---

## 📦 Gereksinimler

- Python 3.10+ (3.13 test edildi)
- pip (Python package manager)

Kurulması gereken Python paketleri:

```bash
pip install -r requirements.txt
````

---

## ⚙️ Kurulum

### 🔸 Otomatik Kurulum (önerilen)

```bash
Çift tıkla: setup.bat
```

Bu işlem:

* Gerekli paketleri yükler (`requirements.txt`)
* `mainfiles/setup.py` dosyasını çalıştırır
* Kurulum sonrası kendini ve `requirements.txt`'yi siler

---

### 🔹 Manuel Kurulum (alternatif)

1. Gerekli bağımlılıkları kur:

   ```bash
   pip install -r requirements.txt
   ```
2. Setup scriptini çalıştır:

   ```bash
   python mainfiles/setup.py
   ```

---

## 📁 .env Dosyası Örneği

Projenin kök klasörüne `.env` dosyası oluşturun:

```env
TOKEN=your_discord_bot_token
CHANNEL_ID=123456789012345678
ADMIN_ID=123456789012345678
```

---

## 🔧 Derleme (Keylogger)

Kurulumdan sonra, `main.py` çalıştırıldığında kullanıcıya:

* Discord Token
* Channel ID

girdisi sorulur ve ardından PyInstaller ile gizli `.exe` dosyası oluşturulur.

---

## ⚠️ Uyarı

> Bu proje yalnızca **eğitim**, **test** ve **geliştirme** amaçlıdır. İzinsiz şekilde herhangi bir sistemde kullanılması, bulunduğunuz ülkenin yasalarına göre suç teşkil edebilir.

---

## 👤 Geliştirici

* Made with ❤️ by [WaqSea](https://github.com/WaqSea)

---

## 📜 Lisans

MIT Lisansı altında yayınlanmıştır. Ayrıntılar için `LICENSE` dosyasını kontrol edin.

```
