<<<REFERANS>>>
# KVKK Uyum Denetleyicisi — Metodoloji Referansı

## Alanın sistematiği
Bu alan, KVKK doktrinini yeniden üretmek değil; bir veri sorumlusunun mevcut durumunu 6698 sayılı Kanun'a karşı **denetlemek**, boşlukları **skorlamak** ve önceliklendirilmiş bir **eylem planına** bağlamaktır. Çalışma mantığı bir denetim (audit) döngüsüdür: kapsam belirleme → kanıt toplama (envanter ve belge incelemesi) → uygunluk testi (madde madde) → bulgu ve risk skoru → düzeltme planı → yeniden denetim. Burada hukukçu, dava açan değil; bir uyum mimarisinin "var/eksik/güncel değil/uygulanmıyor" durumunu tespit eden ve hesap verebilirlik (accountability) ilkesini somut belgelere bağlayan kişidir. Tüm bulgular ölçülebilir, kapatılabilir ve sorumlu/termin atanmış olmalıdır; "genel olarak uyumsuz" demek denetim çıktısı değildir.

## Başat normlar ve madde atıfları
- **KVKK m.4** — genel ilkeler (hukuka uygunluk, doğruluk/güncellik, belirli-açık-meşru amaç, ölçülülük, süreyle sınırlılık). Her denetim kalemi nihayetinde bu ilkelere bağlanır; hesap verebilirlik buradan doğar.
- **KVKK m.5-6** — işleme şartları; envanterdeki her faaliyetin geçerli bir hukuki sebebe (açık rıza dışı şartlar öncelikli) oturup oturmadığı test edilir. m.6, 7499 sayılı Kanun ile 01.06.2024'ten itibaren yeni rejime tabidir.
- **KVKK m.10** ve Aydınlatma Tebliği — aydınlatma metinlerinin zorunlu unsur ve zamanlama denetimi.
- **KVKK m.7** ve İmha Yönetmeliği — saklama-imha politikası, süre matrisi, periyodik imha (azami 6 ay).
- **KVKK m.8-9** — yurt içi/yurt dışı aktarım; m.9, 7499 ile yeniden kurgulandı (yeterlilik kararı, standart sözleşme, taahhütname, bağlayıcı şirket kuralları, arızi haller).
- **KVKK m.11, m.13** ve Başvuru Tebliği — ilgili kişi başvuru prosedürü ve 30 gün yanıt süresi denetimi.
- **KVKK m.12** ve Teknik-İdari Tedbirler Rehberi — veri güvenliği tedbirleri ve veri ihlali müdahale planı; ihlal bildirimi en geç 72 saat.
- **KVKK m.16** ve Sicil Yönetmeliği — VERBİS kayıt yükümlülüğü ve istisna eşikleri.
- **KVKK m.18** — idari para cezaları; bulgu risk skorunda yaptırım ağırlığı buradan tartılır. 7499 sonrası dava yolu idare mahkemesidir.

## Çalışma yöntemi
1. **Kapsam ve rol**: Denetlenen tüzel kişi veri sorumlusu mu, veri işleyen mi; hangi birimler, hangi sistemler kapsamda? Kapsam yazılı sabitlenir.
2. **Kanıt toplama**: Mevcut belge seti istenir (aydınlatma, rıza, politikalar, VERBİS çıktısı, sözleşmeler, ihlal kayıtları). Beyan değil belge esastır.
3. **Madde madde test**: Her başlık için bir kontrol maddesi; sonuç "Uygun / Kısmen / Uygunsuz / Kapsam dışı" olarak işaretlenir, kanıt referansı yazılır.
4. **Risk skoru**: Her bulguya olasılık ve etki (yaptırım + itibar + ilgili kişi zararı) verilir; yüksek/orta/düşük önceliklendirilir.
5. **Eylem planı**: Her bulguya düzeltici aksiyon, sorumlu ve termin atanır; yeniden denetim tarihi belirlenir.

