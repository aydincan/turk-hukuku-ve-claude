---
name: borca-aykirilik-tazminat
description: "Borçlunun borcunu hiç veya gereği gibi ifa etmemesinden doğan tazminat sorumluluğunun unsurları, kusur karinesi ve zarar hesabı tartışıldığında kullanılır."
---

# Borca Aykırılık ve Tazminat Sorumluluğu

## Görev
Borçlunun borca aykırı davranışından doğan tazminat sorumluluğunu (TBK m.112 vd.) unsurları, kusur karinesi, illiyet ve zarar hesabı yönünden değerlendirmek.

## Soğuk başlangıç (intake)
- Borç hiç mi ifa edilmedi, geç mi, yoksa kötü mü ifa edildi?
- Alacaklının uğradığı zarar nedir; doğrudan/dolaylı, fiili zarar/yoksun kalınan kâr?
- Borçlunun yardımcı kişileri (ifa yardımcısı) devrede miydi?
- Sorumsuzluk anlaşması veya sınırlandırma var mı?

## Denetim şeması
1. Temel norm: TBK m.112 — borç hiç veya gereği gibi ifa edilmezse borçlu, kendisine bir kusur yüklenemeyeceğini ispat etmedikçe zararı gidermekle yükümlüdür. Burada kusur karinesi vardır; ispat yükü borçludadır (haksız fiilden farkı).
2. Unsurlar: (a) borca aykırı davranış, (b) zarar, (c) illiyet bağı, (d) kusur (karine ile var sayılır). Kusursuzluk ispatı veya uygun illiyetin kesilmesi sorumluluğu kaldırır.
3. İfa yardımcısının fiili: m.116 — borçlu, yardımcı kişilerin verdiği zarardan kendi fiili gibi sorumludur; bu sorumluluk sözleşmeyle sınırlandırılabilir (m.115 sınırları içinde).
4. Sorumsuzluk anlaşması: m.115 — ağır kusur (kasıt/ağır ihmal) için önceden yapılan sorumsuzluk anlaşması kesin hükümsüzdür; uzmanlık gerektiren faaliyet/izinli işlerde hafif kusur için bile geçersizdir.
5. Zararın belirlenmesi ve indirim: m.114 atfıyla haksız fiil hükümleri (m.51-52) kıyasen; müterafik kusur ve hâkimin takdiri (m.52), öngörülebilirlik.
6. Zamanaşımı: Kural 10 yıl (m.146); kanunda özel süre varsa o uygulanır.
7. İspat yükü: Aykırılığı ve zararı alacaklı; kusursuzluğunu borçlu ispatlar.

## Çıktı modülleri
- Sorumluluk unsurları kontrol listesi (kusur karinesi vurgulu).
- Zarar kalemleri ve indirim sebepleri tablosu.
- Sorumsuzluk/sınırlama maddelerinin geçerlilik denetimi.

## Plugin bağlamı

Bu beceri `borclar-hukuku-genel` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
