> ⚠️ Bu belge tamamen KURGUSAL ve anonimdir; gerçek bir kişi, olay veya dava ile ilgisi yoktur. Eğitim/deneme amaçlıdır.

# Örnek Dosya: KVKK Veri İhlali ve Kurul Bildirimi

Bu klasör, KVKK alanındaki hukuk skill'lerini gerçekçi bir senaryoyla denemek için hazırlanmış,
**tamamen kurgusal** bir örnek dosyadır. Bir e-ticaret şirketinin müşteri veritabanına yetkisiz
erişim sonucu ortaya çıkan kişisel veri ihlali ve Kişisel Verileri Koruma Kurulu'na (Kurul)
bildirim süreci ele alınmaktadır.

---

## 1) Kısa Olay Özeti

**Taraflar (hepsi kurgusal):**
- **Veri sorumlusu:** Demir Yapı Tic. A.Ş. ("Şirket") — çevrimiçi yapı malzemesi satışı yapan
  bir e-ticaret işletmesi.
- **Veri işleyen:** BulutNet Bilişim Ltd. Şti. — Şirket'in müşteri veritabanını barındıran
  bulut hizmet sağlayıcısı.
- **İlgili kişiler:** Şirket'in çevrimiçi mağazasına kayıtlı yaklaşık 48.500 müşteri.
- **İdari makam:** Kişisel Verileri Koruma Kurumu / Kurul.
- **Şikâyetçi ilgili kişi (örnek):** A. Yılmaz — verilerinin sızdırıldığını öğrenip Şirket'e
  başvuran ve ardından Kurul'a şikâyette bulunan müşteri.

**Uyuşmazlık:**
Şirket'in kullandığı bir yönetim panelindeki güncellenmemiş bir bileşendeki açık üzerinden,
kimliği belirsiz üçüncü kişiler müşteri veritabanına yetkisiz erişim sağlamış; ad-soyad, e-posta,
telefon, teslimat adresi ve sipariş geçmişi verileri dışarı sızdırılmıştır. İhlal, bağımsız bir
güvenlik araştırmacısının bildirimiyle fark edilmiştir. Şirket'in ihlali Kurul'a "en kısa sürede
ve her hâlde 72 saat içinde" bildirme yükümlülüğünü zamanında yerine getirip getirmediği ve
gerekli teknik-idari tedbirleri alıp almadığı tartışmalıdır.

**Talepler:**
- İlgili kişi A. Yılmaz: Verilerinin işlenmesinin durdurulması/silinmesi, uğradığı zararın
  tazmini ve Şirket hakkında KVKK m.18 uyarınca idari yaptırım uygulanması.
- Kurum/Kurul: İhlalin bildirim zamanlamasının, alınan tedbirlerin ve veri işleyen ile sorumluluk
  paylaşımının incelenmesi; KVKK m.12 ve m.18 kapsamında değerlendirme.
- Şirket (savunma): İhlalin makul sürede tespit edilip bildirildiği, gerekli tedbirlerin alındığı,
  kusurun büyük ölçüde veri işleyene atfedilebileceği savunması.

---

## 2) Kronoloji

| # | Tarih | Olay |
|---|-------|------|
| 1 | 02.03.2026 | Yönetim panelindeki bir bileşen için yayımlanan güvenlik yamasının Şirket tarafından uygulanmaması (açığın oluştuğu tarih). |
| 2 | 18.04.2026 | Yetkisiz erişimin gerçekleştiği tahmin edilen tarih (sonradan log incelemesiyle belirlenmiştir). |
| 3 | 09.05.2026 | Bağımsız güvenlik araştırmacısı, sızan verinin bir forumda satışa çıktığını Şirket'e e-posta ile bildirir. |
| 4 | 09.05.2026 | Şirket olayı doğrular, etkilenen sistemi devre dışı bırakır ve iç inceleme başlatır. |
| 5 | 12.05.2026 | Şirket, ihlali Kurum'a "Veri İhlali Bildirim Formu" ile bildirir (olayı öğrenmesinden ~3 gün sonra). |
| 6 | 15.05.2026 | Şirket, etkilenen ilgili kişilere e-posta ve web sitesi duyurusu ile bilgilendirme yapar. |
| 7 | 21.05.2026 | İlgili kişi A. Yılmaz, KVKK m.13 uyarınca Şirket'e yazılı başvuruda bulunur. |
| 8 | 18.06.2026 | A. Yılmaz, Şirket'in cevabını yetersiz bularak KVKK m.14 uyarınca Kurul'a şikâyette bulunur. |

