---
name: kullanmama-defi-ve-ispati
description: "Karşı taraf markayı uzun süredir kullanmıyorsa veya size karşı kullanmama itirazı/def'i ileri sürüldüyse; beş yıllık ciddi kullanım koşulu ve ispat yükünü m.9-m.19/2 üzerinden yönetmek için kullanılır."
---

# Kullanmama Def'i ve Kullanımın İspatı

## Görev
Markanın "kullan ya da kaybet" ilkesini işletmek: tescilden sonra beş yıl içinde Türkiye'de ciddi biçimde kullanılmayan markanın itiraz/dava dayanağı olmasını engellemek (m.19/2 def'i; iptal için m.26/1-a, m.9). İspat yükü kural olarak marka sahibindedir.

## Soğuk başlangıç (intake)
- Dayanak marka kaç yıldır tescilli (beş yıl doldu mu)?
- Hangi mal/hizmette kullanım iddia ediliyor?
- Kullanım Türkiye'de, ciddi ve tescil edildiği biçimde mi?
- Kullanmama için haklı sebep var mı (idari engel, ithalat yasağı)?

## Denetim şeması
1. **Beş yıllık süre.** Tescil tarihinden (veya son ciddi kullanımdan) itibaren kesintisiz beş yıl kullanmama aranır (m.9/1).
2. **Def'i hakkı (m.19/2).** Yayına itirazda, itiraz dayanağı marka beş yıldır tescilliyse başvuru sahibi kullanım ispatı isteyebilir; ispatlanamazsa itiraz o markaya dayanılarak reddedilir.
3. **Ciddi kullanım ölçütü.** Pazarda gerçek ticari amaçla, markanın esas işlevine uygun, somut ve süreklilik gösteren kullanım; sırf hakkı korumak için sembolik kullanım yeterli değildir.
4. **Kapsam.** Kullanım, tescilli mal/hizmetin hangileri için ispatlandıysa koruma o kapsamla sınırlanır; kısmî kullanmama kısmî iptal/etkisizlik doğurur.
5. **Ayırt ediciliği değiştirmeyen kullanım.** Markanın ayırt edici karakterini değiştirmeyen farklı unsurlarla kullanım da kullanım sayılır (m.9/2).
6. **Haklı sebep.** Marka sahibinin iradesi dışındaki engeller (ruhsat bekleme, ithalat yasağı) kullanmamayı mazur gösterebilir.

## Çıktı modülleri
- Beş yıllık süre ve kullanım dönemi cetveli.
- Ciddi kullanım delil listesi (fatura, katalog, reklam, ambalaj — tarihli).
- Def'i/iptal talebi taslağı ve ispat yükü notu.

## Plugin bağlamı

Bu beceri `marka-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
