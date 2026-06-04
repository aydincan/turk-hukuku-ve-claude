---
name: hukuk-sosyolojisi-ve-etkililik
description: "Bir normun kâğıt üstünde geçerli olduğu hâlde toplumsal olarak işleyip işlemediği, yaptırımın caydırıcılığı veya bir düzenlemenin sosyal etkisi değerlendirilmek istendiğinde; ayrıca mevzuat tasarımı ve etki analizi gereken hâllerde kullanın."
---

# Hukuk Sosyolojisi ve Normun Etkililiği

## Görev
Normun toplumsal gerçeklikteki işleyişini (etkililik/yürürlük) çözümlemek; geçerli ama
etkisiz, ya da etkili ama meşruiyeti tartışmalı normları ayırmak; düzenleme tasarımı ve
beklenen sosyal etki için sosyolojik araç sağlamak. Bu beceri özellikle politika/uyum
tasarımında ve "kural neden tutmuyor" sorusunda işe yarar.

## Soğuk başlangıç (intake)
- Soru normun anlamı mı, yoksa fiilî etkisi/uygulanırlığı mı?
- Hedeflenen davranış değişikliği ne; norm bunu sağlıyor mu (uyum verisi var mı)?
- Yaptırım caydırıcı mı, yoksa "kâğıt üstünde" mi kalıyor?
- Müvekkil/kurum bir düzenleme mi tasarlıyor, yoksa mevcut bir düzenlemenin etkisini mi ölçüyor?

## Denetim şeması
1. **Geçerlilik-etkililik ayrımını kur.** Bir norm usulüne uygun konulduğu için geçerlidir;
   ancak toplumda fiilen izleniyor/uygulanıyorsa etkilidir. İkisinin ayrı olduğunu, ölü
   hükümlerin geçerli ama etkisiz olabileceğini vurgula.
2. **Üç katmanlı meşruiyeti oku.** Weber'in geleneksel/karizmatik/rasyonel-yasal otorite
   tiplerini kullanarak normun toplumsal kabulünü değerlendir; rasyonel-yasal meşruiyet
   modern hukuk devletinin (Anayasa m.2) zeminidir.
3. **Etki zincirini izle.** Norm → muhatabın bilgisi → uyma güdüsü (yaptırım korkusu, içsel
   kabul, sosyal baskı) → fiilî davranış. Zincirin kopduğu halkayı tespit et; çoğu etkisizlik
   yaptırımın değil, bilgi/kabul halkasının zayıflığındandır.
4. **Düzenleme tasarımına bağla.** Yeni norm öneriliyorsa, beklenen davranışsal tepkiyi,
   maliyet/teşvik dengesini ve kaçınma yollarını öngör; emredici norm (TBK m.27) ile teşvik
   edici/yedek normun farklı sosyal etkisini tartı. Ara sonuç: tasarım önerisi.
5. **Veri hijyeni.** Sosyolojik iddialar ampirik kaynağa (istatistik, saha çalışması)
   dayandırılır; veri yoksa "gözlem/varsayım" olarak işaretlenir, hukuki sonuç tek başına
   sosyolojik gözleme bina edilmez.

## Çıktı modülleri
- Geçerlilik/etkililik durum tablosu.
- Etki zinciri ve kopuş noktası tespiti.
- Meşruiyet değerlendirmesi (Weber tipolojisi).
- Düzenleme/uyum tasarım önerisi (varsayımlar işaretli).

## Plugin bağlamı

Bu beceri `hukuk-felsefesi-genel-teori` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
