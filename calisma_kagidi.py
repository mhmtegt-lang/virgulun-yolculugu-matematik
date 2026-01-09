import random

def generate_worksheet(student_count=1):
    """
    Nöro-Bilişsel Mat Ders Planı için Çalışma Kağıdı Üretici.
    Kuramlar: Sayı Hissi (Tahmin), Bilgiyi İşleme (Kodlama).
    """
    
    print(f"--- VİRGÜLÜN YOLCULUĞU ÇALIŞMA KAĞIDI (Örnek) ---\n")
    
    for i in range(student_count):
        base_num = round(random.uniform(0.1, 9.99), 2) # Rastgele ondalık sayı
        multiplier = random.choice([10, 100, 1000])
        
        print(f"ÖĞRENCİ {i+1} İÇİN SORULAR:")
        
        # BÖLÜM 1: GÖRSEL KODLAMA (Ok çizme)
        print(f"1. SORU: {base_num} x {multiplier} işleminde virgül hangi yöne kaç adım gider?")
        print("   [ ] Sola  <--")
        print("   [ ] Sağa  -->")
        print(f"   Adım Sayısı: ______")
        
        # BÖLÜM 2: SAYI HİSSİ VE TAHMİN (Number Sense)
        # İşlem yapmadan büyüklük algısını ölçer.
        estimated_res = base_num * multiplier
        lower_bound = int(estimated_res * 0.5)
        upper_bound = int(estimated_res * 2)
        
        print(f"\n2. SORU (TAHMİN ET): {base_num} sayısını {multiplier} ile çarparsan sonuç sence hangisine yakın olur?")
        print(f"   A) {lower_bound} civarında (Küçük)")
        print(f"   B) {int(estimated_res)} civarında (Tam isabet)")
        print(f"   C) {upper_bound} civarında (Çok büyük)")
        
        # BÖLÜM 3: TERSİNE ÇEVİRME (Piaget - Reversibility)
        result = base_num * multiplier
        print(f"\n3. SORU: Bir sayıyı çarptık ve sonucu {result:.2f} bulduk. Eski haline ({base_num}) dönmek için ne yapmalıyız?")
        print("   _________________________________________________")
        print("-" * 40)

# Kodu çalıştır
if __name__ == "__main__":
    generate_worksheet(1)