## Kaynak hijyeni
VERBİS eşikleri, idari para cezası tutarları ve standart sözleşme metinleri her yıl/güncellemeyle değişir; bunları ezberden değil kvkk.gov.tr üzerinden teyit et ve raporda `[doğrulanacak — kvkk.gov.tr]` olarak işaretle. Kurul ilke kararı ve rehberlerine (Teknik-İdari Tedbirler, İyi Uygulama rehberleri) atıf yaparken tarih/sayıyı doğrula; uydurma karar numarası yazma. İdari yaptırıma karşı dava içtihadı için karararama.danistay.gov.tr ve idare/bölge idare mahkemesi kararları, cezai boyut için karararama.yargitay.gov.tr, anayasal boyut için kararlarbilgibankasi.anayasa.gov.tr kullanılır. Mevzuat metnini mevzuat.gov.tr'den, 7499 sonrası m.6/m.9 değişikliklerini mutlaka güncel metinle doğrula.
<<<BECERI>>>
slug: denetim-kapsami-ve-yontem
ad: Denetim Kapsamı ve Yöntem Belirleme
aciklama: Bir KVKK uyum taraması başlatılırken kapsamın, denetlenecek birim ve sistemlerin, rol tespitinin ve denetim yönteminin sabitlenmesi gerektiğinde kullanılır.
<<<GOVDE>>>
# Denetim Kapsamı ve Yöntem Belirleme

## Görev
KVKK uyum taramasının iskeletini kurmak: neyin, hangi rol bakımından, hangi kanıtlarla ve hangi skorlama mantığıyla denetleneceğini yazılı olarak sabitlemek. Kapsamı tanımlanmamış denetim, bulgu üretmez.

## Soğuk başlangıç (intake)
1. Denetlenen kuruluşun sektörü, çalışan sayısı ve işlediği başlıca veri kategorileri nedir?
2. Tarama tüm kuruluşu mu, yoksa belirli birim/süreçleri (İK, pazarlama, müşteri hizmetleri) mi kapsıyor?
3. Kuruluş bu süreçlerde veri sorumlusu mu, veri işleyen mi?
4. Daha önce denetim yapıldı mı, açık bulgu var mı, hangi belgeler hazır?

## Denetim şeması
1. **Rol tespiti (KVKK m.3)**: Kapsamdaki her faaliyet için veri sorumlusu/veri işleyen sıfatı belirlenir; yükümlülükler asıl olarak sorumluya düşer, işleyene m.12 sözleşmesiyle aktarılan kısımlar ayrı izlenir.
2. **Kapsam matrisi**: Birim × süreç × sistem (CRM, İK yazılımı, web sitesi, çağrı merkezi, bulut/SaaS) tablosu çıkarılır; her hücre denetim kalemine dönüşür.
3. **Kanıt kuralı**: Her kontrol maddesi için beyan değil belge istenir (politika, ekran görüntüsü, log, sözleşme). Belge yoksa bulgu "Uygunsuz" kabul edilir; hesap verebilirlik ispat yükü veri sorumlusundadır (m.4 — accountability).
4. **Skorlama tanımı**: Her madde "Uygun / Kısmen / Uygunsuz / Kapsam dışı"; risk = olasılık × etki (yaptırım m.18 + itibar + ilgili kişi zararı).
5. **Ara sonuç**: Kapsam, rol ve skorlama mantığı yazıya dökülmeden kanıt toplamaya geçilmez; aksi halde bulgular karşılaştırılamaz.

İspat yükü: Uyumu belgelerle ispat yükümlülüğü veri sorumlusundadır; denetçi yokluk halinde uygunsuzluk lehine karine kurar.

## Çıktı modülleri
- Denetim kapsam ve rol tanımı belgesi.
- Birim/süreç/sistem kapsam matrisi.
- Skorlama ve kanıt kuralı tanım sayfası.
<<<BECERI>>>
slug: veri-envanteri-cikarma
ad: Kişisel Veri İşleme Envanteri Çıkarma
aciklama: Kuruluşun hangi veriyi hangi amaç ve hukuki sebeple işlediğinin haritalanması, mevcut envanterin doğrulanması veya sıfırdan envanter oluşturulması gerektiğinde kullanılır.
<<<GOVDE>>>
# Kişisel Veri İşleme Envanteri Çıkarma

## Görev
Tüm uyum mimarisinin temel taşı olan kişisel veri işleme envanterini çıkarmak veya mevcut envanteri fiili işleme ile karşılaştırarak doğrulamak. Diğer her belge (aydınlatma, VERBİS, saklama matrisi) envanterle tutarlı olmak zorundadır.

## Soğuk başlangıç (intake)
1. Hangi süreçlerde kişisel veri toplanıyor (işe alım, satış, üyelik, ziyaretçi kaydı, kamera)?
2. Her süreçte hangi veri kategorileri işleniyor; özel nitelikli veri (m.6) var mı?
3. Veri kimlerden alınıyor, kime aktarılıyor, nerede saklanıyor (yurt içi/yurt dışı, bulut)?
4. Mevcut bir envanter var mı, ne zaman güncellendi?

