<<<REFERANS>>>
# Bilişim Hukuku ve Siber Güvenlik — Metodoloji Referansı

## Alanın sistematiği
Bilişim hukuku, tek bir kodda toplanmamış; ceza, idari (düzenleyici) ve özel hukuk katmanlarının kesiştiği melez bir alandır. Çalışırken üç eksen birlikte düşünülmelidir: (i) bilişim sistemlerine ve verilere yönelik fiillerin **cezai** boyutu (TCK), (ii) kişisel veri ve elektronik haberleşme alanındaki **idari/düzenleyici** yükümlülükler (KVKK, 5651, BTK), (iii) siber olaydan doğan **tazminat ve sözleşmesel** sorumluluk (TBK). Aynı somut olay (örneğin bir veri ihlali) çoğu zaman üç eksende de sonuç doğurur; bu nedenle olayı tek bir başlığa hapsetmeden çok yönlü tasnif şarttır.

## Başat normlar ve madde atıfları
- **Bilişim suçları:** TCK m.243 (bilişim sistemine girme), m.244 (sistemi engelleme, bozma, verileri yok etme/değiştirme), m.245 (banka/kredi kartlarının kötüye kullanılması), m.245/A (yasak cihaz veya programlar). Verilerle bağlantılı diğer suçlar: TCK m.135-140 (kişisel verilerin kaydedilmesi, hukuka aykırı verme/ele geçirme, yok etmeme), m.132-134 (haberleşmenin gizliliği, özel hayat). Bilişim yoluyla işlenen dolandırıcılığın nitelikli hali TCK m.158/1-f.
- **Kişisel veri ve ihlal:** 6698 sayılı KVKK m.12 (veri güvenliği yükümlülükleri), m.12/5 (ihlalin Kurula ve ilgili kişiye bildirimi), m.18 (idari para cezaları). Kurul kararları ve veri ihlali bildirim formu kvkk.gov.tr üzerinden takip edilir.
- **İnternet ortamı:** 5651 sayılı Kanun — içerik/yer/erişim sağlayıcı tanımları ve sorumluluğu, m.8 (erişimin engellenmesi), m.8/A (gecikmesinde sakınca bulunan hallerde tedbir), m.9 (içeriğin çıkarılması ve erişimin engellenmesi başvurusu), m.9/A (özel hayatın gizliliği). Trafik/yer sağlayıcı loglarının tutulması yükümlülükleri.
- **Dijital delil:** CMK m.134 (bilgisayarlarda, programlarda ve kütüklerde arama, kopyalama, elkoyma); CMK m.116-123 (arama-elkoyma genel rejimi). Adli Bilişim İncelemesi yönergeleri ve imaj alma/hash doğrulama uygulaması.
- **Diğer:** 5809 sayılı Elektronik Haberleşme Kanunu ve BTK düzenlemeleri; e-imza için 5070 sayılı Kanun; banka ve ödeme sistemleri için sektörel mevzuat (BDDK/6493).

## Çalışma yöntemi
1. **Olayı katmana ayır:** Fiil bir suç mu, bir idari yükümlülük ihlali mi, yoksa bir tazminat sorumluluğu mu doğuruyor? Çoğu zaman üçü birden.
2. **Yer/zaman/sistem tespiti:** Olayın işlendiği sistem, etkilenen veri, zaman damgaları ve loglar belirlenir; delil bütünlüğü en başta korunur.
3. **Norm altına yerleştirme (altlama):** Her fiil için tip unsurlarını (TCK), yükümlülük şartlarını (KVKK m.12, 5651) ve sorumluluk unsurlarını (TBK m.49 vd.) ayrı ayrı denetle.
4. **Yetki/görev haritası:** Cezada Cumhuriyet savcılığı/asliye ceza-ağır ceza; KVKK'da idare ve idari yargı; tazminatta asliye hukuk/tüketici/ticaret; 5651 tedbirlerinde sulh ceza hâkimliği.
5. **Strateji ve süre:** Bildirim süreleri (KVKK ihlal bildirimi), şikâyet süreleri, zamanaşımı ve delil kaybı riskleri en baştan takvimlenir.

## Kaynak hijyeni
Mevzuat daima madde/fıkra/bent ile verilir; KVKK Kurul kararları karar tarih ve sayısıyla, içtihat ise mahkeme + daire + esas/karar no + tarih ile doğrulanır. İçtihat doğrulaması için karararama.yargitay.gov.tr, idari uyuşmazlıklar için karararama.danistay.gov.tr, anayasal şikâyet için kararlarbilgibankasi.anayasa.gov.tr kullanılır. Karar numarası hatırdan yazılmaz; doğrulanmamış künye `[doğrulanacak]` olarak işaretlenir. Teknik standartlar (TS ISO/IEC 27001, adli bilişim kılavuzları) kaynağıyla anılır.
<<<BECERI>>>
slug: temel-kavramlar-ve-sistem
ad: Bilişim Hukukunun Temel Kavramları ve Sistematiği
aciklama: Bilişim/siber bir olayın hangi hukuk katmanlarına (ceza, KVKK, 5651, tazminat) dokunduğunu çözmek, kavramları yerli yerine oturtmak ve doğru başlığa yönlendirmek gerektiğinde kullanılır.
<<<GOVDE>>>
# Bilişim Hukukunun Temel Kavramları ve Sistematiği

