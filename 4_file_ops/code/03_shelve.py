"""
Das Thema dieser Datei ist die Verwendung des `shelve`-Moduls in Python.

- `shelve` ist ein Modul der Python-Standardbibliothek für einfache
  persistente Datenspeicherung.
- Es bietet ein Dictionary-ähnliches Interface.
- Python-Objekte werden automatisch mittels `pickle`
  serialisiert und deserialisiert.
- Schlüssel müssen Strings sein.
- Werte können beliebige serialisierbare Python-Objekte sein.

Intern verwendet `shelve` ein DBM-Backend (`dbm`), dessen konkrete
Implementierung vom Betriebssystem und der Python-Installation abhängt.
Typische Backends sind `dbm.gnu`, `dbm.ndbm` oder `dbm.dumb`.

Die erzeugten Dateien unterscheiden sich daher je nach System.
Mögliche Dateien sind beispielsweise:

- basename.db
- basename.dat
- basename.dir
- basename.bak

Es kann jedoch auch nur eine einzelne Datei oder eine andere
Dateistruktur entstehen.

Da die verwendeten Datenbankformate systemabhängig sind, sollten
Shelve-Dateien nicht als plattformübergreifendes Austauschformat
verwendet werden.

Alternativen zu `shelve` sind:

- `pickle` für die reine Objektserialisierung.
- `json` für plattformunabhängige Textdateien.
- `sqlite3` für eine echte relationale Datenbank.
"""

from pathlib import Path
import shelve
