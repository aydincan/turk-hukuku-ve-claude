<<<REFERANS>>>
# Dava ve Dosya Takip — Metodoloji Referansı

## Alanın sistematiği
Dava dosyası takibi, bir uyuşmazlığın baştan sona izlenebilir, denetlenebilir ve süre güvenli biçimde yönetilmesidir. Burada amaç hukuki nitelendirme değil; dosyaya hızlı ve eksiksiz hâkim olmayı sağlayan yapılandırılmış çıktılar (dosya özeti, taraf-vekil tablosu, vakıa kronolojisi, delil dizini, süre takvimi, eksik/çelişki listesi) üretmektir. Çıktılar Excel'lenebilir (kolonlu, satırlanabilir) ve UYAP iş akışına uyumlu olmalıdır. Esas işlev: dağınık evrakı tek bir doğruluk kaynağına dönüştürmek ve usuli risk (süre kaçırma, eksik delil, görevsiz/yetkisiz mahkeme) üretmeden ilerlemektir.

## Başat normlar ve madde atıfları
Takip işi büyük ölçüde usul hukukunun zaman ve şekil disiplinine dayanır.
- HMK 6100 (medeni yargılama): dava şartları ve ilk itirazlar (HMK m.114-116), görev (m.1) ve yetki (m.5 vd.), dava dilekçesi zorunlu unsurları (HMK m.119), cevap dilekçesi ve süresi (HMK m.126-127, kural 2 hafta), ön inceleme (m.137 vd.), ispat yükü (HMK m.190) ve delil türleri (senet m.199 vd., tanık m.240 vd., bilirkişi m.266 vd., keşif m.288 vd.). Süreler ve tatil-tebligat etkisi (HMK m.90 vd.); istinaf süresi 2 hafta (HMK m.345), temyiz süresi 2 hafta (HMK m.361).
- CMK 5271 (ceza yargılaması): iddianame (CMK m.170), itiraz süreleri ve kanun yolları (CMK m.267-268, kural 7 gün), istinaf (CMK m.272-273, 7 gün), temyiz (CMK m.291, 15 gün), koruma tedbirleri (gözaltı, tutuklama m.100 vd.).
- Tebligat ve süre: 7201 sayılı Tebligat Kanunu; sürelerin tebliğ/öğrenme ile işlemeye başlaması.
- İcra takibi varsa İİK 2004: itiraz süresi 7 gün (İİK m.62), itirazın iptali davası 1 yıl (İİK m.67), kambiyo takibinde itiraz 5 gün (İİK m.168).
- İdari yargı dosyası varsa 2577 İYUK: genel dava açma süresi 60 gün (İYUK m.7).

## Çalışma yöntemi
1. Önce dosya envanteri: hangi evrak var, hangisi eksik, tarihleri ne. 2. Taraf-vekil-mahkeme künyesini çıkar (esas no, mahkeme, taraflar, vekiller, dava türü, talep). 3. Vakıaları tarih sırasıyla kronolojiye diz; her vakıayı dayandığı evrak/sayfaya bağla. 4. Delilleri dizinle: delil adı, türü, ibraz eden, dayandığı vakıa, durumu (sunuldu/beklenen/itirazlı). 5. Süre takvimini kur: her süre için başlangıç olayı, dayanak madde, son gün, durum. 6. Eksik ve çelişki listesini üret: ibraz edilmemiş delil, cevaplanmamış iddia, çelişen beyan. Her çıktıda kaynağa (evrak adı + tarih + sayfa) atıf zorunlu; belgede olmayan vakıa uydurulmaz.

