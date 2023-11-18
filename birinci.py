
def selamla(isim):
    print(f"merhaba {isim}")
    
def main():
    
    barbie = Barbie("mor",
                    "mavi",
                    "beyaz",
                    "açık pembe",
                    "lila",
                    "açık mavi",
                    "barbie")
    
    
    
    isim = barbie.isim
    selamla(isim=isim)



class Barbie:
    
    def __init__(self, sac_rengi, goz_rengi, elbise_ust, elbise_alt, ayakkabı, bilezik, isim):
      self.isim = isim
      self.sac_rengi = sac_rengi
      self.goz_rengi = goz_rengi
      self.elbise_ust = elbise_ust
      self.elbise_alt =elbise_alt
      self.ayakkabı = ayakkabı
      self.bilezik = bilezik
      
    
if __name__ == "__main__":
    main()

