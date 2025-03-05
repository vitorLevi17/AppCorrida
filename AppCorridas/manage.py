#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# 3-Enviar para os aplicativos e receber os preços
#"(Alterar o estimativas.py)
# 'rows': [{'elements': [{'distance': {'text': '627 km', 'value': 626790}, 'duration': {'text': '7 hours 35 mins', 'value': 27301},
# 'rows': [{'elements': [{'distance': {'text': '627 km', 'value': 626790}, 'duration': {'text': '7 hours 35 mins', 'value': 27301},

# hospedar
# anuncios
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
