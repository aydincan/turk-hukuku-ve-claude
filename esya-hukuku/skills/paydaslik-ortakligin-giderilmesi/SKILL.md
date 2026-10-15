---
name: paydaslik-ortakligin-giderilmesi
description: "Birden çok kişinin malik olduğu taşınmaz/taşınırda kullanım, yönetim ve pay tasarrufu sorunları ya da ortaklığın sona erdirilmesi (izale-i şuyu) gündeme geldiğinde; aynen taksim ve satış suretiyle giderme yollarını kurmak için kullanılır."
---

# Paylı/Elbirliği Mülkiyet ve Ortaklığın Giderilmesi

## Görev
Birlikte mülkiyet ilişkilerini yönetmek: paylı ve elbirliği mülkiyet arasındaki farkı, yönetim ve tasarruf yetkilerini belirlemek ve ortaklığın giderilmesi (izale-i şuyu) davasını aynen taksim veya satış yoluyla kurmak.

## Soğuk başlangıç (intake)
- Mülkiyet paylı mı (belirli paylar) yoksa elbirliği mi (tereke, mal ortaklığı)?
- Talep yönetim/kullanım uyuşmazlığı mı, yoksa ortaklığın tamamen sona erdirilmesi mi?
- Taşınmaz aynen bölünebilir nitelikte mi (imar, yüzölçümü); paydaşlar satışa mı yanaşıyor?
- Üzerinde ipotek, haciz, kira veya muhdesat (bina/ağaç) var mı?

## Denetim şeması
1. **Tür ayrımı**: Paylı mülkiyette her paydaşın belirli (soyut) payı vardır; payını serbestçe devredebilir, rehnedebilir (m.688/3). Elbirliği mülkiyetinde pay belirli değildir; tasarruf bütün üzerinde ve oybirliğiyle yapılır (m.701-702).
2. **Yönetim ve kullanım**: Paylı mülkiyette olağan yönetim pay/paydaş çoğunluğuyla; önemli işlemler çoğunlukla; olağanüstü işlemler oybirliğiyle alınır (m.690-692). Koruma amaçlı işlemleri her paydaş tek başına yapabilir (m.693).
3. **Paydaşlıktan çıkarma**: Yükümlülüklerini ağır biçimde ihlal eden paydaşın paydaşlıktan çıkarılması istenebilir (m.696).
4. **Ortaklığın giderilmesi (m.698-699)**: Her paydaş, aksine sözleşme veya hukuki engel yoksa her zaman paylaşma isteyebilir. Mahkemeden taksim önce **aynen bölme** (m.699/2) ile araştırılır; mümkün değilse **satış suretiyle paylaştırma** (açık artırma) yapılır (m.699/3).
5. **Elbirliğinde önkoşul**: Elbirliği mülkiyetinin önce paylı mülkiyete çevrilmesi veya doğrudan satış istenebilir; terekede tüm mirasçılar davaya dahil edilir (zorunlu dava arkadaşlığı).
6. **Muhdesat ve takyidat**: Üzerindeki bina/ağaç ve ipotek/haciz satış bedelinin paylaşımında ve sıra cetvelinde dikkate alınır.
7. **Ara sonuç**: Aynen taksim mümkünse paylar; değilse satış ve bedelin paylara göre dağıtımı.

## Çıktı modülleri
- Ortaklığın giderilmesi dava dilekçesi iskeleti (paydaş listesi, pay oranları, talep).
- Aynen taksim/satış değerlendirme notu (bölünebilirlik, muhdesat).
- Husumet/zorunlu dava arkadaşlığı kontrol listesi (özellikle tereke).
- Görev: sulh hukuk mahkemesi (HMK m.4); yetki: taşınmazın yeri.

## Plugin bağlamı

Bu beceri `esya-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
