import eel,os,re,sys

eel.init('web')

grades = ['大一', '大二','大三', '大四', '碩一', '碩二']
color = ['#1976D2','#BBDEFB','#00BCD4','#212121','#757575','#2196F3']
regex = r"<font color=#\w*>\D*<br>\w*<br>\w{3}\d{4}</font>"
files=[]


def getColor(x):
    global color
    color=x.split(',')
    print(color)
eel.getColors()(getColor)

@eel.expose
def getPath(x):
    flag=0
    Data=[]
    filedata=[]
    files=os.listdir(x)
    for nowindex,fileName in enumerate(files):
        if fileName=='out.md': flag+=1
        if bool(re.search(r'\w*.md',fileName)) and fileName!='out.md':
            path=os.path.join(os.path.dirname(x),x,fileName)
            with open(path, 'r', encoding='utf-8') as f:
                filedata.append(f.read())
                if bool(re.search(r'^<.*</font>', filedata[nowindex-flag])):
                    filedata[nowindex-flag] = re.sub(r'^<.*>', '', filedata[nowindex-flag])

                studentName, grade = re.search(r'(\w+)_(\w{2})\.md', fileName).groups()
                filedata[nowindex-flag] = re.sub(regex, f'<font color={color[grades.index(grade)]}>{studentName}<br></font>', filedata[nowindex-flag])
                filedata[nowindex-flag] = re.split(r'\|', filedata[nowindex-flag])
            Data=filedata[0]
            for i in filedata[1:]:
                for j in range(len(Data)):
                    if not bool(re.search(i[j], Data[j])):
                        Data[j] += i[j]
            eel.showLog(f'{fileName}已完成')
    with open(os.path.join(os.path.dirname(x),x,'out.md'), 'w', encoding='utf-8') as f:
        for i in grades:
            f.write(f'<font color={color[grades.index(i)]}>{i}</font> ')
        f.write('\n')
        for i in Data[:-1]:
            if i != '':
                f.write(i+"|")
            else:
                f.write(''+"|")
    eel.showLog(f'已完成全部檔案，請查看out.md')
    eel.showMD('|'.join(Data))


eel.start('index.html',size=(1018,650),position=(100,100),block=False)

while True: 
    eel.sleep(3)

