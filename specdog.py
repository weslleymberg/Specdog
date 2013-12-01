import sys
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
    notifier = pyinotify.Notifier(watch_manager, default_proc_fun=handler)
    watch_manager.add_watch(path, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
    notifier.loop()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >> sys.stderr, 'Usage: specdog "<command>"'
        sys.exit(1)

    path = "."
    extension = ".py"
    command = sys.argv[1]

    auto_command(path, extension, command)
