from distutils.core import setup

setup(name='threadedcomments',
      version='0.1',
      description='A simple yet flexible threaded commenting system.',
      author='Eric Florenzano',
      author_email='floguy@gmail.com',
      url='http://code.google.com/p/django-threadedcomments/',
      packages=['threadedcomments',
                'threadedcomments.templatetags', 
                'threadedcomments.management.commands'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )