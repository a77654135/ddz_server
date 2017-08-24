#coding:utf-8
import os,sys
import shutil

ROOT_FILENAME = "root.proto"
DEST_FILENAME = "ddzproto.proto"
PROTOC_FILENAME = "ddzproto_pb2.py"

def readTextFromFile(filepath):
    f = open(filepath,'r')
    text = f.read()
    f.close()
    return text

def buildMain():
    base_dir = os.path.dirname(os.path.realpath(__file__))

    for filename in [DEST_FILENAME,PROTOC_FILENAME,PROTOC_FILENAME + 'c']:
        delFilePath = os.path.join(base_dir,filename)
        if os.path.exists(delFilePath):
            os.unlink(delFilePath)


    segments_dir = os.path.join(base_dir,'segments')
    assert os.path.isdir(segments_dir)

    rootFilePath = os.path.join(segments_dir,ROOT_FILENAME)
    assert os.path.isfile(rootFilePath)

    outputText = readTextFromFile(rootFilePath)

    FileList = os.listdir(segments_dir)
    for filename in FileList:
        if filename == ROOT_FILENAME:
            continue
        if filename == DEST_FILENAME:
            continue

        if filename[-6:] != '.proto':
            continue

        filepath = os.path.join(segments_dir,filename)
        if not os.path.isfile(filepath):
            continue

        print 'reading {0}'.format(filename)
        outputText += '\n\n//!!Content From {0}\n\n'.format(filename)
        outputText += readTextFromFile(filepath)

    dstPath = os.path.join(base_dir,DEST_FILENAME)
    f = open(dstPath,'w')
    f.write(outputText)
    f.close()

    os.system('protoc -I=. --python_out=. {0}'.format(DEST_FILENAME))

    outputFilePath = os.path.join(base_dir,PROTOC_FILENAME)
    if os.path.exists(outputFilePath):
        # 把PROTOC_FILENAME copy到项目中
        spath = os.path.join(base_dir, '..', 'server', 'common', PROTOC_FILENAME)
        if os.path.exists(spath):
            os.remove(spath)
        shutil.copyfile(outputFilePath, spath)
        print r"copyfile :   {0}".format(spath)
        os.remove(outputFilePath)
        print('Success!')
    else:
        print('build protocol failed!')

if __name__ == '__main__':
    buildMain()
