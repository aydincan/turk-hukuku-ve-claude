---
name: veri-ihlali-bildirimi
description: "Bir veri ihlali (sızıntı, yetkisiz erişim, kayıp) yaşandığında ya da güvenlik tedbirleri denetlenirken; Kurul'a ve ilgili kişilere bildirim yükümlülüğü ve süreleri değerlendirilirken kullanılır."
---

# Veri İhlali ve Güvenlik Yükümlülüğü

## Görev
KVKK m.12 kapsamında veri güvenliği tedbirlerini denetlemek ve bir veri ihlali gerçekleştiğinde Kurul'a ve ilgili kişilere bildirim sürecini, sürelerini ve içeriğini doğru yönetmek.

## Soğuk başlangıç (intake)
1. Ne oldu — yetkisiz erişim, sızıntı, kayıp, fidye yazılımı, yanlış alıcıya gönderim?
2. İhlal ne zaman, nasıl tespit edildi (tespit anı süreyi başlatır)?
3. Hangi kişi grupları ve veri kategorileri etkilendi, sayısı nedir?
4. Özel nitelikli veri veya finansal veri etkilendi mi (zarar riski yüksek olabilir)?

## Denetim şeması
1. **Güvenlik yükümlülüğü — m.12/1**: Veri sorumlusu, verinin hukuka aykırı işlenmesini ve erişilmesini önlemek, muhafazasını sağlamak için uygun teknik ve idari tedbirleri almak zorundadır. Kurul'un teknik-idari tedbirler rehberi ölçü alınır.
2. **Kurul'a bildirim — m.12/5**: İhlal öğrenildiği tarihten itibaren en kısa sürede ve 72 saat içinde Kurul'a bildirilir. Bildirim Kurul'un belirlediği form üzerinden yapılır; 72 saat aşılırsa gecikme gerekçesi açıklanır.
3. **İlgili kişiye bildirim**: İhlalden etkilenen kişiler de makul en kısa sürede bilgilendirilir; bu, ilgili kişilerin önlem almasını sağlamaya yöneliktir.
4. **İçerik**: Bildirimde ihlalin niteliği, etkilenen veri kategorileri ve kişi sayısı, olası sonuçlar, alınan/önerilen tedbirler ve irtibat bilgisi yer alır.
5. **Ara sonuç**: Bildirim yükümlülüğünün ihlali m.18 kapsamında ayrı bir yaptırım sebebidir; ihlal anından itibaren kanıt zinciri (loglar, müdahale kayıtları) korunmalıdır.

İspat yükü: Tedbirlerin alındığını ve bildirimin süresinde yapıldığını veri sorumlusu ispatlar; müdahale dokümantasyonu hem yaptırım hem tazminat davalarında belirleyicidir.

## Çıktı modülleri
- İhlal müdahale ve 72 saat takip cetveli.
- Kurul bildirim formu taslağı ([doldurulacak] alanlarla).
- İlgili kişi bilgilendirme metni ve etkilenen kayıt listesi şablonu.

## Plugin bağlamı

Bu beceri `kvkk-veri-koruma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
