---
name: ek-tahakkuk-ceza
description: "Sonradan kontrol veya inceleme sonucu çıkarılan ek tahakkuk ve gümrük idari para cezası kararlarının hukuka uygunluğunu denetlemek gerektiğinde; ceza tipini, matrahı ve dayanağı madde madde sınamak için kullanılır."
---

# Ek Tahakkuk ve Ceza Kararlarının Denetimi

## Görev
Gümrük idaresinin sonradan kontrol/inceleme sonucu düzenlediği ek tahakkuk ve idari para cezası kararlarını hukuka uygunluk yönünden denetlemek; ceza tipini doğru sınıflandırmak ve indirim/iptal imkânlarını ortaya koymak.

## Soğuk başlangıç (intake)
- Karar hangi tarihte tebliğ edildi; ek tahakkukun ve cezanın tutarı ve dayanağı nedir?
- İhtilaf kıymet, menşe, sınıflandırma yoksa beyana aykırılık ekseninde mi?
- Ceza hangi maddeye dayandırılmış (m.234 vergi farkı, m.235 yasak/kısıtlama, m.241 usulsüzlük)?
- Beyanın düzeltilmesi (m.234/3) veya kendiliğinden bildirim imkânı kullanıldı mı?

## Denetim şeması
1. Karar tipini ayır: Vergi kaybına bağlı ceza için 4458 m.234 (kıymet/menşe/sınıflandırma farkına bağlı, vergi farkının belirli katı). İthalat/ihracatta yasak-kısıtlama ihlalleri için m.235. Şekle/usule aykırılık için m.241 (usulsüzlük cezası). Yanlış maddeye dayanan ceza sakattır.
2. Ek tahakkuk dayanağı: Tahakkuk ettirilmeyen vergiler m.193-197 çerçevesinde sonradan tahakkuk ettirilir. Hesap hatası, çifte tahakkuk veya matrah yanlışlığı denetlenir.
3. İndirim/bertaraf: m.234/3 uyarınca yükümlünün beyanın yanlışlığını idare tespit etmeden önce bildirmesi veya kararın tebliğinden itibaren süresinde ödeme cezada indirim sağlayabilir; m.234/6 (indirimli ödeme) ve uzlaşma (m.244) imkânları değerlendirilir.
4. Geri verme/kaldırma: Kanunen alınmaması gereken vergi alınmışsa m.211 uyarınca geri verme/kaldırma talebi; süre ve usul kontrol edilir.
5. İspat yükü: Cezayı gerektiren maddi olayı (vergi farkı, beyana aykırılık) idare ispatlar; yükümlü beyanının doğruluğunu ve iyi niyetini, hesap hatasını veya ceza şartlarının oluşmadığını ortaya koyar.
6. Ara sonuç: Cezanın tipi, matrahı ve dayanağı doğrulanır; iptal/indirim gerekçeleri ve hangi yolun (itiraz, uzlaşma, dava) öncelikli olduğu belirlenir. İlkesel içtihat için Danıştay 7. ve 9. Daire kararlarına bakılır [doğrulanacak].

## Çıktı modülleri
- Ceza tipi-dayanak-matrah denetim tablosu
- İndirim/uzlaşma/dava karşılaştırmalı strateji notu
- Geri verme-kaldırma başvuru taslağı (uygunsa)

## Plugin bağlamı

Bu beceri `gumruk-disticaret` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
