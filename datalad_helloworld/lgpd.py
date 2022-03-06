"""DataLad demo command"""

__docformat__ = 'restructuredtext'

from os.path import curdir
from os.path import abspath

from datalad.interface.base import Interface
from datalad.interface.base import build_doc
from datalad.support.param import Parameter
from datalad.distribution.dataset import datasetmethod
from datalad.interface.utils import eval_results
from datalad.support.constraints import EnsureChoice

from datalad.interface.results import get_status_dict
import pandas as pd
import logging
lgr = logging.getLogger('datalad.helloworldlgpd.lgpd')


# decoration auto-generates standard help
@build_doc
# all commands must be derived from Interface
class HelloWorldLgpd(Interface):
    # first docstring line is used a short description in the cmdline help
    # the rest is put in the verbose help and manpage
    """Short description of the command

    Long description of arbitrary volume.
    """

    # parameters of the command, must be exhaustive
    _params_ = dict(
        zanguage=Parameter(
            # cmdline argument definitions, incl aliases
            args=("-z", "--zanguage"),
            # documentation
            doc="""language to say "hello" in""",
            # type checkers, constraint definition is automatically
            # added to the docstring
            constraints=EnsureChoice('y', 'n')),
    )
    

    @staticmethod
    # decorator binds the command to the Dataset class as a method
    @datasetmethod(name='lgpd')
    # generic handling of command results (logging, rendering, filtering, ...)
    @eval_results
    # signature must match parameter list above
    # additional generic arguments are added by decorators
    def __call__(zanguage='y'):
        if zanguage == 'y':
            msg = str(pd.__version__)
        elif zanguage == 'n':
            msg = str(pd.__version__)
            msg += " == no"
        else:
            msg = ("unknown commange: '%s'", zanguage)
        yield get_status_dict(
            action='lgpd',
            status='ok' if zanguage in ('y','n') else 'error',
            message=msg
        )
            
