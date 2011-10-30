#!/usr/bin/env python
# coding: utf-8
'''
    shpysh
    ~~~~~

    The main callable for shpysh.

    :copyright:  2011 by Lee Olayvar
    :license: MIT, see LICENSE for more details.
'''

import os
import sys
import urwid


def start_urwid():
    '''Load the gui, and start capturing the user input.'''

    input_container = urwid.Edit('input: ')
    
    history_container = urwid.SimpleListWalker([input_container])
    listbox = urwid.ListBox(history_container)

    def update_on_cr(input):
        if input != 'enter':
            return

        focus_widget, position = listbox.get_focus()

        if not hasattr(focus_widget, 'edit_text'):
            return
        else:
            if focus_widget.edit_text == 'exit':
                raise urwid.ExitMainLoop()

        history_container.insert(position, urwid.Text(focus_widget.edit_text))
        history_container.set_focus(position+1)
        focus_widget.edit_text = ''
        return True

    loop = urwid.MainLoop(listbox, unhandled_input=update_on_cr)
    loop.run()

def main(args):
    '''The main shpysh call.

    :param args:
        The string arguments given to the shpysh executable.
    '''

    start_urwid()

if __name__ == '__main__':
    main('')

