
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import flickrapi
import os

class FlickrUploadPlugin:
    def __init__(self):

        #fill in your account / app secrets
        self.api_key = ''
        self.api_secret = ''

        self.flickr = flickrapi.FlickrAPI(self.api_key, self.api_secret)

    def upload(self, data):
        name = os.path.split(data)
        name = name[-1]

        print "File to upload: "+str(name)

        try:
            print "Starting Flickr Upload"
            self.flickr.upload(filename=data, title=name, is_public=0)

            print "Flick upload finished!"
            print "Success"
            return True
        except:
            print "Fail"
            return False

    def test_upload(self):
        """
        Method which could be called to test the upload function
        """

        test_file = "/opt/FotoShareN9/plugins/flickr/img/flickr-icon.png"
        try:
            self.upload(test_file)
            print "Flickr upload works!"
            return True
        except:
            print "Flickr upload failed!"
            return False


if __name__ == "__main__":
    FlickrUploadPlugin().test_upload()
