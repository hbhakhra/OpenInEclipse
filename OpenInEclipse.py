import sublime, sublime_plugin
import subprocess

def settings():
  """Shortcut to the settings"""
  return sublime.load_settings("OpenInEclipse.sublime-settings")

class OpenInEclipse(sublime_plugin.WindowCommand):
	def run(self):
		eclipse_path = settings().get('eclipse_path')
		subprocess.Popen(eclipse_path + " \"" + self.window.active_view().file_name() + "\"")
