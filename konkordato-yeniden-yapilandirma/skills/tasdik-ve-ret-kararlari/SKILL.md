---
name: tasdik-ve-ret-kararlari
description: "Konkordatonun tasdiki için aranan şartların denetimi, tasdik veya ret kararının sonuçları ve bu kararlara karşı kanun yollarının işletilmesi gerektiğinde kullanılır."
---

# Tasdik, Ret ve Kanun Yolları

## Görev
Konkordatonun mahkemece tasdiki için İİK m.305 şartlarını denetlemek, tasdik (m.306) ve ret (m.308) kararlarının sonuçlarını çözümlemek, kanun yollarını (istinaf/temyiz) işletmek.

## Soğuk başlangıç (intake)
- Komiserin esas hakkındaki raporu mahkemeye sunuldu mu?
- Çoğunluk sağlandı, depo şartları yerine getirildi mi?
- İmtiyazlı alacakların ödenmesi güvenceye bağlandı mı?
- Tasdik/ret kararı verildi mi, hangi tarihli?

## Denetim şeması
1. **Tasdik şartları (m.305).** (a) Teklifin borçlunun kaynaklarıyla orantılı olması (rehinli malların satışından veya devamlı işletmeden elde edilecek gelir gözetilir); (b) İİK m.206/1. sırada yer alan alacakların tam ödenmesinin güvenceye bağlanması (alacaklı vazgeçmedikçe); (c) yargılama giderleri ve konkordatonun yerine getirilmesi için gerekli giderlerin depo edilmesi.
2. **Tasdik kararı (m.306).** Mahkeme tasdik kararında alacaklıların hangi ölçüde alacaklarından vazgeçtiğini, ödeme takvimini ve gerekirse bir kayyım/denetim mekanizmasını gösterir. Tasdik kararı ilan ve tescil edilir.
3. **Tasdikin sonuçları (m.308/c-h).** Konkordato, tasdik edilmeyen alacaklar dâhil tüm alacaklılar için bağlayıcı hâle gelir (çekişmeli alacaklar ve rehinli/yakın istisnaları saklı). Rehinli alacaklılarla yapılan anlaşma ayrıca düzenlenir (m.308/h).
4. **Ret (m.308).** Şartlar yoksa talep reddedilir; borçlu iflasa tabi ise ve borca batıksa doğrudan iflasına karar verilebilir (m.308/son). İspat yükü: tasdik şartlarının varlığını borçlu ortaya koyar.
5. **Kanun yolları.** Tasdik/ret kararına karşı istinaf ve temyiz yolu (İİK ve HMK genel hükümleri çerçevesinde) açıktır; süreler titizlikle hesaplanır. Yargıtay 23. Hukuk Dairesi içtihadı esas alınır `[doğrulanacak — karararama.yargitay.gov.tr]`. Ara sonuç: hangi kanun yoluna, hangi sürede başvurulacağı.

## Çıktı modülleri
- Tasdik şartları denetim raporu.
- Tasdik/ret kararı sonuç analizi.
- İstinaf/temyiz dilekçesi taslağı (yer tutuculu) ve süre hesabı.
- Karar sonrası icra/tescil adımları listesi.

## Plugin bağlamı

Bu beceri `konkordato-yeniden-yapilandirma` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
