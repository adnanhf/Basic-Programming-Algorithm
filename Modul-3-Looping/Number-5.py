vocal,consonant,mywords = 0,0,input("Masukkan kalimat : ")
for letter in mywords:
  if letter in 'aiueoAIUEO':
    vocal+=1
  elif letter not in 'aiueoAIUEO' and letter!=' ':
    consonant+=1
print("Banyak Vokal : ",vocal)
print("Banyak Konsonan : ",consonant)