## Görev
Bilişim/siber bir vakıayı doğru hukuki katmanlara ayırmak; bilişim sistemi, veri, içerik/yer/erişim sağlayıcı, dijital delil gibi temel kavramları tanımlayıp olayı isabetli alt-becerilere yönlendirmek.

## Soğuk başlangıç (intake)
1. Olay ne? (yetkisiz erişim, veri sızıntısı, dolandırıcılık, içerik ihlali, sistem kesintisi?)
2. Etkilenen ne? (bilişim sistemi mi, kişisel veri mi, banka/kart verisi mi, itibar/içerik mi?)
3. Taraf kim? (mağdur birey, kurum/veri sorumlusu, hizmet sağlayıcı, şüpheli?)
4. Beklenti? (şikâyet/ceza, uyum/idari savunma, tazminat, içerik kaldırma?)

## Denetim şeması
1. **Katman tespiti.** Olayı üç eksende sorgula: cezai (TCK m.243-245, m.135-140, m.158/1-f), idari/düzenleyici (KVKK m.12; 5651 m.8-9; BTK), özel hukuk (TBK m.49 vd. haksız fiil; sözleşmesel sorumluluk). Bir olay birden çok eksende sonuç doğurabilir.
2. **Bilişim sistemi kavramı.** TCK uygulamasında bilişim sistemi, verileri toplayıp işleyen manyetik/elektronik her türlü sistemdir; cep telefonu, sunucu, bulut hesabı dahil. Fiilin bir bilişim sistemi üzerinde gerçekleşip gerçekleşmediği tipikliğin ön şartıdır.
3. **Veri ayrımı.** Kişisel veri (KVKK/TCK m.135-140) ile sistem verisi (TCK m.244) ayrılır; banka/kredi kartı verisi için özel norm TCK m.245 önceliklidir.
4. **Sağlayıcı kavramı.** 5651 kapsamında içerik, yer, erişim ve toplu kullanım sağlayıcı ayrımı sorumluluk rejimini belirler; doğru sıfat saptanmadan tedbir/sorumluluk tartışılamaz.
5. **Ara sonuç.** Hangi katmanların devrede olduğu ve hangi alt-becerinin (suçlar, ihlal müdahalesi, dijital delil, sorumluluk, içerik kaldırma) öncelikli olacağı belirlenir. İspat yükü her katmanda ayrıdır: cezada iddia makamında, idari uyumda veri sorumlusunda (KVKK m.12 tedbirlerini aldığını ispat), tazminatta zarar görende.

## Çıktı modülleri
- Katman haritası (ceza / KVKK / 5651 / tazminat) ve öncelik sırası.
- Kavram tablosu: etkilenen sistem, veri türü, taraf sıfatları.
- Yönlendirme notu: hangi alt-beceriyle devam edileceği ve ilk aksiyonlar.
<<<BECERI>>>
slug: bilisim-suclari-tck-243-245
ad: Bilişim Suçları (TCK 243-245)
aciklama: Yetkisiz erişim, sistemi engelleme/bozma, veri yok etme/değiştirme veya banka-kredi kartı kötüye kullanımı gibi bir bilişim suçunun unsurlarını ve nitelikli hallerini denetlemek, şikâyet/savunma stratejisi kurmak gerektiğinde kullanılır.
<<<GOVDE>>>
# Bilişim Suçları (TCK 243-245)

## Görev
Somut fiili TCK'nın bilişim alanındaki suç tipleriyle altlamak; unsurları, nitelikli halleri, içtimaı ve şikâyet/dava stratejisini belirlemek.

## Soğuk başlangıç (intake)
1. Fiil tam olarak ne? (sisteme girme, kalma, engelleme, veri silme/değiştirme, kart kullanımı?)
2. Yetki var mıydı? (rıza, erişim hakkı, görev sınırı aşıldı mı?)
3. Bir zarar/menfaat doğdu mu? (haksız çıkar, sistemde bozulma, veri kaybı?)
4. Mağdur/şüpheli ve elimizdeki deliller neler?

## Denetim şeması
1. **TCK m.243 — sisteme hukuka aykırı girme.** Bir bilişim sisteminin bütününe veya bir kısmına hukuka aykırı olarak girmek ya da orada kalmaya devam etmek. Temel suç için sistem içindeki verileri ele geçirmek/zarar vermek şart değildir; m.243/2 bedeli karşılığı yararlanılan sistemlerde indirim, m.243/3 verilerin yok olması/değişmesi halinde ağırlaştırma, m.243/4 sistem içeriği bedelsiz yararlanılabilen sistemler için özel hüküm öngörür.
2. **TCK m.244 — engelleme, bozma, verileri yok etme/değiştirme.** Sistemin işleyişini engelleme/bozma (f.1) ile verileri bozma, yok etme, değiştirme, erişilmez kılma, sisteme veri yerleştirme veya var olanı başka yere gönderme (f.2). Banka, kredi kurumu veya kamu kurumu aleyhine işlenmesi ağırlaştırıcıdır (f.3). Fiil başka suç oluşturmuyorsa bu maddeler uygulanır (tali norm karakteri).
3. **TCK m.245 — banka/kredi kartının kötüye kullanılması.** Başkasına ait kartı ele geçirip/elde bulundurup kullanma (f.1), sahte kart üretme/satma/kabul etme (f.2), sahte kartla yarar sağlama (f.3). m.245/A yasak cihaz/program bulundurma. Etkin pişmanlık ve şikâyete bağlılık halleri (akrabalar arası) gözetilir.
4. **İspat ve içtima.** Kast aranır; taksirle işlenemez. Aynı fiil dolandırıcılık (m.158/1-f) veya kişisel verilere ilişkin suçları (m.135-140) da oluşturabilir; gerçek/görünüşte içtima ayrımı yapılır. İspat yükü iddia makamındadır; failin kimliği IP, log ve adli bilişim raporuyla bağlanır.
5. **Ara sonuç.** Hangi madde(ler), nitelikli hal, içtima ilişkisi ve soruşturma/savunma ekseni netleştirilir.