## Kaynak hijyeni
Tarih, esas/karar numarası, süre ve tutar gibi veriler yalnızca dosyadaki evraktan alınır; tahmin edilmez. Belgede bulunmayan bilgi [doldurulacak] yer tutucusuyla işaretlenir. Süre hesapları daima dayanak maddeyle (ör. HMK m.127, CMK m.268) ve başlangıç tarihiyle gösterilir; hesabın doğrulanması kullanıcıya bırakılır. UYAP'tan gelen veriler ekran/evrak referansıyla kaydedilir. İçtihat gerekiyorsa karar künyesi uydurulmaz; karararama.yargitay.gov.tr ya da karararama.danistay.gov.tr üzerinden doğrulanması [doğrulanacak] notuyla istenir. Bu eklenti hukuki nitelendirme ve strateji üretmez; dosyaya hâkimiyet ve usuli süre güvenliği sağlar — esasa dair değerlendirme ilgili alan eklentilerine bırakılır.
<<<BECERI>>>
slug: dosya-ozeti-cikarma
ad: Dosya Özeti Çıkarma
aciklama: Dağınık bir dava dosyasından künye, talep, taraflar ve aşamayı tek sayfalık yapılandırılmış özete dönüştürmek gerektiğinde; yeni gelen veya devralınan dosyaya hızlı hâkim olmak için kullan.
<<<GOVDE>>>
# Dosya Özeti Çıkarma

## Görev
Bir dava dosyasının dağınık evrakını; künye, taraflar, talep, aşama ve sıradaki iş kalemlerini içeren tek sayfalık, Excel'lenebilir bir özete indirgemek. Amaç dosyaya 5 dakikada hâkim olmayı sağlamaktır.

## Soğuk başlangıç (intake)
- Dosya hangi yargı koluna ait: hukuk (HMK), ceza (CMK), icra (İİK), idari (İYUK)?
- Elinde hangi evrak var (dava/iddianame, cevap, bilirkişi raporu, tensip, ara karar, UYAP dökümü)?
- Mahkeme ve esas numarası ile tarafların adları belli mi?
- Özet kimin için: hâkim olmak için mi, müvekkile rapor için mi, devir için mi?

## Denetim şeması
1. Künye kalemi: mahkeme adı, esas no, dava türü, dava tarihi, talep sonucu. HMK m.119 zorunlu unsurları (taraflar, talep, vakıalar, hukuki sebep, deliller) dosyada mevcut mu, eksik unsur var mı denetle. Eksikse [doldurulacak].
2. Taraf kalemi: davacı/davalı (ceza dosyasında şüpheli-sanık-müşteki-katılan), vekilleri, tebligat adresleri. Vekâletname dosyada mı; yoksa eksik listesine yaz.
3. Talep ve dayanak: dava dilekçesindeki talep sonucu ile hukuki sebepleri evraktan birebir aktar; yorum ekleme.
4. Aşama tespiti: dilekçeler aşaması mı, ön inceleme (HMK m.137) mi, tahkikat mı, istinaf mı? Son işlem tarihinden çıkar.
5. Ara sonuç: bir sonraki kritik adım (duruşma, cevap süresi, rapora itiraz) ve son günü ile birlikte not et; her veri kaynağına (evrak + tarih + sayfa) bağlanır. Belgede olmayan bilgi uydurulmaz.

## Çıktı modülleri
- Tek sayfalık künye tablosu (mahkeme, esas no, taraflar, talep, aşama).
- Sıradaki iş kalemleri listesi (ne, ne zaman, dayanak madde).
- Eksik evrak ve [doldurulacak] alanları listesi.
<<<BECERI>>>
slug: taraf-vekil-tablosu
ad: Taraf ve Vekil Tablosu
aciklama: Çok taraflı veya birden çok vekilli dosyalarda taraf-sıfat-vekil-adres-tebligat ilişkisini netleştirmek ve tebligat ile husumet hatalarını önlemek için tablo kurarken kullan.
<<<GOVDE>>>
# Taraf ve Vekil Tablosu

## Görev
Dosyadaki tüm tarafları, sıfatlarını, vekillerini ve tebligat bilgilerini tek tabloda toplayıp husumet, taraf teşkili ve tebligat hatalarını görünür kılmak.

