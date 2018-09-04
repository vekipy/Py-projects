import sys
import time

def Meni ():
 print ('\nIzaberite program koji zelite iz menija:\n 3-Izgradnja zida\n 5-Igra lavirint\n\
 8-Ocene\n 9- Izlaz')
 return 
     


def zid ():
    dz=input('Uneti duzinu zida: ');
    vz=input('Uneti visinu zida: ');
    dc=input('Uneti duzinu cigle: ');
    vc=input('Uneti visinu cigle: ');
    brpoduz=float(dz)/(dc);
    brpovis=float(vz)/(vc);
    brcigala=brpoduz*brpovis;
    print ("Broj cigala je  "+ str(brcigala))
    return

def lavirint ():
 def ras_1 ():
     unos=raw_input ('Naisli ste na raskrsnicu. \n Mozete ici levo ili desno, izaberite:');
     if unos=='d':
         print ('Odabrali ste desno')
         slepa_2 ()
     elif unos=='l':
         print ('Odabrali ste levo')
         ras_2 ()
     return
 def ras_2 ():
     print ('Hodate dugackim hodnikom...')
     time.sleep (2)
     unos=raw_input ('Naisli ste na raskrsnicu. \n Mozete ici pravo ili desno, izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         slepa_1 ()
     elif unos=='d':
         print ('Odabrali ste desno')
         ras_3 ()
     return
 def slepa_2 ():
     print ('Usli ste u slepu ulicu. Okrecete se nazad.')
     time.sleep (2)
     print ('Posle 2 minuta nailazite na raskrsnicu')
     unos=raw_input ('Naisli ste na raskrsnicu. \n Mozete ici pravo ili levo, izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         ras_2 ()
     elif unos=='l':
         print ('Odabrali ste levo. \n Vratili ste se na pocetak lavirinta.\n Okrecete se i hodate pravo')
         ras_1 ()
     return
 def slepa_1 ():
     print ('Usli ste u slepu ulicu. Okrecete se nazad.')
     time.sleep (2)
     unos=raw_input ('Naisli ste na raskrsnicu. \n Mozete ici pravo ili levo, izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         ras_1_prim ()
     elif unos=='l':
         print ('Odabrali ste levo')
         ras_3 ()
     return  
 def ras_1_prim ():
     unos=raw_input ('Vratili ste na raskrsnicu. \n Mozete ici pravo ili desno, izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         slepa_2 ()
     elif unos=='d':
         print ('Odabrali ste desno. \n Vratili ste se na pocetak lavirinta.\n Okrecete se i hodate pravo')
         ras_1 ()
     return

 def ras_2_prim ():
     unos=raw_input ('Naisli ste na raskrsnicu. \n Mozete ici levo ili desno, izaberite:');
     if unos=='l':
         print ('Odabrali ste da idete levo')
         ras_1_prim ()
     elif unos=='d':
         print ('Odabrali ste desno')
         slepa_1 ()
     return

 def ras_3 ():
    print ('Hodate izmedju drvoreda...')
    time.sleep (2)
    unos=raw_input ('Nailazite na raskrsnicu. \n Mozete ici pravo ili desno, izaberite:');
    if unos=='p':
         print ('Odabrali ste da idete pravo')
         ras_4 ()
    elif unos=='d':
         print ('Odabrali ste desno')
         ras_5 ()
    return

 def ras_3_prim ():
     unos=raw_input ('Naisli ste ste na raskrsnicu. \n Mozete ici pravo ili levo, izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         ras_2_prim ()
     elif unos=='l':
         print ('Odabrali ste levo')
         ras_5 ()
     return

 def ras_4 ():
     unos=raw_input ('Posle dugog hodanja naisli ste na raskrsnicu. \n Mozete ici pravo ili desno, izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         slepa_3 ()
     elif unos=='d':
         print ('Odabrali ste desno')
         time.sleep (2)
         print ('Idete osvetljenom stazom...\n Nailazite na drveni most. Oprezno predjite preko.')
         time.sleep (1.5)
         print ('Presli ste most, nastavljate da hodate, ored vama je krivina udesno.\n Skrecete i hodate pravo nizbrdo... ')
         ras_5_prim ()
     return

 def slepa_3 ():
     print ('Ovo je slepa ulica. Okrenite se i vratite nazad')
     time.sleep (1)
     unos=raw_input ('Vratili ste na raskrsnicu. \n Mozete ici pravo ili levo, izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         ras_3_prim ()
     elif unos=='l':
         print ('Odabrali ste levo.\n Prelazite preko mosta. Skrecete desno i hodate nizbrdo')
         ras_5_prim ()
     return
 def ras_5 ():
     unos=raw_input ('Nailazite na veliku raskrsnicu. \n Mozete ici pravo, levo ili desno. Izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         ras_6 ()
     elif unos=='l':
         print ('Odabrali ste levo.\n Hodate uzbrdo, skrecete levo i prelazite most.')
         ras_4_prim ()
     elif unos=='d':
         print ('Odabrali ste desno')
         slepa_4 ()
     return

 def slepa_5 ():
     print ('Upali ste u mocvaru, ovo je slepa ulica. Okrenite se i vratite nazad')
     time.sleep (1)
     unos=raw_input ('Vratili ste na raskrsnicu. \n Mozete ici pravo ili desno, izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         ras_5_sec ()
     elif unos=='d':
         print ('Odabrali ste desno')
         print ('Cestitamo, pronasli ste BLAGO! :)')
     return

 def ras_6 ():
     unos=raw_input ('Dosli ste do raskrsnice. \n Mozete ici pravo ili levo. Izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         slepa_5 ()
     elif unos=='l':
         print ('Odabrali ste levo')
         print ('Cestitamo, pronasli ste BLAGO! :)')
     return

 def ras_5_prim ():
     unos=raw_input ('Dosli ste do velike raskrsnice. \n Mozete ici pravo, desno ili levo. Izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         slepa_4 ()
     elif unos=='l':
         print ('Odabrali ste levo')
         ras_6 ()
     elif unos=='d':
         print ('Odabrali ste da idete desno')
         ras_3_sec ()
     return

 def ras_5_sec ():
     unos=raw_input ('Dosli ste do raskrsnice. \n Mozete ici pravo, levo ili desno. Izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo')
         ras_3_prim ()
     elif unos=='l':
         print ('Odabrali ste levo')
         slepa_4 ()
     elif unos=='d':
         print ('Odabrali ste da idete desno')
         ras_4_prim ()
     return

 def ras_4_prim ():
     unos=raw_input ('Dosli ste do raskrsnice. \n Mozete ici desno ili levo. Izaberite:');
     if unos=='d':
         print ('Odabrali ste da idete desno')
         slepa_3 ()
     elif unos=='l':
         print ('Odabrali ste levo')
         ras_3_prim ()
     return

 def slepa_4 ():
     unos=raw_input ('Usli ste u slepu ulicu, okrenite se i \n vratite se nazad. \n Mozete ici pravo, desno ili levo. Izaberite:');
     if unos=='d':
         print ('Odabrali ste da idete desno')
         ras_6 ()
     elif unos=='l':
         print ('Odabrali ste levo')
         ras_3_sec ()
     elif unos=='p':
         print ('Odabrali ste pravo')
         ras_4_prim ()
     return

 def ras_3_sec ():
     unos=raw_input ('Dosli ste do raskrsnice. \n Mozete ici desno ili levo. Izaberite:');
     if unos=='d':
         print ('Odabrali ste da idete desno')
         ras_4 ()
     elif unos=='l':
         print ('Odabrali ste levo')
         ras_2_prim ()
     return

 print ('Dobro dosli u igru Lavirint. Vas zadatak je da pronadjete cup sa zlatom. \
            \n Unosenjem slova sa tastature: l,d,p birate kuda cete ici na raskrsnicama \
            \n l- levo, d- desno ili p-pravo')
 time.sleep (2)
 print ('Spremni....\n Pocinjemo!')
 time.sleep (1)
 print ('Otvarate velika drvena vrata, pred Vama se pruza dugacak put...')
 time.sleep (1)
 print ('Hodate pravo...')
 ras_1 ();
 return
                
              
def ocene ():
    br_petica=0;
    br_jedinica=0;
    
    while True:
        b=input('Unesi ocenu  ');
        if b==5:
            br_petica=br_petica+1;
        elif b==1:
            br_jedinica=br_jedinica+1;
        elif 1>b or b>5:
            break
         
    print ('Broj petica je '+ str(br_petica))
    print ('Broj jedinica je '+ str(br_jedinica))
    return
    
def Program ():
    while True:
     Meni ()
     a=input('Uneti svoj izbor (3,5,8 ili 9): ');
     if a==3:
        zid ()
     elif a==5:
        lavirint ()
     elif a==8:
        ocene ()
     elif a==9:
        print ('Izlazak iz programa')
        sys.exit ()
     else:
        print ('Uneli ste pogresnu vrednost, odaberite ponovo')
     time.sleep (1)
    return (a)

Program ();
        
