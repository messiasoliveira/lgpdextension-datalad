"""DataLad demo command"""

__docformat__ = 'restructuredtext'

from os.path import curdir
from os.path import abspath

from datalad.interface.base import Interface
from datalad.interface.base import build_doc
from datalad.support.param import Parameter
from datalad.distribution.dataset import datasetmethod
from datalad.interface.utils import eval_results
from datalad.support.constraints import EnsureChoice,EnsureStr

from datalad.interface.results import get_status_dict
from datalad_helloworld.main import Main
import logging
lgr = logging.getLogger('datalad.helloworld.hello_cmd')


# decoration auto-generates standard help
@build_doc
# all commands must be derived from Interface
class HelloWorld(Interface):
    # first docstring line is used a short description in the cmdline help
    # the rest is put in the verbose help and manpage
    """Short description of the command

    Long description of arbitrary volume.
    """

    # parameters of the command, must be exhaustive
    _params_ = dict(
        path=Parameter(
            args=("-f","--filepath"),
            doc="""Filepath is the correctly address to configuration file. Ex.: c:\..\..\_settings.json""",
            constraints=EnsureStr()),
    )

    @staticmethod
    # decorator binds the command to the Dataset class as a method
    @datasetmethod(name='hello_cmd')
    # generic handling of command results (logging, rendering, filtering, ...)
    @eval_results
    # signature must match parameter list above
    # additional generic arguments are added by decorators
    def __call__(path=None):
        if path:
            lgpd = LgpdExtension(path)
            lgpd.run()
            msg = lgpd.getmessage()
        
        yield get_status_dict(
            # an action label must be defined, the command name make a good
            # default
            action='lgpdextension',
            # most results will be about something associated with a dataset
            # (component), reported paths MUST be absolute
            path=abspath(curdir),
            # status labels are used to identify how a result will be reported
            # and can be used for filtering
            status='ok' if path else 'error',
            # arbitrary result message, can be a str or tuple. in the latter
            # case string expansion with arguments is delayed until the
            # message actually needs to be rendered (analog to exception
            # messages)
            message=msg)

class HelloWorldHello():
    def __init__(self,language):
        self.language = language
    def get_ret(self):
        if self.language == 'en':
            msg = "hello"
        elif self.language == 'de':
            msg = 'Tachchen!'
        else:
            msg = ("unknown language: '%s'", self.language)
        return msg

class LgpdExtension:
    def __init__(self,path=None):
        self.path = path
        self.result = None
    def run(self):
        self.result = Main(self.path).run()
    def getmessage(self):
        if self.result:
            msg = "Applied all changes"
        else:
            msg = self.result
        return msg