## Denetim şeması
1. **Faaliyet bazlı kayıt**: Her işleme faaliyeti için satır açılır — faaliyet adı, veri konusu kişi grubu, veri kategorileri, işleme amacı.
2. **Hukuki sebep haritalama (m.5/m.6)**: Her faaliyet için geçerli işleme şartı yazılır; açık rıza dışı sebepler önce denenir, açık rızaya gereksiz bağımlılık "kırmızı bayrak" olarak işaretlenir.
3. **Aktarım ve saklama sütunları**: Alıcı/alıcı grupları, yurt içi/yurt dışı aktarım, aktarım mekanizması (m.8-9), azami saklama süresi (m.4/2-d dayanağıyla).
4. **Özel nitelikli ve hassas alanlar**: m.6 verisi, çocuk verisi, biyometrik/kamera kayıtları ayrı işaretlenir; bunlar yüksek risk grubudur.
5. **Tutarlılık çapraz kontrolü**: Envanter, VERBİS kaydı ve aydınlatma metinleriyle satır satır karşılaştırılır; uyumsuzluklar bulgu listesine geçer.
6. **Ara sonuç**: Eksik/çelişkili envanter, m.4 ilke ihlallerinin ve VERBİS hatalarının kaynağıdır; envanter "yaşayan" belge olarak güncelleme döngüsüne bağlanır.

İspat yükü: İşlemenin geçerli şarta dayandığını ve envanterin gerçeği yansıttığını veri sorumlusu gösterir.

