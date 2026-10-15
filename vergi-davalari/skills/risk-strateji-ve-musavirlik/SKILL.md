---
name: risk-strateji-ve-musavirlik
description: "Vergi uyuşmazlığında dava-uzlaşma-ödeme seçeneklerini kazanma olasılığı, maliyet, nakit akışı ve ceza riskine göre tartıp müvekkile bütüncül strateji önerisi hazırlamak için kullanılır."
---

# Risk Değerlendirmesi ve Vergi Uyuşmazlık Stratejisi

## Görev
Uyuşmazlığın bütününü değerlendirerek dava, uzlaşma, indirimli ödeme veya bekleme seçeneklerini kazanma olasılığı, maliyet, süre, nakit akışı ve olası adli (VUK m.359) risk bakımından tartmak; müvekkile gerekçeli strateji önerisi sunmak.

## Soğuk başlangıç (intake)
1. Toplam mali risk ne (vergi aslı + ceza + faiz) ve müvekkilin ödeme kapasitesi nedir?
2. Uyuşmazlığın çekirdeği hukuki yorum mu, maddi/hesap meselesi mi?
3. Sahte belge / kaçakçılık iddiası var mı (adli boyut riski)?
4. Müvekkilin önceliği maliyeti minimize etmek mi, esastan haklılığı tescil ettirmek mi, hızlı kapanış mı?

## Denetim şeması
1. **Hukuki güç analizi.** Tarhiyat ve cezaların her bir kalemi için iptal şansı (zayıf/orta/güçlü) ilgili madde ve içtihat eğilimiyle (Danıştay daire kararları, `[doğrulanacak]`) işaretlenir.
2. **Maliyet-fayda.** Dava harcı/vekâlet, gecikme faizi (VUK m.112) ve gecikme zammı (AATUHK m.51) birikimi, uzlaşma/indirim (VUK m.376) ile dava sonucu beklentisi karşılaştırılır.
3. **Nakit akışı ve tahsilat baskısı.** İYUK m.27/4 otomatik durma var mı; haciz riski varsa teminat/tecil (AATUHK m.48) ile YD seçenekleri tartılır.
4. **Adli risk köprüsü.** Sahte belge düzenleme/kullanma iddiası varsa VUK m.359 kapsamında ayrı bir ceza yargılaması riski; idari dava ile ceza davası arasındaki etkileşim ve mütalaa şartı (VUK m.367) not edilir. Ara sonuç: idari uyuşmazlık stratejisi adli riski ağırlaştırmayacak şekilde kurgulanır.
5. **Senaryolar.** En iyi / beklenen / en kötü senaryolar tutarsal olarak sunulur; her senaryo için tavsiye edilen eylem ve son tarih belirlenir.

## Çıktı modülleri
- Kalem bazlı kazanma olasılığı ve risk matrisi.
- Seçenek karşılaştırması (dava / uzlaşma / indirimli ödeme) — maliyet, süre, sonuç.
- Müvekkile gerekçeli strateji önerisi ve karar takvimi.

## Plugin bağlamı

Bu beceri `vergi-davalari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