## Çıktı modülleri
- Suç vasfı analizi (madde-fıkra, unsur tablosu, nitelikli haller).
- Şikâyet dilekçesi / savunma iskeleti.
- Delil-fiil bağlama notu ve içtima değerlendirmesi.
<<<BECERI>>>
slug: veri-ihlali-siber-olay-mudahale
ad: Veri İhlali ve Siber Olay Müdahalesi
aciklama: Yaşanan bir veri ihlali veya siber saldırı sonrası KVKK m.12 bildirim yükümlülüğü, kriz yönetimi ve hukuki müdahale adımlarını planlamak; bildirim sürelerini ve içeriklerini belirlemek gerektiğinde kullanılır.
<<<GOVDE>>>
# Veri İhlali ve Siber Olay Müdahalesi

## Görev
Gerçekleşmiş veya şüpheli bir veri ihlali/siber olayda hukuki müdahale akışını kurmak; KVKK bildirim yükümlülüklerini, içeriklerini ve eş zamanlı ceza/sözleşme adımlarını yönetmek.

## Soğuk başlangıç (intake)
1. Ne oldu ve ne zaman fark edildi? (sızıntı, fidye yazılımı, yetkisiz erişim?)
2. Hangi kişisel veriler ve kaç ilgili kişi etkilendi? (özel nitelikli veri var mı?)
3. Veri sorumlusu kim, yurt dışı aktarım/işleyen zinciri var mı?
4. Sistem hâlâ tehdit altında mı, loglar/imaj korundu mu?

## Denetim şeması
1. **Kapsam ve sınıflandırma.** Olayın KVKK m.12/5 anlamında bir "veri ihlali" (kişisel verilerin kanuni olmayan yollarla başkalarınca elde edilmesi) olup olmadığı belirlenir. İhlal yoksa salt güvenlik olayı olarak iç süreç işler.
2. **Bildirim yükümlülüğü (KVKK m.12/5).** Veri sorumlusu ihlali öğrendiği tarihten itibaren en kısa sürede Kurula bildirir; Kurul kararları uyarınca bu süre kural olarak **72 saat** olarak uygulanır. İlgili kişilere de makul en kısa sürede bildirim yapılır. Form ve içerik kvkk.gov.tr'deki ihlal bildirim usulüne göre hazırlanır (ihlalin niteliği, etkilenen veri/kişi sayısı, olası sonuçlar, alınan önlemler).
3. **Delil ve sistem güvenliği.** Adli bilişim için imaj/log korunur (bkz. dijital delil becerisi); müdahale ekibinin hareketleri kayda alınır. İz silmemek esastır.
4. **Ceza ekseni.** Fiil aynı zamanda TCK m.243-244 ve m.135-140 kapsamında suç olabilir; suç duyurusu seçeneği değerlendirilir. İspat yükü: KVKK uyumunda veri sorumlusu, m.12'deki teknik/idari tedbirleri aldığını ispatla yükümlüdür; aksi halde m.18 idari para cezası riski doğar.
5. **Sözleşme ve aktarım ekseni.** Veri işleyen/alt işleyen sözleşmeleri, yurt dışı aktarım şartları ve müşteri/iş ortağı bildirim yükümlülükleri kontrol edilir. **Ara sonuç:** Bildirim takvimi, sorumlu rolleri ve risk önceliklendirmesi netleştirilir.

## Çıktı modülleri
- 72 saatlik aksiyon takvimi ve sorumlu matrisi.
- Kurul ihlal bildirim formu taslağı ve ilgili kişi bilgilendirme metni.
- Ceza/sözleşme eksenli ek aksiyon listesi.
<<<BECERI>>>
slug: dijital-delil-elde-etme-degerlendirme
ad: Dijital Delilin Elde Edilmesi ve Değerlendirilmesi
aciklama: Loglar, imajlar, e-posta, mesaj kayıtları gibi dijital delillerin hukuka uygun elde edilmesi, bütünlüğünün korunması ve mahkemede değerlendirilebilirliğini denetlemek gerektiğinde kullanılır.
<<<GOVDE>>>
# Dijital Delilin Elde Edilmesi ve Değerlendirilmesi

## Görev
Dijital delillerin hukuka uygun şekilde elde edilip edilmediğini, bütünlük zincirinin korunup korunmadığını ve yargılamada değerlendirilebilirliğini denetlemek; itiraz veya delil tespiti stratejisi kurmak.

## Soğuk başlangıç (intake)
1. Hangi dijital delil? (log, disk imajı, e-posta, WhatsApp/mesaj, ekran görüntüsü?)
2. Nasıl elde edildi? (CMK m.134 kararıyla mı, taraf rızasıyla mı, tek taraflı mı?)
3. Bütünlük korundu mu? (hash, imaj, zaman damgası, gözetim zinciri var mı?)
4. Delil kim aleyhine ve hangi yargılamada (ceza/hukuk) kullanılacak?

