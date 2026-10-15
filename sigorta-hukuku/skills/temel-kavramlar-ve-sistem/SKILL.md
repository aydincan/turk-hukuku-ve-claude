---
name: temel-kavramlar-ve-sistem
description: "Sigorta türünün (zarar/can, zorunlu/ihtiyari) belirlenmesi, taraf ve kavramların oturtulması, doğru kanun ve genel şartların seçilmesi gerektiğinde; uyuşmazlığı hangi rejimin yöneteceğini saptamak için ilk başvurulacak beceri."
---

# Sigorta Hukuku Temel Kavramları ve Sistematik

## Görev
Önündeki sigorta ilişkisini doğru rejime oturtmak: sigorta türünü, uygulanacak normu (TTK Altıncı Kitap, KTK, 5684) ve devreye girecek genel şartları belirleyip uyuşmazlığın iskeletini kurmak.

## Soğuk başlangıç (intake)
1. Hangi tür sigorta? (kasko, trafik, konut/yangın, ferdi kaza, hayat, sağlık, sorumluluk, nakliyat?)
2. Zorunlu mu ihtiyari mi; teminat zarar mı can sigortası mı?
3. Poliçe, genel şartlar ve özel şartlar elde mi; sigorta bedeli/teminat tutarı nedir?
4. Taraflar kim: sigorta ettiren, sigortalı, lehtar, zarar gören üçüncü kişi?
5. Riziko ne zaman/nasıl gerçekleşti; ihbar yapıldı mı?

## Denetim şeması
1. **Tür tespiti.** TTK m.1453 vd. zarar sigortası mı, m.1487 vd. can sigortası mı? Bu ayrım tazminat ilkesi (m.1459) ve halefiyetin (m.1472) uygulanıp uygulanmayacağını belirler.
2. **Sözleşmenin kurulması.** TTK m.1401-1425: icap/kabul, poliçe verme (m.1424), genel şartların bağlayıcılığı. Ara sonuç: geçerli bir sözleşme ve teminat var mı?
3. **Norm seçimi.** İhtiyari sigortada TTK; zorunlu trafik sigortasında öncelikle KTK m.91 vd. ve Karayolları Motorlu Araçlar Zorunlu Mali Sorumluluk Sigortası Genel Şartları; düzenleyici sorunlarda 5684. İstisna: özel kanun genel kanunu önceler.
4. **Genel şartların okunması.** Teminat kapsamı, istisnalar, muafiyet, riziko adresi/aracı poliçeden ve genel şarttan çıkarılır. İspat yükü: teminat kapsamını talep eden, istisnayı sigortacı (TMK m.6 mantığı).
5. **Yol ve süre kontrolü.** Sigorta Tahkim Komisyonu (5684 m.30) mı genel mahkeme mi; zamanaşımı TTK m.1420 (kural iki yıl) ya da KTK m.109.

## Çıktı modülleri
- Sigorta türü ve uygulanacak norm haritası.
- Taraflar ve sıfatları tablosu (sigorta ettiren/sigortalı/lehtar/üçüncü kişi).
- Teminat-istisna-muafiyet özeti ve ispat yükü dağılımı.
- Olası yol ve zamanaşımı uyarısı.

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
