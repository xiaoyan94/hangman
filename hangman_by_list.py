#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from random import randint
#词库
wordList = ['nice','experience','my','heart','crystal','ubuntu',\
			'eye','hello','is','am','are','jump','like','love',\
			'funy','python','linux','unix','good','word','world']
#词库随机选一个词
word = list(wordList[randint(0,len(wordList) - 1)])
length = len(word)
print length,u"个字母的单词：","_ "*length
#存储猜过的字母
guess_str = list("_"*length)
#生命值
life = 10
#循环猜单词
while True and guess_str!=word and life > 0:
	print u"\n剩余",life,u"条命"
	#letter保存所猜字母
	letter = raw_input("Enter a letter: ")
	if not 'a'<=letter <='z' or len(str(letter)) > 1:
		print "Wrong input!"
		print " ".join(guess_str)
		continue
	#所猜字母不在单词中 死一次
	if letter not in word:
		life = life -1
		print " ".join(guess_str)

	#所猜字母在单词中出现一次 并且是第一次猜 则猜中
	elif word.count(letter) == 1 and letter not in guess_str:
		pos = word.index(letter)
		guess_str[pos] = letter
		print " ".join(guess_str)
	#                        第二次猜 死

	#所猜字母在单词中出现多次 并且是第一次猜对 则猜中
	elif word.count(letter) > 1 and letter not in guess_str:
		pos = word.index(letter)
		guess_str[pos] = letter
		print " ".join(guess_str)	

	#所猜字母在单词中出现多次 但不是第一次猜对 
	elif guess_str.count(letter) < word.count(letter):
		guess_str.reverse()
		pos0 = guess_str.index(letter)
		guess_str.reverse()
		pos = word.index(letter,length - pos0)
		guess_str[pos] = letter
		print " ".join(guess_str)
	#其他情况 没猜中 死
	else:
		life = life -1
		print " ".join(guess_str)
#猜中所有字母
if life > 0:
	print "\nNice! You are so smart."
#生命值消耗完
else:
	print u"\nShame! 正确的单词：","".join(word)


#---the end---
os.system("pause")





