## Denetim şeması
1. **Elde etme yetkisi.** Ceza yargılamasında bilgisayar, program ve kütüklerde arama, kopyalama ve elkoyma CMK m.134'e tabidir: kural olarak hâkim kararı, sistemdeki verilerin yedeklenmesi ve istem halinde bir kopyasının ilgiliye verilmesi gerekir. Genel arama-elkoyma rejimi (CMK m.116-123) tamamlayıcıdır.
2. **Hukuka aykırı delil yasağı.** Hukuka aykırı elde edilen delil hükme esas alınamaz (Anayasa m.38/6; CMK m.206/2-a, m.217/2, m.230/1). Özel hayata/haberleşmeye müdahale ile elde edilen kayıtlar TCK m.132-134 kapsamında ayrıca suç oluşturabilir; bir suçun işlendiğini gösteren tesadüfen elde edilmiş kayıtların durumu ayrıca değerlendirilir.
3. **Bütünlük ve zincir.** İmaj alma, hash (özet) değeri, zaman damgası ve gözetim zinciri (chain of custody) belgelenmelidir; bütünlüğü ispatlanamayan delilin değeri tartışmalıdır. Ekran görüntüsü/mesaj çıktısı tek başına zayıf delildir, teknik doğrulama ile desteklenmelidir.
4. **Hukuk yargılamasında.** HMK uyarınca senet/belge ve diğer deliller rejimi (HMK m.199 belge tanımı elektronik verileri kapsar) ile delil tespiti (HMK m.400 vd.) yolları kullanılır. **İspat yükü** delili sunan taraftadır; karşı taraf bütünlük ve hukuka uygunluk itirazını ileri sürer.
5. **Ara sonuç.** Delilin elde edilme usulü, bütünlüğü ve değerlendirilebilirliği; itiraz veya delil tespiti talebi gerekli mi belirlenir.

## Çıktı modülleri
- Delil değerlendirme tablosu (kaynak, yetki, bütünlük, hukuka uygunluk).
- Hukuka aykırılık/itiraz dilekçesi iskeleti.
- Delil tespiti veya bilirkişi (adli bilişim) talebi taslağı.
<<<BECERI>>>
slug: 5651-icerik-erisim-engelleme
ad: 5651 İçerik Kaldırma ve Erişim Engelleme
aciklama: İnternette yer alan hukuka aykırı içeriğe karşı içeriğin çıkarılması, erişimin engellenmesi ve özel hayatın korunması başvurularını; içerik/yer/erişim sağlayıcı sorumluluğunu çözmek gerektiğinde kullanılır.
<<<GOVDE>>>
# 5651 İçerik Kaldırma ve Erişim Engelleme

## Görev
İnternet ortamındaki hukuka aykırı içeriğe karşı 5651 sayılı Kanun yollarını seçmek; doğru başvuru merciini, usulü ve süreyi belirlemek; sağlayıcı sorumluluğunu değerlendirmek.

## Soğuk başlangıç (intake)
1. İçerik ne ve nerede? (URL, platform, yayın tarihi?)
2. İhlal türü ne? (kişilik hakkı, özel hayat, hakaret, telif, katalog suç?)
3. Önce sağlayıcıya başvuruldu mu, yanıt geldi mi?
4. Acil mi (özel hayat, gecikmesinde sakınca) yoksa olağan mı?

## Denetim şeması
1. **Sağlayıcı sıfatı.** 5651'de içerik, yer, erişim ve toplu kullanım sağlayıcı tanımları (m.2) sorumluluk ve muhatabı belirler. Yer sağlayıcı kural olarak içeriği denetlemekle yükümlü değildir ancak uyar-kaldır yükümlülüğü doğabilir.
2. **İçeriğin çıkarılması / erişimin engellenmesi (m.9).** Kişilik hakkı ihlal edilen kişi önce içerik/yer sağlayıcıya başvurabilir; sonuç alınamazsa sulh ceza hâkimliğine başvurarak içeriğin çıkarılması ve/veya erişimin engellenmesini isteyebilir. Hâkim kararını talepten itibaren kanunda öngörülen kısa sürede (24 saat) verir; karara karşı itiraz yolu açıktır.
3. **Özel hayatın gizliliği (m.9/A).** Özel hayatın gizliliğinin ihlali halinde doğrudan BTK'ya başvurarak erişimin engellenmesi istenebilir; gecikmesinde sakınca bulunan hallerde BTK Başkanı resen tedbir uygulayıp 24 saat içinde hâkim onayına sunar.
4. **Katalog suçlar ve resen engelleme (m.8).** Kanunda sayılan katalog suçlara ilişkin içerikte hâkim/savcı veya BTK kararıyla erişim engellenir. Ölçülülük gereği URL bazlı engelleme tercih edilir; aşırı geniş engelleme hukuka aykırı olabilir.
5. **İspat ve ara sonuç.** İhlal ve içeriğin varlığı başvurucu tarafından belgelenir (ekran görüntüsü + URL + tarih, mümkünse noter/teknik tespit). Doğru yol (m.9 / m.9/A / m.8), mercі ve süre belirlenir.

