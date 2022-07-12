def order(sentence):
  sentence_list = sentence.split(' ')
  number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  sentence_res = {}
  sentence_res_ = ''
  for i in sentence_list:
    for n in number:
      if n in i:
        sentence_res[n] = i
  for key in range(1, len(sentence_res) + 1):
    sentence_res_ += sentence_res[str(key)]
    sentence_res_ += ' '
  return  sentence_res_


print(order("is2 Thi1s T4est 3a 5gfgf 6etwtge"))