---

## 3) Hangi Becerilerle Denenebilir

### `kvkk-veri-koruma` eklentisi
- **Veri ihlali bildirim süresi analizi:** Olayın öğrenildiği tarih (09.05.2026) ile Kurum'a
  bildirim tarihi (12.05.2026) arasındaki sürenin "72 saat" kuralına uygunluğunu değerlendirme.
- **Veri ihlali bildirim formu taslağı:** `ihlal-kronolojisi.md` ve `etkilenen-veriler.csv`
  verilerinden hareketle Kurum'a sunulacak bildirim formu metni üretme.
- **İlgili kişi bilgilendirme metni:** Etkilenen kişilere gönderilecek bildirim (m.12 uyarınca)
  taslağının hazırlanması ve hangi unsurları içermesi gerektiğinin denetlenmesi.
- **Veri sorumlusu / veri işleyen sorumluluk paylaşımı:** Şirket ile BulutNet arasındaki
  sözleşmesel sorumluluk dağılımının KVKK m.12/2 çerçevesinde analizi.

### `kvkk-uyum-checker` eklentisi
- **Teknik ve idari tedbirler kontrol listesi:** Şirket'in aldığı/almadığı tedbirlerin KVKK m.12
  ve Kurul'un "Veri Güvenliğine İlişkin İdari ve Teknik Tedbirler" rehberi ışığında denetlenmesi.
- **Aydınlatma ve açık rıza uyumu:** Müşteri kaydında alınan aydınlatma metni ve rızaların
  m.10 ve m.5'e uygunluğunun kontrolü.
- **Saklama ve imha politikası uyumu:** Sipariş geçmişi verilerinin saklama süresinin
  Kişisel Veri Saklama ve İmha Politikası gereklilikleriyle kıyaslanması.
- **İdari para cezası risk değerlendirmesi:** KVKK m.18 kapsamında olası yaptırım aralığının
  ve hafifletici/ağırlaştırıcı unsurların değerlendirilmesi.

---

## 4) Örnek Sorular

1. "Şirket ihlali öğrendiği tarihten 3 gün sonra Kurum'a bildirmiş. Bu, KVKK m.12 ve Kurul'un
   72 saat kuralı bakımından zamanında sayılır mı? Sürenin başlangıç anı nasıl belirlenir?"
2. "Etkilenen kişilere gönderilecek bildirim metnini, KVKK m.12 ve Kurul rehberinin aradığı
   asgari unsurları kapsayacak şekilde hazırlar mısın?"
3. "`etkilenen-veriler.csv` dosyasındaki veri kategorilerine bakarak, bu ihlalin 'özel nitelikli
   kişisel veri' içerip içermediğini ve risk seviyesini değerlendirir misin?"
4. "Şirket ile veri işleyen BulutNet arasındaki sorumluluğu KVKK m.12/2 çerçevesinde nasıl
   paylaştırırsın? Şirket veri işleyene rücu edebilir mi?"
5. "Bu olayda Şirket için KVKK m.18 kapsamında olası idari para cezası aralığı nedir ve hangi
   hafifletici unsurlar ileri sürülebilir?"

---

## 5) Klasördeki Belgeler

| Dosya | İçerik |
|-------|--------|
| `README.md` | Bu dosya — olay özeti, kronoloji, beceri önerileri, örnek sorular. |
| `olay-ozeti.md` | Olayın ayrıntılı anlatımı; taraflar, teknik arka plan, hukuki çerçeve ve değerlendirme notları. |
| `ihlal-kronolojisi.md` | İhlalin tespit, müdahale ve bildirim aşamalarının saat/tarih ayrıntılı zaman çizelgesi. |
| `etkilenen-veriler.csv` | Etkilenen veri kategorileri, kayıt sayıları, hassasiyet ve risk seviyesi tablosu. |

---

*Tüm isim, tarih, tutar ve numaralar kurgusaldır. Mevzuat atıfları (KVKK m.5, m.10, m.12, m.13,
m.14, m.18; 6098 s. TBK m.49 vd.) genel niteliktedir; somut olaya uygulanması her zaman güncel
mevzuat ve Kurul kararlarıyla doğrulanmalıdır. Anılan içtihat/Kurul karar künyeleri kullanılmamış,
gerekli yerlerde "[doğrulanacak]" notu düşülmüştür.*
