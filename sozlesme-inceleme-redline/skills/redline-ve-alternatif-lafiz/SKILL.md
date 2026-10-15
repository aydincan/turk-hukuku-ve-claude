---
name: redline-ve-alternatif-lafiz
description: "Riskli maddeler için somut düzeltme metni, alternatif lafız ve yedek (fallback) pozisyonlar üretip gerekçelendirmek gerektiğinde kullanılır."
---

# Redline ve Alternatif Lafız Üretimi

## Görev
Tespit edilen her riskli madde için "mevcut lafız → önerilen lafız → gerekçe (madde atfıyla)" üçlüsünü ve yedek pozisyonları üreterek müzakereye hazır redline metni oluşturmak.

## Soğuk başlangıç (intake)
- Hangi maddeler redline'a girecek (risk haritasından gelen öncelikli liste)?
- Müvekkilin ideal ve kabul edilebilir asgari pozisyonu ne (anchor + fallback)?
- Karşı tarafın metni değiştirme esnekliği ve pazarlık gücü ne?
- Üslup: agresif tam redline mi, dengeli "market standard" mı?

## Denetim şeması
1. **Önceliklendirme**: Deal-breaker maddeler tam yeniden yazılır; pazarlık maddelerine alternatif sunulur; kabul edilebilir maddelere yalnız not düşülür.
2. **Lafız tasarımı**: Her öneri için (a) mevcut metin, (b) önerilen metin, (c) gerekçe — emredici dayanak (TBK m.27, m.115, m.182) veya denge/menfaat gerekçesi. Belirsiz ifadeler ölçülebilir/tetikleyicili hale getirilir.
3. **Karşılıklılık enjeksiyonu**: Tek taraflı hak/yükümlülükler karşılıklı hale getirilir (fesih, ceza, gizlilik, tazminat).
4. **Yedek pozisyon (fallback)**: Her kritik talep için 1-2 kademeli geri çekilme lafzı (örn. sınırsız tavan → işlem bedeli tutarında tavan → 2 katı tavan).
5. **Tutarlılık denetimi**: Değiştirilen madde tanımlar, çapraz atıflar ve diğer maddelerle çelişmesin; "severability/bölünebilirlik" ve "tüm sözleşme" kayıtlarıyla uyum.
6. **Yer tutucu disiplini**: Bilinmeyen veriler (tutar, süre, taraf) `[doldurulacak]`; teyit gereken mevzuat/içtihat `[doğrulanacak]` etiketiyle bırakılır, uydurulmaz.

## Çıktı modülleri
- Redline tablosu: madde / mevcut lafız / önerilen lafız / gerekçe / öncelik.
- Yedek pozisyon (fallback) basamakları.
- Markup'lı sözleşme metni veya değişiklik listesi (track-changes mantığı).

## Plugin bağlamı

Bu beceri `sozlesme-inceleme-redline` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
