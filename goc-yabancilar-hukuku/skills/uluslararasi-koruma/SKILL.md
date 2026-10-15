---
name: uluslararasi-koruma
description: "Sığınma, mülteci, ikincil veya geçici koruma talebi söz konusu olduğunda; koruma başvurusunun statü tespiti, başvuru usulü, geri gönderme yasağı ve ret kararına itiraz için kullanılır."
---

# Uluslararası ve Geçici Koruma

## Görev
Yabancının koruma ihtiyacını YUKK koruma rejimine yerleştirmek, doğru statüyü (mülteci, şartlı mülteci, ikincil koruma, geçici koruma) belirlemek, başvuru ve itiraz sürecini yönetmek; geri gönderme yasağını her aşamada güvence altına almak.

## Soğuk başlangıç (intake)
1. Menşe/ikamet ülkesi ve geri dönüşte karşılaşılacak somut risk (zulüm, ölüm cezası, işkence, silahlı çatışma) nedir?
2. Türkiye'ye giriş tarihi ve koruma talebi kayda alındı mı (kayıt tarihi)?
3. Suriye uyruklu/vatansız mı (geçici koruma kapsamı) yoksa diğer uyruk mu?
4. Verilen bir karar (kabul edilemez, açıkça dayanaktan yoksun, ret) ve tebliğ tarihi var mı?

## Denetim şeması
1. **Statü ayrımı**: Mülteci — Avrupa ülkesi kaynaklı olaylar nedeniyle (YUKK m.61, coğrafi sınırlama). Şartlı mülteci — Avrupa dışı kaynaklı zulüm korkusu (m.62). İkincil koruma — m.63: ölüm cezası, işkence/insanlık dışı muamele veya ayrım gözetmeyen şiddet riski.
2. **Geçici koruma**: Kitlesel akın halinde Geçici Koruma Yönetmeliği (Suriye); bireysel statü belirleme yerine grup esaslı koruma.
3. **Başvuru usulü**: m.65 — valiliklere bizzat başvuru, kayıt, mülakat; başvuru sahibinin hak ve yükümlülükleri (m.67-69).
4. **Geri gönderme yasağı (non-refoulement)**: m.4 ve m.55 — başvuru sonuçlanana ve karar kesinleşene kadar uzaklaştırılamama; AİHS m.3 ile birlikte mutlak nitelik.
5. **Karar ve itiraz**: Kabul edilemez başvuru (m.72), açıkça dayanaktan yoksunluk (m.79), ret kararları. İtiraz — Uluslararası Koruma Değerlendirme Komisyonu ve/veya idare mahkemesine dava; sürelere dikkat.
**İspat yükü**: Başvuran riskini makul/inandırıcı biçimde ortaya koyar; tereddütte başvuranın lehine yorum (şüpheden yararlanma) ilkesi gözetilir. İdare risk değerlendirmesini güncel ülke bilgisiyle yapmakla yükümlüdür.

## Çıktı modülleri
- Statü belirleme analizi ve dayanak madde tablosu.
- Başvuru/mülakat hazırlık notu ve risk anlatısı taslağı.
- Ret/kabul edilemezlik kararına karşı itiraz/dava dilekçesi iskeleti.

## Plugin bağlamı

Bu beceri `goc-yabancilar-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
