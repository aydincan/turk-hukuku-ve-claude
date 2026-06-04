> ⚠️ Bu belge tamamen KURGUSAL ve anonimdir; gerçek bir kişi, olay veya dava ile ilgisi yoktur. Eğitim/deneme amaçlıdır.

# Örnek Dava Dosyası: İşçi Alacağı ve Haksız Fesih

Bu klasör, İş Hukuku alanında bir "işçi alacağı ve haksız (geçersiz/usulsüz) fesih" senaryosunu konu alan tamamen kurgusal bir örnek dava dosyasıdır. Amaç, hukuk eklenti ve becerilerini gerçekçi bir veri seti üzerinde denemektir.

## 1. Kısa Olay Özeti

**Taraflar (tamamen kurgusal):**
- **Davacı / İşçi:** A. Yılmaz — montaj ustası
- **Davalı / İşveren:** Demir Yapı İnşaat San. ve Tic. Ltd. Şti. ("Demir Yapı Ltd. Şti.")
- Maaşların ödendiği banka: (M) Bankası A.Ş. (kurgusal)

**Uyuşmazlık:**
A. Yılmaz, Demir Yapı Ltd. Şti. nezdinde 3 Mart 2018 – 12 Şubat 2024 tarihleri arasında, yaklaşık 5 yıl 11 ay süreyle, belirsiz süreli iş sözleşmesiyle montaj ustası olarak çalışmıştır. İşveren, 12 Şubat 2024 tarihinde iş sözleşmesini "performans düşüklüğü ve iş yavaşlaması" gerekçesiyle yazılı olarak feshetmiştir. İşçi, feshin geçerli/haklı bir nedene dayanmadığını; fesihten önce savunmasının alınmadığını; ihbar öneline uyulmadığını; kıdem ve ihbar tazminatları ile birikmiş fazla mesai, yıllık izin ve UBGT (ulusal bayram ve genel tatil) alacaklarının ödenmediğini ileri sürmektedir.

**İşçinin talepleri:**
- Kıdem tazminatı
- İhbar tazminatı
- Fazla çalışma (fazla mesai) ücreti
- Yıllık ücretli izin alacağı
- Ulusal bayram ve genel tatil (UBGT) ücreti
- (Şartları varsa) işe iade / kötüniyet tazminatı yönünden değerlendirme

**İşverenin savunma ekseni (kurgusal):**
İşçinin son dönemde verimliliğinin düştüğü, devamsızlık ve iş yavaşlatması bulunduğu; fazla mesai yaptırılmadığı; izinlerin kullandırıldığı; alacakların bulunmadığı.

## 2. Kronoloji

| Sıra | Tarih | Olay |
|------|-------|------|
| 1 | 03.03.2018 | A. Yılmaz, Demir Yapı Ltd. Şti.'de montaj ustası olarak belirsiz süreli iş sözleşmesiyle işe başlar (giriş bildirgesi verilir). |
| 2 | 2018 – 2023 | İşçi haftalık 6 gün, ortalama günde 10–11 saat çalışır; ücretin bir kısmı bordro dışı (elden) ödenir (iddia). |
| 3 | 20.01.2024 | İşveren, sözlü olarak "işlerin azaldığını" belirterek işçiyi uyarır; yazılı savunma istenmez. |
| 4 | 12.02.2024 | İşveren, iş sözleşmesini "performans düşüklüğü ve iş yavaşlaması" gerekçesiyle yazılı bildirimle, ihbar öneli tanımadan derhal feshederek işçinin işine son verir (bkz. fesih-bildirimi.md). |
| 5 | 12.02.2024 | İşçiye SGK çıkışı yapılır; kıdem ve ihbar tazminatı ödenmez, ibraname imzalatılmak istenir, işçi imzalamaz. |
| 6 | 28.02.2024 | İşçi, vekili aracılığıyla işverene noter ihtarnamesi keşide ederek alacaklarının ödenmesini talep eder (bkz. ihtarname.md). |
| 7 | 11.03.2024 | İşveren ihtarnameye süresinde cevap verir, alacakları reddeder. |
| 8 | 25.03.2024 | İşçi, dava şartı arabuluculuğa başvurur; 18.04.2024'te "anlaşamama" ile sonuçlanır ve son tutanak düzenlenir. |

> Not: İşe iade talebi yönünden, 12.02.2024 tarihli fesih bildiriminin tebliğinden itibaren 1 ay içinde arabulucuya başvuru zorunluluğu (İş K. m.20, 7036 s. m.3) dikkate alınmalıdır; süre ve işyeri çalışan sayısı (30+) ile işçinin 6 aylık kıdemi gibi işe iade şartları kurguda mevcut kabul edilmiştir.

