"""

Disk Management Toolkit for live backup and disk changes

Copyright (C) 2024-2025 QB Networks

Copyright (C) 2017-2025 Masscollabs Services

Copyright (C) 2017-2025 Procyberian and contributors

Copyright (C) 2017-2025 Mass Collaboration Labs and contributors

Copyright (C) 2017-2025 amassivus and contributors

Copyright (C) 2024-2025 godigitalist and contributors

Copyright (C) 2024-2025 bilsege and contributors

Copyright (C) 2024-2025 Birleşik Dergi Yazarları

Copyright (C) 2024-2025 Andromeda Computing Services and contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import sys

def convert_gib_to_gb(gib):
    """
    Convert GiB (Gibibytes) to GB (Gigabytes).
    
    1 GiB = 1024^3 bytes
    1 GB = 1000^3 bytes
    """
    gb = gib * (1024**3) / (1000**3)
    return gb

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert.py <size_in_gib>")
        sys.exit(1)
    
    try:
        size_in_gib = float(sys.argv[1])
    except ValueError:
        print("Please provide a valid number for size in GiB.")
        sys.exit(1)
    
    size_in_gb = convert_gib_to_gb(size_in_gib)
    print(f"{size_in_gib} GiB is approximately {size_in_gb:.2f} GB")