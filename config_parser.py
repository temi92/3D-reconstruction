import ConfigParser

class Configuration(object):

    def __init__(self):
        # default config file
        self.config_file = "/home/temi/DIGIART/conf.ini" 

        # create the global parser object
        self.parser = ConfigParser.SafeConfigParser()

        # read the config file into memory
        self.read()

    def read(self):
        try:
            self.parser.read(self.config_file)
        except IOError as e:
            print 'Error {0} reading config file: {1}: '.format(e.errno, e.strerror)
        return
    
    # save - saves the config to disk
    def save(self):
        try:
            with open(self.config_file, 'wb') as configfile:
                self.parser.write(configfile)
        except IOError as e:
            print 'Error {0} writing config file: {1}: '.format(e.errno, e.strerror)
        return

    # check_section - ensures the section exists, creates it if not
    def check_section(self, section):
        if not self.parser.has_section(section):
            self.parser.add_section(section)
        return

    def get_boolean(self, section, option, default):
        try:
            return self.parser.getboolean(section, option) 
        except ConfigParser.Error:
            return default

    # set_boolean - sets the boolean to the specified section/option
    def set_boolean(self, section, option, new_value):
        self.check_section(section) 
        self.parser.set(section, option, str(bool(new_value)))
        return

    # get_integer - returns the integer found in the specified section/option or the default if not found
    def get_integer(self, section, option, default):
        try:
            return self.parser.getint(section, option)
        except ConfigParser.Error:
            return default

    # set_integer - sets the integer to the specified section/option
    def set_integer(self, section, option, new_value):
        self.check_section(section)
        self.parser.set(section, option, str(int(new_value)))
        return

    # get_float - returns the float found in the specified section/option or the default if not found
    def get_float(self, section, option, default):
        try:
            return self.parser.getfloat(section, option)
        except ConfigParser.Error:
            return default

    # set_float - sets the float to the specified section/option
    def set_float(self, section, option, new_value):
        self.check_section(section)
        self.parser.set(section, option, str(float(new_value)))
        return

    # get_string - returns the string found in the specified section/option or the default if not found
    def get_string(self, section, option, default):
        try:
            return self.parser.get(section, option)
        except ConfigParser.Error:
            return default

    # set_string - sets the string to the specified section/option
    def set_string(self, section, option, new_value):
        self.check_section(section)
        self.parser.set(section, option, str(new_value))
        return

    # main - tests BalloonConfig class
    def main(self):
        print "config file: %s" % self.config_file


	"""
        # write and read a boolean
        section = 'Test_Section1'
        option = 'Test_boolean'
        print "Writing %s/%s = True" % (section,option)
        self.set_boolean(section,option,True)
        print "Read %s/%s : %s" % (section, option, self.get_boolean(section, option, False))
	"""
        # write and read an integer
        section = 'image_settings'
        option = 'images'
        self.set_integer(section,option,30)
        print "Read %s/%s : %s" % (section, option, self.get_integer(section, option, 99))
	
	
        # write and read a float
        section = 'filter_settings'
        option = 'distance_threshold'
        self.set_float(section,option,0.5)
        #print "Read %s/%s : %s" % (section, option, self.get_float(section, option, 0.01))


        # save the config file
        self.save()

        return

# declare config object
config = Configuration()

if __name__ == "__main__":
	config.main()
