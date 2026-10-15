---
name: malpraktis-komplikasyon-ayrimi
description: "İstenmeyen tıbbi sonucun önlenebilir bir kusur (malpraktis) mu yoksa öngörülen ama kaçınılmaz bir komplikasyon mu olduğunu ayırmak için kullanılır; komplikasyon yönetimi kusurunu da değerlendirir."
---

# Malpraktis ve Komplikasyon Ayrımı

## Görev
İstenmeyen sonucun hukuki niteliğini belirlemek: önlenebilir özen ihlali (malpraktis/sorumluluk doğurur) mu, yoksa özenli davranışa rağmen ortaya çıkan komplikasyon (kural olarak sorumluluk doğurmaz) mu.

## Soğuk başlangıç (intake)
1. İstenmeyen sonuç literatürde bu müdahalenin bilinen komplikasyonu mu?
2. Müdahale endikasyona ve tıbbi standarda uygun yapıldı mı?
3. Komplikasyon ortaya çıktığında zamanında teşhis ve müdahale edildi mi?
4. Hasta bu komplikasyon riski hakkında önceden aydınlatıldı mı?

## Denetim şeması
1. **Standarda uygunluk testi**: Müdahale tekniği, endikasyonu ve zamanlaması tıbbın güncel verilerine uygun mu? Uygunsa malpraktis ihtimali zayıflar.
2. **Öngörülebilirlik/kaçınılabilirlik**: Komplikasyon, dikkatli bir hekimce öngörülebilir ama somut olayda kaçınılmaz mıydı? Kaçınılabilir bir sonuç önlenmemişse bu malpraktistir (TBK m.49, TCK m.22 taksir).
3. **Komplikasyon yönetimi kusuru**: Komplikasyon meşru olsa bile, geç teşhis, yanlış sevk, takipsizlik veya yetersiz müdahale bağımsız bir kusur oluşturur ve sorumluluk doğurur.
4. **Aydınlatma bağlantısı**: Komplikasyon riski önceden bildirilmemişse, sonuç hukuken hastaya yüklenemez (bkz. Aydınlatılmış Onam Denetimi).
5. **İspat ve bilirkişi**: Ayrım maddi-teknik bir sorundur; ATK ve uzmanlık dalı bilirkişisi belirleyicidir. Rapor metodolojisi ayrıca denetlenmelidir.
6. **Ara sonuç**: Standarda uygun + öngörülen + iyi yönetilen + aydınlatılmış sonuç = komplikasyon (sorumluluk yok). Aksi her hâlde malpraktis tartışması açılır.

## Çıktı modülleri
- Malpraktis/komplikasyon ayrım tablosu (kriter bazlı)
- Komplikasyon yönetimi kusuru kontrolü
- Bilirkişiye sorulacak teknik sorular taslağı
- İlkesel içtihat atfı (Yargıtay 12. CD / 3. HD) [doğrulanacak]

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
