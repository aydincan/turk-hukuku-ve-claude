---
name: hukuki-durum-tespiti-due-diligence
description: "Bir yatırım veya devralma öncesi girişimin hukuki durum tespiti (due diligence) yapılırken; kurumsal, sözleşmesel, fikri mülkiyet, iş hukuku, vergi ve KVKK risklerinin taranması, bulguların raporlanması ve red flag tespiti için kullanılır."
---

# Hukuki Durum Tespiti (Due Diligence)

## Görev
Yatırım/devralma öncesi girişimin hukuki risklerini sistematik taramak; kapanış öncesi giderilmesi gereken (condition precedent) ve fiyata/garantiye yansıması gereken bulguları ayırmak; DD raporu üretmek.

## Soğuk başlangıç (intake)
1. İşlem tipi: azınlık yatırımı mı, kontrol devri/M&A mi?
2. Şirketin yaşı, çalışan sayısı, fikri mülkiyet ağırlığı ne?
3. Hangi başlıklar kritik: IP, iş hukuku, vergi/teşvik, sözleşmeler, KVKK?
4. Daha önce yatırım turu/SAFE/borç var mı (cap table karmaşası)?
5. Süre ve veri odası (data room) erişimi hazır mı?

## Denetim şeması
1. Kurumsal: Esas sözleşme, pay defteri (TTK m.499), GK/YK kararları, ticaret sicili kayıtları; cap table'ın belgelerle örtüşmesi; geçmiş artırım/devirlerin geçerliliği (m.456, m.490).
2. Sözleşmesel: Müşteri/tedarikçi sözleşmelerinde kontrol değişikliği (change of control) ve devir yasağı; SAFE/dönüştürülebilir enstrümanların dönüşüm etkisi; SHA çakışması.
3. Fikri mülkiyet: Ürün/kod/markanın şirkete ait olduğunun teyidi — kurucu ve çalışan IP devir sözleşmeleri (6769 SMK; çalışan buluşu hükümleri; 5846 FSEK eser/mali hak devri); açık kaynak lisans uyumu.
4. İş hukuku: İş sözleşmeleri, fazla mesai/kıdem riskleri (4857), SGK uyumu (5510), ESOP/danışman ilişkilerinin niteliği (işçi mi serbest mi).
5. Vergi/teşvik: VUK uyumu, TGB/Ar-Ge teşvik şartlarının fiilen sağlanması (4691/5746), olası geçmiş dönem riskleri.
6. KVKK: Veri envanteri, aydınlatma/açık rıza, VERBİS, veri ihlali geçmişi (6698 m.10-12); DD sırasında veri aktarımının kendisi m.8-9 ile altlanır.
7. Red flag ve çıkış: Bulguları "kapanış ön şartı / fiyat düzeltmesi / beyan-tekeffül-tazminat" olarak sınıfla; düzeltilemez riskte işlemden çekilme önerisi.

## Çıktı modülleri
- Veri odası talep listesi (başlık başlık).
- DD bulgu/risk raporu (önem derecesi ve madde atıflı).
- Red flag listesi ve kapanış ön şartı/garanti önerileri.

## Plugin bağlamı

Bu beceri `girisim-startup-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
