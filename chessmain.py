class gamestate:
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","Bb","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wb","wN","wR"]]
        self.whiteMove =True 
        self.moveLog = []