---
name: alacaklilar-toplantisi-cogunluk
description: "Alacakların bildirimi, alacaklılar toplantısının yapılması ve konkordatonun kabulü için aranan çoğunlukların hesaplanması gerektiğinde kullanılır."
---

# Alacaklıların Daveti, Toplantı ve Çoğunluk

## Görev
Alacaklıları davet, alacakların bildirimi ve incelenmesi (İİK m.299-301), alacaklılar toplantısı ve konkordatonun kabulü için aranan nitelikli çoğunluğun (m.302) doğru hesaplanması.

## Soğuk başlangıç (intake)
- Alacaklılar davet ilanı yapıldı mı, bildirim süresi içinde miyiz?
- Kaydedilen toplam alacak ve alacaklı sayısı nedir?
- Rehinle temin edilmiş ve imtiyazlı alacaklar çoğunluk hesabında nasıl dışlanıyor?
- Çekişmeli (ihtilaflı) alacaklar var mı?

## Denetim şeması
1. **Alacaklıları davet (m.299).** Komiser, alacaklıları alacaklarını bildirmeye ilanla davet eder; bildirim süresi ve usulü denetlenir.
2. **Alacakların incelenmesi (m.300-301).** Borçlu, bildirilen alacaklar hakkında beyana davet edilir; komiser alacakları inceleyip rapor hazırlar. Çekişmeli alacakların çoğunluğa etkisi mahkemece m.308/c çerçevesinde değerlendirilir.
3. **Çoğunluğun hesabı (m.302/3).** Konkordato şu hâllerden biriyle kabul edilmiş sayılır: (a) kaydedilmiş alacaklıların ve alacakların yarısını aşan çoğunluk; veya (b) kaydedilmiş alacaklıların dörtte birini ve alacakların üçte ikisini aşan çoğunluk. İspat: tutanak ve alacak cetveliyle.
4. **Hesaba katılmayanlar (m.302/4-6).** Rehinle tam karşılanan alacaklar ve İİK m.206/1. sıradaki imtiyazlı alacaklar çoğunluk hesabında dikkate alınmaz; borçlunun yakınlarının alacakları için özel kural. Bunların doğru dışlanması denetlenir.
5. **Toplantı ve imza süresi.** Konkordato projesinin kabulü için tanınan süre (m.302/1) içinde imza/kabul beyanları toplanır. Ara sonuç: çoğunluk sağlandı mı, tasdik talebine geçilebilir mi.

## Çıktı modülleri
- Çoğunluk hesap tablosu (kişi sayısı ve alacak miktarı bazında).
- Dışlanan alacaklar (rehinli/imtiyazlı/yakın) listesi.
- Çekişmeli alacak değerlendirme notu.
- Toplantı tutanağı kontrol listesi.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
