#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from random import randint
#词库
try:
	f = open('wordlist.txt','r')
	wordlist = f.readlines()
	for i,line in enumerate(wordlist):
		wordlist[i] = line.strip()
	f.close()
except:
	wordlist = ['one','two','three','four','five','six','seven','eight','nine','ten']

while True:
	#词库随机选一个词
	word = list(wordlist[randint(0,len(wordlist) - 1)])
	length = len(word)
	print length,u"个字母的单词：","_ "*length
	#存储猜过的字母
	guess_str = list("_"*length)
	#生命值
	life = 10
	#循环猜单词
	while True and guess_str!=word and life > 0:
		print u"剩余",life,u"条命"
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
		print "Nice! You are so smart."
	#生命值消耗完
	else:
		print u"Shame! 正确的单词：","".join(word)
	print u'继续游戏吗？'
	char = raw_input('Enter \'q\' to quit. ')
	if char == 'q' or char == 'Q':
		print 'byebye~~ ^_^'
		break

#---the end---
os.system("pause")





