## Soğuk başlangıç (intake)
- Kaç taraf var ve sıfatları ne (davacı, davalı, fer'î müdahil, ihbar olunan)?
- Her tarafın vekili belli mi, vekâletname dosyada mı?
- Tebligat adresleri ve KEP/MERSIS bilgileri mevcut mu?
- Ceza dosyası ise şüpheli/sanık, müşteki/katılan, mağdur ayrımı yapıldı mı?

## Denetim şeması
1. Sıfat kolonu: HMK'da davacı-davalı; çok taraflılıkta ihtiyari/zorunlu dava arkadaşlığı (HMK m.57-59) var mı denetle. Zorunlu dava arkadaşlığında taraf teşkili eksikse dava şartı sorunu doğar (HMK m.114), eksik listesine yaz.
2. Vekil kolonu: her taraf için vekil adı, baro-sicil, vekâletname tarihi. Vekâletname yoksa veya kapsamı dar ise (özel yetki gerektiren işlemler için) işaretle.
3. Tebligat kolonu: adres, tüzel kişilerde MERSIS/KEP. Tebligat Kanunu (7201) gereği usulsüz tebligat riskini not et; tebligatın geçerliliği süreleri etkiler.
4. Müdahil/üçüncü kişi: fer'î müdahale (HMK m.66), davanın ihbarı (HMK m.61) varsa ayrı satır.
5. Ara sonuç: taraf teşkili tamam mı, husumet doğru tarafa mı yöneltilmiş, hangi tebligat eksik — kontrol listesi olarak çıkar. Adres ve sıfatlar yalnızca evraktan alınır.

## Çıktı modülleri
- Taraf-sıfat-vekil-adres-tebligat kolonlu Excel tablosu.
- Eksik vekâletname / eksik taraf teşkili uyarı listesi.
- Tebligat riski notları.
<<<BECERI>>>
slug: vakia-kronolojisi
ad: Vakıa Kronolojisi
aciklama: Olayların ve usul işlemlerinin tarih sırasıyla dizilmesi, her vakıanın dayandığı evraka bağlanması ve zaman içindeki boşlukların görülmesi gerektiğinde kullan.
<<<GOVDE>>>
# Vakıa Kronolojisi

## Görev
Maddi olayları ve usul işlemlerini tarih sırasıyla dizip her birini dayandığı belgeye bağlayarak dosyanın zaman çizgisini ve boşluklarını görünür kılmak.

## Soğuk başlangıç (intake)
- Uyuşmazlığın başlangıç olayı (sözleşme, kaza, fesih, suç tarihi) hangi tarih?
- Hangi evrak hangi olayı belgeliyor (sözleşme, fatura, tutanak, tebligat)?
- Maddi olay kronolojisi mi, usul işlemleri kronolojisi mi, yoksa ikisi birden mi?
- Tarih çelişkisi yaratan belgeler var mı?

## Denetim şeması
1. Olay satırı: tarih, olay/işlem, dayanak evrak (ad + sayfa), tarafı. Tarih belirsizse [doldurulacak] yaz; yaklaşık tarih uydurma.
2. Maddi olay - usul ayrımı: maddi vakıalar (zamanaşımı ve hak düşürücü süre başlangıcı için kritik) ile usul işlemleri (tebligat, duruşma, ara karar) ayrı renk/kolon.
3. Süre tetikleyici tespiti: her olayın bir süreyi başlatıp başlatmadığını işaretle (tebligat → cevap süresi HMK m.127; karar tebliği → istinaf süresi HMK m.345). Bu satırlar süre takvimine devredilir.
4. Boşluk ve çelişki: kronolojideki açıklanamayan aralıklar ve çelişen tarihler ayrı not. İspat yükü (HMK m.190) açısından hangi vakıayı kimin ispatlaması gerektiğini belirt.
5. Ara sonuç: zaman çizgisi + süre tetikleyici işaretleri + boşluk listesi. Her satır kaynağa bağlı; belgesiz vakıa eklenmez.

## Çıktı modülleri
- Tarih-olay-dayanak-taraf kolonlu kronoloji tablosu.
- Süre tetikleyici olaylar alt listesi.
- Tarih boşlukları ve çelişkileri notu.
<<<BECERI>>>
slug: sure-takvimi-ve-zamanasimi
ad: Süre Takvimi ve Zamanaşımı
aciklama: Cevap, itiraz, istinaf, temyiz gibi usul süreleri ile zamanaşımı/hak düşürücü sürelerin son günlerini dayanak maddeyle hesaplayıp takvime bağlamak gerektiğinde kullan.
<<<GOVDE>>>
# Süre Takvimi ve Zamanaşımı

## Görev
Dosyadaki tüm usul sürelerini ve maddi zamanaşımı/hak düşürücü süreleri başlangıç olayı, dayanak madde ve son günüyle birlikte takvime dönüştürmek; süre kaçırma riskini sıfırlamak.

## Soğuk başlangıç (intake)
- Hangi yargı kolu: hukuk (HMK), ceza (CMK), icra (İİK), idari (İYUK)?
- Süreyi başlatan olay ve tarihi belli mi (tebligat, öğrenme, karar tarihi)?
- Hangi süreler işliyor (cevap, itiraz, kanun yolu, bilirkişiye itiraz)?
- Adli tatil veya resmî tatil araya giriyor mu?

## Denetim şeması
1. Süre kalemini tanımla ve dayanağını yaz: cevap dilekçesi 2 hafta (HMK m.127); bilirkişi raporuna itiraz 2 hafta (HMK m.281); hukukta istinaf 2 hafta (HMK m.345), temyiz 2 hafta (HMK m.361). Cezada itiraz 7 gün (CMK m.268), istinaf 7 gün (CMK m.273), temyiz 15 gün (CMK m.291). İcrada itiraz 7 gün (İİK m.62), kambiyoda 5 gün (İİK m.168); itirazın iptali 1 yıl (İİK m.67). İdaride 60 gün (İYUK m.7).
2. Başlangıç olayını sabitle: süre kural olarak tebliğ/öğrenme ile başlar; tarihi evraktan al, yoksa [doldurulacak].
3. Tatil ve son gün: adli tatilin (HMK m.102-104) süreye etkisini ve son günün tatile rastlamasını (uzama) kontrol et. Hesabı dayanak maddeyle göster.
4. Zamanaşımı/hak düşürücü süre: maddi hukuk süresini ilgili alanın kanunundan al (ör. genel zamanaşımı TBK m.146 on yıl; haksız fiil TBK m.72). Bu süreler usul süresinden ayrı izlenir.
5. Ara sonuç: her süre için son gün ve risk seviyesi; hesabın kullanıcıca doğrulanması istenir. Tarih uydurulmaz.

## Çıktı modülleri
- Süre-başlangıç-dayanak madde-son gün-durum kolonlu takvim tablosu.
- Yaklaşan/kritik süreler uyarı listesi.
- Hesap doğrulama notu ([doğrulanacak] son günler).
<<<BECERI>>>
slug: delil-dizini-ve-ispat-yuku
ad: Delil Dizini ve İspat Yükü
aciklama: Dosyadaki delilleri dizinleyip her birini ilgili vakıaya ve ispat yüküne bağlamak, sunulan-beklenen-itirazlı delilleri ayırt etmek gerektiğinde kullan.
<<<GOVDE>>>
# Delil Dizini ve İspat Yükü

## Görev
Dosyadaki tüm delilleri türü, ibraz edeni, dayandığı vakıa ve durumuyla dizinlemek; her çekişmeli vakıada ispat yükünün kimde olduğunu eşlemek.

## Soğuk başlangıç (intake)
- Hangi deliller dosyada (senet, fatura, tanık listesi, bilirkişi raporu, keşif tutanağı, yazışma)?
- Hangi vakıalar çekişmeli, hangileri ikrar edilmiş?
- Henüz sunulmamış ama dayanılan delil var mı?
- Karşı tarafın delillerine itiraz edilmiş mi?

## Denetim şeması
1. Delil satırı: delil adı, türü, ibraz eden, dayandığı vakıa, durum (sunuldu / beklenen / itirazlı). Delil türleri: senet (HMK m.199 vd.), tanık (HMK m.240 vd.), bilirkişi (HMK m.266 vd.), keşif (HMK m.288), yemin.
2. İspat yükü eşlemesi: HMK m.190 ve TMK m.6 uyarınca bir vakıadan lehine hak çıkaran tarafın ispatla yükümlü olduğunu uygula; her çekişmeli vakıanın karşısına yükümlü tarafı yaz.
3. Senetle ispat kuralı: belirli tutarı aşan hukuki işlemlerde senetle ispat zorunluluğu (HMK m.200) ve tanıkla ispat sınırı (HMK m.201) gözetilerek tanık deliline güvenilirlik notu düşülür.
4. Eksik delil: dayanılan ama sunulmamış delil ve celbi gereken belge (HMK m.219-221 ibraz yükümlülüğü, müzekkere) ayrı liste.
5. Ara sonuç: hangi vakıa hangi delille ispatlanıyor, hangisi açıkta — boşluk haritası. Delil içeriği evraktan alınır; var olmayan delil yazılmaz.

## Çıktı modülleri
- Delil-tür-ibraz eden-vakıa-durum kolonlu dizin tablosu.
- İspat yükü eşleme tablosu (çekişmeli vakıa → yükümlü taraf).
- Eksik/celbi gereken delil listesi.
<<<BECERI>>>
slug: eksik-ve-celiski-listesi
ad: Eksik ve Çelişki Listesi
aciklama: Dosyada cevaplanmamış iddiaları, ibraz edilmemiş delilleri ve taraf beyanları arasındaki çelişkileri sistematik biçimde tespit etmek gerektiğinde kullan.
<<<GOVDE>>>
# Eksik ve Çelişki Listesi

## Görev
Dosyadaki boşlukları (cevaplanmamış iddia, eksik evrak, ibraz edilmemiş delil) ve tutarsızlıkları (çelişen beyan, çelişen tarih/tutar) bir kalite-kontrol listesine dönüştürmek.

## Soğuk başlangıç (intake)
- Dava ve cevap dilekçeleri ile varsa replik-düplik elinde mi?
- Hangi iddialar karşı tarafça yanıtsız bırakılmış?
- Beyanlar, tutarlar veya tarihler arasında göze çarpan çelişki var mı?
- Hangi evrakın dosyada olması gerekirken olmadığını biliyor musun?

## Denetim şeması
1. Cevaplanmamış iddia: dava dilekçesindeki her vakıaya karşı cevap dilekçesinde açık/örtülü itiraz var mı? Cevapta açıkça inkâr edilmeyen vakıanın ikrar/çekişmesizlik etkisini (HMK m.128) işaretle.
2. Eksik evrak: dilekçelerde dayanılan ama dosyada bulunmayan belgeler; HMK m.121 ve m.129 gereği dilekçeye eklenmesi gereken delillerin eksikliği.
3. Çelişki taraması: aynı tarafın farklı evrakındaki çelişen beyanlar; taraflar arası çelişen tutar/tarih; bilirkişi raporu ile dosya arasındaki uyumsuzluk. Her çelişkiyi kaynak evrak + sayfa ile göster.
4. Usuli eksik: dava şartı (HMK m.114-115), ilk itiraz (HMK m.116) ve süresinde ileri sürülmeyen savunma genişletme yasağı (HMK m.141) açısından risk notları.
5. Ara sonuç: önceliklendirilmiş eksik/çelişki listesi (kritik / orta / düşük). Tespitler yalnızca evraka dayanır; varsayım eklenmez.

## Çıktı modülleri
- Eksik kalemler tablosu (ne eksik, dayanak, etki).
- Çelişki tablosu (çelişen ifadeler, kaynak evrak, sayfa).
- Önceliklendirilmiş aksiyon listesi.
<<<BECERI>>>
slug: durusma-hazirlik-ve-ara-karar-takibi
ad: Duruşma Hazırlığı ve Ara Karar Takibi
aciklama: Yaklaşan duruşmaya hazırlanmak, tensip ve ara kararların gereklerini izlemek, her celse için yapılacaklar ve verilecek beyanları listelemek gerektiğinde kullan.
<<<GOVDE>>>
# Duruşma Hazırlığı ve Ara Karar Takibi

## Görev
Her duruşma öncesi dosyanın güncel durumunu, ara kararların gereğini ve celsede yapılacak işlemleri bir hazırlık çek-listesine dönüştürmek; ara kararların kaçırılmasını önlemek.

## Soğuk başlangıç (intake)
- Bir sonraki duruşma tarihi ve aşaması (ön inceleme, tahkikat, sözlü yargılama) ne?
- En son ara karar ne idi ve gereği yerine getirildi mi?
- Bu celsede sunulacak beyan, delil veya itiraz var mı?
- Tanık/bilirkişi/keşif gibi bekleyen işlem var mı?

## Denetim şeması
1. Ara karar dökümü: tensip zaptı ve her celse zaptındaki ara kararları madde madde çıkar; her birinin muhatabı, gereği ve süresi (ör. iki hafta kesin süre, HMK m.94 kesin süre sonucu) ile takip et.
2. Aşamaya göre gündem: ön inceleme celsesinde sulh teşviki, ilk itiraz ve dava şartı incelemesi (HMK m.137-140); tahkikatta delil toplama ve tanık dinleme; sözlü yargılamada esas hakkında beyan.
3. Kesin süre riski: kesin süreye bağlanan işlemler (delil avansı, gider avansı HMK m.120, delil bildirimi) yerine getirilmedi ise hak kaybı uyarısı.
4. Sunulacaklar: bu celsede ibraz edilecek beyan/delil listesi ve dayanağı; mazeret gerekiyorsa mazeret dilekçesi notu.
5. Ara sonuç: celse-bazlı hazırlık çek-listesi ve açık ara karar gerekleri. Tarih ve ara karar metni evraktan alınır.

## Çıktı modülleri
- Ara karar takip tablosu (karar, muhatap, gereği, süre, durum).
- Duruşma hazırlık çek-listesi.
- Kesin süre / hak kaybı uyarıları.
<<<BECERI>>>
slug: gorev-ve-yetki-kontrolu
ad: Görev ve Yetki Kontrolü
aciklama: Davanın doğru görevli ve yetkili mahkemede açılıp açılmadığını, görevsizlik-yetkisizlik veya gönderme riskini denetlemek gerektiğinde kullan.
<<<GOVDE>>>
# Görev ve Yetki Kontrolü

## Görev
Dosyanın görevli mahkeme (dava konusuna göre) ve yetkili mahkeme (yer itibarıyla) bakımından doğru yerde olup olmadığını denetlemek; görevsizlik/yetkisizlik ile zaman kaybı riskini erken yakalamak.

## Soğuk başlangıç (intake)
- Dava konusu ve türü ne (alacak, tazminat, tüketici, iş, ticari, aile)?
- Dava hangi mahkemede ve hangi yerde açılmış?
- Taraflar arasında yetki sözleşmesi veya tahkim şartı var mı?
- Kesin yetki gerektiren bir dava türü söz konusu mu?

## Denetim şeması
1. Görev: HMK m.1 gereği görev kamu düzenindendir ve re'sen incelenir. Genel görevli asliye hukuk (HMK m.2) ile özel görevli mahkemeleri ayırt et: tüketici mahkemesi (6502 TKHK m.73), iş mahkemesi (7036 m.5), ticari dava-asliye ticaret (TTK m.4-5), aile mahkemesi, FSHM. Yanlış görevli mahkeme → görevsizlik kararı ve gönderme.
2. Yetki: genel yetki davalının yerleşim yeri (HMK m.6); özel/kesin yetki halleri (taşınmazda taşınmazın yeri HMK m.12; sözleşmede ifa yeri HMK m.10; haksız fiilde HMK m.16). Kesin yetki re'sen gözetilir.
3. Yetki sözleşmesi/tahkim: tacir-kamu tüzel kişisi arasında yetki sözleşmesi (HMK m.17) geçerli mi; tahkim şartı varsa tahkim ilk itirazı (HMK m.116) riski.
4. İtiraz zamanı: yetki ilk itirazdır, cevap süresinde ileri sürülmezse düşer (HMK m.116, m.117, m.19); görev her aşamada gözetilir.
5. Ara sonuç: görev/yetki uygun mu, değilse hangi mahkemeye gönderme ve süre etkisi. Mevzuat dışı varsayım yapılmaz.

## Çıktı modülleri
- Görev/yetki değerlendirme notu (doğru mahkeme + dayanak madde).
- Görevsizlik/yetkisizlik riski ve gönderme senaryosu.
- İtiraz süresi ve usul uyarısı.
<<<BECERI>>>
slug: kanun-yolu-takibi
ad: Kanun Yolu Takibi (İstinaf ve Temyiz)
aciklama: Karar sonrası istinaf ve temyiz yollarının açık olup olmadığını, süreleri, kesinlik sınırlarını ve dilekçe gereklerini izlemek gerektiğinde kullan.
<<<GOVDE>>>
# Kanun Yolu Takibi (İstinaf ve Temyiz)

## Görev
Verilen kararın hangi kanun yoluna tabi olduğunu, süresini, kesinlik sınırını ve başvuru gereklerini takvime bağlamak; kanun yolu hakkının süre veya parasal sınır nedeniyle kaybını önlemek.

## Soğuk başlangıç (intake)
- Karar hangi mahkemeden ve ne zaman tebliğ edildi?
- Karar miktarı/değeri ne (kesinlik sınırı kontrolü için)?
- Hukuk, ceza, icra yoksa idari karar mı?
- Aleyhe olan kısım ve başvuru sebepleri belirlendi mi?

## Denetim şeması
1. Yol tespiti: ilk derece kararına istinaf (BAM), istinaf kararına temyiz (Yargıtay/Danıştay). Hukukta istinaf süresi 2 hafta (HMK m.345), temyiz 2 hafta (HMK m.361); cezada istinaf 7 gün (CMK m.273), temyiz 15 gün (CMK m.291); idaride istinaf/temyiz süreleri İYUK m.45-46.
2. Kesinlik sınırı: parasal sınır altında istinaf/temyiz kapalı olabilir (HMK m.341 istinaf, m.362 temyiz kesinlik sınırları; her yıl güncellenir → sınır [doğrulanacak]). Sınırı yıl bazında doğrulat.
3. Başlangıç: süre tebliğ ile başlar; gerekçeli karar tebliğ edilmemişse süre işlemeye başlamaz, bu durumu not et.
4. Dilekçe gereği: istinaf/temyiz dilekçesinde sebeplerin gösterilmesi (HMK m.342, m.364); harç ve gider yatırma şartı (eksiklik halinde başvurudan vazgeçilmiş sayılma riski).
5. Ara sonuç: hangi yol açık, son gün, parasal sınır durumu ve hazırlanacak dilekçe. Tarih ve miktar evraktan alınır; sınır değerleri doğrulanmak üzere işaretlenir.

## Çıktı modülleri
- Kanun yolu takvimi (yol, süre, son gün, kesinlik durumu).
- Kesinlik sınırı doğrulama notu ([doğrulanacak]).
- Başvuru dilekçesi gerekleri çek-listesi.
<<<BECERI>>>
slug: icra-ve-takip-dosyasi-takibi
ad: İcra ve Takip Dosyası Takibi
aciklama: Bir ilamlı veya ilamsız icra takibinin aşamasını, itiraz/itirazın iptali sürelerini, haciz ve satış adımlarını izlemek gerektiğinde kullan.
<<<GOVDE>>>
# İcra ve Takip Dosyası Takibi

## Görev
İcra takip dosyasının türünü, aşamasını ve kritik sürelerini izleyip haciz-satış-paraya çevirme zincirini takip etmek; itiraz ve süre kaynaklı hak kayıplarını önlemek.

## Soğuk başlangıç (intake)
- Takip türü ne: ilamlı, ilamsız, kambiyo senetlerine özgü, rehnin paraya çevrilmesi?
- Ödeme/icra emri tebliğ edildi mi, tarihi ne?
- Borçlu itiraz etti mi, ettiyse hangi tarihte?
- Haciz uygulandı mı, satış aşamasına gelindi mi?

## Denetim şeması
1. Tür ve aşama: ilamsız takipte ödeme emrine itiraz 7 gün (İİK m.62) → itiraz takibi durdurur → alacaklı itirazın iptali (İİK m.67, 1 yıl) ya da itirazın kaldırılması (İİK m.68) yoluna gider. Kambiyo takibinde itiraz 5 gün ve icra mahkemesine (İİK m.168, m.170).
2. İlamlı takip: ilama dayalı takipte icranın geri bırakılması (İİK m.33) dışında itirazla durmaz; tehir-i icra şartlarını kontrol et.
3. Haciz-satış zinciri: haciz talebi süresi (İİK m.78, ödeme emrinin kesinleşmesinden itibaren), satış isteme süresi (İİK m.106) ve düşme riski (İİK m.110); kıymet takdiri ve satış ilanı.
4. İstihkak ve şikâyet: üçüncü kişi istihkak iddiası (İİK m.96 vd.), icra memuru işlemine şikâyet (İİK m.16, kural 7 gün).
5. Ara sonuç: takibin kesinleşip kesinleşmediği, açık süreler ve sıradaki adım. Tarihler ve tutarlar yalnızca takip dosyasından alınır.

## Çıktı modülleri
- Takip aşaması ve süre takvimi tablosu.
- İtiraz/itirazın iptali/kaldırılması karar ağacı notu.
- Haciz-satış adım takibi ve düşme riski uyarısı.
<<<BECERI>>>
slug: uyap-evrak-yonetimi
ad: UYAP ve Evrak Yönetimi
aciklama: UYAP üzerinden gelen evrakı, e-tebligatları ve dosya dökümlerini düzenli bir evrak listesine bağlamak, tebliğ tarihlerini ve evrak bütünlüğünü doğrulamak gerektiğinde kullan.
<<<GOVDE>>>
# UYAP ve Evrak Yönetimi

## Görev
UYAP'tan gelen evrakı, e-tebligatları ve dosya safahatını numaralı, tarihli ve sayfa referanslı bir evrak listesine dönüştürmek; tebliğ tarihlerini ve evrak bütünlüğünü doğrulayarak süre takvimini beslemek.

## Soğuk başlangıç (intake)
- Elinde UYAP safahat dökümü, e-tebligat kayıtları veya taranmış evrak var mı?
- Hangi evrakın tebliğ tarihi kritik (karar, bilirkişi raporu, dava dilekçesi)?
- Evrak numaralandırılmış/sayfalanmış mı?
- Eksik veya okunaksız belge var mı?

## Denetim şeması
1. Evrak envanteri: her belgeye sıra no, tarih, tür, gönderen/alıcı ve sayfa aralığı ver; safahat dökümüyle eşleştir. Eksik sıra varsa [doldurulacak].
2. Tebliğ doğrulama: e-tebligatta tebliğ tarihi muhatabın elektronik adrese ulaşmasından itibaren beşinci günün sonu sayılır (7201 sayılı Tebligat Kanunu m.7/a); bu tarihi süre takvimine tetikleyici olarak aktar.
3. Bütünlük kontrolü: eki olduğu belirtilen ama dosyada bulunmayan ekler, imzasız/okunaksız sayfalar ayrı not.
4. Süre köprüsü: tebliğ tarihi belirlenen her evrak için tetiklediği süre (cevap, itiraz, kanun yolu) Süre Takvimi becerisine devredilir; çift kayıt önlenir.
5. Ara sonuç: numaralı evrak listesi + doğrulanmış tebliğ tarihleri + eksik/okunaksız liste. Tarihler UYAP kaydından alınır; tahmin edilmez.

## Çıktı modülleri
- Numaralı evrak listesi (no, tarih, tür, taraf, sayfa).
- Tebliğ tarihi doğrulama tablosu.
- Eksik/okunaksız evrak ve eklerin listesi.
<<<SON>>>
