---
name: olay-tespiti-ve-vakia-cekirdegi
description: "Dağınık belge, beyan ve yazışmalardan mütalaanın dayanacağı çelişmesiz maddi vakıa çekirdeğini ayıklamak, tartışmalı ve eksik noktaları işaretlemek gerektiğinde kullanılır; hukuki değerlendirme öncesi zorunlu adımdır."
---

# Olay Tespiti ve Vakıa Çekirdeği

## Görev
Mütalaanın üzerine kurulacağı maddi olayı, sunulan kaynaklardan tarafsızca ve kronolojik olarak çıkarmak. Hukuki değerlendirme ancak sağlam bir vakıa zemini üzerine oturursa geçerlidir; "altlama"nın küçük önermesi burada üretilir.

## Soğuk başlangıç (intake)
- Hangi belgeler verildi? (Sözleşme, yazışma, ihtarname, tutanak, dekont, bilirkişi raporu)
- Taraflar kim, sıfatları ve aralarındaki hukuki ilişki ne?
- Olayın başlangıç ve bitiş tarihleri; kritik tarihler neler?
- Hangi vakıalar taraflar arasında çekişmeli, hangileri ihtilafsız?

## Denetim şeması
1. Kaynak ayrımı: Her vakıa için dayanağı belirlenir — belgeyle sabit mi, tek taraflı beyan mı, varsayım mı? Belgeyle sabit vakıalar çekirdeği oluşturur.
2. Kronoloji kurma: Vakıalar tarih sırasına dizilir; zaman çizelgesi zamanaşımı, temerrüt, hak düşürücü süre hesapları için zemindir.
3. Çekişmeli/ihtilafsız ayrımı: İspat yükü (TMK m.6, HMK m.190) açısından kritik olan çekişmeli vakıalar ayrı işaretlenir; mütalaa "şu vakıa ispatlanırsa sonuç A, ispatlanamazsa sonuç B" şeklinde koşullu kurulabilir.
4. Hukuken önemli vakıa süzgeci: Uygulanacak kuralın şartlarını ilgilendirmeyen anlatı detayları ayıklanır; sadece subsumption'a girecek vakıalar tutulur.
5. Eksik bilgi ve varsayım haritası: Sonucu değiştirebilecek eksik belgeler listelenir; mütalaa metninde "şu belge görülmediğinden değerlendirme dışıdır" notu düşülür.
6. Ara sonuç: Çelişmesiz vakıa çekirdeği + çekişmeli vakıa listesi + varsayımlar üçlüsü netleşir.

## Çıktı modülleri
- Maddi olay özeti (tarafsız, kronolojik, 1-2 paragraf)
- Zaman çizelgesi tablosu (tarih | olay | dayanak belge)
- Çekişmeli vakıa ve ispat yükü tablosu
- Eksik belge / varsayım listesi

## Plugin bağlamı

Bu beceri `hukuki-mutalaa` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
