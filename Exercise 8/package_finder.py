from pathlib import Path
import re

package = re.compile(r'^(?:from|import)\s+(\w+)')

def package_finder():
    requirements = Path('.') / 'requirements.txt'
    requirements.touch(exist_ok=True)

    with open(requirements, 'a') as r:
        matches = []
        for path in Path('.').glob('*.py'):
            if path.is_file():
                with path.open() as file:
                    for line in file:
                        match = re.search(package, line)
                        if match is not None and match.group(1) not in matches:
                            matches.append(match.group(1))
        print(matches)
        for match in matches:
            r.write(f'{match}\n')

package_finder()