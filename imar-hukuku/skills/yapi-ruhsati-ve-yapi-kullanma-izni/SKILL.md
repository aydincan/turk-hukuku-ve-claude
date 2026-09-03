---
name: yapi-ruhsati-ve-yapi-kullanma-izni
description: "Yapı ruhsatı, ruhsat yenileme/temdit veya yapı kullanma izni (iskân) süreçleri ve bunların reddine karşı dava gündeme geldiğinde; ruhsata tabi işler, ruhsat eki projeler ve fenni mesuliyet ilişkisi sorulduğunda kullanılır."
---

# Yapı Ruhsatı ve Yapı Kullanma İzni

## Görev
Ruhsat ve iskân süreçlerini denetlemek; ruhsat verilmesi/reddi ya da iptali işlemlerine karşı hukuki yolu kurmak.

## Soğuk başlangıç (intake)
- Yapı yeni mi, ekleme/tadilat mı, basit onarım mı (ruhsata tabi mi)?
- Ruhsat başvurusu yapıldı mı, reddedildiyse gerekçesi ne?
- Plan, imar durumu ve aplikasyon krokisi uygun mu; eksik belge var mı?
- İskân (yapı kullanma izni) talep edildi mi, ruhsata aykırılık var mı?

## Denetim şeması
1. **Ruhsata tabi işler (3194 m.21)**: Kural olarak bütün yapılar ruhsata tabidir. Basit tamir-onarım ve derz, sıva, boya gibi işler ruhsat gerektirmez (m.21/son). Ruhsata tabi olup olmadığı önce ayrılır.
2. **Ruhsat şartları (m.20-22)**: Plan, yönetmelik ve imar durumuna uygunluk; tapu/yapı sahipliği, mimari-statik-mekanik-elektrik projeleri ve fenni mesuller. İdare başvuruyu **30 gün** içinde sonuçlandırır; eksik varsa bildirir, eksik giderilince 15 günde ruhsat verilir.
3. **Ret işleminin denetimi**: Ret gerekçesi plana/yönetmeliğe somut dayandırılmalı; dayanaksız ret, sebep ve gerekçe yönünden sakattır. İdarenin takdiri kamu yararı ve eşitlikle sınırlıdır.
4. **Süre ve temdit (m.29)**: Ruhsat tarihinden itibaren **2 yıl** içinde inşaata başlanmalı, **5 yıl** içinde bitirilmeli; süre dolarsa ruhsat hükümsüz, yeniden ruhsat (temdit) gerekir. Süre geçmesi kazanılmış hak tartışmasını doğurur.
5. **Yapı kullanma izni (m.30)**: Yapı ruhsat ve eklerine uygun tamamlanınca iskân verilir; aykırılık varsa önce m.32/m.42 süreci işler. İskânsız yapıda abonelik ve hukuki sonuçlar sınırlanır.
6. **İspat ve ara sonuç**: Onaylı projeler, yapı denetim raporları, imar durum belgesi delildir. Hukuka aykırı ret/iptal varsa İYUK m.7 süresinde iptal davası; gerekiyorsa YD. Ruhsatın üçüncü kişi (komşu) tarafından iptali davasında menfaat ve süre ayrıca kurulur.

## Çıktı modülleri
- Ruhsat/iskân başvuru belge kontrol listesi.
- Ret işleminin unsur denetimi notu.
- Süre/temdit ve kazanılmış hak değerlendirmesi.
- Ret veya iptale karşı dava dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `imar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
