---
name: hasta-haklari
description: "Sağlık hizmeti sırasında bilgilendirme, mahremiyet, kayıtlara erişim, tedaviyi reddetme gibi hasta haklarının ihlal edilip edilmediğini ve başvuru yollarını değerlendirmek için kullanılır."
---

# Hasta Hakları ve İhlal Değerlendirmesi

## Görev
Hasta haklarına ilişkin bir ihlal iddiasını mevzuata göre nitelemek, idari ve yargısal başvuru yollarını belirlemek.

## Soğuk başlangıç (intake)
1. Hangi hak ihlal edildi: bilgilendirme, mahremiyet, hizmete erişim, tedaviyi reddetme, kayıtlara erişim?
2. Olay kamu mu özel sağlık kuruluşunda mı geçti?
3. Hasta hakları birimine/SABİM/CİMER başvurusu yapıldı mı?
4. İhlalden doğan bir maddi/manevi zarar var mı?

## Denetim şeması
1. **Hak kataloğu**: Hasta Hakları Yönetmeliği — hizmetten genel olarak faydalanma, bilgilendirme (m.15), kayıtları inceleme, mahremiyet, rıza ve reddetme (m.24-31), tıbbi özen. Mahremiyet aynı zamanda KVKK (6698) kapsamında özel nitelikli sağlık verisidir.
2. **İhlalin tespiti**: İlgili hakkın somut içeriği ile fiilî durum karşılaştırılır; mevzuata aykırılık ve hastanın bundan etkilenmesi aranır.
3. **İdari yol**: Hasta hakları kurulu, SABİM, CİMER; kamu hizmeti ise idareye başvuru. Disiplin yönü için meslek odası/Bakanlık.
4. **Yargısal yol**: Maddi/manevi tazminat (özel kuruluş → adli yargı; kamu → tam yargı davası, İYUK m.13). Kişilik hakkı ihlali için TMK m.24-25, TBK m.58.
5. **Veri/mahremiyet ekseni**: Sağlık verisinin izinsiz paylaşımı KVKK m.6 ve TCK m.136 (verileri hukuka aykırı verme/ele geçirme) yönünden ayrıca değerlendirilir.
6. **Ara sonuç**: İhlal + zarar/etki varsa uygun başvuru yolu seçilir; sadece usuli ihlalde idari başvuru öne çıkar.

## Çıktı modülleri
- İhlal edilen hak ve dayanak madde eşlemesi
- Başvuru yolu haritası (idari + yargısal)
- Tazminat/şikâyet dilekçesi taslağı (yer tutuculu)
- KVKK boyutu uyarı notu

## Plugin bağlamı

Bu beceri `saglik-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
