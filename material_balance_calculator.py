

class SystemModel(object):

    def __init__(self, number_of_streams,number_of_nodes):
        super().__init__()
        self.number_of_streams = number_of_streams
        self.number_of_nodes = number_of_nodes

    def __str__(self):
        return 