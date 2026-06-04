---
name: aktarim-ve-verbis-denetimi
description: "Yurt içi/yurt dışı veri aktarım mekanizmalarının (7499 sonrası m.9) ve VERBİS kayıt yükümlülüğü ile kayıt içeriğinin doğruluğu denetlenirken kullanılır."
---

# Aktarım ve VERBİS Kayıt Denetimi

## Görev
İki sık ihlal başlığını birlikte denetlemek: (1) yurt içi (m.8) ve 7499 ile yeniden kurgulanan yurt dışı (m.9) aktarımların doğru mekanizmaya dayanıp dayanmadığı; (2) VERBİS (m.16) kayıt yükümlülüğü ve kaydın envanterle tutarlılığı.

## Soğuk başlangıç (intake)
1. Veri kimlere aktarılıyor — yurt içi üçüncü kişi, yurt dışı alıcı, bulut/SaaS sağlayıcı?
2. Yurt dışı alıcının bulunduğu ülke Kurul'un yeterlilik kararı verdiği bir ülke mi?
3. Aktarım sürekli mi, arızi mi; mevcut bir aktarım sözleşmesi var mı?
4. Kuruluşun VERBİS kaydı var mı, güncel mi; istisna iddiası belgeli mi?

## Denetim şeması
1. **Yurt içi aktarım (m.8)**: Aktarım da işlemedir; m.5/m.6 şartına ve m.4 ilkelerine dayanmalı. Veri işleyene aktarımda m.12 sözleşmesi şart; eksikse bulgu.
2. **Yurt dışı hiyerarşisi (m.9, 7499 sonrası)**: Önce yeterlilik kararı (m.9/1); yoksa uygun güvenceler (m.9/3 — uluslararası anlaşma, Kurul onaylı bağlayıcı şirket kuralları, Kurul'un ilan ettiği standart sözleşme [imzadan itibaren 5 iş günü içinde Kurul'a bildirim], izinli taahhütname); bunlar yoksa yalnızca arızi haller (m.9/6). Sürekli aktarımda arızi haller mekanizması kullanılamaz — bu yaygın bir hatadır.
3. **VERBİS yükümlülük testi (m.16)**: İşlemeye başlamadan önce kayıt esastır. İstisna eşikleri (çalışan sayısı/yıllık mali bilanço, ana faaliyetin özel nitelikli veri işleme olmaması) Kurul kararıyla belirlenir [güncel eşikler doğrulanacak — kvkk.gov.tr]; yurt dışında yerleşik sorumlu için eşik aranmaz.
4. **Kayıt içeriği tutarlılığı**: VERBİS'teki amaç, veri kategorisi, alıcı grupları, aktarım ve saklama süreleri envanterle birebir karşılaştırılır; sapma bulgudur.
5. **Ara sonuç**: Yanlış aktarım mekanizması ve eksik/tutarsız VERBİS kaydı m.18 yaptırım sebebidir.

İspat yükü: Aktarım güvencelerinin ve VERBİS istisnasının varlığını (çalışan/bilanço belgeleriyle) veri sorumlusu ispatlar.

## Çıktı modülleri
- Aktarım envanteri (alıcı, ülke, mekanizma, dayanak, bildirim durumu).
- Yurt dışı aktarım karar akış şeması (yeterlilik → güvence → arızi hal).
- VERBİS–envanter tutarlılık raporu ve istisna değerlendirme notu.

## Plugin bağlamı

Bu beceri `kvkk-uyum-checker` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
