class FakePacket(object):

    def __init__(self, **kwargs):
        self._src_ip = kwargs.get('src_ip')
        self._dst_ip = kwargs.get('dst_ip')
        self._protocol = kwargs.get('protocol')
        self._payload = FakeTransportPacket(**kwargs)

    def get_src_ip(self):
        return self._src_ip

    def get_dst_ip(self):
        return self._dst_ip

    def get_protocol(self):
        return self._protocol

    def get_payload(self):
        return self._payload


class FakeTransportPacket(object):
    
    def __init__(self, **kwargs):
        self._src_port = kwargs.get('src_port')
        self._dst_port = kwargs.get('dst_port')

    def get_src_port(self):
        return self._src_port

    def get_dst_port(self):
        return self._dst_port


