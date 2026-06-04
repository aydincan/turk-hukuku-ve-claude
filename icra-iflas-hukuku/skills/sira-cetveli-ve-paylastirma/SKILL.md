---
name: sira-cetveli-ve-paylastirma
description: "Hacze birden çok alacaklı katıldığında veya iflasta, satış bedelinin alacaklılar arasında hangi sırayla dağıtılacağını belirlemek ve sıra cetveline itiraz/şikâyet etmek gerektiğinde kullanılır."
---

# Sıra Cetveli ve Paraların Paylaştırılması

## Görev
Satıştan elde edilen bedeli alacaklılar arasında doğru sırayla paylaştırmak; rehinli, imtiyazlı ve adi alacakların sırasını belirlemek; sıra cetveline karşı sıra (icra mahkemesi) veya esas (genel mahkeme) itirazını yürütmek.

## Soğuk başlangıç (intake)
- Birden çok haciz/alacaklı var mı; iflas masası söz konusu mu?
- Rehinli alacak var mı (öncelik); kamu alacağı (6183) gündemde mi?
- Sıra cetveli tebliğ edildi mi (7 günlük itiraz süresi)?
- İtirazın konusu sıraya mı, alacağın esasına/miktarına mı yönelik?

## Denetim şeması
1. **Garameten paylaşım kuralı (m.140)**: Satış tutarı tüm alacakları karşılamıyorsa icra müdürü sıra cetveli düzenler; aynı derecedeki alacaklılar arasında garameten (oranlı) paylaşım yapılır.
2. **Öncelik sırası**: Rehinli alacaklar rehin konusu bedelden öncelikle ödenir (m.151 vd.); kamu alacaklarının önceliği 6183 s.K. çerçevesinde değerlendirilir; iflasta alacak sıraları İİK m.206-207'ye göre belirlenir (rehinli, imtiyazlı I-IV, adi).
3. **İtiraz türü (m.142)**: Sıraya itiraz icra mahkemesine; alacağın esasına/miktarına itiraz genel mahkemede ayrı davayla ileri sürülür. Süre tebliğden 7 gündür.
4. **İspat yükü**: İtiraz eden, cetveldeki tertibin/alacağın hatalı olduğunu ispatlar; muvazaa/sıra önceliği iddiaları belgeyle desteklenir.
5. **Hacze iştirak etkisi**: m.100/101 iştiraki cetveldeki payları değiştirir; ilk haciz tarihi belirleyicidir.
6. **Ara sonuç**: Düzeltilmiş dağıtım tablosu ve itiraz stratejisi oluşturulur.

## Çıktı modülleri
- Sıra/dağıtım tablosu (alacaklı × sıra × pay).
- Sıra cetveline itiraz dilekçesi (sıra/esas ayrımıyla).
- Öncelik analizi (rehinli/imtiyazlı/kamu/adi).

## Plugin bağlamı

Bu beceri `icra-iflas-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