## 3. Hangi Becerilerle Denenebilir

### is-hukuku-bireysel
- **Kıdem ve ihbar tazminatı hesabı:** Giriş/çıkış tarihleri ve giydirilmiş brüt ücret üzerinden kıdem süresi ve tazminat tutarının hesaplanması (kıdem tavanı kontrolü dahil). Bkz. `bordro-ozeti.csv`.
- **Fesih analizi:** 12.02.2024 tarihli feshin geçerli/haklı neden ve usul (yazılı bildirim, savunma alma — İş K. m.19, m.18-21) yönünden değerlendirilmesi; haklı/geçerli/usulsüz fesih ayrımı.
- **Fazla mesai, UBGT, yıllık izin alacağı hesabı:** Çalışma düzeni (6 gün, ~10-11 saat) üzerinden haftalık 45 saati aşan kısmın %50 zamlı hesabı; hafta tatili ve UBGT günleri; devreden yıllık izin bakiyesi.
- **İşe iade değerlendirmesi:** İşyeri çalışan sayısı, 6 aylık kıdem, fesih sebebinin yazılı bildirimi ve süreler (İş K. m.18-21) yönünden iş güvencesi kapsamı.

### hukuk-muhakemesi
- **Görev ve yetki:** Uyuşmazlığın İş Mahkemeleri'nin görevine girmesi (7036 s. İş Mahkemeleri Kanunu m.5); yetkili mahkeme (davalı işverenin yerleşim yeri / işin yapıldığı yer).
- **Dava şartı arabuluculuk:** 7036 s. m.3 uyarınca işçilik alacakları ve işe iade için dava şartı arabuluculuk; son tutanağın dava dilekçesine eklenmesi (HMK m.114/2 ile dava şartı).
- **İspat yükü ve deliller:** Fazla mesai ve ücret iddialarında ispat yükü dağılımı, tanık, bordro ve banka kayıtlarının (M Bankası) değerlendirilmesi; bilirkişi incelemesi (HMK m.266).
- **Belirsiz alacak / kısmi dava tercihi:** Talep türünün (belirsiz alacak davası — HMK m.107) ve faiz başlangıçlarının değerlendirilmesi.

### dava-dilekce-atolyesi
- **Dava dilekçesi taslağı:** HMK m.119'a uygun unsurlarla (taraflar, konu, açıklamalar, deliller, hukuki sebepler, talep sonucu) işçilik alacakları dava dilekçesinin hazırlanması.
- **İhtarname düzenleme:** `ihtarname.md` taslağının usule uygun gözden geçirilmesi/iyileştirilmesi.
- **Cevap ve cevaba cevap dilekçesi:** İşveren savunmasına karşı dilekçe iskeleti.
- **Arabuluculuk başvuru/talep dilekçesi:** Son tutanak ve başvuru evrakı taslağı.

## 4. Örnek Sorular

1. "Bu dosyada 12.02.2024 tarihli fesih geçerli/haklı bir nedene mi dayanıyor? Fesih usulü (savunma alma, yazılı bildirim) İş Kanunu m.19 açısından usule uygun mu?"
2. "`bordro-ozeti.csv` ve giriş/çıkış tarihlerine göre A. Yılmaz'ın kıdem ve ihbar tazminatını giydirilmiş brüt ücret üzerinden hesaplar mısın? Kıdem tavanı uygulanacak mı?"
3. "Haftada 6 gün, günde ~10,5 saat çalışma düzenine göre haftalık fazla mesai ve UBGT alacağını nasıl hesaplarım? İspat yükü kimde?"
4. "İşçilik alacakları için dava açmadan önce hangi dava şartı (arabuluculuk) tamamlanmalı ve dava hangi mahkemede, kime karşı, hangi yetki kuralına göre açılır?"
5. "HMK m.119'a uygun bir işçilik alacakları dava dilekçesi taslağı hazırlar mısın? Belirsiz alacak davası mı, kısmi dava mı tercih edilmeli?"

## 5. Klasördeki Belgeler

| Dosya | İçerik |
|-------|--------|
| `README.md` | Bu dosya: olay özeti, kronoloji, beceri önerileri, örnek sorular. |
| `olay-ozeti.md` | Olayın ayrıntılı anlatımı, taraf bilgileri, hukuki konular ve açık sorular. |
| `fesih-bildirimi.md` | İşverenin 12.02.2024 tarihli yazılı fesih bildirimi (kurgusal). |
| `ihtarname.md` | İşçi vekilinin 28.02.2024 tarihli noter ihtarnamesi taslağı (kurgusal). |
| `bordro-ozeti.csv` | Aylık bordro/ücret özeti; brüt-net ücret, prim, fazla mesai ve ödeme bilgileri (kurgusal veri). |
