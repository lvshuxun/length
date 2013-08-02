input_name=r"input.txt"
output_name=r"out.txt"
fo=open(output_name,'w')
fo.write("lvshuxun@126.com\n")
bIsDic=True
dTra=dict()
dTra['m']=1.0
with open(input_name) as fi:
	for line in fi:
		if line[-1]=="\n":
			line =line[:-1]
		#print line
		if line=="":
			bIsDic=False
		else:
			aS=line.split(" ")
			#print aS
			if bIsDic:
				fTmp=float(aS[3])/float(aS[0])
				dTra[aS[1]]=fTmp
				if aS[1]=="foot" :
					dTra["feet"]=fTmp
				elif aS[1]=="inch":
					dTra["inches"]=fTmp
				else:
					dTra[aS[1]+'s']=fTmp
			else:
				iPtr=0
				fTmp=0.0
				iFlag=1
				while iPtr<len(aS):
					fTmp += iFlag * float(aS[iPtr]) * dTra.get(aS[iPtr+1])
					iPtr += 2
					if iPtr<len(aS):
						if aS[iPtr]=="-":
							iFlag = -1
						else:
							iFlag = 1
						iPtr += 1
				fo.write("\n%3.2f m"%fTmp)


fo.close()
fi.close()
