
#Autor: A.Veljovic (vekipy)
#The program allows you to choose from menu what task you want to execute. You can choose between three tasks or to exit
#by typing given number from the list.

import sys
import time

def Meni ():
 print ('\nIzaberite program koji zelite iz menija (Choose from the menu):\n 3-Izgradnja zida(Wall building)\n 5-Igra lavirint (Labyrint game)\n\
 8-Ocene (School notes)\n 9- Izlaz (Exit)')
 return 
     


def zid ():
    dz=input('Uneti duzinu zida (Input length of the wall): ');
    vz=input('Uneti visinu zida (Input height of the wall): ');
    dc=input('Uneti duzinu cigle (Input lenght of the brick): ');
    vc=input('Uneti visinu cigle (Input height of the brick): ');
    brpoduz=float(dz)/(dc);
    brpovis=float(vz)/(vc);
    brcigala=brpoduz*brpovis;
    print ("Broj cigala je (The number of bricks is)  "+ str(brcigala))
    return

def lavirint ():
 def ras_1 ():
     unos=raw_input ('Naisli ste na raskrsnicu(You arrived on intersection ). \n Mozete ici levo ili desno, izaberite \n \
     (You can go left or right, choose): ');
     if unos=='d':
         print ('Odabrali ste desno. (You have chosen right)')
         slepa_2 ()
     elif unos=='l':
         print ('Odabrali ste levo (You have chosen left)')
         ras_2 ()
     return
 def ras_2 ():
     print ('Hodate dugackim hodnikom...(You are walking through long hallway)')
     time.sleep (2)
     unos=raw_input ('Naisli ste na raskrsnicu (You arrived on intersection).\
     \n Mozete ici pravo ili desno, izaberite (Choose right or straight): ');
     if unos=='p':
         print ('Odabrali ste da idete pravo (You have chosen straight )')
         slepa_1 ()
     elif unos=='d':
         print ('Odabrali ste desno (You have chosen right)')
         ras_3 ()
     return
 def slepa_2 ():
     print ('Usli ste u slepu ulicu. Okrecete se nazad. \n \
     (You enter the blind street. You are turning back)')
     time.sleep (2)
     print ('Posle 2 minuta nailazite na raskrsnicu (After 2 minutes you have arrived on intersection)')
     unos=raw_input ('Naisli ste na raskrsnicu. \n Mozete ici pravo ili levo, izaberite: \
     (You can go straight or left. Choose:) ');
     if unos=='p':
         print ('Odabrali ste da idete pravo (You have chosen to go straight)')
         ras_2 ()
     elif unos=='l':
         print ('Odabrali ste levo. \n Vratili ste se na pocetak lavirinta.\n Okrecete se i hodate pravo \
         (You have chosen left. You have been returned on the begining of labyrinth. You have been truned around and have walked straight )')
         ras_1 ()
     return
 def slepa_1 ():
     print ('Usli ste u slepu ulicu. Okrecete se nazad. (You enter in blind street and you are turning back)')
     time.sleep (2)
     unos=raw_input ('Naisli ste na raskrsnicu. \n Mozete ici pravo ili levo, izaberite: \
     (You are on intersection. You can go straight or left, choose): ');
     if unos=='p':
         print ('Odabrali ste da idete pravo (You have chosen straight)')
         ras_1_prim ()
     elif unos=='l':
         print ('Odabrali ste levo (You have chosen left)')
         ras_3 ()
     return  
 def ras_1_prim ():
     unos=raw_input ('Vratili ste na raskrsnicu. \n Mozete ici pravo ili desno, izaberite: \
     (You are back on intersetion. You can go straight or right, choose): ');
     if unos=='p':
         print ('Odabrali ste da idete pravo (You have chosen straight): ')
         slepa_2 ()
     elif unos=='d':
         print ('Odabrali ste desno. \n Vratili ste se na pocetak lavirinta.\n Okrecete se i hodate pravo \
         (You have chosen right and you are at the begining of lybirinth. You are turned around and walk straight)')
         ras_1 ()
     return

 def ras_2_prim ():
     unos=raw_input ('Naisli ste na raskrsnicu. \n Mozete ici levo ili desno, izaberite \
     (You are on intersection. You can go left or right, choose): ');
     if unos=='l':
         print ('Odabrali ste da idete levo (You have chosen left)')
         ras_1_prim ()
     elif unos=='d':
         print ('Odabrali ste desno (You have chosen right): ')
         slepa_1 ()
     return

 def ras_3 ():
    print ('Hodate izmedju drvoreda...(You are walking through trees)')
    time.sleep (2)
    unos=raw_input ('Nailazite na raskrsnicu. \n Mozete ici pravo ili desno, izaberite \n (You are on intersection \
    You can go straight or right, choose): ');
    if unos=='p':
         print ('Odabrali ste da idete pravo(You have chosen straight)')
         ras_4 ()
    elif unos=='d':
         print ('Odabrali ste desno(You have chosen right)')
         ras_5 ()
    return

 def ras_3_prim ():
     unos=raw_input ('Naisli ste ste na raskrsnicu. \n Mozete ici pravo ili levo, izaberite \
     (You are on intersection. You can go straight or left, choose): ');
     if unos=='p':
         print ('Odabrali ste da idete pravo(You have chosen straight)')
         ras_2_prim ()
     elif unos=='l':
         print ('Odabrali ste levo(You have chosen left)')
         ras_5 ()
     return

 def ras_4 ():
     unos=raw_input ('Posle dugog hodanja naisli ste na raskrsnicu. \n Mozete ici pravo ili desno, izaberite \
     (After long walking you are coming on intersection. You can go straight or right, choose): ');
     if unos=='p':
         print ('Odabrali ste da idete pravo(You have chosen straight)')
         slepa_3 ()
     elif unos=='d':
         print ('Odabrali ste desno(You have chhosen right)')
         time.sleep (2)
         print ('Idete osvetljenom stazom...\n Nailazite na drveni most. Oprezno predjite preko.\n \
         (You are walking on the light track...There are wooden bridge in front of you. Go across carefuly)')
         time.sleep (1.5)
         print ('Presli ste most, nastavljate da hodate, pred vama je krivina udesno.\n Skrecete i hodate pravo nizbrdo...\n \
         (You have gone across the bridge, continue to walk. You are going right and continue straight...)')
         ras_5_prim ()
     return

 def slepa_3 ():
     print ('Ovo je slepa ulica. Okrenite se i vratite nazad \n (This is blind street, return back)')
     time.sleep (1)
     unos=raw_input ('Vratili ste na raskrsnicu. \n Mozete ici pravo ili levo, izaberite \n \
     (You are back on the intersection. You can go straight or left, choose): ');
     if unos=='p':
         print ('Odabrali ste da idete pravo(You have chosen straight)')
         ras_3_prim ()
     elif unos=='l':
         print ('Odabrali ste levo.\n Prelazite preko mosta. Skrecete desno i hodate nizbrdo. \n \
         (You have chosen right. You are going across the bridge, continue to the right and walking straight down the road.)')
         ras_5_prim ()
     return
 def ras_5 ():
     unos=raw_input ('Nailazite na veliku raskrsnicu. \n Mozete ici pravo, levo ili desno. Izaberite \n \
     (You are on big intersection):');
     if unos=='p':
         print ('Odabrali ste da idete pravo(You have chosen right)')
         ras_6 ()
     elif unos=='l':
         print ('Odabrali ste levo.\n Hodate uzbrdo, skrecete levo i prelazite most.(You have chosen right)')
         ras_4_prim ()
     elif unos=='d':
         print ('Odabrali ste desno(You have chosen right)')
         slepa_4 ()
     return

 def slepa_5 ():
     print ('Upali ste u mocvaru, ovo je slepa ulica. Okrenite se i vratite nazad')
     time.sleep (1)
     unos=raw_input ('Vratili ste na raskrsnicu. \n Mozete ici pravo ili desno, izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo(You have chosen right)')
         ras_5_sec ()
     elif unos=='d':
         print ('Odabrali ste desno(You have chosen right)')
         print ('Cestitamo, pronasli ste BLAGO! :)')
     return

 def ras_6 ():
     unos=raw_input ('Dosli ste do raskrsnice. \n Mozete ici pravo ili levo. Izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo(You have chosen right)')
         slepa_5 ()
     elif unos=='l':
         print ('Odabrali ste levo(You have chosen right)')
         print ('Cestitamo, pronasli ste BLAGO! :)')
     return

 def ras_5_prim ():
     unos=raw_input ('Dosli ste do velike raskrsnice. \n Mozete ici pravo, desno ili levo. Izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo(You have chosen right)')
         slepa_4 ()
     elif unos=='l':
         print ('Odabrali ste levo(You have chosen right)')
         ras_6 ()
     elif unos=='d':
         print ('Odabrali ste da idete desno(You have chosen right)')
         ras_3_sec ()
     return

 def ras_5_sec ():
     unos=raw_input ('Dosli ste do raskrsnice. \n Mozete ici pravo, levo ili desno. Izaberite:');
     if unos=='p':
         print ('Odabrali ste da idete pravo(You have chosen right)')
         ras_3_prim ()
     elif unos=='l':
         print ('Odabrali ste levo(You have chosen right)')
         slepa_4 ()
     elif unos=='d':
         print ('Odabrali ste da idete desno(You have chosen right)')
         ras_4_prim ()
     return

 def ras_4_prim ():
     unos=raw_input ('Dosli ste do raskrsnice. \n Mozete ici desno ili levo. Izaberite:');
     if unos=='d':
         print ('Odabrali ste da idete desno(You have chosen right)')
         slepa_3 ()
     elif unos=='l':
         print ('Odabrali ste levo(You have chosen right)')
         ras_3_prim ()
     return

 def slepa_4 ():
     unos=raw_input ('Usli ste u slepu ulicu, okrenite se i \n vratite se nazad. \n Mozete ici pravo, desno ili levo. Izaberite:');
     if unos=='d':
         print ('Odabrali ste da idete desno(You have chosen right)')
         ras_6 ()
     elif unos=='l':
         print ('Odabrali ste levo(You have chosen right)')
         ras_3_sec ()
     elif unos=='p':
         print ('Odabrali ste pravo(You have chosen right)')
         ras_4_prim ()
     return

 def ras_3_sec ():
     unos=raw_input ('Dosli ste do raskrsnice. \n Mozete ici desno ili levo. Izaberite:');
     if unos=='d':
         print ('Odabrali ste da idete desno(You have chosen right)')
         ras_4 ()
     elif unos=='l':
         print ('Odabrali ste levo(You have chosen right)')
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
        
