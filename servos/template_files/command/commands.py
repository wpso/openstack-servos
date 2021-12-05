from servos.core.commands import Command
from optparse import make_option


class DemoCommand(Command):
    name = 'demo'
    option_list = (
        make_option('-d', '--demo', dest='demo', default=False, action='store_true',
                    help='Demo command demo.'),
    )
    help = ''
    args = ''
    check_services_dirs = True
    check_services = False

    def handle(self, options, global_options, *args):
        print 'This is a demo of DemoCommand, you can enter: '
        print
        print '    servos help demo'
        print
        print 'to test this command'
        print
        print 'options=', options
        print 'global_options=', global_options
        print 'args=', args
