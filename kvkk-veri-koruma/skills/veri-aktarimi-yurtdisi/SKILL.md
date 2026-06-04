---
name: veri-aktarimi-yurtdisi
description: "Kişisel verinin üçüncü kişilere ya da yurt dışına aktarılacağı durumlarda, 7499 sonrası m.9 rejimine göre yeterlilik kararı, uygun güvence veya arızi haller değerlendirilirken kullanılır."
---

# Veri Aktarımı ve Yurt Dışına Aktarım

## Görev
Yurt içi (m.8) ve özellikle 7499 sayılı Kanunla yeniden kurgulanan yurt dışı aktarım (m.9) rejimini somut aktarıma uygulamak; aktarımın hangi mekanizmaya dayanacağını belirleyip gerekli belgeleri tasarlamak.

## Soğuk başlangıç (intake)
1. Veri kime aktarılıyor — yurt içi üçüncü kişi mi, yurt dışındaki alıcı mı, bulut/SaaS sağlayıcı mı?
2. Alıcı ülke Kurul'un yeterlilik kararı verdiği bir ülke mi?
3. Aktarım sürekli mi, tek seferlik/arızi mi?
4. Grup içi aktarım mı (bağlayıcı şirket kuralları gündeme gelebilir)?

## Denetim şeması
1. **Yurt içi aktarım — m.8**: Aktarım da bir işlemedir; m.5/m.6'daki şartlardan birine dayanmalı, m.4 ilkelerine uymalıdır. Veri işleyene aktarımda m.12 sözleşmesi şarttır.
2. **Yurt dışı — yeterlilik kararı (m.9/1)**: Kurul'un yeterli koruma bulunduğunu ilan ettiği ülke/sektör/uluslararası kuruluşa aktarım, ek güvence olmaksızın yapılabilir.
3. **Uygun güvenceler (m.9/3)**: Yeterlilik kararı yoksa ve taraflar yazılı olarak uygun güvenceyi sağlıyorsa aktarım mümkündür: (a) yurt dışı kamu kurumları/uluslararası kuruluşlar arası anlaşma, (b) bağlayıcı şirket kuralları (Kurul onaylı), (c) Kurul'un ilan ettiği standart sözleşme (imzadan itibaren 5 iş günü içinde Kurul'a bildirim), (ç) taahhütname (Kurul izniyle).
4. **Arızi haller (m.9/6)**: Yukarıdakiler yoksa, yalnızca arızi olmak kaydıyla açık rıza, sözleşmenin ifası, üstün kamu yararı, hakkın tesisi/korunması, fiili imkânsızlık veya alenileştirilmiş veri gibi sınırlı hâller.
5. **Ara sonuç**: Sürekli/sistematik aktarımda arızi haller mekanizması kullanılamaz; standart sözleşme veya yeterlilik kararı esastır. Eski "açık rıza + taahhütname" pratiğine körü körüne dayanma.

İspat yükü: Aktarım mekanizmasının ve güvencelerin varlığını veri sorumlusu ispatlar; standart sözleşme bildirimi süresinde yapılmazsa yaptırım riski doğar.

## Çıktı modülleri
- Aktarım kararı akış şeması (yeterlilik → uygun güvence → arızi hal).
- Standart sözleşme/taahhütname seçimi notu ve bildirim takvimi.
- Aktarım envanteri tablosu (alıcı, ülke, mekanizma, dayanak).

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