## Çıktı modülleri
- Faaliyet bazlı işleme envanteri tablosu (Excel'lenebilir).
- Hukuki sebep–faaliyet eşleştirme ve "açık rıza bağımlılığı" uyarı listesi.
- Envanter–VERBİS–aydınlatma tutarlılık çapraz kontrol raporu.
<<<BECERI>>>
slug: aydinlatma-acik-riza-denetimi
ad: Aydınlatma ve Açık Rıza Metni Denetimi
aciklama: Mevcut aydınlatma metinlerinin ve açık rıza beyanlarının m.10, Aydınlatma Tebliği ve Rıza Tebliği'ne uygunluğu denetlenirken ya da bu metinler taslaklanırken kullanılır.
<<<GOVDE>>>
# Aydınlatma ve Açık Rıza Metni Denetimi

## Görev
Kuruluşun aydınlatma metinlerini ve açık rıza beyanlarını madde madde denetlemek; zorunlu unsur, zamanlama ve ikisinin birbirinden ayrı tutulması kurallarına uygunluğu test edip eksikleri bulgu listesine bağlamak.

## Soğuk başlangıç (intake)
1. Hangi kanallarda aydınlatma yapılıyor (web formu, işe alım, sözleşme, çağrı merkezi, kamera tabelası)?
2. Her kanal için ayrı metin var mı, yoksa tek genel metin mi kullanılıyor?
3. Açık rıza alınıyor mu; alınıyorsa aydınlatmadan ayrı bir onay olarak mı?
4. Rızanın geri alınması için bir mekanizma var mı?

## Denetim şeması
1. **Zorunlu unsur testi (m.10/1)**: Her metinde (a) veri sorumlusu/temsilci kimliği, (b) işleme amaçları, (c) aktarılan alıcı grupları ve amacı, (ç) toplama yöntemi ve hukuki sebebi, (d) m.11 hakları bulunmalı. "vb.", "gerektiğinde" gibi muğlak ifadeler eksiklik sayılır (Aydınlatma Tebliği).
2. **Zamanlama**: Aydınlatma, verinin elde edildiği anda yapılmalı; sonradan yapılan aydınlatma ihlaldir.
3. **Ayrılık ilkesi**: Aydınlatma ile açık rıza tek metinde/tek onay kutusunda birleştirilemez; aydınlatma rıza şartına bağlanamaz. Birleşik kullanım kırmızı bulgudur.
4. **Açık rızanın geçerliliği (m.3/1-a)**: Rıza özgür irade + belirli konu + bilgilendirme unsurlarını taşımalı; ön işaretli kutu, hizmet şartına bağlı rıza ("rıza vermezsen hizmet yok") geçersizdir.
5. **Hukuki sebebin doğru gösterimi**: Metinde her amaç için m.5/m.6 sebebi açık rıza ile karıştırılmadan gösterilmeli.
6. **Ara sonuç**: Eksik/geç aydınlatma m.18/1-a yaptırım riski; geçersiz rıza ise işlemenin tümünü hukuka aykırı kılar.

İspat yükü: Aydınlatmanın usulüne uygun yapıldığını ve rızanın geçerli alındığını veri sorumlusu kayıt/onay loguyla ispatlar.

## Çıktı modülleri
- Metin başına m.10 unsur kontrol listesi (Uygun/Eksik).
- Aydınlatma–açık rıza ayrımı uygunsuzluk raporu.
- Kanal bazlı düzeltilmiş aydınlatma/rıza taslakları ([doldurulacak] yer tutucularıyla).
<<<BECERI>>>
slug: saklama-imha-denetimi
ad: Saklama ve İmha Politikası Denetimi
aciklama: Saklama sürelerinin mevzuat dayanağına uygunluğu, imha yöntemleri ve periyodik imha düzeni denetlenirken ya da saklama-imha politikası ve süre matrisi kurulurken kullanılır.
<<<GOVDE>>>
# Saklama ve İmha Politikası Denetimi

## Görev
KVKK m.4 (süreyle sınırlılık), m.7 (silme/yok etme/anonim hale getirme) ve İmha Yönetmeliği uyarınca saklama sürelerini, imha yöntemlerini ve periyodik imha düzenini denetlemek; süre matrisini mevzuat dayanağına oturtmak.

## Soğuk başlangıç (intake)
1. Veri kategorisi başına saklama süreleri belirlenmiş mi; dayanağı hangi kanun?
2. Saklama ve İmha Politikası var mı (VERBİS'e kayıtlılar için zorunlu)?
3. İmha hangi ortamlarda, hangi yöntemle yapılıyor (fiziksel, elektronik, bulut)?
4. Periyodik imha tutanağı ve logları tutuluyor mu?

## Denetim şeması
1. **Süre dayanağı testi (m.4/2-d)**: Her kategori için süre, kanuni saklama yükümlülüğü (örn. TTK m.82 ticari defterler, VUK saklama süreleri, iş hukuku zamanaşımları) ve amaç gereği ihtiyaç birlikte değerlendirilerek belirlenmeli; "ihtiyaten süresiz saklama" m.4 ihlalidir.
2. **İmha yükümlülüğünün doğması (m.7)**: İşleme sebebi sona erdiğinde veri re'sen veya talep üzerine silinir/yok edilir/anonim hale getirilir; üç yöntem ortam ve amaca göre seçilir.
3. **Periyodik imha**: İmha Yönetmeliği uyarınca politika sahibi sorumlu, periyodik imhayı azami 6 ayda bir yapar; işlemler kayıt altına alınır ve bu kayıtlar en az 3 yıl saklanır.
4. **Anonimleştirme kontrolü**: Geri döndürülebilen "anonimleştirme" hâlâ kişisel veridir ve KVKK kapsamındadır; tersine mühendislik testi yapılmalı.
5. **Ara sonuç**: Amaç bittiği halde saklamaya devam, hem m.4 ihlali hem TCK m.138 (verileri yok etmeme) riskidir; politika fiili imha kayıtlarıyla uyumlu olmalı.

İspat yükü: İmhanın usulüne uygun yapıldığını veri sorumlusu imha tutanağı ve loglarıyla ispatlar.

## Çıktı modülleri
- Veri kategorisi bazlı saklama süresi matrisi (mevzuat dayanağıyla).
- Saklama ve İmha Politikası uygunluk bulgu listesi.
- Periyodik imha tutanağı ve log şablonu.
<<<BECERI>>>
slug: aktarim-ve-verbis-denetimi
ad: Aktarım ve VERBİS Kayıt Denetimi
aciklama: Yurt içi/yurt dışı veri aktarım mekanizmalarının (7499 sonrası m.9) ve VERBİS kayıt yükümlülüğü ile kayıt içeriğinin doğruluğu denetlenirken kullanılır.
<<<GOVDE>>>
# Aktarım ve VERBİS Kayıt Denetimi

## Görev
İki sık ihlal başlığını birlikte denetlemek: (1) yurt içi (m.8) ve 7499 ile yeniden kurgulanan yurt dışı (m.9) aktarımların doğru mekanizmaya dayanıp dayanmadığı; (2) VERBİS (m.16) kayıt yükümlülüğü ve kaydın envanterle tutarlılığı.

## Soğuk başlangıç (intake)
1. Veri kimlere aktarılıyor — yurt içi üçüncü kişi, yurt dışı alıcı, bulut/SaaS sağlayıcı?
2. Yurt dışı alıcının bulunduğu ülke Kurul'un yeterlilik kararı verdiği bir ülke mi?
3. Aktarım sürekli mi, arızi mi; mevcut bir aktarım sözleşmesi var mı?
4. Kuruluşun VERBİS kaydı var mı, güncel mi; istisna iddiası belgeli mi?

## Denetim şeması
1. **Yurt içi aktarım (m.8)**: Aktarım da işlemedir; m.5/m.6 şartına ve m.4 ilkelerine dayanmalı. Veri işleyene aktarımda m.12 sözleşmesi şart; eksikse bulgu.
2. **Yurt dışı hiyerarşisi (m.9, 7499 sonrası)**: Önce yeterlilik kararı (m.9/1); yoksa uygun güvenceler (m.9/3 — uluslararası anlaşma, Kurul onaylı bağlayıcı şirket kuralları, Kurul'un ilan ettiği standart sözleşme [imzadan itibaren 5 iş günü içinde Kurul'a bildirim], izinli taahhütname); bunlar yoksa yalnızca arızi haller (m.9/6). Sürekli aktarımda arızi haller mekanizması kullanılamaz — bu yaygın bir hatadır.
3. **VERBİS yükümlülük testi (m.16)**: İşlemeye başlamadan önce kayıt esastır. İstisna eşikleri (çalışan sayısı/yıllık mali bilanço, ana faaliyetin özel nitelikli veri işleme olmaması) Kurul kararıyla belirlenir [güncel eşikler doğrulanacak — kvkk.gov.tr]; yurt dışında yerleşik sorumlu için eşik aranmaz.
4. **Kayıt içeriği tutarlılığı**: VERBİS'teki amaç, veri kategorisi, alıcı grupları, aktarım ve saklama süreleri envanterle birebir karşılaştırılır; sapma bulgudur.
5. **Ara sonuç**: Yanlış aktarım mekanizması ve eksik/tutarsız VERBİS kaydı m.18 yaptırım sebebidir.

İspat yükü: Aktarım güvencelerinin ve VERBİS istisnasının varlığını (çalışan/bilanço belgeleriyle) veri sorumlusu ispatlar.

## Çıktı modülleri
- Aktarım envanteri (alıcı, ülke, mekanizma, dayanak, bildirim durumu).
- Yurt dışı aktarım karar akış şeması (yeterlilik → güvence → arızi hal).
- VERBİS–envanter tutarlılık raporu ve istisna değerlendirme notu.
<<<BECERI>>>
slug: veri-guvenligi-tedbir-denetimi
ad: Veri Güvenliği ve Teknik-İdari Tedbir Denetimi
aciklama: KVKK m.12 kapsamında teknik ve idari güvenlik tedbirlerinin Kurul rehberine göre denetlenmesi veya tedbir boşluklarının tespiti gerektiğinde kullanılır.
<<<GOVDE>>>
# Veri Güvenliği ve Teknik-İdari Tedbir Denetimi

## Görev
KVKK m.12/1 uyarınca veri sorumlusunun aldığı teknik ve idari tedbirleri Kurul'un Teknik ve İdari Tedbirler Rehberi ölçütünde denetlemek; boşlukları risk seviyesine göre işaretlemek. Bu beceri hukuki uyumu güvenlik kontrolleriyle köprüler.

## Soğuk başlangıç (intake)
1. Verilere kimler erişiyor; yetki ve erişim kontrolü (rol bazlı) tanımlı mı?
2. Veriler şifreleniyor mu (durağan/iletimde); yedekleme ve loglama var mı?
3. Çalışanlarla gizlilik taahhüdü ve KVKK farkındalık eğitimi yapılıyor mu?
4. Veri işleyenlerle (bulut, dış hizmet) m.12 sözleşmesi ve güvenlik denetimi var mı?

## Denetim şeması
1. **İdari tedbirler**: Kişisel veri envanteri, kurumsal politikalar, gizlilik taahhütleri, erişim yetki matrisi, eğitim ve farkındalık programı, veri işleyenlerle m.12 sözleşmeleri ve denetim hakkı. Her biri "var/eksik" işaretlenir.
2. **Teknik tedbirler**: Yetkilendirme ve kimlik doğrulama, ağ güvenliği, şifreleme, log tutma, sızma testi/zafiyet taraması, yedekleme, anti-virüs/güvenlik duvarı, silme/yok etme altyapısı. Özel nitelikli veride (m.6) Kurul ek tedbir bekler (örn. şifreleme ve daha sıkı erişim kontrolü).
3. **Veri işleyen zinciri**: Bulut/SaaS ve dış hizmet sağlayıcılarla yazılı m.12 sözleşmesi, sorumluluk paylaşımı ve denetim yetkisi kontrol edilir; sözleşmesiz işleyen yüksek risk bulgusudur.
4. **Orantılılık**: Tedbirler verinin niteliği ve riskiyle orantılı olmalı; eksik tedbir, ihlal halinde m.18 ve tazminat sorumluluğunu ağırlaştırır.
5. **Ara sonuç**: Güvenlik tedbiri eksikliği yalnızca ihlal anında değil, denetimde de m.12 ihlali olarak skorlanır.

İspat yükü: Uygun tedbirlerin alındığını veri sorumlusu belge ve kayıtla ispatlar; tedbirlerin yokluğu ihlalde kusur karinesini güçlendirir.

## Çıktı modülleri
- Teknik/idari tedbir kontrol listesi (Rehber kalemleriyle eşleşen, Uygun/Eksik).
- Veri işleyen sözleşme ve güvenlik denetim durum tablosu.
- Tedbir boşluğu risk haritası ve öncelikli aksiyon listesi.
<<<BECERI>>>
slug: veri-ihlali-mudahale-hazirligi
ad: Veri İhlali Müdahale Hazırlığı Denetimi
aciklama: Kuruluşun veri ihlali müdahale planının varlığı ve yeterliliği denetlenirken, 72 saatlik Kurul bildirim ve ilgili kişi bilgilendirme süreçleri test edilirken kullanılır.
<<<GOVDE>>>
# Veri İhlali Müdahale Hazırlığı Denetimi

## Görev
KVKK m.12/5 kapsamında kuruluşun veri ihlaline hazırlığını denetlemek: müdahale planı, ekip ve roller, 72 saatlik Kurul bildirim akışı ve ilgili kişi bilgilendirme mekanizması mevcut ve işler mi? Bu beceri olay anına değil, olaya hazırlığa odaklanır.

## Soğuk başlangıç (intake)
1. Yazılı bir veri ihlali müdahale planı var mı; ekip ve roller (kim karar verir, kim bildirir) tanımlı mı?
2. İhlali tespit eden çalışanın bildirim yapacağı iç kanal belli mi?
3. Daha önce yaşanan ihlal var mı; nasıl yönetildi, kayıt tutuldu mu?
4. 72 saatlik süreyi takip edecek bir mekanizma/şablon hazır mı?

## Denetim şeması
1. **Plan varlığı (m.12)**: Yazılı müdahale planı, eskalasyon zinciri ve karar matrisi olmalı. Plan yoksa veya güncel değilse yüksek risk bulgusu.
2. **Tespit→bildirim akışı**: İhlalin öğrenildiği an süreyi başlatır. Kurul'a bildirim en kısa sürede ve en geç 72 saat içinde, Kurul'un belirlediği form üzerinden yapılır; 72 saat aşılırsa gecikme gerekçesi açıklanmalı. Bu akışın test edilebilir (tatbikatlı) olması beklenir.
3. **İlgili kişi bilgilendirme**: Etkilenen kişiler makul en kısa sürede bilgilendirilir; bilgilendirme metni şablonu hazır olmalı.
4. **Bildirim içeriği**: İhlalin niteliği, etkilenen veri kategorileri ve kişi sayısı, olası sonuçlar, alınan/önerilen tedbirler ve irtibat bilgisi. Eksik içerik ayrı yükümlülük ihlalidir.
5. **Kanıt zinciri**: Loglar ve müdahale kayıtlarının korunacağı düzen kurulmalı; bu kayıtlar hem yaptırım hem tazminat davasında belirleyicidir.
6. **Ara sonuç**: Hazırlıksızlık, ihlal anında 72 saatin aşılmasına ve m.18 ek yaptırımına yol açar.

İspat yükü: Bildirimin süresinde ve usulüne uygun yapıldığını/yapılacağını veri sorumlusu plan ve kayıtlarla ispatlar.

## Çıktı modülleri
- Veri ihlali müdahale planı uygunluk kontrol listesi.
- 72 saat takip cetveli ve Kurul bildirim formu taslağı ([doldurulacak]).
- İlgili kişi bilgilendirme metni şablonu ve eskalasyon karar matrisi.
<<<BECERI>>>
slug: ilgili-kisi-basvuru-sureci-denetimi
ad: İlgili Kişi Başvuru Süreci Denetimi
aciklama: Kuruluşun ilgili kişi başvurularını karşılama prosedürünün m.13 ve Başvuru Tebliği'ne uygunluğu, 30 günlük yanıt süresine riayet ve şikâyete geçiş riski denetlenirken kullanılır.
<<<GOVDE>>>
# İlgili Kişi Başvuru Süreci Denetimi

## Görev
Kuruluşun m.11 haklarına dayanan başvuruları nasıl karşıladığını denetlemek: başvuru kanalları, kimlik doğrulama, 30 günlük yanıt süresi, gerekçeli ret usulü ve Kurul'a şikâyete geçişin önlenmesi açısından sürecin sağlamlığını ölçmek.

## Soğuk başlangıç (intake)
1. İlgili kişi başvurusu için ilan edilmiş bir kanal/form var mı (web, KEP, yazılı)?
2. Gelen başvuruyu kim alıyor, kim yanıtlıyor; sorumlu birim belli mi?
3. Başvuru–yanıt süreleri kayıt altında mı; geçmişte süre aşımı yaşandı mı?
4. Ret kararları gerekçelendiriliyor mu?

## Denetim şeması
1. **Kanal ve usul (m.13, Başvuru Tebliği)**: Başvuru yazılı veya Kurul'un belirlediği yöntemlerle (KEP, güvenli elektronik imza, kayıtlı e-posta vb.) yapılır; kuruluş bu kanalları ilan etmiş ve işler tutmuş olmalı.
2. **Kimlik doğrulama**: Başvuranın ilgili kişi olduğunun doğrulanması gerekir; aşırı bilgi talebi ise ölçülülük ihlali olur — denge denetlenir.
3. **Yanıt süresi**: Talep en kısa sürede ve en geç 30 gün içinde sonuçlandırılır. İşlemin maliyeti varsa Kurul tarifesi uygulanır; süre aşımı doğrudan şikâyet ve yaptırım riskidir.
4. **Gerekçeli ret**: Ret kararı gerekçesiz olamaz; m.11 haklarından hangisinin neden reddedildiği açıklanmalı.
5. **Şikâyete geçiş (m.14)**: Ret, eksik yanıt veya 30 günde yanıtsızlık halinde ilgili kişi, öğrenmeden itibaren 30 ve her hâlde başvurudan itibaren 60 gün içinde Kurul'a şikâyet edebilir. Veri sorumlusuna başvuru, şikâyet için zorunlu ön şarttır.
6. **Ara sonuç**: Süresinde, gerekçeli ve kayıtlı yanıt, hem şikâyeti hem yaptırımı önler.

İspat yükü: Başvurunun süresinde ve gereği gibi yanıtlandığını veri sorumlusu yanıt kayıtlarıyla ispatlar.

## Çıktı modülleri
- Başvuru süreci uygunluk kontrol listesi ve süre takip cetveli.
- Standart başvuru formu ve gerekçeli yanıt (kabul/ret) şablonları.
- Süre aşımı/şikâyet riski uyarı raporu.
<<<BECERI>>>
slug: cerez-pazarlama-uyumu
ad: Çerez ve Pazarlama Uyumu Denetimi
aciklama: Web sitesi çerezleri, çerez aydınlatması ve ticari elektronik ileti (İYS) süreçlerinin KVKK ve ilgili mevzuata uygunluğu denetlenirken kullanılır.
<<<GOVDE>>>
# Çerez ve Pazarlama Uyumu Denetimi

## Görev
İki yüksek görünürlüklü uyum alanını denetlemek: (1) web sitesi/uygulama çerezlerinin ve çerez aydınlatmasının KVKK m.5/m.10 ve Kurul Çerez Rehberi'ne uygunluğu; (2) ticari elektronik ileti gönderiminin 6563 sayılı Kanun ve İYS (İleti Yönetim Sistemi) düzeninde olup olmadığı.

## Soğuk başlangıç (intake)
1. Sitede hangi çerezler var (zorunlu, analitik, pazarlama, üçüncü taraf)?
2. Çerez aydınlatma/rıza arayüzü var mı; ön işaretli kutu veya "kabul et" zorlaması var mı?
3. Pazarlama iletisi (SMS, e-posta, arama) gönderiliyor mu; alıcı onayı nasıl alındı?
4. İYS kaydı ve onay yönetimi yapılıyor mu?

## Denetim şeması
1. **Çerez tasnifi**: Zorunlu (işlevsel) çerezler için rıza aranmaz; analitik ve pazarlama/üçüncü taraf çerezler için açık rıza ve aydınlatma gerekir (Kurul Çerez Rehberi). Tüm çerezleri tek "kabul" altında toplayan banner kırmızı bulgudur.
2. **Rıza geçerliliği (m.3/1-a)**: Çerez rızası özgür, belirli ve bilgilendirilmiş olmalı; ön işaretli kutu, "kabul etmeden devam edemezsin" (cookie wall) ve reddi zorlaştıran tasarım geçersizdir.
3. **Aydınlatma (m.10)**: Çerez politikası; çerez türü, amacı, süresi, üçüncü taraf alıcıları ve hakların kullanımını içermeli.
4. **Ticari elektronik ileti (6563)**: İleti için önceden onay esastır (esnaf/tacir istisnaları ve mevcut müşteri sınırlı istisnası ayrı değerlendirilir); her iletide kolay ret (opt-out) imkânı bulunmalı.
5. **İYS kontrolü**: Onaylar İYS'ye yüklenmeli ve ret talepleri İYS üzerinden işlenmeli; İYS dışı gönderim yaptırım riskidir.
6. **Ara sonuç**: Çerez ihlali KVKK m.18, ileti ihlali 6563 idari para cezası kapsamındadır; iki rejim paralel işler.

İspat yükü: Çerez rızasının ve ileti onayının geçerli alındığını veri sorumlusu/gönderen kayıt ve İYS verisiyle ispatlar.

## Çıktı modülleri
- Çerez envanteri ve tasnif tablosu (zorunlu/rızaya tabi).
- Çerez banner ve politika uygunluk bulgu listesi.
- İYS onay/ret yönetimi ve ticari ileti uygunluk raporu.
<<<BECERI>>>
slug: uyum-boslugu-raporu-eylem-plani
ad: Uyum Boşluğu Raporu ve Eylem Planı
aciklama: Tüm denetim bulgularının tek raporda birleştirilmesi, risk önceliklendirmesi ve sorumlu-termin atanmış düzeltici eylem planı çıkarılması gerektiğinde kullanılır.
<<<GOVDE>>>
# Uyum Boşluğu Raporu ve Eylem Planı

## Görev
Önceki becerilerin bulgularını tek bir uyum boşluğu (gap analysis) raporunda birleştirmek; her bulguyu risk seviyesine göre önceliklendirip sorumlu ve termin atanmış düzeltici eylem planına bağlamak. Bu, denetimin nihai teslim çıktısıdır.

## Soğuk başlangıç (intake)
1. Hangi başlıklarda denetim tamamlandı (envanter, aydınlatma, aktarım/VERBİS, güvenlik, ihlal, başvuru, çerez)?
2. Yönetimin risk iştahı ve düzeltme için kaynağı/önceliği nedir?
3. Yasal/ticari olarak hangi bulgular acil (yaptırım riski yüksek)?
4. Yeniden denetim ne zaman planlanacak?

## Denetim şeması
1. **Bulgu konsolidasyonu**: Her başlıktan gelen bulgular tek tabloda toplanır — bulgu, ilgili madde (m.4/5/6/7/9/10/12/13/16), kanıt durumu, mevcut durum (Uygun/Kısmen/Uygunsuz).
2. **Risk skorlama (m.18 ağırlıklı)**: Her bulguya olasılık × etki verilir; etki = idari para cezası riski (m.18) + ilgili kişi zararı/tazminat + itibar. Yüksek/orta/düşük olarak sınıflanır. Özel nitelikli veri (m.6), yurt dışı aktarım ve güvenlik bulguları kural olarak yüksek başlar.
3. **Önceliklendirme**: "Hızlı kazanım" (düşük efor-yüksek etki) ile "yapısal" (yüksek efor) bulgular ayrılır; aydınlatma/başvuru gibi belge düzeltmeleri çoğunlukla hızlı kazanımdır.
4. **Eylem planı**: Her bulguya düzeltici aksiyon, sorumlu kişi/birim, termin ve doğrulama yöntemi atanır.
5. **Hesap verebilirlik döngüsü (m.4)**: Plan, periyodik gözden geçirme ve yeniden denetim tarihiyle kapatılır; uyum tek seferlik değil sürekli süreçtir.
6. **Ara sonuç**: Skorlanmamış ve sorumlu atanmamış bulgu, rapor değil yalnızca gözlemdir.

İspat yükü (accountability): Veri sorumlusu, m.4 ve tüm yükümlülüklere uyumu işleyen süreç ve belgelerle ispatlayabilmelidir; rapor bu ispat altyapısının haritasıdır.

## Çıktı modülleri
- Konsolide uyum boşluğu (gap analysis) skor tablosu.
- Önceliklendirilmiş düzeltici eylem planı (bulgu–aksiyon–sorumlu–termin).
- Yönetici özeti ve yeniden denetim takvimi.
<<<SON>>>
