---
name: belge-konismento-carter-inceleme
description: "Eldeki deniz ticareti belgelerini (konişmento, çarter parti, sörvey/ekspertiz raporu, gemi jurnali, protesto) hızla okuyup riskli kayıtları, çelişkileri ve eksik delilleri çıkarmak gerektiğinde kullan."
---

# Belge İnceleme (Konişmento, Çarter ve Sörvey)

## Görev
Deniz ticareti dosyasındaki belgeleri sistemli biçimde okuyup riskli/asimetrik kayıtları, çelişkileri ve eksik delilleri tespit etmek; sözleşmesel pozisyonu ve ispat durumunu hızla çıkarmak.

## Soğuk başlangıç (intake)
- Hangi belgeler mevcut (konişmento, çarter parti, manifesto, ordino, sörvey, gemi jurnali, protesto/rezerv)?
- Belgeler tutarlı mı; konişmento ile çarter parti çatışıyor mu?
- Sözleşmede tahkim, yetki, yabancı hukuk, sorumluluk ve sürastarya kayıtları nasıl?
- Eksik veya okunamayan kritik belge var mı?

## Denetim şeması
1. **Konişmento denetimi**: Zorunlu içeriği (TTK m.1228 vd.) ve türünü (nama/emre/hamiline) belirle; "temiz/clean" mi yoksa rezerv kayıtlı mı olduğunu, yükün durumuna ilişkin karine etkisini (taşıyan aleyhine/lehine) değerlendir.
2. **Çarter parti kayıtları**: Navlun, FIOST, starya/sürastarya, off-hire, tahkim ve uygulanacak hukuk klozlarını çıkar; konişmentoya atıf (incorporation) yoluyla hangi kayıtların yük ilgilisine karşı ileri sürülebileceğini değerlendir.
3. **Sörvey/ekspertiz ve protesto**: Sörvey raporunun bağımsızlığını, hasar tespiti ve nedensellik açıklamasını denetle; ziya/hasar ihbar ve protestolarının süresinde ve usulünce yapılıp yapılmadığını kontrol et.
4. **Çelişki ve boşluk taraması**: Belgeler arası tutarsızlıkları (ağırlık, koli sayısı, tarih, taraf adı) listele; ispat bakımından eksik delilleri ([gemi jurnali], [VDR kaydı], [yükleme fotoğrafı] gibi) işaretle.
5. **İspat ve ara sonuç**: Her belgenin kimin lehine karine/delil oluşturduğunu belirt; çıktıda sözleşmesel pozisyonu güçlü/zayıf yönleriyle özetle ve hangi belgenin temin edilmesi gerektiğini öner. Belirsiz alanlara `[doğrulanacak]` notu düş.

## Çıktı modülleri
- Belge envanteri ve eksik belge listesi
- Riskli/asimetrik kayıtlar tablosu (kloz bazında)
- Çelişki/ispat haritası ve temin edilecek deliller notu

## Plugin bağlamı

Bu beceri `deniz-ticareti-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
