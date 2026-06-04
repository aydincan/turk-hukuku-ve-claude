> ⚠️ Bu belge tamamen KURGUSAL ve anonimdir; gerçek bir kişi, olay veya dava ile ilgisi yoktur. Eğitim/deneme amaçlıdır.

# Olay Özeti — Demir Yapı Tic. A.Ş. Veri İhlali

## 1. Taraflar

- **Veri Sorumlusu:** Demir Yapı Tic. A.Ş. ("Şirket"), İstanbul merkezli, çevrimiçi yapı malzemesi
  satışı yapan bir e-ticaret işletmesi. VERBİS'e kayıtlıdır (kayıt no: KURGUSAL-000000).
- **Veri İşleyen:** BulutNet Bilişim Ltd. Şti., Şirket'in müşteri veritabanını ve uygulama
  sunucularını barındıran bulut altyapı hizmet sağlayıcısı. Taraflar arasında 01.01.2025 tarihli
  "Veri İşleyen Sözleşmesi" (kurgusal) mevcuttur.
- **İlgili Kişiler:** Şirket'in çevrimiçi mağazasına kayıtlı yaklaşık 48.500 gerçek kişi müşteri.
- **Şikâyetçi (örnek ilgili kişi):** A. Yılmaz, Şirket müşterisi.
- **İdari Makam:** Kişisel Verileri Koruma Kurumu / Kişisel Verileri Koruma Kurulu ("Kurul").

## 2. Teknik Arka Plan (Kurgusal)

Şirket, müşteri yönetimi için üçüncü taraf bir web tabanlı yönetim paneli kullanmaktadır. Bu
panelde kullanılan bir bileşen için 02.03.2026 tarihinde bir güvenlik yaması (kritik seviye)
yayımlanmış; ancak yama, Şirket'in bilgi işlem ekibi tarafından zamanında uygulanmamıştır.

Açıktan yararlanan kimliği belirsiz üçüncü kişiler, tahminen 18.04.2026 tarihinde müşteri
veritabanına yetkisiz erişim sağlamış ve veriyi dışarı aktarmıştır. Veritabanı; ad-soyad,
e-posta adresi, telefon numarası, teslimat adresi ve sipariş geçmişi alanlarını içermektedir.
Parolalar özetlenmiş (hash) ve tuzlanmış (salt) biçimde tutulduğundan, açık metin parola sızıntısı
tespit edilmemiştir. Ödeme kartı bilgileri Şirket sistemlerinde saklanmadığından (ödeme, PCI-DSS
uyumlu üçüncü taraf üzerinden alınmaktadır) sızıntıya dâhil değildir.

İhlal, bağımsız bir güvenlik araştırmacısının 09.05.2026 tarihinde sızan verinin bir çevrimiçi
forumda satışa çıktığını e-posta ile bildirmesiyle fark edilmiştir.

## 3. İhlalin Tespiti ve Müdahale

- **09.05.2026:** Şirket bildirimi alır, ihlali doğrular, etkilenen yönetim panelini devre dışı
  bırakır, parola sıfırlama zorunluluğu getirir ve iç inceleme ile log analizi başlatır.
- **12.05.2026:** Şirket, ihlali Kurum'a "Kişisel Veri İhlali Bildirim Formu" ile bildirir.
- **15.05.2026:** Etkilenen ilgili kişilere e-posta ve web sitesi duyurusu yoluyla bilgilendirme
  yapılır; oltalama (phishing) uyarısı paylaşılır.
- **18.04.2026–09.05.2026** arasında geçen sürede ihlalin fark edilememiş olması, log izleme ve
  saldırı tespit sistemlerinin yeterliliği bakımından ayrıca tartışma konusudur.

## 4. Hukuki Çerçeve

### 4.1. Veri Güvenliği Yükümlülüğü — KVKK m.12
6698 sayılı Kişisel Verilerin Korunması Kanunu m.12/1 uyarınca veri sorumlusu;
(a) kişisel verilerin hukuka aykırı olarak işlenmesini önlemek,
(b) kişisel verilere hukuka aykırı erişimi önlemek,
(c) kişisel verilerin muhafazasını sağlamak
amacıyla uygun güvenlik düzeyini temin etmeye yönelik gerekli her türlü teknik ve idari tedbiri
almakla yükümlüdür.

