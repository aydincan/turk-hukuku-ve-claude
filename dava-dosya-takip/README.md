# Dava ve Dosya Takip Yardımcısı

Dava dosyası işleme: yapılandırılmış dosya özeti, taraf-vekil ve süre takvimi, vakıa kronolojisi, delil dizini ve eksik/çelişki listesi; dosyaya hızlı hâkim olmayı sağlayan Excel'lenebilir çıktılar.

**Başat mevzuat:** HMK 6100, CMK 5271

## Beceriler

- `genel-bakis` — Giriş, triyaj ve yönlendirme (önce bunu çalıştırın).
- `dosya-ozeti-cikarma` — Dağınık bir dava dosyasından künye, talep, taraflar ve aşamayı tek sayfalık yapılandırılmış özete dönüştürmek gerektiğinde; yeni gelen veya devralınan dosyaya hızlı hâkim olmak için kullan.
- `taraf-vekil-tablosu` — Çok taraflı veya birden çok vekilli dosyalarda taraf-sıfat-vekil-adres-tebligat ilişkisini netleştirmek ve tebligat ile husumet hatalarını önlemek için tablo kurarken kullan.
- `vakia-kronolojisi` — Olayların ve usul işlemlerinin tarih sırasıyla dizilmesi, her vakıanın dayandığı evraka bağlanması ve zaman içindeki boşlukların görülmesi gerektiğinde kullan.
- `sure-takvimi-ve-zamanasimi` — Cevap, itiraz, istinaf, temyiz gibi usul süreleri ile zamanaşımı/hak düşürücü sürelerin son günlerini dayanak maddeyle hesaplayıp takvime bağlamak gerektiğinde kullan.
- `delil-dizini-ve-ispat-yuku` — Dosyadaki delilleri dizinleyip her birini ilgili vakıaya ve ispat yüküne bağlamak, sunulan-beklenen-itirazlı delilleri ayırt etmek gerektiğinde kullan.
- `eksik-ve-celiski-listesi` — Dosyada cevaplanmamış iddiaları, ibraz edilmemiş delilleri ve taraf beyanları arasındaki çelişkileri sistematik biçimde tespit etmek gerektiğinde kullan.
- `durusma-hazirlik-ve-ara-karar-takibi` — Yaklaşan duruşmaya hazırlanmak, tensip ve ara kararların gereklerini izlemek, her celse için yapılacaklar ve verilecek beyanları listelemek gerektiğinde kullan.
- `gorev-ve-yetki-kontrolu` — Davanın doğru görevli ve yetkili mahkemede açılıp açılmadığını, görevsizlik-yetkisizlik veya gönderme riskini denetlemek gerektiğinde kullan.
- `kanun-yolu-takibi` — Karar sonrası istinaf ve temyiz yollarının açık olup olmadığını, süreleri, kesinlik sınırlarını ve dilekçe gereklerini izlemek gerektiğinde kullan.
- `icra-ve-takip-dosyasi-takibi` — Bir ilamlı veya ilamsız icra takibinin aşamasını, itiraz/itirazın iptali sürelerini, haciz ve satış adımlarını izlemek gerektiğinde kullan.
- `uyap-evrak-yonetimi` — UYAP üzerinden gelen evrakı, e-tebligatları ve dosya dökümlerini düzenli bir evrak listesine bağlamak, tebliğ tarihlerini ve evrak bütünlüğünü doğrulamak gerektiğinde kullan.

## Kullanım

```
/plugin install dava-dosya-takip@turk-hukuku-skills
```

Eklenti kurulduktan sonra Claude'a olayınızı anlatın ya da belgeyi yükleyin; `genel-bakis`
becerisi sizi uygun uzman beceriye yönlendirir.

---

> ⚠️ **Sorumluluk reddi:** Bu eklenti deneyseldir ve **hukuki danışmanlık değildir**.
> Çıktılar yürürlükteki mevzuat ve doğrulanmış içtihatla teyit edilmelidir. Nihai
> sorumluluk yetkili hukukçudadır. Ayrıntı için kökteki `SORUMLULUK-REDDI.md`.
