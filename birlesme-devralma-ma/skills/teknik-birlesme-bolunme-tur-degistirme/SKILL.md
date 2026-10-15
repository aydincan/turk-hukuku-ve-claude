---
name: teknik-birlesme-bolunme-tur-degistirme
description: "TTK m.134 vd. kapsamında devralma veya yeni kuruluş yoluyla birleşme, TTK m.159 bölünme ve TTK m.180 tür değiştirme işlemlerinin belge, organ kararı ve alacaklı koruma adımlarını yürütmek için kullanılır."
---

# Teknik Birleşme, Bölünme ve Tür Değiştirme

## Görev
TTK'daki yapısal değişiklik işlemlerinin (birleşme/bölünme/tür değiştirme) zorunlu belge ve organ kararı adımlarını ve alacaklı/ortak koruma mekanizmalarını uygulamak.

## Soğuk başlangıç (intake)
- İşlem birleşme mi, bölünme mi (tam/kısmi), tür değiştirme mi?
- Taraf şirketlerin türleri ve büyüklükleri ne?
- Küçük ölçekli şirketler için kolaylaştırılmış usul (TTK m.155-156) uygulanabilir mi?
- Ayrılma akçesi veya pay değişim oranı tartışmalı mı?

## Denetim şeması
1. **Birleşme**: TTK m.136 türler arası birleşme izni; birleşme sözleşmesi (TTK m.145-146), birleşme raporu (TTK m.147), inceleme hakkı (TTK m.149), genel kurul onayı (TTK m.151) ve gerekli nisaplar.
2. **Alacaklı koruması**: TTK m.157 — alacaklılara çağrı ve teminat talebi hakkı; m.158 ortakların kişisel sorumluluğunun devamı.
3. **Pay sahibi koruması**: Pay/ortaklık haklarının korunması (TTK m.140), ayrılma akçesi (TTK m.141); denkleştirme davası (TTK m.191).
4. **Bölünme**: TTK m.159 tam/kısmi bölünme; bölünme sözleşmesi/planı (TTK m.167), m.169 raporu; m.175 sorumluluk (müteselsil).
5. **Tür değiştirme**: TTK m.180-182; tür değiştirme planı (TTK m.185) ve raporu (TTK m.186); ortakların paylarının korunması (TTK m.183).
6. **Tescil ve ilan**: Ticaret siciline tescille hüküm doğar; külli halefiyet sonucu.
7. **İspat/dayanak**: Değişim oranı bilirkişi/değerleme raporu ile desteklenir.

## Çıktı modülleri
- İşlem türüne göre belge ve organ kararı kontrol listesi
- Birleşme/bölünme/tür değiştirme sözleşmesi-planı iskeleti
- Alacaklı çağrı metni ve süre takvimi
- Tescil dosyası içerik listesi

## Plugin bağlamı

Bu beceri `birlesme-devralma-ma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
