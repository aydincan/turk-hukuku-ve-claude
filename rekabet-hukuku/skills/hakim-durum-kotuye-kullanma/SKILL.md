---
name: hakim-durum-kotuye-kullanma
description: "Bir teşebbüsün pazar gücüne dayanarak dışlayıcı (yıkıcı fiyat, fiyat sıkıştırması, münhasırlık, bağlama, ayrımcılık) veya sömürücü davranışta bulunduğu iddialarını 4054 m.6 çerçevesinde değerlendirmek istendiğinde kullanılır."
---

# Hâkim Durumun Kötüye Kullanılması (m.6)

## Görev
Önce ilgili pazarda hâkim durumun varlığını tespit etmek, ardından söz konusu tek taraflı davranışın 4054 m.6 anlamında kötüye kullanma oluşturup oluşturmadığını ve nesnel haklılık savunmasını değerlendirmek.

## Soğuk başlangıç (intake)
- Teşebbüsün ilgili pazardaki yaklaşık payı ve konumu nedir; rakip ve giriş engeli durumu?
- İddia edilen davranış: yıkıcı/aşırı fiyat, fiyat sıkıştırması, münhasırlık, bağlama, mal vermeyi reddetme, ayrımcılık mı?
- Davranış dışlayıcı mı (rakip dışlama) yoksa sömürücü mü (müşteri sömürüsü)?
- Müvekkil hâkim teşebbüs mü, yoksa dışlanan rakip/şikâyetçi mi?

## Denetim şeması
1. **İlgili pazar + hâkimlik (m.3, m.6)** — ilgili pazar tanımlanır; hâkim durum, pazarda rakiplerden ve müşterilerden bağımsız hareket edebilme gücüdür. Yüksek pazar payı kuvvetli gösterge olmakla birlikte tek başına belirleyici değildir; giriş engelleri, dengeleyici alıcı gücü ve dikey bütünleşme birlikte değerlendirilir.
2. **Davranışın nitelendirilmesi** — m.6 bentleri örnek niteliğindedir:
   - Dışlayıcı: yıkıcı fiyat, fiyat sıkıştırması (marj sıkıştırması), münhasır alım/satım, sadakat indirimleri, bağlama-paketleme, mal/hizmet vermeyi reddetme (zorunlu unsur doktrini), ayrımcı koşullar.
   - Sömürücü: aşırı/adil olmayan fiyat ve haksız ticari koşullar dayatma.
3. **Etki analizi** — kötüye kullanma için kural olarak pazarı kapama/dışlama etkisi veya tüketici zararı gösterilmelidir; uygun rakip (as-efficient competitor) testi gibi iktisadi araçlar kullanılır.
4. **Nesnel haklılık ve etkinlik savunması** — davranışın nesnel olarak haklı olduğu veya etkinlik kazanımı sağladığı ileri sürülebilir; ispat yükü bu noktada teşebbüse geçer.
5. **Ara sonuç ve yaptırım** — hâkimlik yoksa m.6 uygulanmaz (davranış m.4 açısından incelenebilir). Hâkimlik + kötüye kullanma + etki varsa ihlal; ceza ciro üzerinden (m.16), ayrıca özel hukukta tazminat (m.57-58).

## Çıktı modülleri
- Hâkimlik analizi (pay, engeller, bağımsız hareket gücü).
- Davranış-tip eşleştirmesi ve dışlama/sömürü ayrımı.
- Nesnel haklılık savunması taslağı veya saldırı argümanları.
- Doğrulanacak Kurul/Danıştay kararı atıfları `[doğrulanacak]`.

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
