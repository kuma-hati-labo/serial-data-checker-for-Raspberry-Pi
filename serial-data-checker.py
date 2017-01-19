# -*- coding: utf-8 -*-
#
#	0x00-0xFF �̏z�f�[�^�̃`�F�b�N�v���O����
#	�V���A������ 0x00-0xFF �̏z�f�[�^����͂��A�������f�[�^��
#	�����Ă��邩���m�F����v���O����
#	���̃v���O�������N�����Ă���f�[�^�̑��o���J�n���邱��
#
import serial
import sys

argvs = sys.argv
argc = len(argvs)
if (argc != 2):
	print u"Error:Need transfar rate"
	sys.exit()

ser = serial.Serial('/dev/ttyAMA0', int(argvs[1]), timeout=5)

n = 0;
e = 0;
while 1:
	data = ser.read(256)
	i = 0;
	while i < 256:
		try:
			if ord(data[i]) != i:
				print n ,
				print "E",
				e += 1
		except IndexError:
			print "Packt count",
			print n,
			print "Error count",
			print e
			sys.exit()
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
		i += 1
	print ".",
	n += 1;
ser.close()
