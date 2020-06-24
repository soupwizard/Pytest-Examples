# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

class Engine:
    
    def __init__(self, name, max_rpm):
        self.name        = name
        self.max_rpm     = max_rpm
        self.rpm         = 0
        self.state       = 'OFF'

    def turn_on(self):
        self.state = 'ON'
        
    def turn_off(self):
        self.state = 'OFF'
        
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
    
    def get_max_rpm(self):
        return self.max_rpm
   
    def get_rpm(self):
        return(self.rpm)
    
    def set_rpm(self, rpm):
        if self.get_state() != 'ON':
            print('WARNING, tried to set rpm with engine in %s state.' % (self.state))
        elif rpm > self.get_max_rpm():
            print('ERROR, setting rpm of %0.2f exceeded max rpm of %0.2f' % (rpm, self.get_max_rpm()))
            self.state = 'BLOWN'
            self.rpm = 0
        else:
            self.rpm = rpm
            
    def print_status(self):
        print('')
        print('Engine: %s Status' % (self.name))
        print('    State: %s' % (self.state))
        print('      RPM: %0.2f' % (self.get_rpm()))
        
   
