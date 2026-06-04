> ⚠️ Bu belge tamamen KURGUSAL ve anonimdir; gerçek bir kişi, olay veya dava ile ilgisi yoktur. Eğitim/deneme amaçlıdır.

# Çek Bilgileri ve Şekil Şartları Denetimi

## 1. Çekin Künyesi (Kurgusal)

| Alan | İçerik |
|------|--------|
| Senet türü | Çek (TTK m.780) |
| Çek seri / no (kurgusal) | KRG-0042-7781234 |
| Keşideci (borçlu) | Çelik Mobilya Sanayi ve Ticaret A.Ş. |
| Lehtar / hamil (alacaklı) | Demir Yapı İnşaat Malzemeleri Ltd. Şti. |
| Muhatap banka | (M) Bankası A.Ş. |
| Şube | Ataşehir Şubesi (kurgusal) |
| IBAN / hesap (kurgusal) | TR00 0000 0000 0000 0000 0000 00 |
| Bedel (rakamla) | 250.000,00 TL |
| Bedel (yazıyla) | İkiyüzellibin Türk Lirası |
| Keşide yeri | İstanbul |
| Keşide tarihi (üzerinde yazılı) | 20.03.2025 |
| Düzenlenme (teslim) tarihi | 15.01.2025 |
| İbraz tarihi | 24.03.2025 |
| Para birimi | Türk Lirası (TL) |

## 2. Zorunlu Şekil Şartları Denetimi (TTK m.780)

| # | Unsur (TTK m.780/1) | Bu çekte | Durum |
|---|----------------------|----------|-------|
| 1 | "Çek" kelimesi (senet dili Türkçe ise) | Var | ✓ |
| 2 | Kayıtsız ve şartsız belirli bir bedelin ödenmesi için havale | Var | ✓ |
| 3 | Muhatabın (bankanın) ticaret unvanı | (M) Bankası A.Ş. | ✓ |
| 4 | Ödeme yeri | Ataşehir Şubesi / İstanbul | ✓ |
| 5 | Düzenlenme tarihi ve yeri | 20.03.2025 — İstanbul | ✓ |
| 6 | Düzenleyenin (keşidecinin) imzası | Çelik Mobilya A.Ş. yetkili imza | ✓ |

> **Tamamlayıcı kurallar (TTK m.781):**
> - Ödeme yeri gösterilmemişse, muhatabın ticaret unvanı yanındaki yer ödeme yeri sayılır.
> - Düzenlenme yeri gösterilmemişse, düzenleyenin (keşidecinin) adı yanında yazılı yer düzenlenme yeri sayılır.
> - Bu denetim örneğinde tüm zorunlu unsurlar mevcuttur; senet **geçerli çek** olarak değerlendirilmiştir.

## 3. İbraz Süresi Analizi (TTK m.796)

- Düzenlendiği yer ile ödeneceği yer **aynı ise** ibraz süresi **10 gün**.
- Düzenlendiği yerden başka bir yerde ödenecekse **1 ay**.
- Bu örnekte keşide yeri ve ödeme yeri İstanbul (aynı yer) kabul edildiğinden ibraz süresi **10 gündür**.
- Süre, çekin üzerinde yazılı keşide tarihinden (20.03.2025) işlemeye başlar.
- İbraz tarihi **24.03.2025**; süresi içinde ibraz edilmiştir.

> Karşılıksızdır kaydının müracaat hakkı doğurması için çekin **ibraz süresi içinde** muhataba ibrazı gerekir (TTK m.808). Burada bu koşul sağlanmıştır.

## 4. Karşılıksızdır İşlemi (TTK m.808 / 5941 s. Çek K. m.3)

| Alan | İçerik |
|------|--------|
| Toplam çek bedeli | 250.000,00 TL |
| Bankaca yapılan kısmi ödeme | 60.000,00 TL |
| Karşılıksız kalan bakiye | 190.000,00 TL |
| Karşılıksızdır kaydı tarihi | 24.03.2025 |
| Kaydı düşen | (M) Bankası A.Ş. Ataşehir Şubesi (kaşe + imza) |
| Kayıt yeri | Çekin arka yüzü |

> Muhatap banka, kısmi karşılık varsa bu kısmı ödemekle yükümlüdür ve kalan bedel için karşılıksızdır işlemi yapar (5941 s. K. m.3). Bu kayıt, protesto yerine geçerek hamile müracaat (rücu) hakkı sağlar (TTK m.808/3).

## 5. Ciro Zinciri (Varsayımsal)

Senedin müracaat haklarının test edilmesi için varsayımsal ciro:

```
Keşideci: Çelik Mobilya A.Ş.
  └── Lehtar: Demir Yapı Ltd. Şti. (ilk hamil)
        └── (varsayımsal) ciro → Kuzey Lojistik Ltd. Şti.
              └── (varsayımsal) ciro → Demir Yapı Ltd. Şti. (son hamil olarak geri alındı)
```

> Tam ve düzenli bir ciro silsilesi (TTK m.790) varsa, son hamil meşru hamil sayılır ve karşılıksız işlem sonrası keşideci ile tüm cirantalara müracaat edebilir (TTK m.788, m.818).

## 6. Zamanaşımı (TTK m.814)

- Hamilin, cirantalar ve keşideci aleyhindeki başvurma hakları **ibraz süresinin bitiminden itibaren 3 yıl** geçmekle zamanaşımına uğrar.
- Bu örnekte ibraz süresi sonu (yaklaşık 30.03.2025) esas alınarak zamanaşımının son günü hesaplanmalıdır. [hesap doğrulanacak]

---

## 7. Veri Tablosu (CSV)

Aşağıdaki tablo, çek alacak kalemlerinin makine-okunur dökümüdür (CSV formatı):

```csv
kalem,aciklama,tutar_TL,tarih,mevzuat
cek_bedeli_toplam,Cekin toplam bedeli,250000.00,2025-03-20,TTK m.780
kismi_odeme,Bankaca yapilan kismi odeme,60000.00,2025-03-24,5941 s. K. m.3
bakiye,Karsiliksiz kalan bakiye,190000.00,2025-03-24,TTK m.808
isleyen_faiz,Ibraz tarihinden takip tarihine faiz,0.00,2025-04-10,TTK m.1530/7
ihtar_gideri,Noter ihtarname masrafi,0.00,2025-03-28,
takip_gideri,Icra takip giderleri,0.00,2025-04-10,Icra Tarifesi
```

> Not: Faiz ve gider tutarları senaryoda 0.00 bırakılmıştır; beceri denemesinde hesaplattırılabilir.
