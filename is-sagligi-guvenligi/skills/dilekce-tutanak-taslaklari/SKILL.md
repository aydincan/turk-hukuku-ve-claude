---
name: dilekce-tutanak-taslaklari
description: "İş kazası tazminat dava dilekçesi, idari ceza itirazı, SGK işlemlerine itiraz ve İSG dokümantasyonu (uyarı, tutanak) taslaklarını üretmek için kullanılır."
---

# Dilekçe, Tutanak ve Başvuru Taslakları

## Görev
İSG dosyasının türüne uygun taslak üretmek: iş kazası tazminat dava dilekçesi, idari para cezası itirazı, SGK işlemine itiraz/dava, ve işveren tarafı için savunma/uyarı/tutanak metinleri. Eksik bilgiler `[doldurulacak]` yer tutucularıyla işaretlenir.

## Soğuk başlangıç (intake)
- Hangi taslak isteniyor (tazminat dilekçesi / ceza itirazı / SGK itirazı / İSG tutanağı)?
- Taraflar, sıfatları ve husumet (asıl işveren-alt işveren) netleşti mi?
- Talep sonucu sayısallaştı mı (fazlaya ilişkin haklar saklı, belirsiz alacak mı)?
- Dayanak deliller ve madde atıfları hazır mı?

## Denetim şeması
1. **Dava dilekçesi mimarisi (HMK m.119):** Mahkeme, taraflar, konu, açık talep sonucu, vakıalar, hukuki sebepler (TBK m.417, m.49-56; 6331 ilgili madde), deliller ve imza. İş kazası tazminatında belirsiz alacak/kısmi dava tercihini ve fazlaya ilişkin hakların saklı tutulmasını ekle.
2. **İdari ceza itirazı:** Sulh ceza hâkimliğine hitap, 5326 m.27 dayanağı, on beş günlük süre vurgusu, ceza-madde uyumsuzluğu ve usul sakatlığı gerekçeleri, iptal/indirim talebi.
3. **SGK işlemine itiraz/dava:** İlgili işleme (rücu, gelir, tespit) göre iş mahkemesine; idari aşamada SGK'ya itiraz gerekiyorsa onu da ele.
4. **İşveren tarafı dokümanları:** İSG kuralına aykırılık savunma tutanağı, uzman/hekim yazılı uyarı metni, KKD zimmet tutanağı, eğitim katılım formu şablonu — ileride ispat için tarih/imza alanlarıyla.
5. **Disiplin:** Madde atıflarını doğru ver; içtihat zikredilecekse künyeyi `[doğrulanacak]` işaretle, uydurma numara yazma. **Ara sonuç:** Taslağı yer tutucularla eksiksiz iskelete oturt.

## Çıktı modülleri
- İstenen tür için tam dilekçe/başvuru taslağı.
- Eksik bilgi `[doldurulacak]` listesi.
- Ekler ve delil dizini önerisi.

## Plugin bağlamı

Bu beceri `is-sagligi-guvenligi` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
