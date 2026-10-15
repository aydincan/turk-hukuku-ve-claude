---
name: gecerlilik-ve-hukumsuzluk
description: "Sözleşmenin içeriğinin emredici hükümlere, ahlaka veya kamu düzenine aykırı olup olmadığı, kesin hükümsüzlük veya gabin iddiası bulunduğunda kullanılır."
---

# Geçerlilik, Hükümsüzlük ve Aşırı Yararlanma

## Görev
Sözleşmenin içerik yönünden geçerliliğini denetlemek; kesin hükümsüzlük, kısmi hükümsüzlük ve aşırı yararlanma (gabin) hâllerini ve sonuçlarını ortaya koymak.

## Soğuk başlangıç (intake)
- Sözleşmenin konusu hukuken mümkün ve belirli mi?
- İçerik emredici bir kurala, ahlaka veya kamu düzenine aykırı mı?
- Taraflardan biri zor durum, deneyimsizlik veya düşüncesizlik içinde miydi; edimler arasında açık oransızlık var mı?
- Sakatlık tüm sözleşmeyi mi yoksa tek bir maddeyi mi etkiliyor?

## Denetim şeması
1. Kesin hükümsüzlük: TBK m.27/f.1 — kanunun emredici hükümlerine, ahlaka, kamu düzenine, kişilik haklarına aykırılık veya başlangıçtaki objektif imkânsızlık. Hâkim resen dikkate alır, herkes ileri sürebilir, sonradan icazetle geçerli hâle gelmez.
2. Kısmi hükümsüzlük: m.27/f.2 — sakatlık yalnız bazı hükümlerde ise sözleşme kalanıyla ayakta kalır; tarafların bu hükümler olmaksızın sözleşmeyi yapmayacağı anlaşılmadıkça. Değiştirilmiş kısmi butlan/lehe yorum imkânı.
3. Aşırı yararlanma (gabin): m.28 — objektif unsur (edimler arası açık oransızlık) + sübjektif unsur (zor durum, deneyimsizlik, düşüncesizlikten yararlanma). Sonuç: oransızlığın giderilmesi veya sözleşmeden dönme; süre bir yıl/beş yıl (m.28/f.2).
4. İmkânsızlık ayrımı: Başlangıçtaki imkânsızlık m.27 (hükümsüzlük); sonraki imkânsızlık m.136 (borçtan kurtulma). Karıştırılmamalı.
5. İspat yükü: Hükümsüzlük iddiasını ileri süren, aykırılık veya gabin unsurlarını ispatla yükümlüdür.
6. Ara sonuç: Sözleşme tümüyle mi, kısmen mi geçersiz; iade ve tazminat sonuçları (sebepsiz zenginleşme, culpa in contrahendo).

## Çıktı modülleri
- Geçerlilik denetim raporu (madde madde).
- Hükümsüzlük türü ve kapsamı değerlendirmesi.
- Gabin hâlinde uyarlama/dönme talep taslağı iskeleti.

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
- **MCP sunucuları kuruluysa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp`
  kanun ve madde metnini mevzuat.gov.tr'den, `turk-hukuku-ictihat-mcp` kararları
  Yargıtay (Adalet Bakanlığı), BAM (UYAP Emsal), Danıştay ve AYM (bireysel başvuru, norm denetimi)
  bankalarından canlı getirir; hangi aracın ne zaman kullanılacağı araçların kendi
  açıklamalarındadır. Bu sunucular varsa doğrulamada önce onları kullan ve dönen
  künyeyi aynen aktar; yoksa yukarıdaki künye kuralları aynen geçerlidir.

## Kimin için

Bu beceri avukatlar ve hukukçular içindir (avukat, stajyer avukat, şirket hukukçusu,
akademisyen, hukuk öğrencisi). Soran, kendi işi için gelen ve hukukçu olmayan bir kişiyse:
kanunun ne dediğini ve ilgili kararları genel olarak açıkla, resmî metni getir; bir süre
işliyor olabilirse kanundaki süreyi ve dayanağını açıkça yaz. Kişiye özel hukuki görüş,
strateji, sonuç tahmini ya da imzalanmaya veya mahkemeye verilmeye hazır belge üretme.
Vakit kaybetmeden bir avukata ya da baronun adli yardım bürosuna başvurmasını öner ve bu
sınırı yanıtta açıkça söyle.

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Hukukçu olmayan bir kişiye kendi somut işi için hukuki görüş, strateji önerisi, sonuç
  tahmini ya da imzalanmaya veya verilmeye hazır belge sunmaz; genel bilgi ve resmî metinle
  yetinir, bir avukata ya da baronun adli yardım bürosuna yönlendirir.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri hukukçular içindir ve hukukçunun çalışmasını yapılandırır; deneyseldir ve tek
başına hukuki sonuç doğurmaz. Çıktılar taslaktır; kullanılmadan önce dosyayı üstlenen
yetkili hukukçu tarafından incelenmeli, yürürlükteki mevzuat ve doğrulanmış içtihatla teyit
edilmelidir. Müvekkile ya da başka bir kişiye iletilecek metinlerde yapay zekâdan
yararlanıldığı belirtilmelidir. Hukuki danışmanlık değildir.*
