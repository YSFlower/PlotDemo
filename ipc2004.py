# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xlrd 
import matplotlib.pyplot as plt

def ConvertData2Float(datalist):
    lf = []
    for f in datalist:
        if type(f) is float:
            lf.append(f)
        else:
            lf.append(None)
           
    return lf

#打开指定的文件 
datafile = r'E:\plot\pyxls\IPC4-hpZ230.xlsx'
data = xlrd.open_workbook(datafile) 

#设置整个图片区域
fig = plt.figure(1)
#plt.tight_layout()
left  = 0.125  # the left side of the subplots of the figure
right = 0.9    # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top = 0.9      # the top of the subplots of the figure
wspace = 0.4   # the amount of width reserved for blank space between subplots,
               # expressed as a fraction of the average axis width
hspace = 0.4   # the amount of height reserved for white space between subplots,
               # expressed as a fraction of the average axis height
plt.subplots_adjust(left, bottom, right, top, hspace, wspace)

#打开指定的工作表 0
sheetindex = 0
Nrows = 50
sheet = data.sheets()[sheetindex]
sheetname = sheet.name
sheetdomainname = sheetname.split('_')[0]
sheetdomainname = 'Airport'
# print sheetname, sheetdomainname

#获得所需列数据 
rowsrange = range(1, Nrows+1)
fftimecolx, asoptimecolx = 6, 17
ffcols = ConvertData2Float(sheet.col_values(fftimecolx))
asopcols = ConvertData2Float(sheet.col_values(asoptimecolx))

# print rowsrange
# print sheet.cell(0, fftimecolx).ctype #ctype: 2-number
# print len(ffcols), ffcols
# print len(asopcols), asopcols

#绘制图形
ax1 = plt.subplot(231)
ax1.set_title(sheetdomainname)
#ax1.set_xlabel('Tasks')
#ax1.set_ylabel('Running Time (s)')

plt.plot(rowsrange, ffcols[0: Nrows], marker='+', markersize=4, linestyle='-.', linewidth=1, label='FF')
plt.plot(rowsrange, asopcols[0: Nrows], marker='^', markersize=4, linestyle=':', linewidth=1, label='AOIP')
plt.semilogy(0.1, 1000)
plt.legend(loc='upper left', frameon=False, fontsize='x-small')

plt.xlim(0, Nrows)
plt.xticks([0, 25, 50])

#打开指定的工作表 1
sheetindex = 1
Nrows = 14
sheet = data.sheets()[sheetindex]
sheetname = sheet.name
sheetdomainname = sheetname.split('_')[0]
sheetdomainname = 'Promela \n(Optical Telegraph)'
# print sheetname, sheetdomainname

#获得所需列数据 
rowsrange = range(1, Nrows+1)
fftimecolx, asoptimecolx = 6, 17
ffcols = ConvertData2Float(sheet.col_values(fftimecolx))
asopcols = ConvertData2Float(sheet.col_values(asoptimecolx))

# print rowsrange
# print sheet.cell(0, fftimecolx).ctype #ctype: 2-number
# print len(ffcols), ffcols
# print len(asopcols), asopcols

#绘制图形
ax2 = plt.subplot(232)
ax2.set_title(sheetdomainname)
#ax2.set_xlabel('Tasks')
#ax2.set_ylabel('Running Time (s)')

plt.plot(rowsrange, ffcols[0: Nrows], marker='+', markersize=4, linestyle='-.', linewidth=1, label='FF')
plt.plot(rowsrange, asopcols[0: Nrows], marker='^', markersize=4, linestyle=':', linewidth=1, label='AOIP')
plt.semilogy(0.1, 1000)
plt.legend(loc='upper left', frameon=False, fontsize='x-small')

plt.xlim(0, Nrows)
plt.xticks([0, 7, 14])

#打开指定的工作表 2
sheetindex = 2
Nrows = 29
sheet = data.sheets()[sheetindex]
sheetname = sheet.name
sheetdomainname = sheetname.split('_')[0]
sheetdomainname = 'Promela \n(Philosophers)'
# print sheetname, sheetdomainname

