"""Blender extension entry point."""

from . import modules


def register():
    modules.register()


def unregister():
    modules.unregister()