### 4.2. İhlal Bildirimi — KVKK m.12/5
İşlenen kişisel verilerin kanuni olmayan yollarla başkaları tarafından elde edilmesi hâlinde, veri
sorumlusu bu durumu **en kısa sürede** ilgilisine ve Kurul'a bildirir. Kurul'un ilke kararı
uyarınca bu bildirimin, ihlalin öğrenildiği tarihten itibaren **72 saat içinde** yapılması esastır.
İlgili kişilere yapılacak bildirim ise makul olan en kısa sürede gerçekleştirilir.

> **Değerlendirme notu:** Somut olayda Şirket, ihlali 09.05.2026'da öğrenmiş ve 12.05.2026'da
> bildirmiştir. Bu süre, takvim olarak ~3 gün (72 saat sınırında/sınıra yakın) olup, sürenin
> başlangıç anının (öğrenme/teyit) ve saat bazlı hesabın incelenmesi gerekir.

### 4.3. Veri Sorumlusu – Veri İşleyen İlişkisi — KVKK m.12/2
Veri sorumlusu, veri işleyenin de bu tedbirleri almasını sağlamakla yükümlüdür ve veri işleyenle
**müştereken sorumludur**. Şirket'in BulutNet'e rücu hakkı, aralarındaki sözleşme ve TBK genel
hükümleri çerçevesinde değerlendirilir.

### 4.4. İlgili Kişinin Hakları — KVKK m.11, m.13, m.14
İlgili kişi, m.11'deki haklarını kullanmak için önce veri sorumlusuna (m.13), tatmin edici cevap
alamazsa veya cevap verilmezse Kurul'a (m.14) başvurabilir. A. Yılmaz bu yolu izlemiştir.

### 4.5. İdari Yaptırımlar — KVKK m.18
Veri güvenliğine ilişkin yükümlülükleri (m.12) yerine getirmeyenler hakkında idari para cezası
öngörülmüştür. Ceza miktarları her yıl yeniden değerleme oranında güncellendiğinden, somut tutar
**ihlal tarihinde yürürlükte olan güncel cetvele göre belirlenmelidir** [doğrulanacak].

### 4.6. Tazminat
İlgili kişinin uğradığı maddi/manevi zarar bakımından genel hükümler (6098 s. TBK m.49 vd.) ve
KVKK m.14/3 saklıdır.

## 5. Tartışmalı Noktalar

1. **Bildirimin zamanlaması:** 72 saatlik sürenin başlangıcı "öğrenme" mi yoksa "teyit/doğrulama"
   anı mıdır? Şirket'in bildirimi süresinde sayılır mı?
2. **Tedbirlerin yeterliliği:** Yamanın 2 aydan uzun süre uygulanmaması, m.12 tedbir yükümlülüğünün
   ihlali sayılır mı?
3. **Tespit gecikmesi:** İhlalin ~3 hafta fark edilememesi, log izleme/SIEM yetersizliği bakımından
   ayrı bir kusur oluşturur mu?
4. **Sorumluluk paylaşımı:** Kusur veri işleyene mi, veri sorumlusuna mı atfedilir? Rücu mümkün mü?
5. **İlgili kişi bilgilendirmesinin niteliği:** 15.05.2026 bildirimi, asgari unsurları (ihlalin
   niteliği, etkilenen veri kategorileri, olası sonuçlar, alınan/önerilen tedbirler, iletişim
   noktası) içeriyor mu?

## 6. Belge ve Delil Listesi (Kurgusal)

- Güvenlik araştırmacısı bildirim e-postası (09.05.2026).
- Şirket iç inceleme raporu ve log analizi çıktıları.
- Kurum'a sunulan Veri İhlali Bildirim Formu (12.05.2026).
- İlgili kişilere gönderilen bilgilendirme metni (15.05.2026).
- Şirket – BulutNet Veri İşleyen Sözleşmesi (01.01.2025).
- A. Yılmaz'ın veri sorumlusuna başvurusu (21.05.2026) ve Şirket cevabı.
- A. Yılmaz'ın Kurul'a şikâyet dilekçesi (18.06.2026).

---

*Bütün isim, tarih, tutar, numara ve teknik ayrıntılar kurgusaldır. Mevzuat madde atıfları genel
bilgilendirme amaçlıdır; somut uygulamada güncel KVKK metni ve Kurul kararlarıyla doğrulanmalıdır.*
