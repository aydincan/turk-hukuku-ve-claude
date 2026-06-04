---
name: kisilik-hakki-ihlali-tazminat
description: "Basın veya yayın yoluyla şeref, itibar veya özel hayatın ihlali nedeniyle tespit, durdurma (men) ve maddi-manevi tazminat taleplerini kurgulamak gerektiğinde kullanılır."
---

# Basın Yoluyla Kişilik Hakkı İhlali ve Tazminat

## Görev
Yayından kaynaklanan kişilik hakkı saldırısında TMK m.24-25 davalarını ve TBK m.49/m.58 tazminat taleplerini unsurlarıyla kurmak, husumet ve hesabı belirlemek.

## Soğuk başlangıç (intake)
1. İhlal eden ifade tam olarak nedir, kim hakkındadır?
2. Yayın organı, sorumlu müdür, yazar/muhabir kim?
3. Somut zarar (manevi elem, ticari itibar kaybı, maddi kayıp) nedir?
4. İhlal devam ediyor mu (online erişilebilirlik)?

## Denetim şeması
1. **Saldırı ve hukuka aykırılık**: TMK m.24/I uyarınca kişiliğe saldırı; m.24/II'deki hukuka uygunluk sebepleri (üstün yarar, rıza, kanuni yetki) yoksa hukuka aykırılık sabittir.
2. **Davalar (TMK m.25)**: Tespit davası (devam eden/etkisi süren saldırı), durdurma/men davası (sürmekte olan saldırı), önleme davası (yakın tehlike). Düzeltme veya kararın ilanı da istenebilir.
3. **Tazminat**: Manevi tazminat TBK m.58; maddi tazminat TBK m.49-52 (kusur, hukuka aykırı fiil, zarar, illiyet). Tüzel kişi için ticari itibar zararı maddi tazminata konu olabilir.
4. **Husumet**: 5187 sayılı Kanun m.11 sorumluluk silsilesini düzenler; eser sahibi, sorumlu müdür ve yayın sahibi birlikte değerlendirilir. Tazminatta yayın sahibi ve ilgili kişiler müteselsil sorumlu olabilir.
5. **İspat yükü**: Saldırı ve zararı davacı, hukuka uygunluk sebebini davalı ispatlar (TMK m.6).
6. **Ara sonuç**: İhlal + hukuka uygunluk sebebinin yokluğu + zarar/illiyet varsa talep kabule değer.

## Çıktı modülleri
- Talep matrisi (tespit/men/önleme/tazminat)
- Husumet tablosu (yazar, sorumlu müdür, yayın sahibi)
- Manevi tazminat takdir gerekçesi taslağı (sınıf/derece, müdahale ağırlığı)

## Plugin bağlamı

Bu beceri `basin-medya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
