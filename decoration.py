# 输出重定向

# 装饰函数 发送到卡夫卡
from kafka import KafkaProducer
from kafka import KafkaConsumer
def output2kafka(producer,topic,key=None,partition=None):
    """
    producerInfoMap={"producer": object,"topic":"","key":b'123'}
    """
    print(producer,topic)
    def func(functionName):
        def func_in(*args, **kwargs):
            #print("-----记录日志-----")
            ret = functionName(*args, **kwargs)
            producer.send(topic,ret,key=b'1')
            return ret
        return func_in
    return func

#producerInfoMap={"producer": KafkaProducer(bootstrap_servers=ip),"topic":"","key":b'123'}