## Çıktı modülleri
- Yol seçim tablosu (sağlayıcı başvurusu / sulh ceza / BTK).
- İçerik çıkarma-erişim engelleme başvuru/dilekçe taslağı.
- İtiraz dilekçesi iskeleti ve ölçülülük argümanı.
<<<BECERI>>>
slug: kurumsal-siber-guvenlik-yukumlulukleri
ad: Kurumsal Siber Güvenlik Yükümlülükleri ve Uyum
aciklama: Bir kurumun siber güvenlik ve veri güvenliği yükümlülüklerini (KVKK m.12 teknik-idari tedbirler, sektörel düzenlemeler, politika ve sözleşme mimarisi) değerlendirmek ve uyum boşluğunu çıkarmak gerektiğinde kullanılır.
<<<GOVDE>>>
# Kurumsal Siber Güvenlik Yükümlülükleri ve Uyum

## Görev
Kurumun siber/veri güvenliği hukuki yükümlülüklerini saptamak; politika, teknik-idari tedbir ve sözleşme mimarisindeki boşlukları çıkarıp uyum yol haritası kurmak.

## Soğuk başlangıç (intake)
1. Kurumun faaliyeti ve sektörü ne? (banka/ödeme, sağlık, telekom, e-ticaret, genel?)
2. Hangi ve ne kadar kişisel veri işleniyor, işleyen/bulut kullanılıyor mu?
3. Mevcut politika, olay müdahale planı, log yönetimi var mı?
4. Tetikleyici ne? (denetim, ihlal sonrası, yatırım/due diligence, proaktif uyum?)

## Denetim şeması
1. **Genel veri güvenliği (KVKK m.12).** Veri sorumlusu, kişisel verilerin hukuka aykırı işlenmesini ve erişilmesini önlemek ile muhafazasını sağlamak üzere uygun **teknik ve idari tedbirleri** almakla yükümlüdür; işleyen ile müştereken sorumludur. Tedbirlerin alındığını ispat yükü kurumdadır. Eksiklik m.18 idari para cezası ve ihlal halinde ağırlaştırılmış sorumluluk doğurur.
2. **Sektörel katman.** Bankacılık/ödeme (BDDK, 6493 ve bilgi sistemleri düzenlemeleri), elektronik haberleşme (BTK/5809 ve ağ güvenliği), kritik altyapı düzenlemeleri ve varsa kurumun tabi olduğu özel rejim eklenir. TS ISO/IEC 27001 ve ilgili standartlar uyum ölçütü olarak referans alınır (sözleşme/idari beklenti düzeyinde).
3. **Belge ve süreç denetimi.** Veri envanteri, saklama-imha politikası, erişim yönetimi, log kayıtları, olay müdahale ve iş sürekliliği planı, sızma testi/zafiyet yönetimi, farkındalık eğitimleri kontrol edilir.
4. **Sözleşme mimarisi.** Veri işleyen sözleşmeleri, gizlilik ve güvenlik taahhütleri, SLA/güvenlik ekleri, sorumluluk sınırlamaları (TBK çerçevesinde geçerlilik), yurt dışı aktarım şartları denetlenir.
5. **Ara sonuç.** Yükümlülük-mevcut durum karşılaştırmasıyla **uyum boşluğu** ve öncelik/risk sıralaması çıkarılır.

## Çıktı modülleri
- Yükümlülük envanteri (genel KVKK + sektörel + standart).
- Uyum boşluğu raporu (boşluk, risk, öncelik, aksiyon).
- Politika/sözleşme eki şablon önerileri.
<<<BECERI>>>
slug: siber-olay-hukuki-sorumluluk-tazminat
ad: Siber Olaydan Doğan Hukuki Sorumluluk ve Tazminat
aciklama: Veri ihlali, sistem kesintisi veya siber saldırı sonrası kurum-müşteri-iş ortağı arasındaki tazminat ve sözleşmesel sorumluluğu; kusur, illiyet ve zarar denetimini yapmak gerektiğinde kullanılır.
<<<GOVDE>>>
# Siber Olaydan Doğan Hukuki Sorumluluk ve Tazminat

## Görev
Bir siber olay sonrası kimin, kime, hangi hukuki sebeple ve ne kadar sorumlu olduğunu (haksız fiil/sözleşme) çözmek; tazminat talebi veya savunma stratejisi kurmak.

## Soğuk başlangıç (intake)
1. Zarar gören kim, zarar ne? (maddi kayıp, itibar, veri kaybı, manevi zarar?)
2. Taraflar arasında sözleşme var mı? (hizmet, işleme, SLA?)
3. Olayın sebebi ne? (kurumun tedbirsizliği, üçüncü kişi saldırısı, çalışan kusuru?)
4. Talep mi savunma mı, muhatap kim?

## Denetim şeması
1. **Sorumluluk temeli seçimi.** Sözleşme varsa borca aykırılık (TBK m.112 vd.) ve borçlunun yardımcı kişilerden sorumluluğu (TBK m.116) önceliklidir; sözleşme yoksa haksız fiil (TBK m.49). Çoğu olayda yarışan sebep söz konusudur; zarar görenin lehine olan seçilebilir.
2. **Haksız fiil unsurları (TBK m.49 vd.).** Fiil (güvenlik tedbirini almama/ihmal), hukuka aykırılık (KVKK m.12 ihlali, gizlilik ihlali), kusur, zarar ve illiyet bağı aranır. KVKK m.12 yükümlülüğünün ihlali hukuka aykırılığın güçlü göstergesidir. Üçüncü kişinin saldırısı illiyeti kesebilir; ancak öngörülebilir saldırıya karşı tedbirsizlik kusuru ortadan kaldırmaz.
3. **Manevi tazminat ve veri.** Kişilik hakkı ihlali (TMK m.24; TBK m.58) ve özel hayatın ihlali manevi tazminata esas olabilir; veri ihlalinde ilgili kişilerin zararı somutlaştırılır.
4. **İspat yükü ve hesap.** Sözleşmesel sorumlulukta borçlu kusursuzluğunu (TBK m.112) ispatlar; haksız fiilde kural olarak zarar görenin ispatı gerekir, KVKK m.12 ise tedbir ispatını kuruma yükler. Zarar kalemleri (fiili zarar, yoksun kalınan kâr, gideri yapılan müdahale masrafları) belgelenir; tazminattan indirim sebepleri (TBK m.52) gözetilir.
5. **Ara sonuç.** Sorumlu sıfatı, hukuki sebep, ispat dağılımı ve zamanaşımı (TBK m.72 haksız fiilde; m.146/147 sözleşmesel) netleştirilir.

