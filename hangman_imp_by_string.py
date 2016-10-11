#!/usr/bin/env python
#encoding:utf-8
from random import choice
wordList = ['experience','my','heart','crystal','ubuntu','eye','hello','is','am','are','jump','like','love','fuck','python','linux','unix']#词库
word = choice(wordList) 													# 词库随机选一个词
guess = list("_"*len(word)) 	
print len(word),u"个字母的单词："," ".join(guess)							# 存储猜过的字母
life = 10 																	# 生命值
while True:																	# 循环猜字母
	letter = raw_input('Enter a letter:')									# letter 保存所猜字母																	# i 保存循环次数（0,1,2,……）
	for i,x in enumerate(list(word)):													# x 遍历答案里的字母
		ltr_loc = "".join(guess).rfind(letter)								# 答案“hello”，已猜出”_ _ l _ o“，则第二次猜‘l’的位置是3
		if ((i > ltr_loc) or (ltr_loc < 0)) and (x == letter):				# i>loc跳过单词中已经猜过的字母
			guess[i] = letter
			life += 1
			break
	print u"已猜中部分："," ".join(guess),u"\n\n剩余",life-1,u"条命"	
	if (life > 0) and ("".join(guess) == word):
		print u"Nice！恭喜你猜对了！正确答案：",word
		break
	life -= 1
	if life == 0:
		print u"Shame！你死了！正确答案：",word
		break