from Classes.Protocol.Commands.LogicCommand import LogicCommand

class LogicQuestsSeenCommand(LogicCommand):
    def __init__(self, payload):
        super().__init__(payload)
        self.questID: int = 0

    def decode(self, byteStream):
        raw = super().decode(byteStream)
        self.questID = raw.reflectReflectablePointerBase("data", 0)
        raw.reflectInt(0, "ev", 0)
        raw.destruct()

    def execute(self, receiver):
        pass

    def getCommandType(self):
        return 503