## Çıktı modülleri
- Sorumluluk haritası (taraf-sebep-kusur-illiyet-zarar).
- Tazminat hesap çerçevesi ve indirim notu.
- Talep/ihtar veya savunma dilekçesi iskeleti.
<<<BECERI>>>
slug: gorev-yetki-yargi-yolu
ad: Görev, Yetki ve Yargı Yolu Haritası
aciklama: Bilişim/siber bir uyuşmazlıkta hangi yargı koluna, hangi mahkemeye/mercie, hangi yetki kuralıyla başvurulacağını belirlemek; ceza-idari-hukuk yolları arasında doğru tercihi yapmak gerektiğinde kullanılır.
<<<GOVDE>>>
# Görev, Yetki ve Yargı Yolu Haritası

## Görev
Bilişim/siber uyuşmazlıkta doğru yargı kolunu, görevli ve yetkili mercii ve başvuru yolunu belirlemek; eş zamanlı yürüyen süreçleri koordine etmek.

## Soğuk başlangıç (intake)
1. Talep ne? (ceza/şikâyet, idari yaptırım itirazı, tazminat, içerik kaldırma, uyum?)
2. Taraflar kim, biri tacir/tüketici mi, idare mi?
3. Olayın yeri/zararın doğduğu yer neresi?
4. Süre kısıtı veya acil tedbir ihtiyacı var mı?

## Denetim şeması
1. **Ceza yolu.** Bilişim suçlarında (TCK m.243-245) şikâyet/ihbar Cumhuriyet başsavcılığına yapılır; kovuşturmada görev kural olarak asliye ceza, ağırlaştırılmış hallerde ağır ceza mahkemesindedir. Yetki suçun işlendiği yer (CMK m.12). Soruşturma gizliliği ve koruma tedbirleri (CMK m.134) bu yolda işler.
2. **5651 tedbir yolu.** İçerik çıkarma/erişim engellemede görevli mercі sulh ceza hâkimliği (m.9), özel hayatta BTK (m.9/A); kararlara itiraz CMK itiraz usulüne tabidir.
3. **İdari yol (KVKK).** Kurul kararlarına (idari para cezası, ilgili kişi başvurusu sonucu) karşı dava idari yargıda açılır; idari para cezasına karşı yol ise niteliğine göre değerlendirilir (Kabahatler Kanunu/idari yargı tartışması). Dava açma süresi (2577 İYUK m.7) gözetilir.
4. **Hukuk yolu.** Tazminat ve sözleşme uyuşmazlıklarında görev: taraflar tacir ve iş ticari ise asliye ticaret (TTK m.4-5); tüketici işlemiyse tüketici mahkemesi/hakem heyeti; aksi halde asliye hukuk. Yetki HMK m.6 (genel) ve haksız fiilde HMK m.16 (haksız fiilin işlendiği/zararın doğduğu yer). Acil koruma için ihtiyati tedbir/delil tespiti (HMK m.389 vd., m.400 vd.).
5. **Ara sonuç.** Eş zamanlı işleyebilecek yollar (ceza + KVKK + tazminat) ve sıralaması, görev-yetki ve süreler tabloya bağlanır. İspat yükü her yolda ayrıca ele alınır.

## Çıktı modülleri
- Yargı yolu/görev/yetki tablosu (yol, mercі, kural, süre).
- Süre ve acil tedbir takvimi.
- Yol koordinasyon notu (eş zamanlı süreçler).
<<<BECERI>>>
slug: sureler-zamanasimi-bildirim
ad: Süreler, Zamanaşımı ve Bildirim Takvimi
aciklama: Bilişim/siber uyuşmazlıkta ceza zamanaşımı, dava açma süreleri, KVKK ihlal bildirim süresi ve başvuru sürelerini hesaplamak ve hak kaybını önleyecek takvim kurmak gerektiğinde kullanılır.
<<<GOVDE>>>
# Süreler, Zamanaşımı ve Bildirim Takvimi

## Görev
Olaya bağlı tüm süreleri (bildirim, şikâyet, dava, zamanaşımı) tespit edip hak düşürücü kayıpları önleyecek bir takvim kurmak.

## Soğuk başlangıç (intake)
1. Olay/öğrenme tarihi ve fark edilme anı ne?
2. Hangi süreçler söz konusu? (ceza, KVKK bildirim, tazminat, idari dava?)
3. Şikâyete bağlı suç var mı, fail/zarar biliniyor mu?
4. Bir tebligat/karar var mı, tarihi ne?

