---
name: temel-kavramlar-ve-sistem
description: "Ekonomik/mali bir fiilin hangi suç tipine ve hangi mevzuat katmanına oturduğunu çözmek, suç genel teorisini (kast, iştirak, içtima, tüzel kişi sorumluluğu) ekonomik suçlara uyarlamak ve dosyanın iskeletini kurmak gerektiğinde kullanılır."
---

# Ekonomik Ceza Hukuku Temel Kavramlar ve Sistematik

## Görev
Ekonomik/mali nitelikli bir fiili doğru suç tipine yerleştirmek, TCK Genel Hükümler süzgecinden geçirmek ve dosyanın çok katmanlı (ceza + yan mevzuat + idari) yapısını ortaya koymak.

## Soğuk başlangıç (intake)
- Fiil ne? (para/belge/vergi/menkul kıymet/kamu görevi hangisiyle ilgili)
- Failin sıfatı ne? (kamu görevlisi, banka mensubu, şirket yöneticisi, mükellef, üçüncü kişi)
- Bir kurum raporu var mı? (VDK, MASAK, SPK, BDDK, müfettiş)
- Soruşturma evresi: şüpheli/iddianame/kovuşturma hangisinde?
- Tüzel kişi mi işin içinde, gerçek kişiye mi sorumluluk bağlanıyor?

## Denetim şeması
1. **Tipiklik — suç tipi seçimi**: Fiili önce TCK özel hükümleriyle eşle (dolandırıcılık m.157-158, güveni kötüye kullanma m.155, zimmet m.247, rüşvet m.252, aklama m.282), sonra yan mevzuatla (VUK m.359, SPK m.106-107-110). Birden çok tip uyuyorsa görünüşte içtima ve fikri içtima (TCK m.44) ile gerçek içtimayı ayır.
2. **Manevi unsur**: Ekonomik suçlar kural olarak kasıtla işlenir (TCK m.21). Vergi kaçakçılığında "bilerek" sahte belge kullanımı; aklamada öncül suç bilgisi aranır. Taksir istisnaidir (m.22).
3. **İştirak**: Yönetici, mali müşavir, aracı kurum çalışanı için faillik mi şeriklik mi (azmettirme m.38, yardım etme m.39) ayrımını yap.
4. **Tüzel kişi**: TCK m.20/2 uyarınca tüzel kişiye ceza verilmez; m.60 güvenlik tedbiri (faaliyet izni iptali, müsadere) ve ilgili kanundaki idari para cezası gündeme gelir.
5. **Dava/mütalaa şartı**: Vergi (VUK m.367) ve SPK (m.115) suçlarında ön şartı kontrol et — yoksa kovuşturma usulden sakat.
6. **Ara sonuç**: Suç tipi, fail sıfatı, manevi unsur, iştirak biçimi ve ön şart durumu tek tabloda netleşir.

## Çıktı modülleri
- Suç tipi-fiil eşleştirme tablosu (madde atıflı)
- Fail/şerik sıfat haritası
- Yan mevzuat ve kurum raporu bağlantı listesi
- Ön şart/dava şartı kontrol notu
- Sonraki adım önerisi (savunma/şikâyet/mütalaa)

## Plugin bağlamı

Bu beceri `ekonomik-ceza` eklentisinin parçasıdır. Eklentinin diğer becerileriyle birlikte
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
- **MCP araçları varsa resmî metni onlardan çek.** `turk-hukuku-mevzuat-mcp` kuruluysa
  kanun/madde metnini hafızadan değil `madde_getir` / `kanun_metni_getir` / `mevzuat_ara`
  ile getir; `turk-hukuku-ictihat-mcp` kuruluysa kararları `ictihat_ara` / `karar_getir`
  ile bulup künyeyi (mahkeme, esas/karar no, tarih) aynen aktar. Bu araçlar mevcutsa
  doğrulamada önce onları kullan; yoksa yukarıdaki künye kuralları aynen geçerlidir.

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
