---
name: ifade-sorgu-savunma-haklari
description: "Şüpheli/sanık ifadesi ve sorgusunda susma hakkı, müdafi yardımı, zorunlu müdafilik ve hukuka aykırı ifade yasağı konularında denetim ve itiraz hazırlanırken kullanılır."
---

# İfade, Sorgu ve Savunma Hakları

## Görev
İfade ve sorgunun savunma hakları yönünden hukuka uygunluğunu denetlemek; ihlal halinde ifadenin delil değerini tartışmak ve etkili savunma stratejisi kurmak.

## Soğuk başlangıç (intake)
- İfade kim tarafından, hangi sıfatla (şüpheli/tanık) alındı?
- Haklar hatırlatıldı mı (susma, müdafi, yakına haber)?
- Müdafi hazır mıydı; zorunlu müdafilik gereken bir hal var mıydı?
- İfade sırasında baskı, vaat, yorma iddiası var mı?
- Sanık daha önceki ifadesini değiştirmek istiyor mu?

## Denetim şeması
1. **Hak bildirimi.** İfade/sorgudan önce yüklenen suç, susma hakkı, müdafiden yararlanma, somut delil isteme ve yakına haber verme hakları bildirilir (CMK m.147/1). Bildirim yapılmadan alınan beyan sakattır.
2. **Müdafi yardımı.** Şüpheli/sanık her zaman bir müdafiin yardımından yararlanabilir (m.149); ifade/sorguda müdafi hazır bulunabilir.
3. **Zorunlu müdafi.** Müdafi yoksa istem aranmaksızın görevlendirme: 18 yaşından küçük, sağır-dilsiz, kendini savunamayacak durumda olan ya da alt sınırı 5 yıldan fazla hapsi gerektiren suçtan yargılananlar için (m.150). Müdafi olmadan alınan ifade hükme esas alınamaz (m.148/4).
4. **Yasak yöntemler.** Kötü muamele, işkence, yorma, ilaç verme, hile, kanuna aykırı vaat ile elde edilen beyanlar rıza olsa da delil olamaz (m.148).
5. **Tekrar ve değiştirme.** Kollukça alınan ve müdafi olmadan alınmış ifade, hâkim/mahkeme önünde doğrulanmadıkça hükme esas alınamaz (m.148/4 ile bağlantılı uygulama).
6. **Ara sonuç.** Hak ihlali tespit edilirse ifadenin dışlanması ve buna dayanan delillerin tartışılması; aksi halde savunma beyanının içeriğine odaklanma.

## Çıktı modülleri
- İfade tutanağı hak-bildirimi denetim listesi.
- İfadenin/sorgunun hükümden dışlanması talebi gerekçesi.
- Zorunlu müdafi gerektiren hallerin kontrol tablosu.
- Sanık savunması taslağı ve çelişki/değişiklik açıklaması.

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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay/BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
