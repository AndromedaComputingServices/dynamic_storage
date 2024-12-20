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
import os
import shutil

def get_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    return total, used, free

def main():
    total, used, free = get_disk_usage()
    print(f"Total: {total // (2**30)} GiB")
    print(f"Used: {used // (2**30)} GiB")
    print(f"Free: {free // (2**30)} GiB")

if __name__ == "__main__":
    main()

# This script is designed to run on a Debian GNU/Linux distribution.
# It retrieves and prints the total, used, and free disk space on the root filesystem.
# The values are displayed in GiB (Gibibytes).
