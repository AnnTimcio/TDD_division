#  Copyright 2024 AnnTimcio
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from unittest import TestCase

from main import division


class Test(TestCase):
    def test_division_50(self):
        self.assertEqual("50%", division(10, 20))

    def test_division_0(self):
        self.assertEqual("0%", division(0, 10))

    def test_division_10(self):
        self.assertEqual("10%", division(1, 10))

    def test_division_40(self):
        self.assertEqual("40%", division(4, 10))

    def test_division_100(self):
        self.assertEqual("100%", division(10, 10))

    def test_division_200(self):
        self.assertEqual("200%", division(200, 100))

    def test_division_33(self):
        self.assertEqual("33%", division(1, 3))

    def test_division_60(self):
        self.assertEqual("60%", division(60, 100))

    def test_division_01(self):
        self.assertEqual("1%", division(1, 100))

    def test_division_80(self):
        self.assertEqual("80%", division(160, 200))

    def test_division_y0(self):
        self.assertEqual("0%", division(160, 0))