## Denetim şeması
1. **KVKK ihlal bildirimi.** Veri ihlalinde Kurula bildirim, öğrenmeden itibaren Kurul uygulaması gereği **72 saat** içinde yapılır; ilgili kişilere de makul en kısa sürede bildirilir. Gecikme ayrı bir yaptırım riskidir.
2. **Ceza zamanaşımı (TCK m.66-72).** Dava zamanaşımı suçun cezasının üst sınırına göre belirlenir (TCK m.66); bilişim suçlarının çoğunda 8 yıllık dilim devreye girer. Şikâyete bağlı suçlarda **6 aylık** şikâyet süresi (TCK m.73) failin ve fiilin öğrenilmesinden itibaren işler. Banka/kart suçları ve nitelikli haller resen takip edilir.
3. **Tazminat zamanaşımı.** Haksız fiilde zarar ve failin öğrenilmesinden itibaren **2 yıl** ve her halde fiilden itibaren **10 yıl** (TBK m.72); fiil aynı zamanda suçsa daha uzun ceza zamanaşımı uygulanır. Sözleşmesel taleplerde genel **10 yıl** (TBK m.146), özel hallerde **5 yıl** (TBK m.147).
4. **İdari/içerik süreleri.** KVKK Kurul kararına/idari yaptırıma karşı dava açma süresi (2577 İYUK m.7, kural 60 gün; idari para cezası niteliğine göre değerlendirilir). 5651 sulh ceza/BTK kararlarına itiraz CMK itiraz süresine (kural 7 gün) tabidir.
5. **Ara sonuç.** Her süre için başlangıç anı, uzunluk, son gün ve durma/kesilme halleri belirlenip tek takvimde toplanır. İspat açısından öğrenme tarihinin belgelenmesi önemlidir.

## Çıktı modülleri
- Süre takvimi tablosu (süreç, başlangıç, uzunluk, son gün, dayanak).
- Hak düşürücü riskler ve öncelikli aksiyonlar.
- Şikâyet/dava/itiraz için son tarih uyarı notu.
<<<BECERI>>>
slug: sozlesme-bildirim-basvuru-taslaklari
ad: Sözleşme, Bildirim ve Başvuru Taslakları
aciklama: Veri işleyen sözleşmesi, gizlilik/güvenlik eki, ihlal bildirimi, içerik kaldırma başvurusu, suç duyurusu gibi bilişim hukukuna özgü metinlerin taslağını üretmek gerektiğinde kullanılır.
<<<GOVDE>>>
# Sözleşme, Bildirim ve Başvuru Taslakları

## Görev
Bilişim/siber alanına özgü hukuki metinleri (sözleşme ekleri, bildirimler, başvurular, dilekçeler) doğru hukuki çerçeveyle ve yer tutucu disiplinine uygun taslamak.

## Soğuk başlangıç (intake)
1. Hangi belge? (veri işleyen sözleşmesi/eki, ihlal bildirimi, içerik kaldırma, suç duyurusu, ihtar?)
2. Taraflar ve sıfatları kim? (veri sorumlusu/işleyen, mağdur, sağlayıcı?)
3. Hangi olgular sabit, hangileri eksik?
4. Muhatap mercі ve dil resmiyeti ne düzeyde olmalı?

## Denetim şeması
1. **Belge tipi ve dayanağı.** Her metin dayanağına bağlanır: veri işleyen sözleşmesi (KVKK m.12 müşterek sorumluluk, aktarım şartları), ihlal bildirimi (KVKK m.12/5 ve Kurul formu), içerik kaldırma (5651 m.9/m.9/A), suç duyurusu (TCK m.243-245; CMK soruşturma), ihtar/tazminat talebi (TBK m.49/m.112).
2. **Zorunlu unsurlar.** Dilekçelerde taraf/mercі, olay özeti, hukuki sebep ve talep sonucu net ayrılır (HMK m.119 mantığı esas alınır). İhlal bildiriminde ihlalin niteliği, etkilenen veri/kişi, olası sonuçlar ve alınan tedbirler yer alır. Sözleşmede güvenlik taahhütleri, denetim, alt işleyen, ihlal bildirim yükümlülüğü ve sorumluluk dağılımı düzenlenir.
3. **Risk ve emredici hüküm süzgeci.** Sorumluluğu tümüyle kaldıran kayıtların TBK m.115 (ağır kusur/kasıtta geçersizlik) ve tüketici/emredici hükümler karşısında geçerliliği denetlenir; KVKK yükümlülükleri sözleşmeyle bertaraf edilemez.
4. **Yer tutucu disiplini.** Doğrulanmamış olgular `[doldurulacak]`, doğrulanmamış içtihat künyesi `[doğrulanacak]` olarak bırakılır; uydurma veri/numara yazılmaz.
5. **Ara sonuç.** Belgenin iskeleti, eksik bilgi listesi ve risk uyarıları birlikte sunulur.

## Çıktı modülleri
- Talep edilen belgenin tam taslağı (başlık, gövde, talep/sonuç).
- Eksik bilgi/olgu listesi ([doldurulacak] dökümü).
- Risk ve müzakere notu (geçerlilik, emredici hüküm uyarıları).
<<<BECERI>>>
slug: risk-strateji-kriz-yonetimi
ad: Risk, Strateji ve Kriz Yönetimi
aciklama: Bir siber olay veya bilişim hukuku ihtilafında ceza-idari-tazminat risklerini bütünsel tartmak, kurum/müvekkil için en iyi-en kötü senaryoyu ve eylem stratejisini belirlemek gerektiğinde kullanılır.
<<<GOVDE>>>
# Risk, Strateji ve Kriz Yönetimi

