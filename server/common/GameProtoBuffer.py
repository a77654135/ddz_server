# coding:utf-8

from common import VGFish_pb2
from common.protoBuilder import ProtoMessageObj, buildProtoBuf, getMessageURI, ProtoBufEnum


'''

  游戏使用的proto buffer操作类,实现protobuf字符流到python对象的互转

  示例:
    from GameProtoBuffer import GameProtoBuffer

    d = {
    'request' : {
      'authRequest' : {
        'registerRequest' : {
          'accountRegister' : {
            'accountName' : 'konas',
            'password': 'hello',
            }
          }
        }
      }
    }

    # 将python dict转化为ptotobuf字符流,用以发送到协议对方
    pbstr = GameProtoBuffer.SerializeMessageToPBString(d)

    # 将ptotobuf字符流转化为PBDataDict对象,从协议对方收到消息后，可以立即调用此方法
    pbMessage = GameProtoBuffer.LoadMessageFromPBString(pbstr)
    print pbMessage

    # 判定某个消息是否存在
    if pbMessage.request.authRequest != None:
      print 'authRequest presented!'
    if pbMessage.request.authRequest == None:
      print 'authRequest not presented!'
    if pbMessage.request.authRequest2 != None:
      print 'authRequest2 presented!'
    if pbMessage.request.authRequest2 == None:
      print 'authRequest2 not presented!'

    # 获取属性值
    print 'register account name : {0}' \
        ''.format(pbMessage.request.authRequest.registerRequest.accountRegister.accountName.val)

    # 打印消息的URI
    print 'URI :',GameProtoBuffer.getMessageURI(pbMessage)

'''


class GameProtoBuffer(object):
    _INSTANCE_ = None

    def __init__(self):
        self.protoBufModule = VGFish_pb2
        self.messageClass = self.protoBufModule.FishMessage
        self.messageInst = self.messageClass()
        self.Enum = ProtoBufEnum(self.protoBufModule)

    # base_dir = os.path.dirname(os.path.realpath(__file__))
    # protocolPath = os.path.relpath(base_dir,"../../protocol")
    # print protocolPath
    # assert os.path.isdir(protocolPath)

    @staticmethod
    def getInstance():
        GPBInst = GameProtoBuffer._INSTANCE_
        if GPBInst is None:
            GPBInst = GameProtoBuffer._INSTANCE_ = GameProtoBuffer()
        return GPBInst

    @staticmethod
    def LoadMessageFromPBString(pbStr):
        '''
            载入一个protobuf的字符流，并解析为message对象
        :param pbStr:
        :return:
        '''

        GPBInst = GameProtoBuffer.getInstance()

        pbMessageInst = GPBInst.messageClass()
        pbMessageInst.ParseFromString(pbStr)

        # print pbMessageInst

        protoObj = ProtoMessageObj(pbMessageInst)
        return protoObj

    @staticmethod
    def SerializeMessageToPBString(msgDic):
        '''
            将一个字典转化为protobuf字符流

        :param msgDic:
        :return:
        '''

        GPBInst = GameProtoBuffer.getInstance()
        messageInst = GPBInst.messageClass()
        messageInst.Clear()
        buildProtoBuf(messageInst, msgDic)

        # print messageInst
        return messageInst.SerializeToString()

    @staticmethod
    def getMessageURI(protoMessage):
        GPBInst = GameProtoBuffer.getInstance()
        if protoMessage.response.val is not None:
            return 'response' + getMessageURI(GPBInst.protoBufModule, protoMessage.response.val)
        else:
            return 'request' + getMessageURI(GPBInst.protoBufModule, protoMessage.request.val)

    @staticmethod
    def getMessageURIVal(protoMessage, URI):
        attrs = URI.split('.')
        sub_obj = protoMessage
        for attr in attrs:
            sub_obj = getattr(sub_obj, attr, None)
            if sub_obj is None:
                break
        if sub_obj:
            return sub_obj.val


if __name__ == '__main__':
    d = {
        'request': {
            'authRequest': {
                'registerRequest': {
                    'accountRegister': {
                        'accountName': 'konas',
                        'password': 'hello',
                    }
                }
            }
        }
    }

    # d = {
    #     'response': {
    #         'errorCode': 0,
    #         'fightResponse': {
    #             'tableSummaryResponse': {
    #                 'tableNum': 100,
    #                 'maxPlayerNumPerTable': 4,
    #                 'tablePlayerNums': [0, 1, 2]
    #             }
    #         }
    #     }
    # }

    # print GameProtoBuffer.getInstance().Enum.AccountType.VGRegister

    # 将python dict转化为ptotobuf字符流,用以发送到协议对方
    pbstr = GameProtoBuffer.SerializeMessageToPBString(d)

    # 将ptotobuf字符流转化为PBDataDict对象,从协议对方收到消息后，可以立即调用此方法
    pbMessage = GameProtoBuffer.LoadMessageFromPBString(pbstr)
    print pbMessage

    # 判定某个消息是否存在
    if pbMessage.request.authRequest != None:
        print 'authRequest presented!'
    if pbMessage.request.authRequest == None:
        print 'authRequest not presented!'
    if pbMessage.request.authRequest2 != None:
        print 'authRequest2 presented!'
    if pbMessage.request.authRequest2 == None:
        print 'authRequest2 not presented!'

    # 获取属性值
    print 'register account name : {0}' \
          ''.format(pbMessage.request.authRequest.registerRequest.accountRegister.accountName.val)

    # 打印消息的URI
    print 'URI :', GameProtoBuffer.getMessageURI(pbMessage)
