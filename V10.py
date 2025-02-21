file_path = 'stocks/stocks/htlf.us.txt' 
import pandas

file = open(file_path, 'r')
lines = file.readlines()
oc = []
totaln = 0
totalv = 0
close = []
lines.pop(0)
for line in lines:
  data = line.split(',')
  totalv += float(data[4]) - float(data[7])
  totaln +=1
  close.append(float(data[7]))
  oc.append([float(data[4]),float(data[7])])
avgreturn = totalv/totaln
riskrate = 0.03
df = pandas.DataFrame(close,columns=["close"])
stdrate = df["close"].std()
sr = (avgreturn-riskrate)/stdrate
print(sr)
