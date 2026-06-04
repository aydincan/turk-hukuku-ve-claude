---
name: yakalama-gozalti-tutuklama
description: "Özgürlüğü kısıtlayan koruma tedbirlerinin yasaya uygunluğunu denetlemek, tutuklamaya itiraz, salıverilme ve adli kontrol talepleri hazırlamak gerektiğinde kullanılır."
---

# Yakalama, Gözaltı ve Tutuklama

## Görev
Özgürlüğü kısıtlayan tedbirlerin sebep, süre ve ölçülülük yönünden hukuka uygunluğunu denetlemek; tutuklamaya itiraz, salıverilme ve adli kontrol taleplerini gerekçelendirmek.

## Soğuk başlangıç (intake)
- Kişi ne zaman ve nasıl yakalandı; gözaltı kararı kim tarafından verildi?
- Tutuklama kararı var mı, hangi suçtan ve hangi tutuklama nedenine dayanıyor?
- Tutuklunun kişisel durumu (sabıka, yerleşik adres, sağlık) nedir?
- Önceki itiraz veya tahliye talebi yapıldı mı, ne zaman?
- Tutuklulukta geçen süre ne kadar?

## Denetim şeması
1. **Yakalama.** Suçüstü halinde herkes yakalayabilir; kolluk gecikmesinde sakınca olan ve savcıya ulaşılamayan hallerde yakalar (CMK m.90). Yakalanana hakları derhal bildirilir (m.90/4).
2. **Gözaltı.** Savcı emriyle, soruşturma için zorunluysa uygulanır; süre yakalama anından itibaren 24 saati, toplu suçlarda her defasında 1 günü geçmemek üzere uzatılabilir (m.91). Yol süresi hariç.
3. **Tutuklama şartları.** Kuvvetli suç şüphesini gösteren somut delil + bir tutuklama nedeni gerekir (m.100): kaçma şüphesi, delil karartma; m.100/3'te sayılan katalog suçlarda neden var sayılabilir. Karar hâkim/mahkemece verilir (m.101).
4. **Ölçülülük ve alternatif.** Tutuklama son çaredir; adli kontrol (m.109) yeterliyse tutuklama orantısızdır (m.100/1 son cümle, Anayasa m.13, m.19).
5. **Süre.** Soruşturmada ve kovuşturmada azami tutukluluk süreleri m.102'de düzenlenir; gerekçeli ve düzenli denetim (m.108, en geç 30 günlük aralıklarla resen inceleme) zorunludur.
6. **İtiraz.** Tutuklama ve uzatma kararlarına karşı m.267-271 uyarınca itiraz edilir; salıverilme her aşamada istenebilir (m.104).
7. **Ara sonuç.** Şart eksikse veya ölçüsüzse itiraz/tahliye talebi; aksi halde adli kontrole çevirme talebi öncelenir.

## Çıktı modülleri
- Tutuklama kararının şart/neden/ölçülülük denetim tablosu.
- Tutuklamaya itiraz veya salıverilme talebi dilekçesi taslağı.
- Adli kontrol önerisi ve dayanak (m.109 tedbir listesi).
- Tutukluluk süresi ve sonraki denetim tarihi takvimi.

## Plugin bağlamı

Bu beceri `ceza-muhakemesi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
