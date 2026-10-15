---
name: rekabet-uyum-programi
description: "Teşebbüsler için önleyici rekabet uyumu kurmak; fiyatlandırma, dağıtım, bilgi paylaşımı, rakip temasları ve yerinde inceleme hazırlığı gibi alanlarda risk taraması ve iç politika tasarlamak istendiğinde kullanılır."
---

# Rekabet Uyum Programı ve Risk Önleme

## Görev
Bir teşebbüsün rekabet hukuku ihlal riskini ihlal gerçekleşmeden azaltmak; ticari uygulamaları (fiyat, dağıtım, bilgi paylaşımı, ihale, rakip temasları) m.4/m.6 süzgecinden geçirerek iç politika, eğitim ve yerinde inceleme protokolü kurmak.

## Soğuk başlangıç (intake)
- Teşebbüsün pazardaki konumu hâkim/lider mi, yoksa pazar payı düşük mü?
- Rakiplerle temas alanları: dernek/birlik üyeliği, ortak ihaleler, kıyaslama (benchmarking), tedarik?
- Dağıtım modeli: bayilik, tek satıcılık, online satış kısıtları, fiyat tavsiyesi var mı?
- Daha önce soruşturma/şikâyet geçmişi var mı?

## Denetim şeması
1. **Yatay risk taraması (m.4)** — rakiplerle fiyat, kapasite, gelecek strateji, müşteri/bölge bilgisi paylaşımı kırmızı çizgidir; dernek toplantıları, kıyaslama çalışmaları ve ihale işbirlikleri ayrı ayrı taranır. Rekabete duyarlı bilginin akışı sınırlandırılır.
2. **Dikey risk taraması (m.4 + 2002/2 Tebliğ)** — yeniden satış fiyatının belirlenmesi (RSF) ve mutlak bölgesel koruma ağır kısıtlamadır; tavsiye fiyat/azami fiyat ile RSF ayrımı netleştirilir, online satış ve platform kısıtları gözden geçirilir.
3. **Hâkim durum riski (m.6)** — pazar payı yüksekse münhasırlık, sadakat indirimi, fiyat sıkıştırması, ayrımcılık ve bağlama uygulamaları nesnel haklılık ekseninde değerlendirilir; hâkim teşebbüsün özel sorumluluğu vurgulanır.
4. **Birleşme/işbirliği kontrolü (m.7)** — gelecek işlemler için bildirim eşiği erken kontrol; gun-jumping önleme.
5. **Yerinde inceleme (dawn raid) protokolü** — m.15 incelemesinde kapıda davranış, yasal danışmana ulaşma, belgelerin korunması, engelleme yasağı (silme/saklama nispi ceza ve karine riski); çalışan eğitimi.
6. **Pişmanlık refleksi** — ihlal tespit edilirse Pişmanlık Yönetmeliği kapsamında ilk başvuran avantajının iç prosedüre yerleştirilmesi.

## Çıktı modülleri
- Risk ısı haritası (yatay/dikey/hâkim durum/işlem).
- İç politika ve kırmızı-çizgi rehberi taslağı.
- Yerinde inceleme (dawn raid) eylem protokolü.
- Eğitim ve periyodik denetim takvimi önerisi.

## Plugin bağlamı

Bu beceri `rekabet-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
