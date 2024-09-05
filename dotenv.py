import os
import re
import warnings

__version__ = '1.4.2'


line_re = re.compile(r"""
    ^(?:export\s+)?([\w\.]+)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^#\n]*)))(?:\s*\#.*)?$
""", re.VERBOSE)

variable_re = re.compile(r"""
    (\\)?(\$)\{?([A-Z0-9_]+)\}?
""", re.IGNORECASE | re.VERBOSE)

def read_dotenv(dotenv=None, override=False):
    """Читает переменные из .env файла и добавляет их в os.environ."""
    if dotenv is None:
        dotenv = os.path.join(os.path.dirname(sys._getframe().f_back.f_code.co_filename), '.env')

    if os.path.isfile(dotenv):
        with open(dotenv) as f:
            for key, value in parse_dotenv(f.read()).items():
                if override:
                    os.environ[key] = value
                else:
                    os.environ.setdefault(key, value)
    else:
        warnings.warn(f"Файл {dotenv} не существует.", stacklevel=2)

def parse_dotenv(content):
    """Разбирает содержимое .env файла и возвращает словарь переменных."""
    env = {}
    for line in content.splitlines():
        match = line_re.match(line)
        if match:
            key, double_quoted, single_quoted, unquoted = match.groups()
            value = double_quoted or single_quoted or unquoted
            if value:
                value = re.sub(r'\\([^$])', r'\1', value)
                value = replace_vars(value, env)
            env[key] = value
        elif not re.match(r'^\s*(?:#.*)?$', line):
            warnings.warn(f"Неверный формат строки: {line}", SyntaxWarning)
    return env

def replace_vars(value, env):

    for _, _, var in variable_re.findall(value):
        value = value.replace(f'${{{var}}}', env.get(var, os.environ.get(var, '')))
    return value
