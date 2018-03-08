# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# coding: utf-8
# pylint: disable=
"""Dataset reader."""
__all__ = ['DataReader']

class DataReader(object):
    """Abstract datareader class. Data reader handles I/O and produces raw samples for a dataset.

    Subclasses need to override `read` that returns a Dataset (and optionally `read_iter` that
    returns an iterable for large files).
    """

    def read(self):
        raise NotImplementedError

    def read_iter(self):
        return self.read()