#获得所需列数据 
rowsrange = range(1, Nrows+1)
fftimecolx, asoptimecolx = 6, 17
ffcols = ConvertData2Float(sheet.col_values(fftimecolx))
asopcols = ConvertData2Float(sheet.col_values(asoptimecolx))

# print rowsrange
# print sheet.cell(0, fftimecolx).ctype #ctype: 2-number
# print len(ffcols), ffcols
# print len(asopcols), asopcols

#绘制图形
ax3 = plt.subplot(233)
ax3.set_title(sheetdomainname)
#ax3.set_xlabel('Tasks')
#ax3.set_ylabel('Running Time (s)')

plt.plot(rowsrange, ffcols[0: Nrows], marker='+', markersize=4, linestyle='-.', linewidth=1, label='FF')
plt.plot(rowsrange, asopcols[0: Nrows], marker='^', markersize=4, linestyle=':', linewidth=1, label='AOIP')
plt.semilogy(0.1, 1000)
plt.legend(loc='upper left', frameon=False, fontsize='x-small')

plt.xlim(0, Nrows)
plt.xticks([0, 14, 29])

#打开指定的工作表 3
sheetindex = 3
Nrows = 29
sheet = data.sheets()[sheetindex]
sheetname = sheet.name
sheetdomainname = sheetname.split('_')[0]
sheetdomainname = 'PSR'
# print sheetname, sheetdomainname

#获得所需列数据 
rowsrange = range(1, Nrows+1)
fftimecolx, asoptimecolx = 6, 17
ffcols = ConvertData2Float(sheet.col_values(fftimecolx))
asopcols = ConvertData2Float(sheet.col_values(asoptimecolx))

# print rowsrange
# print sheet.cell(0, fftimecolx).ctype #ctype: 2-number
# print len(ffcols), ffcols
# print len(asopcols), asopcols

#绘制图形
ax4 = plt.subplot(234)
ax4.set_title(sheetdomainname)
#ax4.set_xlabel('Tasks')
#ax4.set_ylabel('Running Time (s)')

plt.plot(rowsrange, ffcols[0: Nrows], marker='+', markersize=4, linestyle='-.', linewidth=1, label='FF')
plt.plot(rowsrange, asopcols[0: Nrows], marker='^', markersize=4, linestyle=':', linewidth=1, label='AOIP')
plt.semilogy(0.1, 1000)
plt.legend(loc='upper left', frameon=False, fontsize='x-small')

plt.xlim(0, Nrows)
plt.xticks([0,14,29])
plt.yticks([0.1,10,1000])

#打开指定的工作表 4
sheetindex = 4
Nrows = 36
sheet = data.sheets()[sheetindex]
sheetname = sheet.name
sheetdomainname = sheetname.split('_')[0]
sheetdomainname = 'Satellite'
# print sheetname, sheetdomainname

#获得所需列数据 
rowsrange = range(1, Nrows+1)
fftimecolx, asoptimecolx = 6, 17
ffcols = ConvertData2Float(sheet.col_values(fftimecolx))
asopcols = ConvertData2Float(sheet.col_values(asoptimecolx))

# print rowsrange
# print sheet.cell(0, fftimecolx).ctype #ctype: 2-number
# print len(ffcols), ffcols
# print len(asopcols), asopcols

#绘制图形
ax4 = plt.subplot(235)
ax4.set_title(sheetdomainname)
#ax4.set_xlabel('Tasks')
#ax4.set_ylabel('Running Time (s)')

plt.plot(rowsrange, ffcols[0: Nrows], marker='+', markersize=4, linestyle='-.', linewidth=1, label='FF')
plt.plot(rowsrange, asopcols[0: Nrows], marker='^', markersize=4, linestyle=':', linewidth=1, label='AOIP')
plt.semilogy(0.1, 1000)
plt.legend(loc='upper left', frameon=False, fontsize='x-small')

plt.xlim(0, Nrows)
plt.xticks([0, 18,36])


foo_fig = plt.gcf() # 'get current figure'
foo_fig.savefig(r'E:\plot\pyxls\IPC4.png', dpi=300)

plt.show()

