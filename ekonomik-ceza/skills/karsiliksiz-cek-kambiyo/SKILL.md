---
name: karsiliksiz-cek-kambiyo
description: "Karşılıksızdır işlemi yapılan çekte adli para cezası ve çek düzenleme/hesap açma yasağı (5941 s. Çek Kanunu m.5), şikâyet süresi ve etkin pişmanlıkla yaptırımın kaldırılması söz konusu olduğunda kullanılır."
---

# Karşılıksız Çek ve Kambiyo Suçları

## Görev
5941 sayılı Çek Kanunu m.5 çerçevesinde karşılıksız çek yaptırımını (adli para cezası ve çek düzenleme yasağı) denetlemek; şikâyet, süre ve etkin ödemeyle düşme imkânını değerlendirmek.

## Soğuk başlangıç (intake)
- Çekin üzerinde "karşılıksızdır" işlemi yapıldı mı, tarihi ne?
- Çek hesabı sahibi kim, çeki düzenleyen/temsilci kim?
- Hamil kim, şikâyet süresi (suçun/işlemin öğrenilmesinden itibaren) işliyor mu?
- Çek bedeli + faiz ödenip yaptırımın kaldırılması (m.5/10) gündemde mi?

## Denetim şeması
1. **Yaptırımın niteliği**: 5941 s. Kanun m.5 — üzerinde karşılıksızdır işlemi yapılmış çekin hamili şikâyette bulunursa, çek bedeli kadar adli para cezası ve çek düzenleme/çek hesabı açma yasağı uygulanır. Bu, şikâyete bağlı bir yaptırımdır.
2. **Fail-sorumlu tespiti**: Çek hesabı tüzel kişiye aitse, çeki düzenleyen yetkili gerçek kişi sorumlu olur (temsil ilişkisi ve imza yetkisi kontrol edilir).
3. **Şikâyet ve süre**: Yaptırım şikâyete bağlıdır; şikâyet süresi ve usulü kontrol edilir. Yetkili mahkeme (icra ceza/asliye ceza) ve görev belirlenir.
4. **Etkin ödeme — yaptırımın kaldırılması (m.5/10)**: Çek bedelinin işleyen faiziyle birlikte ödenmesi halinde, soruşturma/kovuşturma/infaz aşamasına göre yaptırım kaldırılır veya çek düzenleme yasağı kalkar; aşama ve ödeme zamanı belirleyicidir.
5. **Hukuk-ceza paralelliği**: Çek aynı zamanda kambiyo senedidir; İİK kapsamında kambiyo takibi (icra) paralel yürür. Ceza yaptırımı ile alacağın icra takibini ayrı yönet.
6. **Ara sonuç**: Karşılıksızdır işleminin geçerliliği, sorumlu sıfatı, şikâyet süresi ve ödeme ile düşme imkânı netleşir.

## Çıktı modülleri
- Karşılıksızdır işlemi/şikâyet süresi kontrolü
- Sorumlu (düzenleyen/temsilci) tespiti
- Etkin ödeme ile yaptırımı kaldırma senaryosu
- İcra (kambiyo takibi) ile koordinasyon notu
- Şikâyet veya savunma dilekçesi taslağı

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
