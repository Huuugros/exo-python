pSeuil,vSeuil=2.3,7.41
pression,volume=float(input()),float(input())
if (volume > vSeuil and pression >pSeuil):
    print('arret totale')
elif (pression > pSeuil):
    print("augmenter le volume de l'enceinte")
elif(volume>vSeuil):
    print("diminuer le volume de l'enceinte")
else:
    print('TOUT VA BIEN')