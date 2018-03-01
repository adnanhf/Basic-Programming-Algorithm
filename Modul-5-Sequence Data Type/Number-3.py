def countWordnSentence(sentences):
  word,sentence=1,0
  for letter in sentences:
    if letter == '.':
      sentence+=1
    elif letter == ' ':
      word+=1

  return word,sentence

def main():
  mysentence=input('Masukkan kalimat: ')
  word_sum,sentence_sum=countWordnSentence(mysentence)
  print(' jumlah kata:',word_sum,'\njumlah kalimat:',sentence_sum)

if __name__ == '__main__':
  main()
