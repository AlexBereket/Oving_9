# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 18:45:06 2021

@author: Bruker
"""

class Sporsmaal:
    def __init__(self, sporsmaal , alternativer , svar=0):
        self.sporsmaal = sporsmaal
        self.svar = svar
        self.alternativer = alternativer
        
    def __str__(self):
        resultat = self.sporsmaal + " \nSvaralternativer: \n"
        for index, verdi in enumerate(self.alternativer):
            resultat += f"{index +1}: {verdi}\n"
        return resultat

    def sjekk_svar(self, bruker_svar):
        if bruker_svar - 1 == self.svar:
            return True
        else:
            return False 
        
    def korrekt_svar_tekst(self):
        korrekt= self.alternativer[self.svar]
        return korrekt

spiller_1_poeng = []
spiller_2_poeng = []

def Quiz():
    
    with open("sporsmaalsfil.txt","r",encoding = "UTF8") as fil:
        for linje in fil:
            linje = linje.split(":")
            alternativ = linje[2].replace("["," ").replace("]"," ")
            quiz_spørsmål = Sporsmaal(linje[0], alternativ.split(","), int(linje[1]))
            print (quiz_spørsmål)
            
            spiller_1_svar = int(input("Skriv inn svaret til spiller 1:"))
            spiller_2_svar = int(input("Skriv inn svaret til spiller 2:"))
            
            if quiz_spørsmål.sjekk_svar(spiller_1_svar):
                print("\nSpiller 1: Korrekt")
                spiller_1_poeng.append(1)
            else:
                print("\nSpiller 1: Feil svar")




            if quiz_spørsmål.sjekk_svar(spiller_2_svar):
                print("\nSpiller 2: Korrekt")
                spiller_2_poeng.append(1)
                print(f"Korrekt svar: {quiz_spørsmål.korrekt_svar_tekst()}\n")
            else:
                print("\nSpiller 2: Feil svar")
                print(f"Korrekt svar: {quiz_spørsmål.korrekt_svar_tekst()}\n")

if __name__ == "__main__":
    Quiz()
    print("Resultat:")
    print("Spiller: 1", len(spiller_1_poeng))
    print("Spiller 2:", len(spiller_2_poeng))               
                
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    