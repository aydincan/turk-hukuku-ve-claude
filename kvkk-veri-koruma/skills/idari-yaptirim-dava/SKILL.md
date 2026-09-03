---
name: idari-yaptirim-dava
description: "Kurul'un idari para cezası veya işleme durdurma kararı verdiği durumlarda; yaptırımın hukuka uygunluğu, savunma stratejisi ve karara karşı dava yolu (7499 sonrası idare mahkemesi) değerlendirilirken kullanılır."
---

# İdari Yaptırım ve Kurul Kararına Karşı Dava

## Görev
KVKK m.18 idari para cezalarını ve Kurul'un idari işlemlerini değerlendirmek; savunma hazırlamak ve 7499 sayılı Kanunla değişen dava yolunu doğru kurgulamak.

## Soğuk başlangıç (intake)
1. Kurul kararı hangi yükümlülük ihlaline dayanıyor (aydınlatma, güvenlik, bildirim, sicil, Kurul kararına uymama)?
2. Karar müvekkile ne zaman tebliğ edildi (dava açma süresi tebliğden başlar)?
3. Verilen ceza miktarı ve gerekçesi nedir; orantılı mı?
4. Kurul soruşturmasında savunma usulüne uygun alındı mı?

## Denetim şeması
1. **Yaptırım kategorileri — m.18/1**: (a) aydınlatma yükümlülüğüne aykırılık, (b) veri güvenliği yükümlülüklerine aykırılık (m.12), (c) Kurul kararlarını yerine getirmeme, (ç) VERBİS kayıt/bildirim yükümlülüğüne aykırılık için ayrı ayrı idari para cezası öngörülmüştür. Cezalar her yıl yeniden değerleme oranıyla güncellenir [güncel tutarlar doğrulanacak — kvkk.gov.tr].
2. **Orantılılık ve gerekçe**: İdari yaptırım, Kabahatler Kanunu m.17 ve idare hukuku ilkeleri uyarınca orantılı ve gerekçeli olmalıdır; eylemin ağırlığı, kusur, tekerrür ve elde edilen yarar dikkate alınır.
3. **Dava yolu (7499 sonrası)**: 7499 sayılı Kanunla m.18'e eklenen hükümle, idari para cezalarına karşı dava yolu sulh ceza hâkimliğinden idare mahkemesine taşınmıştır. İdari yaptırım kararının iptali için 2577 sayılı İYUK uyarınca idare mahkemesinde iptal davası açılır; geçiş hükümleri ve tebliğ tarihine göre yetkili merci dikkatle belirlenmelidir.
4. **Süre**: İYUK m.7 uyarınca tebliğden itibaren 60 günlük dava açma süresi; gerekiyorsa yürütmenin durdurulması talep edilir (İYUK m.27).
5. **Ara sonuç**: Savunmada usule (savunma hakkı, gerekçe, orantılılık) ve esasa (işleme şartının varlığı, m.4 uyumu) birlikte girilir.

İspat yükü: İşlemenin hukuka uygunluğunu veri sorumlusu; yaptırımın maddi/hukuki dayanağını idare gerekçeli kararla ortaya koyar.

## Çıktı modülleri
- Kurul kararı analiz ve savunma stratejisi notu.
- İdare mahkemesinde iptal dilekçesi iskeleti (İYUK uyumlu).
- Yürütmeyi durdurma talebi gerekçe taslağı ve süre hesabı.

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
