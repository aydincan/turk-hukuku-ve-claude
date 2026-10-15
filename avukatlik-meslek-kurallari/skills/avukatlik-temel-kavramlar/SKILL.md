---
name: avukatlik-temel-kavramlar
description: "Avukatlığın hukuki niteliği, kaynak hiyerarşisi (1136 sayılı Kanun, TBB Meslek Kuralları, yönetmelikler, tarife) ve meslek-müvekkil-baro üçlüsü hakkında genel çerçeve ve yön bulma için kullanılır."
---

# Avukatlık Mesleğinin Temel Kavramları ve Sistematiği

## Görev
Avukatlık hukukunun temel kavramlarını, kaynak hiyerarşisini ve sistematiğini ortaya koymak;
bir soruyu doğru norm katmanına ve doğru alt-beceriye yönlendirmek.

## Soğuk başlangıç (intake)
1. Soru avukatın hak/yetkileri mi, müvekkille iç ilişki (sözleşme-ücret-sır) mı, yoksa
   disiplin/baro boyutu mu?
2. Kişi avukat mı, stajyer mi, müvekkil mi, karşı taraf mı?
3. Olayda menfaat çatışması veya sır riski görünüyor mu?
4. Uyuşmazlık hangi aşamada (danışma, sözleşme, dava, azil, disiplin şikâyeti)?

## Denetim şeması
1. **Niteliği belirle.** Avukatlık hem kamu hizmeti hem serbest meslektir; yargının kurucu
   unsuru ve bağımsız savunmadır (Av. K. m.1-2). Bu nitelik, bağımsızlık ve sır gibi tüm
   meslek kurallarının temel gerekçesidir.
2. **Kaynak hiyerarşisini kur.** Çekirdek: 1136 sayılı Avukatlık Kanunu. Üstüne TBB Meslek
   Kuralları, Avukatlık Kanunu Yönetmeliği, TBB Reklam Yasağı Yönetmeliği ve yıllık TBB
   Avukatlık Asgari Ücret Tarifesi gelir. Müvekkil ilişkisinin maddi temeli vekâlet
   sözleşmesidir (TBK m.502 vd.).
3. **Genel davranış normunu uygula.** Avukat görevini özenle, doğrulukla ve onurla yapar;
   meslek kurallarına uyar (Av. K. m.34, TBB Meslek Kuralları m.3-4). Ara sonuç: somut
   davranış bu genel normla bağdaşıyor mu?
4. **Doğru alt-beceriye yönlendir.** Sır → sir-saklama; çatışma → cikar-catismasi; ücret →
   vekalet-ucreti; disiplin → disiplin-sorumlulugu; arama/dokunulmazlık → avukatin-yetkileri;
   tarife/karşı taraf vekâlet ücreti → ücret becerisi. İspat yükü genel kuralda davacıdadır
   (TMK m.6), disiplinde kovuşturmayı yürüten organdadır.

## Çıktı modülleri
- Sorunu doğru norm katmanına yerleştiren kısa harita.
- İlgili madde atıfları listesi (Av. K. + TBB Meslek Kuralları + tarife yılı).
- Önerilen alt-beceri ve eksik bilgi soruları.

## Plugin bağlamı

Bu beceri `avukatlik-meslek-kurallari` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
