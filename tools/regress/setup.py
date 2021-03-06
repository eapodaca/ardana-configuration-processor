#
# (c) Copyright 2015 Hewlett Packard Enterprise Development LP
# (c) Copyright 2017-2018 SUSE LLC
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
import os.path

import setuptools


def read_file(fn):
    with open(os.path.join(os.path.dirname(__file__), fn)) as f:
        return f.read()

setuptools.setup(
    setup_requires=['pbr'],
    pbr=True,
    version="0.0.1",
    license=read_file("LICENSE.md"),
)
