---
name: istirak-faillik-katki
description: "Birden fazla kişinin bir suça katıldığı durumlarda müşterek/dolaylı faillik, azmettirme ve yardım etme ayrımını ve bağlılık kuralını uygulamak gerektiğinde kullanılır."
---

# İştirak — Faillik ve Suça Katılma

## Görev
Bir suça birden fazla kişinin katıldığı hâllerde her katılanın konumunu (fail, müşterek fail, dolaylı fail, azmettiren, yardım eden) belirleyip cezai sorumluluğu dağıtmak.

## Soğuk başlangıç (intake)
- Suça kaç kişi, hangi rolde katıldı?
- Fiil üzerinde kim ortak hâkimiyet kurdu; kim sadece destek verdi?
- Bir kişi başkasını suç işlemeye karar verdirdi mi (azmettirme)?
- Katkı, suçun işlenmesinden önce/sırasında mı, manevi mi maddi mi?

## Denetim şeması
1. **Faillik (m.37/1):** Suçun kanuni tanımındaki fiili gerçekleştiren faildir; birlikte işleyenler müşterek faildir (fiil üzerinde ortak hâkimiyet ölçütü).
2. **Dolaylı faillik (m.37/2):** Başkasını araç olarak kullanarak suç işleme; aracın kusur yeteneksizliğinden yararlanmada ceza artırılabilir.
3. **Azmettirme (m.38):** Başkasını belli bir suç işlemeye karar verdirme; fail kadar ceza. Üstsoy-altsoy ilişkisi ve azmettirenin belirlenememesi yönünden özel hükümler vardır.
4. **Yardım etme (m.39):** Suç işlemeye teşvik, kararı kuvvetlendirme, yol gösterme (manevi); araç sağlama, fiilin işlenmesini kolaylaştırma (maddi). Ceza, suçun cezasından indirilerek belirlenir. Ara sonuç: katkı icrai faillik düzeyine ulaştı mı, yardım düzeyinde mi kaldı?
5. **Bağlılık kuralı (m.40):** İştirak için kasten ve hukuka aykırı bir fiilin varlığı yeterlidir; herkes kendi kusuruna göre sorumludur. Özgü suçlarda (failin özel sıfat gerektiren suç) özel sıfatı olmayan kişi ancak yardım eden/azmettiren olabilir.
6. **Gönüllü vazgeçme ve iştirak:** Katılanlardan birinin vazgeçmesi (m.41) kendi sorumluluğunu etkiler.

## Çıktı modülleri
- Katılan bazlı rol-sorumluluk tablosu (madde atıflı).
- Müşterek faillik vs. yardım etme ayrım gerekçesi.
- Her katılan için ceza belirleme notu.
- Eksik delil ve `[doğrulanacak]` içtihat ihtiyacı.

## Plugin bağlamı

Bu beceri `ceza-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
