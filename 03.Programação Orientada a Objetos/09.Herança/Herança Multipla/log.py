class LogMixin:
    @staticmethod
    def write(self,msg):
        with open('log.log','a+') as f:
            f.write(msg)
            f.write('\n')
    
    def log_info(self,msg):
        self.write('INFO:',msg)

    def log_error(self,msg):
        self.write('ERROR:',msg)