## Görev
Çok katmanlı bir bilişim/siber olayda riskleri tartmak, senaryoları çıkarmak ve müvekkil/kurum için tutarlı bir hukuki strateji ile kriz yönetim planı kurmak.

## Soğuk başlangıç (intake)
1. Kurumun/müvekkilin pozisyonu ne? (mağdur, sorumlu, hem mağdur hem sorumlu?)
2. En kritik risk ne? (ceza, idari para cezası, tazminat, itibar, operasyon kesintisi?)
3. Karşı taraf/düzenleyici aktif mi? (savcılık, KVKK, müşteri talepleri?)
4. Zaman baskısı ve kaynak kısıtı ne düzeyde?

## Denetim şeması
1. **Risk envanteri.** Üç eksende risk çıkarılır: ceza (TCK m.243-245, m.135-140 maruziyeti), idari (KVKK m.18 para cezası, sektörel yaptırım), özel hukuk (TBK m.49/m.112 tazminat, toplu talep riski). Her risk olasılık ve etki ile derecelendirilir.
2. **Pozisyon analizi.** Kurum aynı anda mağdur (saldırıya uğrayan) ve potansiyel sorumlu (tedbirsizlik) olabilir; bu ikili konum stratejiyi belirler. Suç duyurusu seçeneği ile sorumluluk savunması çelişmemelidir.
3. **Senaryo çıkarma.** En iyi/orta/en kötü senaryolar; her birinde olasılık, mali etki, süre ve karşı hamle. Delil durumu ve ispat yükü dağılımı (KVKK'da tedbir ispatı kurumda; cezada iddia makamında) senaryoları belirler.
4. **Strateji tercihi.** Erken bildirim ve iş birliği (yaptırım hafifletici), uzlaşma/sulh, savunma hattı, eş zamanlı yargı yolları koordinasyonu; itibar/iletişim ile hukuki adımların uyumu. Ölçülülük: aşırı reaksiyon yeni risk doğurmamalı.
5. **Ara sonuç.** Önceliklendirilmiş aksiyon listesi, sorumlu kişiler ve karar noktaları net bir kriz planına bağlanır.

## Çıktı modülleri
- Risk matrisi (eksen, olasılık, etki, öncelik).
- Senaryo tablosu (en iyi/orta/en kötü + aksiyon).
- Kriz yönetim planı ve karar/iletişim notu.
<<<BECERI>>>
slug: muvekkil-iletisim-bilgilendirme
ad: Müvekkil ve Paydaş İletişimi
aciklama: Siber olay veya bilişim ihtilafında müvekkili, yönetim kurulunu, çalışanları veya etkilenen ilgili kişileri hukuken doğru ama anlaşılır biçimde bilgilendirmek ve bildirim metinleri kurmak gerektiğinde kullanılır.
<<<GOVDE>>>
# Müvekkil ve Paydaş İletişimi

## Görev
Teknik ve hukuki açıdan karmaşık bir siber olayı, ilgili paydaşlara (müvekkil/yönetim, çalışanlar, etkilenen ilgili kişiler, düzenleyici) doğru, ölçülü ve anlaşılır biçimde aktaracak iletişim metinlerini kurmak.

## Soğuk başlangıç (intake)
1. Muhatap kim? (yönetim kurulu, müvekkil, çalışanlar, etkilenen müşteriler, basın?)
2. Hangi mesaj zorunlu, hangisi ihtiyari? (yasal bildirim mi, bilgilendirme mi?)
3. Hassasiyet düzeyi ne? (devam eden tehdit, soruşturma gizliliği, itibar?)
4. Hangi olgular kesin doğrulanmış, hangileri henüz belirsiz?

## Denetim şeması
1. **Mesaj-muhatap eşleştirmesi.** Her paydaşa içerik ve dil ayarlanır: yönetime risk/karar odaklı, çalışanlara talimat odaklı, ilgili kişilere KVKK m.12/5 bildirim içeriği (ihlalin niteliği, etkilenen veriler, önlemler, başvuru kanalları), düzenleyiciye resmi ve eksiksiz.
2. **Doğruluk ve ölçü.** Sadece doğrulanmış olgular paylaşılır; belirsizlikler abartılmadan/küçümsenmeden ifade edilir. Sorumluluk doğurabilecek peşin kabul ifadelerinden kaçınılır; aynı zamanda yanıltıcı/eksik bilgi yaptırım riski yaratır.
3. **Gizlilik ve ayrıcalık.** Soruşturma gizliliği (CMK), avukat-müvekkil gizliliği ve ticari sır gözetilir; iç hukuki değerlendirme notları ile dışa açık bildirimler ayrılır.
4. **Eylem yönlendirmesi.** İlgili kişilere somut koruyucu adımlar (şifre değişimi, kart bloke, dolandırıcılık uyarısı) ve başvuru kanalı sunulur; çalışanlara müdahale talimatı verilir.
5. **Ara sonuç.** Hangi metnin kime, hangi kanaldan, hangi zamanlamayla gideceği ve hukuki onay gereği belirlenir. İçtihat/karar atfı yapılacaksa künye doğrulanır; doğrulanmamışsa `[doğrulanacak]` işaretlenir.

## Çıktı modülleri
- Paydaş-mesaj matrisi ve zamanlama.
- İlgili kişi bilgilendirme / çalışan talimatı / yönetim brifing metinleri.
- Sade dil özeti ve hukuki onay/uyarı notu.
<<<SON>>>
