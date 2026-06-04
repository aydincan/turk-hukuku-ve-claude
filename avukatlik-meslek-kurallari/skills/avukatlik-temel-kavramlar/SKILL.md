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

## Bu beceri ne yapmaz

- Avukatlık veya hukuki danışmanlık yerine geçmez; nihai hukuki sorumluluk yetkili
  hukukçudadır.
- Müvekkili, onun açık kararı olmadan bağlamaz.
- Belgelerle ya da net beyanla desteklenmeyen vakıaları olgu gibi değerlendirmez.
- Menfaat çatışması veya meslek kuralı (1136 s.K., TBB Meslek Kuralları) sorunu
  görülürse dosyadan sorumlu avukata yönlendirir.

---

*Bu beceri deneyseldir ve hukukçunun çalışmasını yapılandırmaya yarar; tek başına hukuki
sonuç doğurmaz. Tüm çıktılar yürürlükteki mevzuat ve doğrulanmış güncel içtihatla teyit
edilmelidir. Hukuki danışmanlık değildir.*
