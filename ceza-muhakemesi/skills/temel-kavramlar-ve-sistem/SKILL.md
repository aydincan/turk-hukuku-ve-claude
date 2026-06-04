---
name: temel-kavramlar-ve-sistem
description: "Ceza muhakemesinin evrelerini, süjelerini, sıfatları ve yetkili mercileri ayırt etmek; bir dosyanın hangi aşamada olduğunu ve hangi usul kurallarının uygulanacağını belirlemek gerektiğinde kullanılır."
---

# Temel Kavramlar ve Muhakeme Sistematiği

## Görev
Ceza muhakemesi dosyasının evresini, süjelerini ve uygulanacak usul rejimini doğru saptamak; kullanıcının elindeki belgeden hangi yetkilerin ve hakların doğduğunu çerçevelemek.

## Soğuk başlangıç (intake)
- Dosya soruşturma evresinde mi (Cumhuriyet savcılığı, "Soruşturma No") yoksa kovuşturma evresinde mi (mahkeme, "Esas No")?
- Müvekkilin sıfatı ne: şüpheli/sanık, mağdur/müşteki/katılan, yoksa tanık mı?
- Elinizdeki belge nedir: ifade tutanağı, iddianame, tensip, gerekçeli karar, takipsizlik (KYOK)?
- Suç tipi ve öngörülen ceza nedir (görevli mahkemeyi ve usulü belirler)?
- Bir süre işliyor mu (gözaltı, tutukluluk, itiraz/istinaf süresi)?

## Denetim şeması
1. **Evre tespiti.** Soruşturma savcı yönetiminde, gizli ve yazılıdır (CMK m.157, m.160). Kovuşturma iddianamenin kabulüyle başlar (m.175), kural olarak aleni ve sözlüdür (m.182).
2. **Süje ve sıfat.** Şüpheli soruşturmada, sanık kovuşturmada (m.2). Mağdurun hakları m.234, katılanın m.237-239'da; sıfat, başvurulabilecek yolları belirler.
3. **Görevli mahkeme.** Ağır ceza mahkemesinin görevi 5235 s.K. m.12'de sınırlı sayıda sayılır (ör. yağma, nitelikli dolandırıcılık, kasten öldürme ve ağırlaştırılmış müebbet/müebbet/on yıldan fazla cezayı gerektiren suçlar); kalanlar asliye ceza. Sulh ceza hâkimliği soruşturma tedbirleri ve itirazlar için (m.10, 5235 s.K. m.10).
4. **Yetki.** Suçun işlendiği yer mahkemesi yetkilidir (m.12); yetki itirazı kovuşturmada ilk oturumda ileri sürülür (m.18).
5. **Ara sonuç.** Evre + sıfat + görev/yetki belirlenince uygulanabilir tedbir, hak ve kanun yolu kümesi netleşir; eksik veya yanlış mercie yapılan başvuru süre kaybına yol açar.

## Çıktı modülleri
- Dosya künyesi tablosu (evre, no, taraflar, sıfatlar, suç, görevli mahkeme).
- Uygulanabilir haklar/yetkiler listesi ve dayanak maddeler.
- İşleyen süreler ve son tarihler uyarısı.
- Bir sonraki adım önerisi ve yönlendirilecek doğru mercii.

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
