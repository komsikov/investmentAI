# -*- coding: utf-8 -*-
from flask import flash


class Asset(object):

    def show_string(self, text):
        if text == '':
            flash("You didn't enter any text to flash")
        else:
            flash(text + "!!!")
