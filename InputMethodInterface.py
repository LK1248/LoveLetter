from RequestInfo import RequestInfo
import abc

class InputMethodInterface:
    def __init__(self):
        self.name = ''

    @abc.abstractmethod
    def get_player_input(self, RequestInfo):
        return None # Not implemented here, will be implemented in child functions

    def get_name(self):
        return(self.name)