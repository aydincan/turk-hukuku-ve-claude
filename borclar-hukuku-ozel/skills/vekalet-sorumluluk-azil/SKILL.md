---
name: vekalet-sorumluluk-azil
description: "Vekilin özen ve sadakat borcuna aykırılığı, talimat dışı işlem, hesap verme talebi veya azil/istifa sonuçları söz konusu olduğunda; vekâlet ilişkisinin denetimi için kullanılır."
---

# Vekâlet — Özen, Hesap Verme, Azil ve İstifa

## Görev
Vekilin TBK m.502-514 kapsamındaki yükümlülüklerini (özen, sadakat, talimat, hesap verme) ve vekâletin sona erme sonuçlarını denetlemek; vekâletsiz iş görme ile sınırı ayırmak.

## Soğuk başlangıç (intake)
- İşin konusu ve vekâletin kapsamı (genel/özel yetki gerektiren işlem var mı)?
- İhlal iddiası ne (talimat dışı, menfaat çatışması, hesap vermeme)?
- Ücret kararlaştırıldı mı; vekil tacir/serbest meslek mi?
- Azil/istifa gerçekleşti mi, zamanı uygun mu?

## Denetim şeması
1. **Özen ve sadakat (m.506).** Vekil, benzer alandaki basiretli bir vekilin göstereceği özeni gösterir; ücretliyse özen ölçüsü ağırlaşır. Menfaat çatışmasında müvekkil menfaati önceliklidir.
2. **Talimata uyma (m.505).** Vekil talimatla bağlı; talimattan ancak müvekkil yararına ve önceden izin alınamayacak hallerde ayrılabilir, aksi halde sonuçtan sorumlu.
3. **Bizzat ifa ve alt vekâlet (m.506/2, 507).** Kural bizzat ifa; yetkisiz alt vekilin fiilinden vekil sorumlu, yetkili devirde seçim/talimatta özenden sorumlu.
4. **Hesap verme ve iade (m.508).** Vekil her istendiğinde hesap verir ve aldıklarını iade eder; geç teslim edilen paraya faiz. Bu yükümlülük emredici niteliktedir.
5. **Sona erme (m.512-513).** Taraflar her zaman azil/istifa edebilir (m.512); uygun olmayan zamanda sona erdiren diğer tarafın zararını giderir. Ölüm/ehliyet kaybı/iflasla da sona erer (m.513).
6. **İspat ve yargı yolu.** İhlal ve zararı müvekkil; talimata/izne uygunluğu ve hesabın doğruluğunu vekil ispatlar (m.508 hesap verme yükü). Ücret/tazminat uyuşmazlığında görevli mahkeme niteliğe göre Asliye Hukuk/Ticaret. Ara sonuç: sorumluluk ve tazminat kalemleri.

## Çıktı modülleri
- Hesap verme talebi / azil bildirimi taslağı.
- Özen-sadakat ihlali değerlendirme notu.
- Tazminat talebi dava iskeleti.

## Plugin bağlamı

Bu beceri `borclar-hukuku-ozel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
