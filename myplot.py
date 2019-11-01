import xlrd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator,FormatStrFormatter


def ConvertData2Float(datalist):
    lf = []
    for f in datalist:
        if type(f) is float:
            lf.append(f)
        else:
            lf.append(None)

    return lf

def max2(l1,l2):
    max1 = -1
    max2 = -1
    for ll1 in l1:
        if ll1 != None and ll1 > max1:
            max1 = ll1
    for ll2 in l2:
        if ll2 != None and ll2 > max2:
            max2 = ll2
    if max2 > max1:
        max1 = max2
    return max1

def count_digit(num):
    count = 1
    while int(int(num)/10)!= 0:
        count += 1
        num /= 10
    return count

datafiles = [r'F:\pyxls\IPC3-hpZ230.xlsx',r'F:\pyxls\IPC4-hpZ230.xlsx',
             r'F:\pyxls\IPC5-hpZ230.xlsx',r'F:\pyxls\IPC7-hpZ230.xlsx',
             r'F:\pyxls\IPC8-hpZ230.xlsx']

for datafile in datafiles:
    data = xlrd.open_workbook(datafile)

    fig = plt.figure(1)
    # plt.tight_layout()
    left = 0.125  # the left side of the subplots of the figure
    right = 0.9  # the right side of the subplots of the figure
    bottom = 0.1  # the bottom of the subplots of the figure
    top = 0.9  # the top of the subplots of the figure
    wspace = 0.4  # the amount of width reserved for blank space between subplots,
    # expressed as a fraction of the average axis width
    hspace = 0.4  # the amount of height reserved for white space between subplots,
    # expressed as a fraction of the average axis height
    plt.subplots_adjust(left, bottom, right, top, hspace, wspace)

    # print(len(data.sheets()))
    for sheet_num in range(len(data.sheets())):
        sheet = data.sheets()[sheet_num]
        sheet_name = sheet.name.split('_')[0]
        # print(sheet.name.split('_')[0])

        row_range = range(1,sheet.nrows+1)
        ff_time_col,asop_time_col = 17,6
        ffcol = ConvertData2Float(sheet.col_values(ff_time_col))
        asopcol = ConvertData2Float(sheet.col_values(asop_time_col))
        if len(data.sheets())>3:
            sub_pic = plt.subplot(2,int((len(data.sheets())+1)/2),sheet_num+1)
        else:
            sub_pic = plt.subplot(1, len(data.sheets()), sheet_num + 1)
        # print((2,int((len(data.sheets())+1)/2),sheet_num+1))
        sub_pic.set_title(sheet_name,fontsize=10)

        plt.plot(row_range,ffcol[0:sheet.nrows],marker='x',markersize=3,linestyle='-.',linewidth=1,label='FF')
        plt.plot(row_range,asopcol[0:sheet.nrows],marker='^',markersize=3,linestyle=':',linewidth=1,label='AOIP')

        # print(max2(ffcol,asopcol))
        p = max2(ffcol,asopcol)
        # print(count_digit(p))
        print(sheet.nrows)
        digit = count_digit(p)

        y_min_tick = MultipleLocator(10)
        if (digit>=3):
            plt.semilogy(0, 1000)
            # y_min_tick = MultipleLocator(10)
            # sub_pic.yaxis.set_minor_locator(y_min_tick)
        elif digit == 2:
            plt.semilogy(0,100)
        else:
            plt.semilogy(0,10)

        plt.xlim(0,sheet.nrows)
        num = sheet.nrows
        plt.xticks([0,int(num/4),int(num/2),int(num/4*3),num])
        if not num%3:
            plt.xticks([0, int(num / 3), int(num / 3*2), num])
        # plt.xticks(fontsize=20)
        # plt.ylim(0.1,1000)
        # plt.xscale('linear')
        # plt.yscale('log')
        plt.legend(loc='upper left', frameon=False, fontsize='x-small')

    foo_pig = plt.gcf()
    plt.savefig(datafile.split('\\')[2][0:4] + '.png',dpi=300)

    plt.show()
