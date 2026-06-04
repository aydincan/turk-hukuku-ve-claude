---
name: temel-kavramlar-ve-vergi-yargisi
description: "Vergi uyuşmazlığının türünü (tarh, tahakkuk, tahsil, ceza) ve doğru yargı yolunu belirlemek, idari aşama ile dava aşaması arasındaki ilişkiyi kurmak için ilk başvurulacak çerçeve beceridir."
---

# Temel Kavramlar ve Vergi Yargısı Sistematiği

## Görev
Müvekkilin elindeki belgeden hareketle uyuşmazlığı doğru sınıflandırmak, hangi normun (maddi vergi kanunu, VUK, AATUHK) ve hangi yargı yolunun devrede olduğunu saptamak, idari çözüm ile dava arasındaki tercihi çerçevelemek.

## Soğuk başlangıç (intake)
1. Elinizde tam olarak hangi belge var: vergi/ceza ihbarnamesi mi, ödeme emri mi, düzeltme/şikâyet reddi mi, ihtiyati haciz/tahakkuk yazısı mı?
2. Belge size ne zaman tebliğ edildi (eline geçti)? Tebligat usulü ne?
3. Uyuşmazlık verginin aslına mı, cezaya mı, faize/gecikme zammına mı yoksa tahsil aşamasına mı ilişkin?
4. Daha önce uzlaşma, düzeltme veya izaha davet süreci işletildi mi?

## Denetim şeması
1. **İşlem türünü belirle.** Tarh işlemi (ihbarname) → dava süresi İYUK m.7 ve VUK m.377 uyarınca 30 gün. Tahsil işlemi (ödeme emri) → AATUHK m.58 uyarınca 7 gün. Düzeltme-şikâyet reddi → VUK m.124 sonrası dava.
2. **Tarh türünü ayır.** Beyana dayalı (VUK m.378, kural olarak dava yok, istisna ihtirazi kayıt), ikmalen (m.29), re'sen (m.30) veya idarece tarh (m.29). Re'sen tarhda takdir sebebi ve yöntemi denetime tabidir.
3. **Görev-yetkiyi yerleştir.** Esasen vergi mahkemesi görevli; İYUK m.37 uyarınca uyuşmazlık konusu işlemi yapan dairenin bulunduğu yerdeki vergi mahkemesi yetkili.
4. **İdari aşama-dava ilişkisini kur.** Uzlaşma (VUK Ek m.1 vd.) ve düzeltme-şikâyet (VUK m.116 vd.) dava süresini etkiler; bunlardan birini seçmek diğerini kapatabilir. Ara sonuç: hangi yolun ceza indirimi, süre ve ispat avantajı sağladığını tablola.
5. **Otomatik durma etkisini not et.** Tarhiyata karşı dava İYUK m.27/4 gereği tahsili kendiliğinden durdurur; ödeme emrine ve ihtirazi kayıtlı davada bu etki yoktur, ayrı YD talebi gerekir.

## Çıktı modülleri
- Uyuşmazlık sınıflandırma tablosu (işlem türü / norm / süre / mahkeme).
- İdari yol vs. dava yolu karşılaştırması (avantaj-risk).
- Bir sonraki adım ve süre uyarısı listesi.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
