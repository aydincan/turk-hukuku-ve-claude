---
name: temel-kavramlar-ve-sistem
description: "Fikri-sınai hak uyuşmazlığında hakkın türünü (marka, patent, tasarım, eser, bağlantılı hak), tescilli/tescilsiz ayrımını ve uygulanacak rejimi (SMK mi FSEK mi) belirleyip doğru kanun ve yargı yoluna yönlendirmek gerektiğinde kullanılır."
---

# Temel Kavramlar ve Sistematik

## Görev
Somut olayda hangi fikri/sınai hakkın söz konusu olduğunu, hakkın kaynağını ve uygulanacak hukuki rejimi (SMK 6769 / FSEK 5846) doğru saptamak; bunu görev-yetki, ispat yükü ve talep seçimine bağlamak.

## Soğuk başlangıç (intake)
- Uyuşmazlık konusu nedir: marka, patent/faydalı model, tasarım, coğrafi işaret yoksa edebî/sanatsal/yazılım eseri mi?
- Hak tescilli mi (TÜRKPATENT no, koruma süresi) yoksa tescilsiz koruma mı (eser, tanınmış marka, tescilsiz tasarım) iddia ediliyor?
- Müvekkil hak sahibi mi, lisans alan mı, devralan mı, yoksa tecavüzle suçlanan taraf mı?
- Talep tazminat mı, tecavüzün durdurulması mı, hükümsüzlük mü, yoksa tedbir mi?

## Denetim şeması
1. Hakkın niteliğini ayır: Sınai haklar SMK ile (marka m.4-7, patent m.82 vd., tasarım m.55 vd.); fikir ve sanat eserleri FSEK m.1/B-2 anlamında "sahibinin hususiyetini taşıyan" ürünler. Yazılım FSEK kapsamında eser (m.2/1), ancak teknik etki içeriyorsa patent boyutu da incelenir.
2. Koruma var mı: Tescilli haklarda sicil ve koruma süresi (marka m.23 yenileme, patent m.101 koruma, tasarım m.69) doğrulanır. Tescilsiz korumada hakkın varlığı davacıya ispat yükü olarak yüklenir (HMK m.190).
3. Hak sahipliği/sıfat: Devir-lisans şerhi sicilden kontrol edilir; lisans alanın dava ehliyeti SMK m.158 ile sınırlıdır (inhisari/basit lisans ayrımı).
4. Rejim çatışması: Aynı ürün hem eser hem tasarım/marka konusu olabilir; kümülatif koruma mümkündür, ancak her hak için ayrı şartlar ve ayrı talep değerlendirilir.
5. Ara sonuç: Uygulanacak kanun, görevli mahkeme türü (FSHM) ve hak sahipliği netleşmeden esas talep kurgulanmaz.

## Çıktı modülleri
- Hak haritası tablosu (hak türü / kaynak / tescil no / koruma süresi / sahip).
- Uygulanacak norm listesi (SMK ve/veya FSEK madde atıflarıyla).
- Eksik bilgi ve doğrulama listesi (sicil kaydı, devir zinciri).

## Plugin bağlamı

Bu beceri `fikri-mulkiyet-dava` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
çalışır; bir konu eklentinin dışına taştığında ilgili başka eklentiyi işaret eder,
aksi hâlde bu eklentinin uygun bir sonraki becerisini önerir.

## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar; mahkeme (Yargıtay / Danıştay /
  Anayasa Mahkemesi / Bölge Adliye Mahkemesi / Bölge İdare Mahkemesi), daire, **esas ve
  karar numarası**, tarih ve doğrulanabilir kaynak ile verilir
  (ör. `karararama.yargitay.gov.tr`, `karararama.danistay.gov.tr`,
  `kararlarbilgibankasi.anayasa.gov.tr`, `mevzuat.gov.tr`, UYAP Emsal).
  **Model hafızasından karar numarası ÜRETME.** Emin olunmayan her künye `[doğrulanacak]`
  olarak işaretlenir.
- **Mevzuat** madde / fıkra / bent ile gösterilir (ör. "TBK m.49/1", "HMK m.114/1-ç").
- **Doktrin** yalnızca kullanıcı kaynağı sağladığında veya lisanslı canlı erişim
  belgelendiğinde kullanılır; yazar, eser, baskı ve sayfa ile.
- Varsayımlar açıkça **"varsayım"** diye işaretlenir; sahte kesinlik üretilmez.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
