import sys
import asyncore
import pyinotify
import subprocess

class OnProjectChangeHandler(pyinotify.ProcessEvent):
    def my_init(self, path, extension, command):
        self.path = path
        self.extension = extension
        self.command = command

    def _run_command(self):
        print >> sys.stdout, 'Running "%s"...' %(self.command)
        command_list = self.command.split(' ')
        subprocess.call(command_list)

    def process_IN_MODIFY(self, event):
        if not event.pathname.endswith(self.extension):
            return
        self._run_command()

def auto_command(path, extension, command):
    watch_manager = pyinotify.WatchManager()
    handler = OnProjectChangeHandler(path=path, extension=extension, command=command)
    pyinotify.AsyncNotifier(watch_manager, handler)
    watch_manager.add_watch(path, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print >> sys.stdout, "Exiting..."
        asyncore.ExitNow()
        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >> sys.stderr, 'Usage: specdog "<command>"'
        sys.exit(1)

    path = "."
    extension = ".py"
    command = sys.argv[1]

    auto_command(path, extension, command)
