#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'unicodepwd': self.unicodePwd
        }

    def unicodePwd(self, pwd):
        return unicode('"{0}"'.format(pwd)).encode('utf-16-le')