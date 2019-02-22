import time
# 输出重定向

# 装饰函数 发送到卡夫卡
from kafka import KafkaProducer
from kafka import KafkaConsumer

""" OutputRedirect"""

def output2kafka(producer,topic,key=None,partition=None):
    """
    producerInfoMap={"producer": object,"topic":"","key":b'123'}
    """
    assert type(producer ) is KafkaProducer
    
    def func(functionName):
        def func_in(*args, **kwargs):
            ret = functionName(*args, **kwargs)
            producer.send(topic,value=ret,key=key,partition=partition)
            print("-----记录日志-----send",time.time())
            return ret
        return func_in
    return func

#producerInfoMap={"producer": KafkaProducer(bootstrap_servers=ip),"topic":"","key":b'123'}


    
"""DataConvers"""
import numpy as np
import json 
def kvFaceEmbedding2kakfa(functionName):
    """
    dict -> bytes
    {name(str):embedding(float64 list)}
    """
    def func_in(*args, **kwargs):

        ret = functionName(*args, **kwargs)
        assert type(ret["id"]) is str,"id is not string "
        assert type(ret["embedding"]) is np.ndarray
        ret["embedding"].dtype=float
        ret["embedding"]=list(ret["embedding"])
        return bytes(json.dumps(ret),"ascii")
    return func_in


