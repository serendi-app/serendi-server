#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laufpartner_server.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
