# -*- encoding: utf-8 -*-


from thefuck.types import Command
from thefuck.rules.fix_alt_space import match, get_new_command


def test_match():
    """ The character before 'grep' is Alt+Space, which happens frequently on the Mac when typing
        the pipe character (Alt+7), and holding the Alt key pressed for longer than necessary. """
    assert match(Command(u'ps -ef | grep foo', '', u'-bash:  grep: command not found'), None)
    assert not match(Command('ps -ef | grep foo', '', ''), None)
    assert not match(Command('', '', ''), None)


def test_get_new_command():
    """ Replace the Alt+Space character by a simple space """
    assert get_new_command(Command(u'ps -ef | grep foo', '', ''), None) == 'ps -ef | grep foo'
