---
name: dilekce-basvuru-taslagi
description: "Sigortacıya ön başvuru, Sigorta Tahkim Komisyonu başvurusu, dava veya cevap dilekçesi gibi sigorta uyuşmazlığına özgü belgelerin taslaklanması istendiğinde kullanılır; doğru hukuki sebep ve talep mimarisiyle metin üretir."
---

# Başvuru ve Dilekçe Taslakları (Sigortacıya Başvuru, Tahkim, Dava)

## Görev
Sigorta uyuşmazlığına özgü belgeleri usulüne uygun taslaklamak: sigortacıya zorunlu ön başvuru, Sigorta Tahkim Komisyonu başvurusu, dava dilekçesi veya cevap dilekçesi; vakıa-hukuki sebep-talep mimarisini kurmak.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor (ön başvuru / tahkim / dava / cevap)?
2. Taraflar, poliçe bilgileri, riziko ve talep tutarı belli mi?
3. Forum seçildi mi (tahkim/ticaret/tüketici) ve başvuru şartı tamam mı?
4. Hangi deliller mevcut (poliçe, eksper raporu, kaza tutanağı, ödeme kanıtı)?

## Denetim şeması
1. **Belge türü ve dayanak.** Ön başvuru için KTK m.97 / 5684 m.30 başvuru şartı; tahkim için 5684 m.30; dava için HMK m.119 zorunlu unsurları. Ara sonuç: hangi format ve zorunlu unsurlar?
2. **Vakıa ve hukuki sebep.** Riziko, teminat ve ihlal vakıaları kronolojik; hukuki sebepler madde atıflı (örn. TTK m.1409/1421 teminat, m.1459 tazminat, m.1472 halefiyet, KTK m.91/97 doğrudan hak).
3. **Talep sonucu.** Net, miktar belirten talep; alacak likitse kesin, değilse belirsiz alacak/kısmi dava tercihi (HMK m.107-109); faiz başlangıcı ve türü (temerrüt/avans faizi).
4. **Delil bağlama.** Her vakıayı bir delile bağla; bilirkişi ve eksper raporu talebi; eksik belgeler için `[doldurulacak]` yer tutucu.
5. **Usul kontrolü.** Görev-yetki, harç/gider, zamanaşımı/hak düşürücü süre, başvuru şartı tamamlığı son kez doğrulanır.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlık, taraflar, açıklamalar, hukuki sebepler, deliller, talep sonucu).
- Madde atıflı hukuki sebep listesi.
- Delil dizini ve `[doldurulacak]` eksik belge listesi.
- Süre/usul uyarı notu.

## Plugin bağlamı

Bu beceri `sigorta-hukuku` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
